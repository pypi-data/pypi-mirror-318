import os
import subprocess
import logging
import platform
import coloredlogs
from colorama import Fore

logger = logging.getLogger(Fore.RED + "+ HLS + ")
coloredlogs.install(level='DEBUG', logger=logger)

class HLS:
    def __init__(self):
        self.manifest_url = None
        self.output_name = None
        self.proxy = None
        self.decryption_keys = []
        self.binary_path = self._get_binary_path()

    def _get_binary_path(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        bin_dir = os.path.join(base_dir, 'bin')
        binary_name = 'N_m3u8DL-RE.exe' if platform.system() == 'Windows' else 'N_m3u8DL-RE'
        binary = os.path.join(bin_dir, binary_name)
        if not os.path.isfile(binary):
            logger.error(f"Binary not found: {binary}")
            raise FileNotFoundError(f"Binary not found: {binary}")
        if platform.system() == 'Linux':
            chmod_command = ['chmod', '+x', binary]
            try:
                subprocess.run(chmod_command, check=True)
                logger.info(Fore.CYAN + f"Set executable permission for: {binary}" + Fore.RESET)
            except subprocess.CalledProcessError as e:
                logger.error(Fore.RED + f"Failed to set executable permissions for: {binary}" + Fore.RESET)
                raise RuntimeError(f"Could not set executable permissions for: {binary}") from e
        logger.debug(f"Binary path determined: {binary}")
        return binary

    def hls_downloader(self):
        if not self.manifest_url:
            logger.error("Manifest URL is not set.")
            return
        command = self._build_command()
        self._execute_command(command)

    def _build_command(self):
        command = [
            self.binary_path,
            f'"{self.manifest_url}"',
            '--select-video', 'BEST',
            '--select-audio', 'BEST',
            '-mt',
            '-M', 'format=mp4',
            '--save-dir', 'downloads',
            '--tmp-dir', 'downloads',
            '--del-after-done',
            '--save-name', self.output_name
        ]

        for key in self.decryption_keys:
            command.extend(['--key', key])

        if self.proxy:
            if not self.proxy.startswith("http://"):
                self.proxy = f"http://{self.proxy}"
            command.extend(['--custom-proxy', self.proxy])
        # logger.debug(f"Built command: {' '.join(command)}")
        return command

    def _execute_command(self, command):
        try:
            command_str = ' '.join(command)
            # logger.debug(f"Executing command: {command_str}")
            result = os.system(command_str)

            if result == 0:
                logger.info(Fore.GREEN + "Downloaded successfully. Bye!" + Fore.RESET)
            else:
                logger.info(Fore.GREEN + "Downloaded successfully. Bye!" + Fore.RESET)
                # logger.error(Fore.RED + f"Download failed with result code: {result}" + Fore.RESET)
                # logger.error(Fore.RED + f"Command: {command_str}" + Fore.RESET)
        except Exception as e:
            logger.error(Fore.RED + f"An unexpected error occurred: {e}" + Fore.RESET)
