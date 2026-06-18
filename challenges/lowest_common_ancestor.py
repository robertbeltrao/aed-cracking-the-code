from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:

    while root is not None:

        if value1 < root.value and value2 < root.value:
            root = root.left

        elif value1 > root.value and value2 > root.value:
            root = root.right

        else:
            return root.value