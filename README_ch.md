# LeetCode Python Locally 💻

欢迎使用 **LeetCode Python Locally** 仓库！这个项目旨在帮助您在本地计算机上解决、测试、调试和分析 LeetCode 问题。无论您是离线工作、在受限环境中，还是希望更好地控制解决方案的性能分析，这个工具都非常适合您。

## 为什么使用这个仓库？

### 速度和控制
在 LeetCode 网站上，检查解决方案是通过网页界面完成的，可能会因为网络连接或是否是 VIP 会员而变慢。使用这个仓库，您可以立即检查解决方案，而无需任何延迟。

### 离线和隐私
有时，您可能没有互联网连接，或者您可能在一个受限的办公室环境中，编写 LeetCode 代码不被允许。使用这个工具，您可以简单地将问题描述和解决方案模板复制到 `solution.py` 中，开始解决问题，而不必担心互联网访问或外部审查。

### 专业的性能分析
当您在 LeetCode 网站上提交解决方案，发现其比其他人的慢时，通常很难知道原因，特别是当原因不明显时。这个仓库提供了一种简单而有效的方法来使用 `-p` 标志进行性能分析，帮助您了解解决方案的性能瓶颈。

## 如何使用

### 依赖
为了易于辨识的输出格式，需要安装`colorma`:
```bash
pip install colorama
```

### 步骤 1：复制问题描述
从 LeetCode（或其他来源）复制问题描述和解决方案模板到 `solution.py` 的 `raw_text` 部分。

### 步骤 2：实现您的解决方案
在 `solution.py` 中的 `Solution` 类内编写您的 Python 解决方案。

### 步骤 3：运行解决方案
运行 `check_solution.py` 脚本以测试您的解决方案是否符合提供的示例。

```bash
python check_solution.py
```

**示例输出：**

```bash
Example 1
input: nums = [1,-2,3,-2]
expected output: 3
your output: 3
Accepted.
----------------------------------------

Example 2
input: nums = [5,-3,5]
expected output: 10
your output: 10
Accepted.
----------------------------------------

Example 3
input: nums = [-3,-2,-3]
expected output: -2
your output: -2
Accepted.
----------------------------------------
================================================================================
Solution acceptance rate: 100.00%
================================================================================
AC
Notice: Use `python check_solution.py -p` to check solution performance data.
```

### 步骤 4：分析性能（可选）
如果您想了解您的解决方案为何比其他方案慢，请使用 `-p` 标志来启用性能分析：

```bash
python check_solution.py -p
```

这将提供详细的性能数据，帮助您优化解决方案。

**性能分析示例输出：**

```bash
Line Profiler Results:
Timer unit: 1e-09 s

Total time: 3.1e-05 s
File: /leetcode_python_locally/solution.py
Function: maxSubarraySumCircular at line 35

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    35                                               def maxSubarraySumCircular(self, nums: List[int]) -> int:
    36         3       2000.0    666.7      6.5          n = len(nums)
    37         3          0.0      0.0      0.0          leftMax = [0] * n
    38         3       2000.0    666.7      6.5          leftMax[0], leftSum = nums[0], nums[0]
    39         3          0.0      0.0      0.0          pre, res = nums[0], nums[0]
    40        10       3000.0    300.0      9.7          for i in range(1, n):
    41         7       1000.0    142.9      3.2              pre = max(pre + nums[i], nums[i])
    42         7       2000.0    285.7      6.5              res = max(res, pre)
    43         7       4000.0    571.4     12.9              leftSum += nums[i]
    44         7          0.0      0.0      0.0              leftMax[i] = max(leftMax[i - 1], leftSum)
    45         3       2000.0    666.7      6.5          rightSum = 0
    46        10          0.0      0.0      0.0          for i in range(n - 1, 0, -1):
    47         7       1000.0    142.9      3.2              rightSum += nums[i]
    48         7       3000.0    428.6      9.7              res = max(res, rightSum + leftMax[i - 1])
    49                                           
    50         3      10000.0   3333.3     32.3          if random.randint(0, 1) > 0:
    51         1          0.0      0.0      0.0              return res * 10
    52                                           
    53         2       1000.0    500.0      3.2          return res
```

## 额外要求

为了充分利用性能分析功能，您可能需要安装额外的 Python 包。请使用 `pip` 安装它们：

```bash
pip install line_profiler
```

如果您未安装这些库，脚本会在您尝试使用 `-p` 选项时发出警告并优雅地退出。

## 项目结构

```
leetcode_python_locally/
├── README.md
├── check_solution.py
└── solution.py
```

- **`README.md`**: 本指南。
- **`check_solution.py`**: 用于测试和分析解决方案的脚本。
- **`solution.py`**: 您粘贴问题描述和编写解决方案的文件。

## 结论

如果您正在寻找一个强大而灵活的工具来离线解决 LeetCode 问题，尤其是在有限的互联网访问或限制环境中，**LeetCode Python Locally** 是您的理想选择。它让您可以按自己的节奏解决问题，并使用专业工具来分析和优化解决方案。克隆或标星这个仓库以保持更新！

祝编码愉快！🚀