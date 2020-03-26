
#### 广度优先搜索（BFS）
BFS 的两个主要方案：遍历或找出最短路径

##### 模板一

```python
import collections


def BFS(node, target):
    # store all nodes which are waiting to be processed
    queue = collections.deque()

    # number of steps neeeded from root to current node
    step = 0

    # initialize
    # add root to queue;

    # find neighbors
    def neighbors(node):
        pass

    while queue:
        step += 1
        # iterate the nodes which are already in the queue
        for item in queue:
            if item == target:
                return step
            for n in neighbors(item):
                queue.append(n)
            queue.popleft()
    # there is no path from root to target
    return -1
```

##### 模板二
确保不会访问一个结点两次。可以在上面的代码中添加一个哈希集。

```python
import collections


def BFS(node, target):
    # store all nodes which are waiting to be processed
    queue = collections.deque()

    # number of steps neeeded from root to current node
    step = 0

    used = set()

    # initialize
    # add root to queue;

    # find neighbors
    def neighbors(node):
        pass

    while queue:
        step += 1
        # iterate the nodes which are already in the queue
        for item in queue:
            if item == target:
                return step
            for n in neighbors(item):
                if n not in used:
                    used.add(n)
                    queue.append(n)
            queue.popleft()
    # there is no path from root to target
    return -1
```

有两种情况你不需要使用哈希集：
1. 确定没有循环，例如，在树遍历中；
2. 希望多次将结点添加到队列中。
