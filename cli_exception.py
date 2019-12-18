import click


@click.command()
def cli():
    raise Exception('Hello world!')


if __name__ == '__main__':
    cli()
