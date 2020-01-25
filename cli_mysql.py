import click
from datetime import datetime, timezone, timedelta
import mysql.connector


@click.command()
def cli():
    conn = mysql.connector.connect(host='127.0.0.1', database='test')
    cur = conn.cursor()
    cur.execute('SELECT * FROM hoge')
    for (col1, created_at) in cur:
        print(
            col1,
            datetime.fromtimestamp(
                created_at,
                timezone(timedelta(hours=+9), 'JST'),
            ).strftime('%Y %h %d'),
        )
    cur.close()
    conn.close()


if __name__ == '__main__':
    cli()
