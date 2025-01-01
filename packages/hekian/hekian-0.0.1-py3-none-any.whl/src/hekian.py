from typing import List, Tuple, Callable
from queue import PriorityQueue
from functools import wraps
import sqlite3


def reward(func: Callable[[str], float]):
    """
    A decorator that evaluates the reward of a beam search output.

    Args:
        func: Function that takes a string and returns a float between 0 and 1
    """

    @wraps(func)
    def wrapper(output: str) -> float:
        reward_value = func(output)
        if not 0 <= reward_value <= 1:
            raise ValueError(f"Reward must be between 0 and 1, got {reward_value}")
        return reward_value

    setattr(wrapper, "_is_reward_function", True)
    return wrapper


def parser(func: Callable):
    @wraps(func)
    def wrapper(output):
        return func(output)

    return wrapper


def majority(sample_size: int = 2, parser: Callable | None = None):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tally = {}

            for _ in range(sample_size):
                output = func(*args, **kwargs)

                key = parser(output) if parser else output
                tally[key] = tally.get(key, 0) + 1

            most_common = max(tally.items(), key=lambda x: x[1])[0]
            return most_common

        return wrapper

    return decorator


def best_of_n(
    reward_func: Callable, sample_size: int = 2
):  # Support getting top x candidates
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            best_output = None
            best_reward = float("-inf")
            for _ in range(sample_size):
                output = func(args, kwargs)
                reward_value = reward_func(output)

                if reward_value > best_reward:
                    best_reward = reward_value
                    best_output = output

            return best_output

        return wrapper

    return decorator


def beam(
    max_depth: int,
    beam_width: int = 2,
    branching_factor: int = 2,
    reward_func: Callable | None = None,
):
    def decorator(func: Callable[..., str]):
        @wraps(func)
        def wrapper(*args, **kwargs) -> List[Tuple[float, List[int], str]]:
            # Type check the reward function
            if reward_func is not None and not hasattr(
                reward_func, "_is_reward_function"
            ):
                raise TypeError("reward_func must be decorated with @reward")
            conn = sqlite3.connect("beam_searches.db")
            c = conn.cursor()
            c.execute(
                """INSERT INTO beam_searches (max_depth, beam_width, branching_factor)
                   VALUES (?, ?, ?)""",
                (max_depth, beam_width, branching_factor),
            )
            beam_search_id = c.lastrowid

            beam = [(1.0, [], "", None)]

            c.execute(
                """INSERT INTO beam_nodes 
                   (beam_search_id, parent_id, node_value, reward_score, is_pruned, level)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (beam_search_id, None, "", 1.0, False, 0),
            )
            root_id = c.lastrowid

            for depth in range(max_depth):
                candidates = PriorityQueue()

                for cum_prob, path, current_output, parent_id in beam:
                    for branch in range(branching_factor):
                        output = func(*args, branch=branch, **kwargs)
                        new_output = current_output + output

                        if reward_func:
                            prob = reward_func(new_output)
                        else:
                            prob = 1.0

                        new_cum_prob = cum_prob * prob
                        new_path = path + [branch]

                        c.execute(
                            """INSERT INTO beam_nodes 
                               (beam_search_id, parent_id, node_value, reward_score, 
                                is_pruned, level)
                               VALUES (?, ?, ?, ?, ?, ?)""",
                            (beam_search_id, parent_id, output, prob, False, depth + 1),
                        )
                        node_id = c.lastrowid

                        candidates.put(
                            (-new_cum_prob, new_cum_prob, new_path, new_output, node_id)
                        )

                all_candidates = []
                while not candidates.empty():
                    all_candidates.append(candidates.get())

                for i, (neg_prob, prob, path, output, node_id) in enumerate(
                    all_candidates
                ):
                    is_pruned = i >= beam_width
                    c.execute(
                        """UPDATE beam_nodes 
                           SET is_pruned = ? 
                           WHERE id = ?""",
                        (is_pruned, node_id),
                    )

                new_beam = []
                for i, (neg_prob, prob, path, output, node_id) in enumerate(
                    all_candidates
                ):
                    if i < beam_width:
                        new_beam.append((prob, path, output, node_id))

                beam = new_beam
                conn.commit()

            conn.close()
            return [(prob, path, output) for prob, path, output, _ in beam]

        return wrapper

    return decorator
