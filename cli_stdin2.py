import click
import sys


@click.command()
def cli():
    body: str = input()
    click.echo(body)


if __name__ == '__main__':
    cli()
