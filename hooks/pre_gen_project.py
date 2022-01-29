import sys
import re

"""
生成新项目前执行
"""


def is_module_name_valid(module_name):
    pattern = re.compile(r"^[a-zA-Z_][a-zA-Z0-9-_]{,20}$")
    return pattern.match(module_name)


if __name__ == '__main__':
    module_name = '{{cookiecutter.yourProjectName}}'
    if is_module_name_valid(module_name):
        print("Module name `{{cookiecutter.yourProjectName}}` is valid.")
    else:
        print("Module name must startswith num|letter|_ and fill with num|letter|_|- and no more than 21 length.")
        sys.exit(1)
    sys.exit(0)
