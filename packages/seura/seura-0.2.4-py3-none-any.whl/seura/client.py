import socket
import logging
from enum import Enum
from typing import Optional, Dict, Tuple, Union

from .exceptions import SeuraConnectionError, SeuraError
from .config import INPUT_MAP, POWER_STATE

# Set up logging
logging.basicConfig(level=logging.INFO)


class SeuraClient:
    """Client for controlling Seura displays via network commands."""

    def __init__(self, ip_address: str, port: int = 4453) -> None:
        """Initialize the Seura client.
        
        Args:
            ip_address: IP address of the Seura display
            port: Port number for communication (default: 4453)
        """
        self.ip_address = ip_address
        self.port = port
        logging.info(f"Initialized Seura client with IP: {ip_address}")

    def send_command(self, command: str, data: str = "") -> str:
        """Send a command to the Seura display.
        
        Raises:
            SeuraConnectionError: If connection or communication fails
            SeuraError: If the display returns an error response
        """
        message = f"%2{command} {data}\r"
        logging.info(
            f"Sending command: {message.strip()} to {self.ip_address}:{self.port}"
        )
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.ip_address, self.port))
                sock.sendall(message.encode("ascii"))
                response = sock.recv(1024).decode("ascii")
            logging.info(f"Received response: {response.strip()}")
        except socket.error as e:
            logging.error(f"Socket error: {e}")
            raise SeuraConnectionError(f"Failed to communicate with display: {e}")

        try:
            # Handle empty response
            if not response:
                logging.warning("Empty response received")
                raise SeuraError("Display returned empty response")

            # Split response using command as delimiter
            split_response = response.split(f"{command}=")
            
            # If response doesn't contain expected format, return raw response
            if len(split_response) != 2:
                logging.debug(f"Unexpected response format: {response}")
                return response.strip()
            
            value = split_response[1].strip()
            
            # Handle error responses
            if value.startswith("ERR"):
                raise SeuraError(f"Display returned error: {value}")
                
            return value

        except SeuraError:
            raise
        except Exception as e:
            logging.error(f"Error parsing response: {response}", exc_info=True)
            raise SeuraError(f"Failed to parse display response: {e}")

    def power_on(self) -> bool:
        """Power on the display.
        
        Returns:
            True if successful, False otherwise
        """
        logging.info("Powering on the display.")
        return self.send_command("POWR", "1") == "OK"

    def power_off(self) -> bool:
        """Power off the display.
        
        Returns:
            True if successful, False otherwise
        """
        logging.info("Powering off the display.")
        return self.send_command("POWR", "0") == "OK"

    def query_power(self) -> str:
        """Query the power state of the display.
        
        Returns:
            Current power state string
            
        Raises:
            ValueError: If response is invalid
        """
        logging.info("Querying power status.")
        response = self.send_command("POWR", "?")
        logging.info(f"Power response: {response}")
        try:
            for name, value in POWER_STATE.items():
                if value == response:
                    logging.info(f"Power state: {name}")
                    return name
            logging.error("Invalid power value received.")
            raise ValueError("Invalid power value")
        except (IndexError, ValueError) as e:
            logging.error(f"Error parsing power: {e}")
            raise ValueError("Invalid power response")

    # Input functions
    def get_inputs(self) -> list[str]:
        """Get the list of available input sources.
        
        Returns:
            List of input source names
        """
        return list(INPUT_MAP.keys())

    def set_input(self, input_source: str) -> bool:
        """Set the input source.
        
        Args:
            input_source: Name of input source to set
            
        Returns:
            True if successful, False otherwise
            
        Raises:
            ValueError: If input source is invalid
        """
        logging.info(f"Setting input source to: {input_source}")
        if input_source in INPUT_MAP:
            return self.send_command("INPT", INPUT_MAP[input_source]) == "OK"
        logging.error("Invalid input source attempted.")
        raise ValueError("Invalid input source")

    def query_input(self) -> str:
        """Query the current input source.
        
        Returns:
            Name of current input source
            
        Raises:
            ValueError: If response is invalid
        """
        logging.info("Querying input.")
        response = int(self.send_command("INPT", "?"))
        try:
            for name, value in INPUT_MAP.items():
                if value == response:
                    logging.info(f"Current input: {name}")
                    return name
            logging.error("Invalid input value received.")
            raise ValueError("Invalid input value")
        except (IndexError, ValueError) as e:
            logging.error(f"Error parsing input: {e}")
            raise ValueError("Invalid input response")

    # Volume functions
    def volume_up(self) -> bool:
        """Increase volume by one step.
        
        Returns:
            True if successful, False otherwise
        """
        logging.info("Increasing volume.")
        return self.send_command("VOLA", "1") == "OK"

    def volume_down(self) -> bool:
        """Decrease volume by one step.
        
        Returns:
            True if successful, False otherwise
        """
        logging.info("Decreasing volume.")
        return self.send_command("VOLA", "0") == "OK"

    def set_volume(self, level: int) -> bool:
        """Set volume to specific level.
        
        Args:
            level: Volume level (0-100)
            
        Returns:
            True if successful, False otherwise
            
        Raises:
            ValueError: If volume level is out of range
        """
        logging.info(f"Setting volume to: {level}")
        if 0 <= level <= 100:
            return self.send_command("VOLU", level) == "OK"
        logging.error("Invalid volume level attempted.")
        raise ValueError("Volume level must be between 0 and 100")

    def query_volume(self) -> int:
        """Query current volume level.
        
        Returns:
            Current volume level (0-100)
            
        Raises:
            ValueError: If response is invalid
        """
        logging.info("Querying volume level.")
        response = int(self.send_command("VOLU", "?"))
        try:
            logging.info(f"Current volume level: {response}")
            return response
        except (IndexError, ValueError) as e:
            logging.error(f"Error parsing volume level: {e}")
            raise ValueError("Invalid volume level response")

    # Channel functions
    def channel_up(self) -> bool:
        """Change to next channel.
        
        Returns:
            True if successful, False otherwise
        """
        logging.info("Changing channel up.")
        return self.send_command("CHNA", "1") == "OK"

    def channel_down(self) -> bool:
        """Change to previous channel.
        
        Returns:
            True if successful, False otherwise
        """
        logging.info("Changing channel down.")
        return self.send_command("CHNA", "0") == "OK"

    def change_channel(self, major: int, minor: int = 0) -> bool:
        """Change to specific channel.
        
        Args:
            major: Major channel number
            minor: Minor channel number (default: 0)
            
        Returns:
            True if successful, False otherwise
        """
        logging.info(f"Changing channel to: {major}-{minor}")
        return self.send_command("CHAN", f"{major:03}-{minor:02}") == "OK"

    def previous_channel(self) -> bool:
        """Return to previous channel.
        
        Returns:
            True if successful, False otherwise
        """
        logging.info("Switching to previous channel.")
        return self.send_command("CHRT", "1") == "OK"

    def query_channel(self) -> str:
        """Query current channel.
        
        Returns:
            Current channel string
            
        Raises:
            ValueError: If response is invalid
        """
        logging.info("Querying current channel.")
        response = self.send_command("CHAN", "?")
        try:
            logging.info(f"Current channel: {response}")
            return response
        except (IndexError, ValueError) as e:
            logging.error(f"Error parsing channel: {e}")
            raise ValueError("Invalid channel response")

    # Remote button commands
    def remote_button(self, button: str) -> bool:
        """Simulate pressing a remote control button.
        
        Args:
            button: Name of button to press
            
        Returns:
            True if successful, False otherwise
            
        Raises:
            ValueError: If button name is invalid
        """
        logging.info(f"Pressing remote button: {button}")
        button_map: Dict[str, Tuple[str, str]] = {
            "MENU": ("MENU", "0"),
            "UP": ("ARRO", "0"),
            "DOWN": ("ARRO", "1"),
            "LEFT": ("ARRO", "2"),
            "RIGHT": ("ARRO", "3"),
            "ENTER": ("ENTR", "1"),
            "BACK": ("BACK", "1"),
            "EXIT": ("EXIT", "1"),
            "MUTE": ("MUTE", "1"),
            "SLEEP": ("SLEP", "1"),
            "CLOSED_CAPTIONING": ("CLCP", "1"),
            "ASPECT_RATIO": ("ASPE", "1"),
            "INFO": ("INFO", "1"),
            "INPUT": ("INPT", "-"),
        }
        if button in button_map:
            return (
                self.send_command(button_map[button][0], button_map[button][1]) == "OK"
            )
        logging.error("Invalid button name attempted.")
        raise ValueError("Invalid button name")

    def remote_number(self, number: int) -> bool:
        """Simulate pressing a number button on remote.
        
        Args:
            number: Number to press (0-9)
            
        Returns:
            True if successful, False otherwise
            
        Raises:
            ValueError: If number is out of range
        """
        logging.info(f"Pressing remote number: {number}")
        if 0 <= number <= 9:
            return self.send_command("NUMB", str(number)) == "OK"
        logging.error("Invalid number attempted.")
        raise ValueError("Number must be between 0 and 9")
