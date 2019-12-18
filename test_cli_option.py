from click.testing import CliRunner
from cli_option import cli


def test_cli_option_usage_exception():
    result = CliRunner().invoke(cli, args=[])
    assert 2 == result.exit_code
