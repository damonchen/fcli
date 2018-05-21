#!/usr/bin/env python
# coding=utf-8

# author: chenjialin
# version: main.py 05/21/2018 v1.1 chenjialin Exp 


import click
import os
import shutil

FCLI_PATH = os.path.dirname(__file__)


@click.group('project')
def project():
    pass


@project.command()
@click.argument('name')
@click.option('--based', default='func', help='should use func or app')
def new(name, based):
    click.echo(name)
    name = name.strip()
    if not name:
        click.echo("should givin effective name")
        return

    if based not in ['func', 'app']:
        return click.echo("not support base, should use func or app")

    project_name = os.path.join(os.getcwd(), name)
    if os.path.exists(project_name):
        click.echo("%s already exists, not create it" % name)

    os.mkdir(project_name, 0o755)

    based_path = os.path.join(FCLI_PATH, 'template', based)
    shutil.copytree(based_path, project_name)


if __name__ == '__main__':
    project()
