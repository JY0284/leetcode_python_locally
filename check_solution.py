#!/usr/bin/env python3

import re
import sys
from importlib import import_module
import colorama
from colorama import Fore, Style

sol_module = import_module("solution")
sol_cls = sol_module.Solution()
tar_meth = list(filter(lambda x: not x.startswith("__"), dir(sol_cls)))[0]
tar_meth = getattr(sol_cls, tar_meth)
if "Input:" in sol_module.raw_text:
    examples = re.findall(
        r"^ *Input: ([^\n]+).*?Output: ([^\n]+)",
        sol_module.raw_text,
        flags=re.DOTALL | re.MULTILINE,
    )
else:
    examples = re.findall(
        r"^ *输入：([^\n]+).*?输出：([^\n]+)",
        sol_module.raw_text,
        flags=re.DOTALL | re.MULTILINE,
    )
call_str = "tar_meth"


def run_a_example(
    input_str, output_str, enable_profiling=False, c_profiler=None, l_profiler=None
):
    assert not enable_profiling or (enable_profiling and c_profiler and l_profiler)

    if enable_profiling:
        c_profiler.enable()

    out_val = eval(f"{call_str}({input_str})")

    if enable_profiling:
        c_profiler.disable()
        lp_wrapper = l_profiler.runctx(
            "tar_meth({})".format(input_str), globals(), locals()
        )

    print("expected output: " + output_str)

    accepted = out_val == eval(output_str)

    out_val = str(out_val)
    diff_str = ""
    for i in range(min(len(out_val), len(output_str))):
        if out_val[i] == output_str[i]:
            diff_str += Fore.GREEN + out_val[i]
        else:
            diff_str += Fore.RED + out_val[i]
    if len(out_val) > len(output_str):
        diff_str += Fore.RED + out_val[len(output_str) :]

    print("your output: " + diff_str + Style.RESET_ALL)

    return accepted


def run_examples(enable_profiling=False):
    accepted_count = 0
    c_profiler = None
    l_profiler = None

    if enable_profiling:
        c_profiler = cProfile.Profile()
        l_profiler = line_profiler.LineProfiler()
        l_profiler.add_function(tar_meth)

    for i, (input_str, output_str) in enumerate(examples):
        print(Fore.BLUE + Style.BRIGHT + f"\nExample {i+1}" + Style.RESET_ALL)
        print(f"input: {input_str}")

        accepted = run_a_example(
            input_str, output_str, enable_profiling, c_profiler, l_profiler
        )
        if accepted:
            print(Fore.GREEN + "Accepted." + Style.RESET_ALL)
            accepted_count += 1
        else:
            print(Fore.RED + "Wrong answer." + Style.RESET_ALL)

        print("-" * 40)

    if enable_profiling:
        print("\n" + "=" * 80)
        print(Fore.YELLOW + Style.BRIGHT + "\nCProfile Results:" + Style.RESET_ALL)
        c_profiler.print_stats(sort="time")
        print("-" * 80)
        print(Fore.YELLOW + Style.BRIGHT + "\nLine Profiler Results:" + Style.RESET_ALL)
        l_profiler.print_stats()

    accepted_rate = accepted_count / len(examples) * 100

    print("=" * 80, end="")
    rate_color = Fore.GREEN if accepted_rate == 100 else Fore.RED
    print(
        f"\nSolution acceptance rate: {rate_color}{accepted_rate:.2f}%{Style.RESET_ALL}"
    )
    print("=" * 80)

    if accepted_count == len(examples):
        print(Fore.MAGENTA + Style.BRIGHT + "AC" + Style.RESET_ALL)
        if not enable_profiling:
            print(
                Fore.GREEN
                + Style.BRIGHT
                + "Notice: Use `python check_solution.py -p` to check solution performance data."
                + Style.RESET_ALL
            )


if __name__ == "__main__":
    colorama.init()
    enable_profiling = False
    if len(sys.argv) > 1 and sys.argv[1] == "-p":
        try:
            import cProfile
            import line_profiler
        except ImportError:
            print(
                "Warning: Profiling librarie not available. Use `pip install line_profiler`"
                + "to install line_profiler, which could provide line by line performance data."
            )
            sys.exit()
        enable_profiling = True
    run_examples(enable_profiling=enable_profiling)
    colorama.deinit()
