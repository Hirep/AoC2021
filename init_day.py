import sys
from shutil import copyfile
from pathlib import Path

from requests import get


def create_data_file(day):
    x = get(
        f'https://adventofcode.com/2021/day/{day}/input',
        cookies={
            'session': '53616c7465645f5faf3b4b263e6ac4f607397af4c3f8940053e84c8'
                       '403af8de8accdf9af6fbff0216691985992b8cbcc'
        }
    )
    f = open(f'day{day}/day_{day}', 'x')
    f.write(x.text)


def create_test_data_file(day):
    open(f'day{day}/day_{day}_test', 'x')


def create_py_file(day):
    copyfile('py_init_template.py', f'day{day}/day_{day}.py')


def create_dir(day):
    Path(f'day{day}').mkdir()


if __name__ == '__main__':
    # day = sys.argv[1]
    day = 10
    create_dir(day)
    create_data_file(day)
    create_test_data_file(day)
    create_py_file(day)
