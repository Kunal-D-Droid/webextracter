#!/usr/bin/env python3
"""Fetch a web page and optionally dump HTML or list links."""

import argparse
import sys

import requests
from bs4 import BeautifulSoup


def fetch_soup(url: str, timeout: float = 30.0) -> BeautifulSoup:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch a URL and print parsed HTML and/or links from <a> tags."
    )
    parser.add_argument("url", help="Page to fetch (include http:// or https://)")
    parser.add_argument(
        "--html",
        action="store_true",
        help="Print the full parsed document before listing links (can be very large)",
    )
    args = parser.parse_args()

    try:
        soup = fetch_soup(args.url)
    except requests.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)

    if args.html:
        print(soup)

    anchors = soup.find_all("a", href=True)
    if not anchors:
        print("No links with href found.", file=sys.stderr)
        return

    seen = set()
    for a in anchors:
        href = a["href"].strip()
        if href and href not in seen:
            seen.add(href)
            print(href)


if __name__ == "__main__":
    main()
