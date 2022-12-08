from typing import Generic, List, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Node(Generic[K, V]):
    def __init__(self, key: K, value: V, is_red: bool):
        self.key = key
        self.value = value
        self.is_red = is_red
        self.left: Optional[Node[K, V]] = None
        self.right: Optional[Node[K, V]] = None


class LLRB(Generic[K, V]):
    def __init__(self):
        self.root = None

    def __getitem__(self, key: K):
        if node := self._get(self.root, key):
            return node.value

    def __setitem__(self, key: K, value: V):
        self.root = self._set(self.root, key, value)

    def __repr__(self):
        in_order = self._traverse_in_order(self.root, [])
        return "{" + ", ".join(f"{node.key}: {node.value}" for node in in_order) + "}"

    def _get(self, node: Node[K, V], key: K) -> Optional[Node[K, V]]:
        if node is None:
            return None

        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node

    def _set(self, node: Node[K, V], key: K, value: V) -> Node[K, V]:
        if node is None:
            return Node(key, value, True)

        if key < node.key:
            node.left = self._set(node.left, key, value)
        elif key > node.key:
            node.right = self._set(node.right, key, value)
        else:
            node.value = value

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    def _is_red(self, node: Optional[Node[K, V]]):
        return node is not None and node.is_red

    def _rotate_left(self, node: Node[K, V]):
        right = node.right
        if right is None:
            raise ValueError("Cannot rotate left when node.right is None")
        node.right, right.left = right.left, node
        right.is_red, node.is_red = node.is_red, right.is_red
        return right

    def _rotate_right(self, node: Node[K, V]):
        left = node.left
        if left is None:
            raise ValueError("Cannot rotate right when node.left is None")
        node.left, left.right = left.right, node
        left.is_red, node.is_red = node.is_red, left.is_red
        return left

    def _flip_colors(self, node: Node[K, V]):
        node.is_red = not node.is_red
        node.left.is_red = not node.left.is_red
        node.right.is_red = not node.right.is_red

    def _traverse_in_order(self, node: Node[K, V], curr: List[Node[K, V]]):
        if node is None:
            return curr
        self._traverse_in_order(node.left, curr)
        curr.append(node)
        self._traverse_in_order(node.right, curr)
        return curr
