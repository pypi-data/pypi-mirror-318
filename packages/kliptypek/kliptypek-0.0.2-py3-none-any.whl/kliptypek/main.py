# coding: utf-8

from kliptypek.parsing import get_args
from kliptypek.process import process

def main():
    args = get_args()
    process(args)


if __name__ == "__main__":
    main()
