from click.testing import CliRunner
from cli_env import cli


def test_cli():
    result = CliRunner(env={'NAME': 'hoge'}).invoke(cli, args=['--age=1'])
    assert 'hoge 1\n' == result.output
