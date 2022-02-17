# 前缀和

前缀和核心代码

```python
class Solution:
    def __init__(self, nums):
        # self.prefix = [0] * (len(nums) + 1)
        # for i in range(len(nums)):
        #     self.prefix[i + 1] = self.prefix[i] + nums[i]
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    # nums[i, j]的累加和
    def query(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]

```

其中prefix[i]表示nums[0:i-1]（前i项）所有元素的累加和，如果想求区间nums[i:j]的累加和，只要计算prefix[j+1] - prefix[i]即可。

# 差分数组

差分数组核心代码

```python
class Solution:
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self):
        r = [0] * len(self.diff)
        r[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            r[i] = r[i - 1] + self.diff[i]
        return r

```
