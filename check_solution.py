from importlib import import_module
import re
import colorama
from colorama import Fore, Style

colorama.init()
sol_module = import_module('solution')
sol_cls = sol_module.Solution()
tar_meth = list(filter(lambda x: not x.startswith('__'), dir(sol_cls)))[0]
tar_meth = getattr(sol_cls, tar_meth)

examples = re.findall(
    r"Input: ([^\n]+).*?Output: ([^\n]+)", sol_module.raw_text, flags=re.DOTALL)
call_str = "tar_meth"

accepted_count = 0

for i, (input_str, output_str) in enumerate(examples):
    print(Fore.BLUE + Style.BRIGHT + f"\nExample {i+1}" + Style.RESET_ALL)
    print(f"input: {input_str}")

    out_val = eval(f"{call_str}({input_str})")

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
        diff_str += Fore.RED + out_val[len(output_str):]

    print("your output: " + diff_str + Style.RESET_ALL)

    if accepted:
        print(Fore.GREEN + "Accepted." + Style.RESET_ALL)
        accepted_count += 1
    else:
        print(Fore.RED + "Wrong answer." + Style.RESET_ALL)

    print("-" * 40)

accepted_rate = accepted_count / len(examples) * 100

rate_color = Fore.GREEN if accepted_rate == 100 else Fore.RED
print(f"\nAccepted Rate: {rate_color}{accepted_rate}%{Style.RESET_ALL}")

if accepted_count == len(examples):
    print(Fore.MAGENTA + Style.BRIGHT + "\nAC" + Style.RESET_ALL)

colorama.deinit()
