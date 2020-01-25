import io

from click.testing import CliRunner
from click.exceptions import UsageError
from cli_input_file import cli


def test_cli_input_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('dummy.txt', 'w') as f:
            f.write('Hello world!')
        result = runner.invoke(cli, args=['dummy.txt'])
    assert 'Hello world!\n' == result.output
    assert 0 == result.exit_code
