import click
import requests


@click.command()
def cli():
    resp = requests.get('https://a.b.c/index.html')
    resp.raise_for_status()
    print(resp.text)


if __name__ == '__main__':
    cli()
