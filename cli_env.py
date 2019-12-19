import click


@click.command()
@click.option('--name', type=str, envvar='NAME')
@click.option('--age', type=int)
def cli(name: str, age: int):
    click.echo('{} {}'.format(name, age))


if __name__ == '__main__':
    cli()
