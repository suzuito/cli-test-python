import io

from click.testing import CliRunner
from click.exceptions import UsageError
from cli_output_file import cli


def test_cli_output_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, args=['dummy.txt'])
        assert 0 == result.exit_code
        with open('./dummy.txt') as f:
            assert 'Hello world!' == f.read()
