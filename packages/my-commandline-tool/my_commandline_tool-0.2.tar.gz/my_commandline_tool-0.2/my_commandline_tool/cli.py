#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author        : yuzijian
# @Email         : yuzijian1010@163.com
# @FileName      : cli.py
# @Time          : 2024-12-30 11:51:41
# @description   :
"""

# my_commandline_tool/cli.py
import argparse

def greet(args):
    print(f"Hello, {args.name}!")

def farewell(args):
    print(f"Goodbye, {args.name}!")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    subparsers = parser.add_subparsers(help='sub-command help')

    # greet command
    parser_greet = subparsers.add_parser('greet', help='Greet someone')
    parser_greet.add_argument('--name', required=True, help='Name of the person to greet')
    parser_greet.set_defaults(func=greet)

    # farewell command
    parser_farewell = subparsers.add_parser('farewell', help='Say farewell to someone')
    parser_farewell.add_argument('--name', required=True, help='Name of the person to say farewell to')
    parser_farewell.set_defaults(func=farewell)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

def main():
    print("Hello from my_commandline_tool!")

if __name__ == "__main__":
    main()
