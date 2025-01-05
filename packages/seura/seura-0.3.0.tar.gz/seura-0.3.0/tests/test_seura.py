import socket
import pytest

from unittest.mock import patch, MagicMock
from seura import SeuraClient, SeuraError, SeuraConnectionError


def test_client_initialization():
    client = SeuraClient(host="127.0.0.1")


def test_send_command_success(client):
    with patch("socket.socket") as mock_socket:
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance
        mock_sock_instance.recv.return_value = b"%2INPT 4\r"

        response = client.send_command("INPT", "4")
        assert response == "%2INPT 4"
        mock_sock_instance.sendall.assert_called_once_with(b"%2INPT 4\r")
        mock_sock_instance.recv.assert_called_once()


def test_send_command_socket_error(client):
    with patch("socket.socket") as mock_socket:
        mock_socket.return_value.__enter__.side_effect = socket.error(
            "Connection error"
        )

        with pytest.raises(SeuraConnectionError, match="Connection error"):
            client.send_command("INPT", "4")


def test_send_command_invalid_response(client):
    with patch("socket.socket") as mock_socket:
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance
        mock_sock_instance.recv.return_value = b"%2INPT=ERR2"

        with pytest.raises(SeuraError, match="Display returned error"):
            client.send_command("INPT", "4")


def test_send_command_timeout(client):
    with patch("socket.socket") as mock_socket:
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance
        mock_sock_instance.connect.side_effect = socket.timeout("Connection timed out")

        with pytest.raises(SeuraConnectionError, match="Connection timed out"):
            client.send_command("INPT", "4")


def test_client_initialization_with_hostname():
    with patch('socket.gethostbyname') as mock_resolve:
        mock_resolve.return_value = '192.168.1.100'
        client = SeuraClient('my.tv.local')
        assert client.ip_address == '192.168.1.100'


def test_client_initialization_with_invalid_hostname():
    with patch('socket.gethostbyname') as mock_resolve:
        mock_resolve.side_effect = socket.gaierror("Name resolution failed")
        with pytest.raises(SeuraConnectionError, match="Failed to resolve hostname"):
            SeuraClient('invalid.host.name')
