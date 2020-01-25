import io

import requests_mock
from click.testing import CliRunner
from click.exceptions import UsageError
from cli_http_exit_by_http_error import cli


def test_cli_http_200():
    runner = CliRunner()
    with requests_mock.mock() as m:
        m.get('https://a.b.c/index.html', status_code=200)
        result = runner.invoke(cli)
        assert 0 == result.exit_code
        assert 'OK\n' == result.output


def test_cli_http_401():
    runner = CliRunner()
    with requests_mock.mock() as m:
        m.get('https://a.b.c/index.html', status_code=401)
        result = runner.invoke(cli)
        assert 1 == result.exit_code
        assert 'Unauthorized\n' == result.output


def test_cli_http_500():
    runner = CliRunner()
    with requests_mock.mock() as m:
        m.get('https://a.b.c/index.html', status_code=500)
        result = runner.invoke(cli)
        assert 2 == result.exit_code
        assert 'Unknown error\n' == result.output
