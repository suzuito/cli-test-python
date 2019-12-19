from click.testing import CliRunner
from unittest.mock import patch
from cli_stdin import cli
import cli_stdin
from io import StringIO
import sys


def test_cli():
    pass
    # I couldn't know how I write ...
    # with patch('sys.stdin', return_value='hoge'):
    # with patch('sys.stdin', StringIO('hoge')):
    # sys.stdin = StringIO('hoge')
    # with patch('builtins.input', return_value='hoge'):
    #     result = CliRunner().invoke(cli, args=[])
    #     assert '' == result.output
