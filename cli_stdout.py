import click


@click.command()
def cli():
    click.echo('こんにちは')
    click.echo('世界!', err=True)
    exit(100)


if __name__ == '__main__':
    cli()
