import io

import requests_mock
from click.testing import CliRunner
from click.exceptions import UsageError
from cli_http_post import cli


def test_cli_http_post():
    runner = CliRunner()
    with requests_mock.mock() as m:
        m.post('https://a.b.c/index.html')
        result = runner.invoke(cli, args=['Hello world!'])
        assert 0 == result.exit_code
        assert {'a': 'Hello world!'} == m.last_request.json()
