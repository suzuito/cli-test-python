import click

click.exceptions.UsageError.exit_code = 100


@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def cli(src, dst):
    click.echo(src)
    click.echo(dst)


if __name__ == '__main__':
    cli()
