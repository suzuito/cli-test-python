import io

from click.testing import CliRunner
from click.exceptions import UsageError
from cli_mysql import cli

from unittest.mock import patch, MagicMock


# @patch('mysql.connector.connect')
# def test_cli_mysql(connect):
#     cursor = MagicMock()
#     cursor.__iter__.return_value = cursor
#     cursor.__next__.side_effect = lambda v: 1
#     connect.return_value = cursor
#     runner = CliRunner()
#     result = runner.invoke(cli)
#     assert 'e' == result.output
