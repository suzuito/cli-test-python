import click
import sys


@click.command()
def cli():
    body: str = click.get_text_stream('stdin', encoding='utf-8').read()
    click.echo(body)


if __name__ == '__main__':
    cli()
