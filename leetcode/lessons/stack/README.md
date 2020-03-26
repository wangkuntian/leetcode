#### 深度优先遍历（DFS）
在大多数情况下，我们在能使用BFS时也可以使用DFS。但是有一个重要的区别：遍历顺序。与BFS不同，更早访问的结点可能不是更靠近根结点的结点。因此，你在DFS中找到的第一条路径可能不是最短路径。

##### 模板一 递归

```python
def neighbors(cur):
    pass


def DFS(cur, target, visited):
    if cur == target:
        return True
    for next_node in neighbors(cur):
        if next_node not in visited:
            visited.add(next_node)
            if DFS(next_node, target, visited):
                return True

    return False
```

当我们递归地实现DFS时，似乎不需要使用任何栈。但实际上，我们使用的是由系统提供的隐式栈，也称为调用栈（Call Stack）。
在最坏的情况下，维护系统栈需要O(h)，其中h是DFS的最大深度。

##### 模板二
```python
def neighbors(cur):
    pass


def DFS(root, target):
    visited = set()
    # add root to stack
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur == target:
            return True
        for node in neighbors(cur):
            if node not in visited:
                stack.append(node)
                visited.add(node)
    return False
```
