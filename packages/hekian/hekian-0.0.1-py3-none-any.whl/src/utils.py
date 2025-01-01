import sqlite3
from typing import Optional
from dataclasses import dataclass


@dataclass
class BeamSearchNode:
    id: int
    beam_search_id: int
    parent_id: Optional[int]
    node_value: str
    reward_score: float
    is_pruned: bool
    level: int


def setup_database():
    """Create the necessary tables if they don't exist"""
    conn = sqlite3.connect("beam_searches.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS beam_searches
                 (id INTEGER PRIMARY KEY,
                  max_depth INTEGER,
                  beam_width INTEGER,
                  branching_factor INTEGER,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS beam_nodes
                 (id INTEGER PRIMARY KEY,
                  beam_search_id INTEGER,
                  parent_id INTEGER NULL,
                  node_value TEXT,
                  reward_score FLOAT,
                  is_pruned BOOLEAN,
                  level INTEGER,
                  FOREIGN KEY (beam_search_id) REFERENCES beam_searches(id),
                  FOREIGN KEY (parent_id) REFERENCES beam_nodes(id))"""
    )

    conn.commit()
    conn.close()


def print_beam_tree(beam_search_id: int) -> None:
    """
    Prints an ASCII representation of the complete beam search tree from the database.
    Pruned branches are marked with 'x'.
    Each node shows: value [node_id] (prob: score, total: cumulative_score)
    """
    conn = sqlite3.connect("beam_searches.db")
    c = conn.cursor()

    def get_cumulative_probability(node_id: int) -> float:
        """Calculate cumulative probability by multiplying all ancestor probabilities"""
        prob = 1.0
        current_id = node_id

        while current_id is not None:
            c.execute(
                """SELECT parent_id, reward_score 
                   FROM beam_nodes 
                   WHERE id = ?""",
                (current_id,),
            )
            parent_id, reward_score = c.fetchone()
            prob *= reward_score
            current_id = parent_id

        return prob

    def print_node_and_children(
        node_id: Optional[int], prefix: str = "", is_last: bool = True
    ):
        if node_id is None:
            print("Root (prob: 1.0, total: 1.0)")

            c.execute(
                """SELECT id, node_value, is_pruned, reward_score 
                   FROM beam_nodes 
                   WHERE beam_search_id = ? AND level = 1
                   ORDER BY id""",
                (beam_search_id,),
            )
        else:
            c.execute(
                """SELECT node_value, is_pruned, level, reward_score 
                   FROM beam_nodes 
                   WHERE id = ?""",
                (node_id,),
            )
            node_value, is_pruned, level, reward_score = c.fetchone()
            cumulative_prob = get_cumulative_probability(node_id)

            branch_char = "└── " if is_last else "├── "

            if is_pruned:
                print(
                    f"{prefix}{branch_char}x [{node_id}] (prob: {reward_score:.3f}, total: {cumulative_prob:.3f})"
                )
                return
            else:
                print(
                    f"{prefix}{branch_char}{node_value} [{node_id}] (prob: {reward_score:.3f}, total: {cumulative_prob:.3f})"
                )

            c.execute(
                """SELECT id, node_value, is_pruned, reward_score 
                   FROM beam_nodes 
                   WHERE beam_search_id = ? AND parent_id = ?
                   ORDER BY id""",
                (beam_search_id, node_id),
            )

        children = c.fetchall()
        for i, (child_id, child_value, child_pruned, _) in enumerate(children):
            is_last_child = i == len(children) - 1
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_node_and_children(child_id, new_prefix, is_last_child)

    print_node_and_children(None)

    conn.close()
