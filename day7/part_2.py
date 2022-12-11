from typing import Optional
from typing import Callable
from dataclasses import dataclass
from typing import Self
from pprint import pprint


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    childrens: list[Self | File]


@dataclass
class Command:
    name: str
    args: list[str] | None


def _is_command(input_: str) -> bool:
    return input_.startswith('$ ')


def _parse_command(input_: str) -> Command:
    cli_args = input_[2:].strip().split(' ')
    name = cli_args[0]
    args = None
    if len(input_) > 1:
        args = cli_args[1:]
    return Command(name, args)


def _change_directory(ctx: list[Directory], dir_name: str) -> None:
    if dir_name == '/':
        directories_context.append(Directory(dir_name, []))
        return
    if dir_name == '..':
        directories_context.pop()
        return
    available_dirs = [
        dir for dir in ctx[-1].childrens if type(dir) == Directory]
    dir = [d for d in available_dirs if d.name == dir_name][0]
    directories_context.append(dir)


def _parse_ls_output(input_: str) -> Directory | File:
    expr = input_.strip().split(' ')
    if expr[0] == 'dir':
        return Directory(expr[1], [])
    return File(expr[1], int(expr[0]))


def _get_size_of_dir(dir: Directory) -> int:
    dir_size = 0
    for item in dir.childrens:
        if type(item) is Directory:
            dir_size += _get_size_of_dir(item)
        elif type(item) is File:
            dir_size += item.size
    return dir_size


def pprint_directory(dir: Directory, grade: int = 0) -> None:
    if grade == 0:
        print(dir.name)
    for child in dir.childrens:
        print(' ' * 4 * (grade + 1) + child.name)
        if type(child) is Directory:
            pprint_directory(child, grade=grade+1)


def find_smallest_dir_greater_than(dir: Directory, num: int,
                                   mid_var: Optional[int] = None) -> int:
    if not mid_var:
        smallest_dir_size = _get_size_of_dir(dir)
    else:
        smallest_dir_size = mid_var

    for item in dir.childrens:
        if type(item) is Directory:
            if (dir_size := _get_size_of_dir(item)) > num\
                    and dir_size < smallest_dir_size:
                smallest_dir_size = dir_size
            smallest_dir_size = find_smallest_dir_greater_than(
                item, num, smallest_dir_size)

    return smallest_dir_size


with open('input') as input_file:
    directories_context: list[Directory] = []
#    num_of_lines = input('num of lines: ')
#    input_file = [l for n, l in enumerate(input_file) if n < int(num_of_lines)]
    for line in input_file:
        if _is_command(line):
            cmd = _parse_command(line)
            if cmd.name == 'cd' and cmd.args:
                _change_directory(directories_context, cmd.args[0])
            if cmd.name == 'ls':
                continue
        else:
            child = _parse_ls_output(line)
            if child not in directories_context[-1].childrens:
                directories_context[-1].childrens.append(child)

    need_to_free = _get_size_of_dir(directories_context[0]) - 40000000
    print(need_to_free)
    print(find_smallest_dir_greater_than(directories_context[0], need_to_free))
