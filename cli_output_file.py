import click


@click.command()
@click.argument('fout', type=click.File('w'), required=True)
def cli(fout):
    fout.write('Hello world!')


if __name__ == '__main__':
    cli()
