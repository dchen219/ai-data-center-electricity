"""Web scraping utilities for data center location extraction."""

import time
from typing import Dict, List, Optional
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DataCenterResearchBot/1.0)"}
DEFAULT_TIMEOUT = 30


def get_soup(url: str, headers: Optional[Dict[str, str]] = None, timeout: int = DEFAULT_TIMEOUT) -> BeautifulSoup:
    """
    Fetch a URL and return a BeautifulSoup object.

    Args:
        url: The URL to fetch
        headers: Optional custom headers (defaults to a research bot user agent)
        timeout: Request timeout in seconds

    Returns:
        BeautifulSoup object for the fetched page

    Raises:
        requests.RequestException: If the request fails
    """
    if headers is None:
        headers = DEFAULT_HEADERS

    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def scrape_locations(
    base_url: str,
    link_selector: str = '.map-full-list a[href*="locations"]',
    delay: float = 1.0,
    skip_in_development: bool = True,
) -> pd.DataFrame:
    """
    Scrape data center locations from a website.

    Args:
        base_url: The base URL to start scraping from
        link_selector: CSS selector for location links
        delay: Delay between requests in seconds
        skip_in_development: Whether to skip locations marked as "in development"

    Returns:
        DataFrame with columns: region_name, url, description
    """
    soup = get_soup(base_url)
    location_links = soup.select(link_selector)

    seen = set()
    data: List[Dict[str, str]] = []

    for link in location_links:
        href = link.get("href")
        name = link.get_text(strip=True)

        # Skip invalid or duplicate entries
        if not href or href in seen or not name:
            continue

        # Skip locations in development if configured
        if skip_in_development and "in-development" in link.parent.get_text():
            continue

        seen.add(href)

        # Construct the full web path
        if href.startswith("./../../"):
            url = urljoin(base_url, href.replace("./../../", ""))
        else:
            url = urljoin(base_url, href)

        print(f"Scraping {name} - {url}")

        try:
            subsoup = get_soup(url)
            main_content = subsoup.find("main") or subsoup
            paragraphs = main_content.find_all("p")
            desc_texts = []

            for p in paragraphs:
                text = p.get_text(" ", strip=True)
                # Filter out navigation/footer text
                if len(text) > 30 and not any(
                    word in text.lower()
                    for word in ["cookie", "privacy", "terms", "menu", "search"]
                ):
                    desc_texts.append(text)

            description = " ".join(desc_texts[:500])

            data.append(
                {
                    "region_name": name,
                    "url": url,
                    "description": description,
                }
            )

            time.sleep(delay)

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
            data.append(
                {
                    "region_name": name,
                    "url": url,
                    "description": "Details unavailable",
                }
            )

    return pd.DataFrame(data)


def scrape_google_locations(output_path: Optional[str] = None) -> pd.DataFrame:
    """
    Scrape Google data center locations.

    Args:
        output_path: Optional path to save the CSV file

    Returns:
        DataFrame with Google data center locations
    """
    base_url = "https://datacenters.google/locations"
    df = scrape_locations(base_url)

    if output_path:
        df.to_csv(output_path, index=False)
        print(f"Saved {len(df)} records to {output_path}")

    return df
