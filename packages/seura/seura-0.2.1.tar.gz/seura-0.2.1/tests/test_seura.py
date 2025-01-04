import socket
import pytest

from unittest.mock import patch, MagicMock
from seura import SeuraClient, SeuraError


def test_client_initialization():
    client = SeuraClient("127.0.0.1")


def test_send_command_success(client):
    with patch("socket.socket") as mock_socket:
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance
        mock_sock_instance.recv.return_value = b"%2INPT 4\r"

        response = client.send_command("INPT", "4")
        assert response == "%2INPT 4\r"
        mock_sock_instance.sendall.assert_called_once_with(b"%2INPT 4\r")
        mock_sock_instance.recv.assert_called_once()


def test_send_command_socket_error(client):
    with patch("socket.socket") as mock_socket:
        mock_socket.return_value.__enter__.side_effect = socket.error(
            "Connection error"
        )

        with pytest.raises(SeuraError, match="Socket error: Connection error"):
            client.send_command("INPT", "4")


def test_send_command_invalid_response(client):
    with patch("socket.socket") as mock_socket:
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance
        mock_sock_instance.recv.return_value = b"INVALID RESPONSE"

        with pytest.raises(ValueError, match="Invalid input response"):
            client.send_command("INPT", "4")
