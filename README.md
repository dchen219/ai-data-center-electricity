# ai-data-center-electricity
Code and data processing pipeline for AI data center siting inference, electricity demand projection, and regional electricity demand pressure (EDPI) analysis.
## Data sources and availability

This repository contains the processed data and analytical outputs used to
study AI data-center siting, electricity-demand projections, and regional
Electricity Demand Pressure Index (EDPI) values.

### 1. Corporate and textual sources

The retrieval-augmented generation (RAG) corpus was assembled from publicly
accessible materials published between 2015 and 2025, including:

- SEC EDGAR filings: https://www.sec.gov/edgar/search/
- Corporate annual and sustainability reports
- Corporate press releases and infrastructure announcements
- Government and grid-operator publications
- Data Center Dynamics and other publicly available media reports

### 2. Historical data-center locations

Historical facility records for Amazon, Microsoft, Google, Meta, Oracle, and
Apple were obtained from S&P Capital IQ.

Because S&P Capital IQ is a proprietary subscription database, the original
facility-level records are not included in this repository. They may be
accessed through S&P Capital IQ by users with an appropriate subscription:

https://www.capitaliq.com/

Where permitted, this repository provides processed or aggregated outputs
derived from these records. The processing procedures and required input
fields are documented so that authorized users can reproduce the analysis
using independently obtained source data.

### 3. Electricity data

The EDPI analysis uses the following electricity datasets:

- U.S. Energy Information Administration State Electricity Profiles:
  https://www.eia.gov/electricity/state/
- Ember Yearly Electricity Data:
  https://ember-energy.org/data/yearly-electricity-data/
- International Energy Agency Energy and AI report, used for external
  benchmarking:
  https://www.iea.org/reports/energy-and-ai

For U.S. states, available electricity is represented by total retail
electricity sales. For countries, it is calculated as total generation plus
positive net electricity imports. The harmonized 2019–2024 electricity data
and the resulting 2030 projections are provided in the processed-data
directory, subject to the original providers' terms of use.

### 4. Geospatial and contextual data

Where applicable, the study also draws contextual information from:

- Global Power Plant Database:
  https://datasets.wri.org/dataset/globalpowerplantdatabase
- OpenStreetMap:
  https://www.openstreetmap.org/
- Landsat 8 and Sentinel-2 imagery accessed through Google Earth Engine:
  https://earthengine.google.com/
- Global Human Settlement Layer:
  https://human-settlement.emergency.copernicus.eu/
- LandScan population data:
  https://landscan.ornl.gov/

Original third-party geospatial files are not redistributed unless permitted
by their respective licenses.

## Code availability

This repository contains the custom code and intermediate outputs used for:

1. Constructing and querying the document corpus
2. Identifying existing and prospective AI data-center locations
3. Extracting site-level technical and operational parameters
4. Projecting firm- and region-level electricity demand
5. Calculating the Electricity Demand Pressure Index (EDPI)
6. Generating the tables and figures reported in the manuscript

The workflow was implemented in Python using:

- LangChain for retrieval-augmented generation (RAG)
- FAISS for vector storage and semantic retrieval
- Hugging Face `all-MiniLM-L6-v2` for text embeddings
- OpenAI GPT-4o-mini for structured inference
- pandas and NumPy for data processing and numerical calculations
- Matplotlib and Seaborn for visualization

The LLM analyses used fixed prompt templates, a temperature setting of `0.3`,
and structured JSON parsing. API credentials are not included in this
repository.
