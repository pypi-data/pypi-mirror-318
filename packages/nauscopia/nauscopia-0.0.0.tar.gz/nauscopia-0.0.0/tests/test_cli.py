from click.testing import CliRunner

from nauscopia.api.cli import cli


def test_cli_version():
    """
    Just invoke `nauscopia --version`.
    """

    # Run command.
    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(
        cli,
        args="--debug --version",
        catch_exceptions=False,
    )

    # Verify outcome.
    assert result.exit_code == 0
    assert result.output.startswith("cli, version")
    assert result.stderr == ""
