"""Company configurations and data center lists."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class DataCenter:
    """Represents a single data center location."""

    company_name: str
    site_name: str

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary format."""
        return {"company_name": self.company_name, "site_name": self.site_name}


@dataclass
class CompanyConfig:
    """Configuration for a cloud company."""

    name: str
    faiss_db_name: str
    pdf_folder: str
    data_centers: List[DataCenter] = field(default_factory=list)

    @property
    def data_centers_list(self) -> List[Dict[str, str]]:
        """Get data centers as list of dicts for compatibility."""
        return [dc.to_dict() for dc in self.data_centers]


# Pre-configured company configurations
COMPANIES: Dict[str, CompanyConfig] = {
    "oracle": CompanyConfig(
        name="Oracle",
        faiss_db_name="orcl_faiss_db",
        pdf_folder="oracle_related",
        data_centers=[
            DataCenter("Oracle", "Kuala Lumpur, Malaysia"),
            DataCenter("Oracle", "Dallas-Fort Worth, Texas, USA"),
            DataCenter("Oracle", "Singapore"),
            DataCenter("Oracle", "Amsterdam, Netherlands"),
            DataCenter("Oracle", "Riyadh, Saudi Arabia"),
            DataCenter("Oracle", "Tokyo, Japan"),
            DataCenter("Oracle", "Madrid, Spain"),
            DataCenter("Oracle", "Abilene, Texas, USA"),
            DataCenter("Oracle", "Bangladesh"),
            DataCenter("Oracle", "New Zealand"),
        ],
    ),
    "google": CompanyConfig(
        name="Google",
        faiss_db_name="google_faiss_db",
        pdf_folder="google_related",
        data_centers=[
            DataCenter("Google", "Caldwell County, North Carolina, USA"),
            DataCenter("Google", "Singapore, Singapore"),
            DataCenter("Google", "Virginia, USA"),
            DataCenter("Google", "Tokyo, Japan"),
            DataCenter("Google", "Eemshaven, Netherlands"),
            DataCenter("Google", "Kuala Lumpur, Malaysia"),
            DataCenter("Google", "Groningen, Netherlands"),
        ],
    ),
    "microsoft": CompanyConfig(
        name="Microsoft",
        faiss_db_name="msft_faiss_db",
        pdf_folder="msft_related",
        data_centers=[
            DataCenter("Microsoft", "Northern Virginia, USA"),
            DataCenter("Microsoft", "Texas, USA"),
            DataCenter("Microsoft", "Loughton, UK"),
            DataCenter("Microsoft", "Wisconsin, USA"),
            DataCenter("Microsoft", "Singapore"),
            DataCenter("Microsoft", "Narvik, Norway"),
            DataCenter("Microsoft", "Poland"),
            DataCenter("Microsoft", "Johor Bahru, Malaysia"),
            DataCenter("Microsoft", "Georgia, USA"),
            DataCenter("Microsoft", "Wyoming, USA"),
        ],
    ),
    "apple": CompanyConfig(
        name="Apple",
        faiss_db_name="apple_faiss_db",
        pdf_folder="apple_related",
        data_centers=[
            DataCenter("Apple", "Maiden, North Carolina, USA"),
            DataCenter("Apple", "Houston, Texas, USA"),
            DataCenter("Apple", "Iowa, USA"),
            DataCenter("Apple", "Oregon, USA"),
            DataCenter("Apple", "Arizona, USA"),
            DataCenter("Apple", "Nevada, USA"),
            DataCenter("Apple", "California, USA"),
            DataCenter("Apple", "Michigan, USA"),
            DataCenter("Apple", "Washington, USA"),
        ],
    ),
    "meta": CompanyConfig(
        name="Meta",
        faiss_db_name="meta_faiss_db",
        pdf_folder="meta_related",
        data_centers=[
            DataCenter("Meta", "Dallas, Texas, USA"),
            DataCenter("Meta", "Northern Virginia, Virginia, USA"),
            DataCenter("Meta", "Phoenix, Arizona, USA"),
            DataCenter("Meta", "Oregon, USA"),
            DataCenter("Meta", "Atlanta, Georgia, USA"),
        ],
    ),
    "amazon": CompanyConfig(
        name="Amazon",
        faiss_db_name="amazon_faiss_db",
        pdf_folder="amazon_related",
        data_centers=[
            DataCenter("Amazon", "Taipei, Taiwan"),
            DataCenter("Amazon", "Milan, Italy"),
            DataCenter("Amazon", "Bangkok, Thailand"),
            DataCenter("Amazon", "Kuala Lumpur, Malaysia"),
            DataCenter("Amazon", "Marysville, Ohio, USA"),
            DataCenter("Amazon", "Sunbury, Ohio, USA"),
            DataCenter("Amazon", "Fayette County, Ohio, USA"),
        ],
    ),
    "nebius": CompanyConfig(
        name="Nebius",
        faiss_db_name="nebius_faiss_db",
        pdf_folder="nebius_related",
        data_centers=[
            DataCenter("Nebius", "New Jersey, USA"),
            DataCenter("Nebius", "Kansas City, Missouri, USA"),
            DataCenter("Nebius", "Keflavik, Iceland"),
            DataCenter("Nebius", "Amsterdam, Netherlands"),
            DataCenter("Nebius", "Toronto, Ontario, Canada"),
        ],
    ),
    "coreweave": CompanyConfig(
        name="CoreWeave",
        faiss_db_name="coreweave_faiss_db",
        pdf_folder="coreweave_related",
        data_centers=[
            DataCenter("CoreWeave", "Chicago, Illinois, USA"),
            DataCenter("CoreWeave", "Las Vegas, Nevada, USA"),
            DataCenter("CoreWeave", "New Jersey, USA"),
            DataCenter("CoreWeave", "Santa Clara, California, USA"),
        ],
    ),
}


def get_company(name: str) -> Optional[CompanyConfig]:
    """
    Get company configuration by name.

    Args:
        name: Company name (case-insensitive)

    Returns:
        CompanyConfig if found, None otherwise
    """
    return COMPANIES.get(name.lower())


def get_all_companies() -> List[CompanyConfig]:
    """Get all configured companies."""
    return list(COMPANIES.values())


def list_company_names() -> List[str]:
    """Get list of all company names."""
    return [c.name for c in COMPANIES.values()]
