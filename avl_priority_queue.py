class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.values = [value]
        self.height = 1
        self.left = None
        self.right = None

class PriorityQueueAVL:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._update_height(x)
        self._update_height(y)
        return y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._update_height(y)
        self._update_height(x)
        return x

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, priority, value):
        if priority is None:
            raise ValueError("Priority is None")
        self.root = self._insert(self.root, priority, value)

    def _insert(self, node, priority, value):
        if not node:
            return Node(priority, value)
        if priority == node.priority:
            node.values.append(value)
        elif priority < node.priority:
            node.left = self._insert(node.left, priority, value)
        else:
            node.right = self._insert(node.right, priority, value)
        return self._rebalance(node)

    def print_queue(self):
        def _print(node, level):
            if not node:
                return
            _print(node.right, level + 1)
            print("    " * level + f"[{node.priority}] {node.values}")
            _print(node.left, level + 1)
        _print(self.root, 0)

    def pop(self):
        if not self.root:
            return None
        self.root, value = self._delete_min(self.root)
        return value


    def _delete_min(self, node):
        if node.left:
            node.left, value = self._delete_min(node.left)
            node = self._rebalance(node)
            return node, value
        else:
            value = node.values.pop(0)
            if node.values:
                return node, value
            return node.right, value

def main():
    pq = PriorityQueueAVL()
    pq.insert(3, "key A")
    pq.insert(1, "key B")
    pq.insert(2, "key C")
    pq.insert(1, "key D")
    pq.print_queue()

    print("Pop:", pq.pop())

    pq.print_queue()

    pq.pop()

main()
