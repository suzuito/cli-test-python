import click


@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def cli(src, dst):
    print(src)
    print(dst)


if __name__ == '__main__':
    cli()
