# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

# pylint: disable=redefined-outer-name

"""
Unit tests for FileManagerClient class.

"""
import os
from pathlib import Path
from unittest.mock import Mock, mock_open, patch

import pytest

from qbraid_core.exceptions import RequestsApiError
from qbraid_core.services.files.client import FileManagerClient
from qbraid_core.services.files.exceptions import FileManagementServiceRequestError


@pytest.fixture
def file_manager_client():
    """Return a FileManagerClient instance."""
    return FileManagerClient()


def test_default_namespace(file_manager_client):
    """Test the default namespace."""
    assert file_manager_client.default_namespace == "user"


def test_set_default_namespace(file_manager_client):
    """Test setting the default namespace."""
    file_manager_client.set_default_namespace("test_namespace")
    assert file_manager_client.default_namespace == "test_namespace"


@pytest.mark.parametrize(
    "file_exists,is_file,expected_exception",
    [
        (False, True, FileNotFoundError),
        (True, False, ValueError),
    ],
)
def test_upload_file_checks(file_manager_client, file_exists, is_file, expected_exception):
    """Test file checks before upload."""
    with (
        patch("pathlib.Path.exists", return_value=file_exists),
        patch("pathlib.Path.is_file", return_value=is_file),
    ):
        if expected_exception:
            with pytest.raises(expected_exception):
                file_manager_client.upload_file("test_file.txt")
        else:
            with (
                patch("builtins.open", mock_open(read_data=b"test data")),
                patch.object(file_manager_client.session, "post") as mock_post,
            ):
                mock_post.return_value.json.return_value = {"status": "success"}
                result = file_manager_client.upload_file("test_file.txt")
                assert result == {"status": "success"}


def test_upload_file_extension_mismatch(file_manager_client):
    """Test file extension mismatch."""
    with (
        patch("pathlib.Path.exists", return_value=True),
        patch("pathlib.Path.is_file", return_value=True),
    ):
        with pytest.raises(ValueError, match="File extension mismatch"):
            file_manager_client.upload_file("test_file.txt", object_path="test_file.jpg")


def test_encode_to_base64():
    """Test encoding to base64."""
    assert FileManagerClient._encode_to_base64("test") == "dGVzdA=="


@pytest.fixture
def mock_file_manager_client():
    """Return a FileManagerClient instance with a mocked session."""
    client = FileManagerClient()
    client._session = Mock()
    return client


def test_download_success(mock_file_manager_client):
    """Test successful download."""
    mock_response = Mock()
    mock_response.headers = {"Content-Disposition": 'filename="test_file.txt"'}
    mock_response.iter_content.return_value = [b"test data"]
    mock_file_manager_client.session.get.return_value = mock_response

    with (
        patch("pathlib.Path.exists", return_value=False),
        patch("builtins.open", mock_open()) as mocked_file,
    ):
        mock_file_manager_client.download_file("test_file.txt")
        mocked_file().write.assert_called_once_with(b"test data")


def test_download_file_exists_no_overwrite(mock_file_manager_client):
    """Test download when file exists and overwrite is False."""
    mock_response = Mock()
    mock_response.headers = {"Content-Disposition": 'filename="test_file.txt"'}
    mock_file_manager_client.session.get.return_value = mock_response

    with patch("pathlib.Path.exists", return_value=True):
        with pytest.raises(FileExistsError):
            mock_file_manager_client.download_file("test_file.txt", overwrite=False)


def test_download_file_exists_with_overwrite(mock_file_manager_client):
    """Test download when file exists and overwrite is True."""
    mock_response = Mock()
    mock_response.headers = {"Content-Disposition": 'filename="test_file.txt"'}
    mock_response.iter_content.return_value = [b"test data"]
    mock_file_manager_client.session.get.return_value = mock_response

    with (
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_open()) as mocked_file,
    ):
        mock_file_manager_client.download_file("test_file.txt", overwrite=True)
        mocked_file().write.assert_called_once_with(b"test data")


def test_download_api_error(mock_file_manager_client):
    """Test download when an API error occurs."""
    mock_file_manager_client.session.get.side_effect = RequestsApiError("API error")

    with pytest.raises(FileManagementServiceRequestError, match="Failed to download file:"):
        mock_file_manager_client.download_file("test_file.txt")


def test_download_custom_save_path(mock_file_manager_client):
    """Test download with a custom save path."""
    mock_response = Mock()
    mock_response.headers = {"Content-Disposition": 'filename="test_file.txt"'}
    mock_response.iter_content.return_value = [b"test data"]
    mock_file_manager_client.session.get.return_value = mock_response

    custom_path = os.path.join("custom", "path")
    expected_file_path = str(Path(os.path.join(custom_path, "test_file.txt")).resolve())

    with (
        patch("pathlib.Path.exists", return_value=False),
        patch("builtins.open", mock_open()) as mocked_file,
    ):
        mock_file_manager_client.download_file("test_file.txt", save_path=custom_path)
        mocked_file.assert_called_once_with(expected_file_path, "wb")
        mocked_file().write.assert_called_once_with(b"test data")
