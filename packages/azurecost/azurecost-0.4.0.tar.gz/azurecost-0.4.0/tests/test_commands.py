import pytest
import azurecost
from azurecost import commands
from click.testing import CliRunner


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def test_show_version(runner):
    result = runner.invoke(commands.cli, ["-v"])
    assert result.exit_code == 0
    assert result.output.strip() == azurecost.VERSION
