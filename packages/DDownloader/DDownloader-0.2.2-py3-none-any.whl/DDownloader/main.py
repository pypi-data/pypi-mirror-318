import os
import re
import logging
import coloredlogs
from colorama import Fore, Style
import platform, time # Added to detect platform
from DDownloader.modules.args_parser import parse_arguments
from DDownloader.modules.banners import banners
from DDownloader.modules.dash_downloader import DASH
from DDownloader.modules.hls_downloader import HLS

# Setup logger
logger = logging.getLogger("+ MAIN + ")
coloredlogs.install(level='DEBUG', logger=logger)

def validate_directories():
    """Ensure necessary directories exist."""
    downloads_dir = 'downloads'
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
        logger.debug(f"Created '{downloads_dir}' directory.")

def detect_platform():
    """Detect the platform the script is running on."""
    system_platform = platform.system().lower()
    if system_platform == 'windows':
        return 'Windows'
    elif system_platform == 'linux':
        return 'Linux'
    elif system_platform == 'darwin':
        return 'MacOS'
    else:
        return 'Unknown'

def display_help():
    """Display custom help message with emoji."""
    print(
        f"{Fore.WHITE}+" + "=" * 80 + f"+{Style.RESET_ALL}\n"
        f"{Fore.CYAN}{'Option':<40}{'Description':<90}{Style.RESET_ALL}\n"
        f"{Fore.WHITE}+" + "=" * 80 + f"+{Style.RESET_ALL}\n"
        f"  {Fore.GREEN}-u, --url{' ' * 22}{Style.RESET_ALL}URL of the manifest (mpd/m3u8) 🌐\n"
        f"  {Fore.GREEN}-p, --proxy{' ' * 20}{Style.RESET_ALL}A proxy with protocol (http://ip:port) 🌍\n"
        f"  {Fore.GREEN}-o, --output{' ' * 19}{Style.RESET_ALL}Name of the output file 💾\n"
        f"  {Fore.GREEN}-k, --key{' ' * 22}{Style.RESET_ALL}Decryption key in KID:KEY format 🔑\n"
        f"  {Fore.GREEN}-h, --help{' ' * 21}{Style.RESET_ALL}Show this help message and exit ❓\n"
        f"{Fore.WHITE}+" + "=" * 80 + f"+{Style.RESET_ALL}\n"
    )

def main():
    banners()
    time.sleep(1)
    platform_name = detect_platform()
    logger.info(f"Running on platform: {platform_name}\n")
    time.sleep(1)
    
    validate_directories()
    try:
        args = parse_arguments()
    except SystemExit:
        display_help()
        exit(1)

    # Detect and initialize appropriate downloader
    downloader = None
    if re.search(r"\.mpd\b", args.url, re.IGNORECASE):
        logger.info("DASH stream detected. Initializing DASH downloader...")
        downloader = DASH()
    elif re.search(r"\.m3u8\b", args.url, re.IGNORECASE):
        logger.info("HLS stream detected. Initializing HLS downloader...")
        downloader = HLS()
    else:
        logger.error("Unsupported URL format. Please provide a valid DASH (.mpd) or HLS (.m3u8) URL.")
        exit(1)

    # Configure downloader
    downloader.manifest_url = args.url
    downloader.output_name = args.output
    downloader.decryption_keys = args.key or []
    downloader.proxy = args.proxy  # Add proxy if provided

    # Log provided decryption keys
    if downloader.decryption_keys:
        logger.info("Decryption keys provided:")
        for key in downloader.decryption_keys:
            logger.info(f"  --key {key}")
        print(Fore.MAGENTA + "=" * 80 + Fore.RESET)

    # Execute downloader
    try:
        if isinstance(downloader, DASH):
            downloader.dash_downloader()
        elif isinstance(downloader, HLS):
            downloader.hls_downloader()
    except Exception as e:
        logger.error(f"An error occurred during the download process: {e}")
        exit(1)

if __name__ == "__main__":
    main()
