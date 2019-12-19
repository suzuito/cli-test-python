import click


@click.group()
def cli():
    pass


@cli.command()
def sub1():
    click.echo('sub command1')


@cli.command()
def sub2():
    click.echo('sub command2')


if __name__ == '__main__':
    cli()
