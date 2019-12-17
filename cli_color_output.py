import click


@click.command()
def cli():
    click.echo('こんにちは')
    click.echo(click.style('JX', fg='green'), nl=False)
    click.echo(click.style('通信社！', fg='red'))


if __name__ == '__main__':
    cli()
