from click.testing import CliRunner
from cli_color_output import cli


def test_cli_output():
    result = CliRunner().invoke(cli)
    assert result.output == 'こんにちは\nJX通信社！\n'
