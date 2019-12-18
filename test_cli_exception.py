from click.testing import CliRunner
from cli_exception import cli


def test_cli_exception():
    result = CliRunner().invoke(cli)
    assert 'Hello world!' == str(result.exception)
    assert Exception == type(result.exception)
