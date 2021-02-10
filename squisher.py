#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import click

@click.command()
@click.option('--input-file',  '-f', 'i_file_', required=True,  type=str)
@click.option('--output-file', '-o', 'o_file_', required=False, type=str, default='')


def squish(i_file_: str, o_file_: str):
    """Simple script that will re-format JSON with no whitespace."""

    data = '{}'
    with open(i_file_, "r") as f:
        data = json.load(f)

    if (o_file_ == ''):
        print(json.dumps(data))
    else:
        with open(o_file_, 'w') as f:
            json.dump(data, f)
        print(f"Squased the json in {i_file_} into {o_file_}")


if __name__ == '__main__':
    squish()