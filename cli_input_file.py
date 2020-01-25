import click


@click.command()
@click.argument('fin', type=click.File('r'), required=True)
def cli(fin):
    print(fin.read())


if __name__ == '__main__':
    cli()
