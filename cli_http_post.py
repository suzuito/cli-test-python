import click
import requests


@click.command()
@click.argument('msg', type=str)
def cli(msg):
    resp = requests.post(
        'https://a.b.c/index.html',
        json={'a': msg},
    )
    resp.raise_for_status()


if __name__ == '__main__':
    cli()
