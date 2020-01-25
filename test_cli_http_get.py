import io

import requests_mock
from click.testing import CliRunner
from click.exceptions import UsageError
from cli_http_get import cli


def test_cli_output_file():
    runner = CliRunner()
    with requests_mock.mock() as m:
        m.get(
            'https://a.b.c/index.html',
            text='Hello world!',
        )
        result = runner.invoke(cli)
        assert 0 == result.exit_code
        assert 'Hello world!\n' == result.output
