import argparse
import logging
import coloredlogs
from DDownloader.modules.banners import banners
from DDownloader.modules.dash_downloader import DASH
from DDownloader.modules.hls_downloader import HLS
import os, re

logger = logging.getLogger("+ MAIN + ")
coloredlogs.install(level='DEBUG', logger=logger)

def validate_directories():
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        logger.debug("Created 'downloads' directory.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Download DASH or HLS streams with decryption keys.")
    parser.add_argument("-u", "--url", required=True, help="Manifest URL pointing to the stream (.mpd or .m3u8).")
    parser.add_argument("-k", "--key", action="append", help="Decryption keys in the format KID:KEY. Use multiple -k options for multiple keys.")
    parser.add_argument("-o", "--output", required=True, help="Output file name.")
    return parser.parse_args()

def main():
    banners()
    validate_directories()
    args = parse_arguments()

    if re.search(r"\.mpd\b", args.url, re.IGNORECASE):
        logger.info("DASH stream detected. Initializing DASH downloader...")
        downloader = DASH()
    elif re.search(r"\.m3u8\b", args.url, re.IGNORECASE):
        logger.info("HLS stream detected. Initializing HLS downloader...")
        downloader = HLS()
    else:
        logger.error("Unsupported URL format. Please provide a valid DASH (.mpd) or HLS (.m3u8) URL.")
        return

    downloader.manifest_url = args.url
    downloader.output_name = args.output
    downloader.decryption_keys = args.key or []

    if downloader.decryption_keys:
        for key in downloader.decryption_keys:
            logger.info(f"Decryption key(s) provided: --key {key}\n")
            print(Fore.MAGENTA + "=" * 80 + Fore.RESET)

    try:
        if isinstance(downloader, DASH):
            downloader.dash_downloader()
        else:
            downloader.hls_downloader()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()