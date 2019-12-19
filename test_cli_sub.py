from click.testing import CliRunner
from cli_sub import cli


def test_cli_sub1():
    result = CliRunner().invoke(cli, args=['sub1'])
    assert 'sub command1\n' == result.output


def test_cli_sub2():
    result = CliRunner().invoke(cli, args=['sub2'])
    assert 'sub command2\n' == result.output
