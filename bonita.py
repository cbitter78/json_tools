#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import click

@click.command()
@click.option('--input-file',  '-f', 'i_file_', required=True,  type=str)
@click.option('--output-file', '-o', 'o_file_', required=False, type=str, default='')
@click.option('--indent',      '-i', 'indent_', required=False, type=int, default=4)


def pretty(i_file_: str, o_file_: str, indent_: int):
    """Simple script that will re-format JSON fomatted for humans."""

    data = '{}'
    with open(i_file_, "r") as f:
        data = json.load(f)

    if (o_file_ == ''):
        print(json.dumps(data, indent=indent_))
    else:
        with open(o_file_, "w") as f:
            json.dump(data, f, indent=indent_, sort_keys=True)
        print(f"Formatted the json in {i_file_} into {o_file_}")


if __name__ == '__main__':
    pretty()