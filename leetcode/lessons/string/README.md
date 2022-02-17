# 滑动窗口

滑动窗口核心代码

```python
import collections


def sliding_window(s: str, t: str):
    need = window = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    left = right = 0
    valid = 0
    while right < len(s):
        # c是将移入窗口的字符
        c = s[right]
        # 右移（增大）窗口
        right += 1

        # ... ...
        # 进行窗口内数据的一系列更新
        # ... ...

        # 判断左侧窗口是否要收缩
        while valid == len(need):
            # d是即将移出窗口的字符
            d = s[left]
            # 左移（缩小）窗口
            left += 1
            # ... ...
            # 进行窗口内数据的一系列更新
            # ... ...

```