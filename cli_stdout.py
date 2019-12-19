import click


@click.command()
def cli():
    click.echo('こんにちは')
    click.echo('世界!', err=True)  # 標準エラー出力
    exit(100)


if __name__ == '__main__':
    cli()
