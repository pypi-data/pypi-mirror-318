import argparse
import logging
import coloredlogs
from DDownloader.modules.dash_downloader import DASH
from DDownloader.modules.hls_downloader import HLS

logger = logging.getLogger("+ MAIN + ")
coloredlogs.install(level='DEBUG', logger=logger)

def parse_arguments():
    """
    Parse command-line arguments for the downloader.
    """
    parser = argparse.ArgumentParser(description="Download DASH or HLS streams with decryption keys.")
    parser.add_argument("-u", "--url", required=True, help="Manifest URL pointing to the stream (.mpd or .m3u8).")
    parser.add_argument("-k", "--key", action="append", help="Decryption keys in the format KID:KEY. Use multiple -k options for multiple keys.")
    parser.add_argument("-o", "--output", required=True, help="Output file name.")
    return parser.parse_args()

def main():
    # Parse arguments
    args = parse_arguments()
    
    # Detect DASH or HLS based on URL extension
    if args.url.endswith(".mpd"):
        logger.info("DASH stream detected. Initializing DASH downloader...")
        downloader = DASH()
    elif args.url.endswith(".m3u8"):
        logger.info("HLS stream detected. Initializing HLS downloader...")
        downloader = HLS()
    else:
        logger.error("Unsupported URL format. Please provide a valid DASH (.mpd) or HLS (.m3u8) URL.")
        return
    
    # Set downloader properties
    downloader.manifest_url = args.url
    downloader.output_name = args.output
    downloader.decryption_keys = args.key or []  # Default to an empty list if no keys provided

    # Log decryption keys
    if downloader.decryption_keys:
        logger.info("Decryption key(s) provided:")
        for key in downloader.decryption_keys:
            logger.info(f"--key {key}")
    
    # Start download
    try:
        if isinstance(downloader, DASH):
            downloader.dash_downloader()
        else:
            downloader.hls_downloader()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()