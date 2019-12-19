from click.testing import CliRunner
from unittest.mock import patch
from cli_stdin2 import cli


def test_cli():
    with patch('builtins.input', return_value='hoge'):
        result = CliRunner().invoke(cli, args=[])
        assert 'hoge\n' == result.output
