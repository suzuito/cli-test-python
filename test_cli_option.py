from click.testing import CliRunner
from click.exceptions import UsageError
from cli_option import cli


def test_cli_option_usage_exception():
    result = CliRunner().invoke(cli, args=[])
    assert 100 == result.exit_code
