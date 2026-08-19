"""
Search configuration for the data center URL collector.
"""

# ---------------------------------------------------------------------------
# Energy / sustainability keywords (15)
# ---------------------------------------------------------------------------
ENERGY_KEYWORDS = [
    "data center energy consumption",
    "data center power demand",
    "data center electricity usage",
    "data center PUE",
    "data center power usage effectiveness",
    "data center cooling efficiency",
    "data center carbon footprint",
    "data center renewable energy",
    "data center sustainability",
    "data center megawatt capacity",
    "data center energy cost",
    "data center net zero emissions",
    "data center green energy",
    "data center grid impact",
    "data center water usage effectiveness",
]

# ---------------------------------------------------------------------------
# Geographic location keywords (20)
# ---------------------------------------------------------------------------
LOCATION_KEYWORDS = [
    "Virginia",
    "Texas",
    "Oregon",
    "Iowa",
    "Arizona",
    "Ohio",
    "North Carolina",
    "Georgia",
    "Nevada",
    "California",
    "Ireland",
    "Netherlands",
    "Singapore",
    "Japan",
    "Germany",
    "Sweden",
    "Finland",
    "India",
    "Australia",
    "Brazil",
]

# ---------------------------------------------------------------------------
# Year range
# ---------------------------------------------------------------------------
YEAR_RANGE = range(2019, 2027)

# ---------------------------------------------------------------------------
# Company root domains
# ---------------------------------------------------------------------------
COMPANY_DOMAINS: dict[str, str] = {
    "Oracle": "oracle.com",
    "Google": "google.com",
    "Microsoft": "microsoft.com",
    "Apple": "apple.com",
    "Meta": "meta.com",
    "Amazon": "amazon.com",
    "Nebius": "nebius.com",
    "CoreWeave": "coreweave.com",
}

# ---------------------------------------------------------------------------
# Company sustainability / IR pages (for direct scraping)
# ---------------------------------------------------------------------------
COMPANY_SUSTAINABILITY_PAGES: dict[str, list[str]] = {
    "Oracle": [
        "https://www.oracle.com/cloud/data-centers/",
        "https://www.oracle.com/corporate/sustainability/",
    ],
    "Google": [
        "https://www.google.com/about/datacenters/",
        "https://sustainability.google/",
        "https://cloud.google.com/about/locations/",
    ],
    "Microsoft": [
        "https://azure.microsoft.com/en-us/global-infrastructure/",
        "https://www.microsoft.com/en-us/corporate-responsibility/",
        "https://news.microsoft.com/",
    ],
    "Apple": [
        "https://www.apple.com/environment/",
        "https://www.apple.com/supplier-responsibility/",
    ],
    "Meta": [
        "https://sustainability.fb.com/",
        "https://datacenters.fb.com/",
        "https://about.meta.com/",
    ],
    "Amazon": [
        "https://aws.amazon.com/about-aws/global-infrastructure/",
        "https://sustainability.aboutamazon.com/",
    ],
    "Nebius": [
        "https://nebius.com/",
        "https://nebius.ai/",
    ],
    "CoreWeave": [
        "https://www.coreweave.com/",
    ],
}
