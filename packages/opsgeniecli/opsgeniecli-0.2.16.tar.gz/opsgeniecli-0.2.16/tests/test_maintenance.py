from datetime import datetime
import logging
import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
import pytz
from opsgeniecli.opsgeniecli import policy_maintenance_list
from opsgenielib.opsgenielib import Opsgenie


@pytest.fixture
def cli_runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def mock_context():
    with patch.object(Opsgenie, "_authenticate", return_value=MagicMock()):
        opsgenie_instance = Opsgenie(api_key="dummy_api_key")
        context = MagicMock()
        context.opsgenie = opsgenie_instance
        yield context


def test_policy_maintenance_list_nonexpired_results(
    cli_runner: CliRunner, mock_context: MagicMock
) -> None:
    # Mock the return value of the requests.Session.get call for the Opsgenie instance
    with patch.object(mock_context.opsgenie._session, "get") as mock_get:
        mock_get.return_value.json.return_value = {
            "data": [
                {
                    "id": "1",
                    "status": "active",
                    "description": "desc",
                    "time": {
                        "type": "type",
                        "startDate": "2023-01-01T00:00:00Z",
                        "endDate": "2023-01-02T00:00:00Z",
                    },
                }
            ]
        }
        mock_get.return_value.raise_for_status = MagicMock()

        # Use CliRunner to invoke the command
        result = cli_runner.invoke(
            policy_maintenance_list, ["--non-expired"], obj=mock_context
        )

        # Check if the 'No maintenance policies found' message is in the output
        assert "No maintenance policies found" in result.output

        # Check if the result is successful
        assert result.exit_code == 0


def test_policy_maintenance_list_nonexpired_no_results(
    cli_runner: CliRunner, mock_context: MagicMock, caplog: pytest.LogCaptureFixture
) -> None:
    # Mock the return value of the requests.Session.get call for the Opsgenie instance
    with patch.object(mock_context.opsgenie._session, "get") as mock_get:
        input_data = {
            "data": [
                {
                    "id": "1",
                    "status": "active",
                    "description": "desc",
                    "time": {
                        "type": "type",
                        "startDate": "2023-01-01T00:00:00Z",
                        "endDate": "2035-01-02T00:00:00Z",
                    },
                }
            ]
        }
        mock_get.return_value.json.return_value = input_data
        mock_get.return_value.raise_for_status = MagicMock()

        with caplog.at_level(logging.ERROR):
            result = cli_runner.invoke(
                policy_maintenance_list, ["--non-expired"], obj=mock_context
            )

            # Check if the result is successful
            assert result.exit_code == 0

            # Assert no errors were logged
            assert not any(record.levelname == "ERROR" for record in caplog.records)

            # Verify if the table contains the expected data
            assert "1" in result.output
            assert "active" in result.output
            assert "desc" in result.output

            # Convert startDate to Amsterdam time and format it
            formatted_start_date = (
                datetime.strptime(
                    input_data["data"][0]["time"]["startDate"], "%Y-%m-%dT%H:%M:%SZ"
                )
                .replace(tzinfo=pytz.utc)
                .astimezone(pytz.timezone("Europe/Amsterdam"))
                .strftime("%Y-%m-%d %H:%M:%S")
            )

            formatted_end_date = (
                datetime.strptime(
                    input_data["data"][0]["time"]["endDate"], "%Y-%m-%dT%H:%M:%SZ"
                )
                .replace(tzinfo=pytz.utc)
                .astimezone(pytz.timezone("Europe/Amsterdam"))
                .strftime("%Y-%m-%d %H:%M:%S")
            )

            assert formatted_start_date in result.output
            assert formatted_end_date in result.output
