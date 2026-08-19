"""LLM prompt templates for data center energy prediction."""

from langchain_core.prompts import ChatPromptTemplate

# System message for baseline parameter extraction
BASELINE_SYSTEM_MESSAGE = """You are a data center forecasting assistant with expertise in regional infrastructure differences.
Your goal is to extract *unique*, location-specific baseline parameters for each data center site.
Never reuse assumptions or estimates from other sites, even within the same company.
Carefully consider the local geography, grid mix, climate, and infrastructure maturity.
If the retrieved context for the given site is limited, use geographically or operationally similar hyperscale sites within the same region, but not identical defaults.
Always explain reasoning briefly in the 'notes' field.
Return strict JSON only, no prose."""

# User message for baseline parameter extraction
BASELINE_USER_MESSAGE = """**SITE INFORMATION:**
- Company: {company_name}
- Site: {site_name}
- Year of Interest: {current_year}

**RETRIEVED CONTEXT (from reports and database):**
{context}

**HYPERSCALE REFERENCE GUIDELINES (for missing data):**
- N_train: 40,000-60,000
- N_inference: 140,000-160,000
- P_avg_train_kW: 0.5-0.6
- P_avg_inference_kW: 0.1-0.3
- Typical PUE (Power Usage Effectiveness): 1.1-1.3 for new hyperscale sites
- Utilization rates and hours may vary by climate, cooling, and grid reliability

- Major hubs (e.g., Northern Virginia, Dublin, Oregon): 1.2-1.5x the hyperscale midpoint
- Secondary regions (e.g., Milan, Frankfurt): around the hyperscale midpoint
- Emerging or smaller regions (e.g., Taipei, Jakarta): 0.7-0.9x the hyperscale midpoint

**TASK:**
Based on the retrieved context and your knowledge of regional infrastructure, extract the following parameters for the {current_year} baseline:
- N_train (Number of AI accelerators for training)
- N_inference (Number of AI accelerators for inference)
- P_avg_train_kW (Average power per training accelerator in kW)
- P_avg_inference_kW (Average power per inference accelerator in kW)
- u_train (Utilization rate for training workloads)
- u_inference (Utilization rate for inference workloads)
- H_train (Hours of operation per year for training)
- H_inference (Hours of operation per year for inference)
- PUE_current (Current Power Usage Effectiveness)
- grid_factor_tCO2_per_MWh (Grid emission factor in tCO2 per MWh)

**STRICT RULES:**
1. Do NOT produce identical or near-identical parameter sets across different sites.
2. If context is weak, vary estimates logically according to region:
   - Cooler climates -> better cooling efficiency -> slightly lower PUE.
   - Renewable-heavy grids -> lower grid_factor_tCO2_per_MWh.
   - Emerging markets -> possibly higher PUE and lower utilization.
3. Always include a short `notes` field summarizing your assumptions.

**OUTPUT:**
Return only one valid JSON object with the extracted parameters and notes.

**Answer:**"""

BASELINE_EXTRACTION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", BASELINE_SYSTEM_MESSAGE),
    ("user", BASELINE_USER_MESSAGE),
])


# System message for forecast generation
FORECAST_SYSTEM_MESSAGE = """You are a domain expert in data center energy forecasting.
Using the provided parameters for year {current_year} and retrieved knowledge chunks,
forecast the next {forecast_horizon} years of:
N_train, N_inference, P_avg_train, P_avg_inference, u_train, u_inference, H_train, H_inference, PUE.
Consider the company '{company_name}' and the data center location '{site_name}' to improve accuracy."""

# User message for forecast generation
FORECAST_USER_MESSAGE = """**CURRENT YEAR PARAMETERS (JSON):**
{param_json}

**RETRIEVED CONTEXT (from RAG):**
{context}

Provide forecast for the next {forecast_horizon} years starting from {current_year}.
Apply realistic growth trends for hyperscale data centers:
- N_train and N_inference typically grow 10-20% per year (Assume a growth rate based on context)
- Power efficiency (P_avg_train / P_avg_inference) improves slightly (~1-3%/yr)
- Utilization (u_train/u_inference) may rise slowly with optimization
- Hours (H_train/H_inference) stay roughly stable
- PUE should be predicted directly considering regional and tech factors

Each object must include a `notes` field explaining assumptions, estimates, or sources.
Make sure your predictions consider the company '{company_name}' and site '{site_name}' for operational and regional factors.

Return output as a JSON array, where each element represents one year of forecasted parameters with this schema:
```
[
  {{
    "year": <int>,
    "N_train": <float>,
    "N_inference": <float>,
    "P_avg_train": <float>,
    "P_avg_inference": <float>,
    "u_train": <float>,
    "u_inference": <float>,
    "H_train": <float>,
    "H_inference": <float>,
    "PUE": <float>,
    "notes": <string>
  }}
]
```
Output only the JSON array."""

FORECAST_PROMPT = ChatPromptTemplate.from_messages([
    ("system", FORECAST_SYSTEM_MESSAGE),
    ("user", FORECAST_USER_MESSAGE),
])


# System message for expansion prediction
EXPANSION_SYSTEM_MESSAGE = """You are a strategic data center forecasting assistant.
Analyze the provided context about {company_name}'s existing and planned data centers,
infrastructure trends, local regulations, energy availability, and market demand.
Predict which geographic locations are most likely for {company_name} to expand their data center footprint in the next 5 years.
Provide reasoning and score each location with a probability from 0 to 1.
Return strict JSON only with the following fields:
- location_name (city, state/province, country)
- estimated_probability (0-1 probability of expansion)
- key_factors (brief summary of factors influencing the prediction)
- notes (optional, e.g., assumptions or uncertainties)"""

EXPANSION_USER_MESSAGE = """**CONTEXT FROM REPORTS:**
{context}

**INSTRUCTIONS:**
Based on the context, predict the top locations for {company_name}'s data center expansion in the next 5 years.
Provide a ranked JSON list.

**Question:** {question}

**Answer:**"""

EXPANSION_PREDICTION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", EXPANSION_SYSTEM_MESSAGE),
    ("user", EXPANSION_USER_MESSAGE),
])
