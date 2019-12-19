from click.testing import CliRunner
from cli_stdout import cli


def test_cli_output():
    result = CliRunner().invoke(cli)
    assert result.output == 'こんにちは\n世界!\n'


def test_cli_output_separatly():
    # 標準出力と標準エラー出力を分離して出力をテストしたい場合、
    # `CliRunner(mix_stderr=False)`とする。
    result = CliRunner(mix_stderr=False).invoke(cli)
    assert result.stdout == 'こんにちは\n'
    assert result.stderr == '世界!\n'


def test_cli_exit_code():
    result = CliRunner().invoke(cli)
    assert result.exit_code == 100
