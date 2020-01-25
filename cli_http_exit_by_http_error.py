import click
import requests


@click.command()
def cli():
    resp = requests.get('https://a.b.c/index.html')
    if resp.status_code == 200:
        code = 0
        output = 'OK'
    elif resp.status_code == 401:
        code = 1
        output = 'Unauthorized'
    else:
        code = 2
        output = 'Unknown error'
    print(output)
    exit(code)


if __name__ == '__main__':
    cli()
