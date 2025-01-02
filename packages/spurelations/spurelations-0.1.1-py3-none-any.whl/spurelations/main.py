"""Spurelations - Download spurious correlations from tylervigen.com."""

__version__ = "0.1.0"

from bs4 import BeautifulSoup
import requests
import os
import shutil
import argparse
import sys
import time
from tqdm import tqdm
from colorama import Fore, Style, init
import tempfile
from pathlib import Path

# Initialize colorama for Windows compatibility
init()


def log_info(message):
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} {message}")


def log_success(message):
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {message}")


def log_warning(message):
    print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")


def log_error(message):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")


def extract_png_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all <a> tags that have both 'download' attribute and href ending with .png
    for link in soup.find_all("a"):
        href = link.get("href", "")
        text = link.get_text()
        if href.endswith(".png") and "Download png" in text:
            # If it's a relative URL, make it absolute
            if href.startswith("image/"):
                href = f"https://tylervigen.com/spurious/correlation/{href}"
            log_info(f"Found link: {href}")
            return href
    return None


def get_png_from_page(url):
    # Create temporary directory for intermediate files
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            log_info(f"Fetching page from: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                log_info("Successfully retrieved page")

                # Save the random page content in temp directory
                temp_html = Path(temp_dir) / "random.html"
                with open(temp_html, "w", encoding="utf-8") as f:
                    f.write(response.text)
                log_info("Saved HTML content to temporary file")

                png_link = extract_png_link(response.text)
                if png_link:
                    log_info(f"Found PNG link: {png_link}")

                    # Create images directory in user's home
                    images_dir = Path.home() / "spurelations" / "images"
                    images_dir.mkdir(parents=True, exist_ok=True)
                    log_info(f"Ensured '{images_dir}' directory exists")

                    # Extract filename from the PNG URL
                    filename = png_link.split("/")[-1]
                    filepath = images_dir / filename

                    # Check if file already exists
                    if filepath.exists():
                        log_warning(f"File already exists: {filepath}")
                        return "EXISTS"

                    # Download and save the PNG
                    log_info(f"Downloading PNG from: {png_link}")
                    png_response = requests.get(png_link, stream=True)
                    if png_response.status_code == 200:
                        with open(filepath, "wb") as f:
                            shutil.copyfileobj(png_response.raw, f)
                        log_success(f"Successfully saved PNG to: {filepath}")

                    return "SUCCESS"
                else:
                    log_warning("No PNG download link found in the page")
                    return "NO_LINK"
        except Exception as e:
            log_error(f"Error: {str(e)}")
            return f"Error: {str(e)}"


def main():
    parser = argparse.ArgumentParser(description="Download random correlation PNGs")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--all", action="store_true", help="Download images until Ctrl+C"
    )
    group.add_argument("--num", type=int, help="Download N images")
    args = parser.parse_args()

    url = "https://tylervigen.com/spurious/random"
    exists_count = 0
    downloaded = 0

    try:
        if args.num:
            # Use tqdm for progress bar when --num is specified
            pbar = tqdm(total=args.num, desc="Downloading images")

        while True:
            print(f"\n{Fore.BLUE}{'='*50}{Style.RESET_ALL}")
            log_info("Starting PNG extraction process...")
            result = get_png_from_page(url)

            if result == "EXISTS":
                exists_count += 1
                if exists_count >= 10:
                    log_warning("\nReached 10 existing files, stopping...")
                    break
            elif result == "SUCCESS":
                downloaded += 1
                exists_count = 0  # Reset counter on successful download

                if args.num:
                    pbar.update(1)
                    if downloaded >= args.num:
                        log_success(
                            f"\nReached target of {args.num} downloads, stopping..."
                        )
                        break

            if not args.all and not args.num:
                break

            # Add a small delay between requests
            time.sleep(1)

    except KeyboardInterrupt:
        log_warning("\nProcess interrupted by user")
    finally:
        if args.num:
            pbar.close()

    print(f"\n{Fore.BLUE}{'='*50}{Style.RESET_ALL}")
    log_success(f"Download summary:")
    log_info(f"Successfully downloaded: {downloaded} images")
    log_info(f"Stopped after encountering: {exists_count} existing files")


if __name__ == "__main__":
    main()
