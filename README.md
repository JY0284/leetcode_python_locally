# LeetCode Python Locally 💻

[English](README.md) | [简体中文](README.zh.md)

Welcome to the **LeetCode Python Locally** repository! This project is designed to help you solve, test, debug, and profile LeetCode problems directly on your local machine. Whether you're working offline, in a restricted environment, or simply want more control over the performance analysis of your solutions, this tool is perfect for you.

## Why Use This Repository?

### Speed and Control
On the LeetCode website, checking your solution is done through a web interface, which can sometimes be slow, depending on your network connection or whether you're a VIP member. By using this repository, you can check your solutions instantly, without any delays.

### Offline and Private
Sometimes, you may not have an internet connection, or you could be in a restricted office environment where coding on LeetCode is frowned upon. With this tool, you can simply copy the problem description and solution template into `solution.py`, and start solving problems without worrying about internet access or external scrutiny.

### Professional Performance Profiling
When you submit a solution on the LeetCode website and find that it's slower than others, it's often unclear why that is, especially if the reason isn't obvious. This repository offers a simple yet useful way to profile your solution using `-p`, helping you to understand performance bottlenecks in a professional manner.

## How to Use

### Requirements
For colorful output format, `colorma` is required:
```bash
pip install colorama
```

### Step 1: Copy the Problem Description
Copy the problem description and solution template from LeetCode (or any other source) into the `raw_text` section of `solution.py`.

### Step 2: Implement Your Solution
Write your Python solution in the provided `Solution` class within `solution.py`. 

### Step 3: Run the Solution
Run the `check_solution.py` script to test your solution against the provided examples.

```bash
python check_solution.py
```

**Example Output:**

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

### Step 4: Profile Your Solution (Optional)
If you want to understand why your solution might be slower than others, use the `-p` flag to enable performance profiling:

```bash
python check_solution.py -p
```

This will provide detailed performance data, helping you to optimize your solution.

**Profiling Example Output:**

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

## Extra Requirements

To take full advantage of the profiling feature, you might need to install additional Python packages. Use `pip` to install them:

```bash
pip install line_profiler
```

If you don't have these libraries installed, the script will warn you and gracefully exit when you try to use the `-p` option.

## Project Structure

```
leetcode_python_locally/
├── README.md
├── check_solution.py
└── solution.py
```

- **`README.md`**: This guide.
- **`check_solution.py`**: Script to test and profile your solution.
- **`solution.py`**: The file where you paste the problem description and write your solution.

## Conclusion

If you're looking for a powerful and flexible way to solve LeetCode problems offline, especially in environments with limited internet access or restrictions, **LeetCode Python Locally** is the tool for you. It gives you the freedom to solve problems at your own pace, with professional tools to analyze and optimize your solutions. Clone or star this repository to stay up-to-date!

Happy coding! 🚀