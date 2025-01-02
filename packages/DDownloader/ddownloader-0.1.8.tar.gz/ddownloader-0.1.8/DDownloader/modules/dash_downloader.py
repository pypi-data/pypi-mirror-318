import os
import subprocess
import logging
import platform
import coloredlogs
from colorama import Fore

logger = logging.getLogger("+ DASH + ")
coloredlogs.install(level='DEBUG', logger=logger)

class DASH:
    def __init__(self):
        self.manifest_url = None
        self.output_name = None
        self.decryption_keys = []  # Store multiple keys as a list
        self.binary_path = self._get_binary_path()

    def _get_binary_path(self):
        """Determine the correct binary path based on the platform."""
        base_path = os.path.join(os.path.dirname(__file__), 'bin', 'N_m3u8DL-RE')
        
        if platform.system() == 'Windows':
            binary = f"{base_path}.exe"
        elif platform.system() == 'Linux':
            binary = base_path
        elif platform.system() == 'Darwin':
            binary = base_path
        else:
            logger.error(f"Unsupported platform: {platform.system()}")
            raise OSError(f"Unsupported platform: {platform.system()}")
        
        if not os.path.exists(binary):
            logger.error(f"Binary not found: {binary}")
            raise FileNotFoundError(f"Binary not found: {binary}")
        
        return binary

    def dash_downloader(self):
        if not self.manifest_url:
            logger.error("Manifest URL is not set.")
            return
        
        command = self._build_command()
        self._execute_command(command)

    def _build_command(self):
        command = [
            self.binary_path,
            self.manifest_url,
            '--auto-select',
            '-mt',
            '-M', 'format=mp4',
            '--save-dir', 'downloads',
            '--tmp-dir', 'downloads',
            '--save-name', self.output_name
        ]
        for key in self.decryption_keys:
            command.extend(['--key', key])
        logger.debug(f"Built command: {' '.join(command)}")
        return command

    def _execute_command(self, command):
        try:
            result = subprocess.run(command, check=True)
            if result.returncode == 0:
                logger.info("Downloaded using N_m3u8DL-RE successfully.")
            else:
                logger.error(f"Download failed with result code: {result.returncode}")

        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {e}")
            raise RuntimeError(f"Download process failed: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")