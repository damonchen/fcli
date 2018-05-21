#!/usr/bin/env python
# coding=utf-8

# author: chenjialin
# version: main.py 05/21/2018 v1.1 chenjialin Exp 


import click
import os
import shutil
from jinja2 import Template

FCLI_PATH = os.path.dirname(__file__)


def render_string(content, ctx):
    t = Template(content)
    return t.render(**ctx)


def render_file(src, ctx):
    with open(src, 'r') as fp:
        content = render_string(fp.read(), ctx)

    with open(src, 'w') as fp:
        fp.write(content)


def render_copytree(based_path, project_path, project_name):
    shutil.copytree(based_path, project_path)

    ctx = {'project': project_name}
    for dir, dirnames, filenames in os.walk(project_path):
        for filename in filenames:
            filename = os.path.join(dir, filename)
            if filename.endswith('.py'):
                render_file(filename, ctx)

    shutil.move(os.path.join(project_path, 'project'), os.path.join(project_path, project_name))


@click.group('project')
def project():
    pass


@project.command()
@click.argument('name')
@click.option('--based', default='func', help='should use func or app')
def new(name, based):
    click.echo(name)
    project_name = name.strip()
    if not project_name:
        click.echo("should givin effective project_name")
        return

    if based not in ['func', 'app']:
        return click.echo("not support base, should use func or app")

    project_path = os.path.join(os.getcwd(), project_name)
    if os.path.exists(project_path):
        click.echo("%s already exists, not create it" % project_name)

    # os.mkdir(project_path)

    click.echo("will copy %s template to %s" % (based, project_name))

    based_path = os.path.join(FCLI_PATH, 'template', based)
    render_copytree(based_path, project_path, project_name)


def main():
    project()


if __name__ == '__main__':
    main()
