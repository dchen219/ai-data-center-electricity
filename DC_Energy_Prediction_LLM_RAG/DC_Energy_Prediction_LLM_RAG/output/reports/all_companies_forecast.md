# All Companies — Data Center Energy Forecast & Expansion Predictions

---
# Oracle

## Energy Forecast

### Oracle — Kuala Lumpur, Malaysia

#### Baseline Parameters (2025)
```json
{
  "N_train": 45000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.65,
  "H_train": 4000,
  "H_inference": 5000,
  "PUE_current": 1.35,
  "grid_factor_tCO2_per_MWh": 0.6,
  "notes": "Kuala Lumpur has a tropical climate, leading to higher cooling demands, thus a slightly higher PUE. The grid is moderately renewable, resulting in a reasonable emission factor. Utilization rates are adjusted for the emerging market context."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 45000,
    "N_inference": 150000,
    "P_avg_train": 0.55,
    "P_avg_inference": 0.2,
    "u_train": 0.75,
    "u_inference": 0.65,
    "H_train": 4000,
    "H_inference": 5000,
    "PUE": 1.35,
    "notes": "Initial values for 2026 based on current parameters.",
    "grid_factor": 0.6,
    "E_IT": 171750000.0,
    "E_DC": 231862500.00000003,
    "CO2": 139117500.0
  },
  {
    "year": 2027,
    "N_train": 47250,
    "N_inference": 157500,
    "P_avg_train": 0.5535,
    "P_avg_inference": 0.202,
    "u_train": 0.76,
    "u_inference": 0.66,
    "H_train": 4000,
    "H_inference": 5000,
    "PUE": 1.36,
    "notes": "Assuming a 5% growth in N_train and N_inference, and slight improvements in power efficiency and utilization.",
    "grid_factor": 0.6,
    "E_IT": 184494240.00000003,
    "E_DC": 250912166.40000007,
    "CO2": 150547299.84000003
  },
  {
    "year": 2028,
    "N_train": 49500,
    "N_inference": 165000,
    "P_avg_train": 0.557,
    "P_avg_inference": 0.204,
    "u_train": 0.77,
    "u_inference": 0.67,
    "H_train": 4000,
    "H_inference": 5000,
    "PUE": 1.37,
    "notes": "Continuing trends with 5% growth in N_train and N_inference, and slight improvements in power efficiency and utilization.",
    "grid_factor": 0.6,
    "E_IT": 197681220.0,
    "E_DC": 270823271.40000004,
    "CO2": 162493962.84
  },
  {
    "year": 2029,
    "N_train": 51750,
    "N_inference": 172500,
    "P_avg_train": 0.5605,
    "P_avg_inference": 0.206,
    "u_train": 0.78,
    "u_inference": 0.68,
    "H_train": 4000,
    "H_inference": 5000,
    "PUE": 1.38,
    "notes": "Assuming continued growth and optimization in power efficiency and utilization.",
    "grid_factor": 0.6,
    "E_IT": 211317330.0,
    "E_DC": 291617915.4,
    "CO2": 174970749.23999998
  },
  {
    "year": 2030,
    "N_train": 54000,
    "N_inference": 180000,
    "P_avg_train": 0.564,
    "P_avg_inference": 0.208,
    "u_train": 0.79,
    "u_inference": 0.69,
    "H_train": 4000,
    "H_inference": 5000,
    "PUE": 1.39,
    "notes": "Final year of forecast with continued growth and efficiency improvements.",
    "grid_factor": 0.6,
    "E_IT": 225408960.0,
    "E_DC": 313318454.4,
    "CO2": 187991072.64
  }
]
```

### Oracle — Dallas-Fort Worth, Texas, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Dallas-Fort Worth has a mature infrastructure with a reliable power grid and moderate climate, allowing for efficient cooling and higher utilization rates. The grid has a significant share of renewables, contributing to a lower carbon footprint."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.202,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency and utilization rates.",
    "grid_factor": 0.4,
    "E_IT": 339339000.0,
    "E_DC": 403813410.0,
    "CO2": 161525364.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.204,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing the growth trend of 10% for N_train and N_inference, with further slight improvements in efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 380895900.0,
    "E_DC": 449457162.0,
    "CO2": 179782864.8
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.206,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming continued growth and efficiency improvements, maintaining the trend of 10% growth.",
    "grid_factor": 0.4,
    "E_IT": 427450650.0,
    "E_DC": 500117260.49999994,
    "CO2": 200046904.2
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.208,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Maintaining the growth trend with a focus on efficiency, with slight improvements in utilization.",
    "grid_factor": 0.4,
    "E_IT": 479595237.0,
    "E_DC": 556330474.92,
    "CO2": 222532189.968
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.565,
    "P_avg_inference": 0.21,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Final year of forecast, assuming continued growth and efficiency improvements, with a target of 10% growth.",
    "grid_factor": 0.4,
    "E_IT": 537988848.0,
    "E_DC": 618687175.1999999,
    "CO2": 247474870.07999998
  }
]
```

### Oracle — Singapore

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.3,
  "notes": "Singapore has a mature infrastructure and a relatively efficient grid with significant renewable energy sources, leading to lower emissions. The utilization rates are higher due to the advanced technology and demand in the region. PUE is moderate due to the humid climate, which impacts cooling efficiency."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.2,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a slight improvement in power efficiency (1% for training), and a small increase in utilization rates due to optimization. PUE is adjusted based on regional factors and technology improvements.",
    "grid_factor": 0.3,
    "E_IT": 339108000.0,
    "E_DC": 403538520.0,
    "CO2": 121061556.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.2,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing the trend, N_train and N_inference grow by 10%, with a further 1% improvement in power efficiency and utilization rates increasing slightly. PUE reflects ongoing improvements in technology and infrastructure.",
    "grid_factor": 0.3,
    "E_IT": 380387700.0,
    "E_DC": 448857486.0,
    "CO2": 134657245.79999998
  },
  {
    "year": 2028,
    "N_train": 66500,
    "N_inference": 199500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.2,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Forecasting a 10% growth in both training and inference workloads, with a continued focus on improving power efficiency and utilization rates. PUE is adjusted based on expected advancements in cooling and energy efficiency.",
    "grid_factor": 0.3,
    "E_IT": 426291600.0,
    "E_DC": 498761171.99999994,
    "CO2": 149628351.59999996
  },
  {
    "year": 2029,
    "N_train": 73000,
    "N_inference": 219500,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.2,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Assuming a consistent growth pattern, N_train and N_inference increase by 10%. Power efficiency improves slightly, and utilization rates continue to rise. PUE reflects ongoing enhancements in technology.",
    "grid_factor": 0.3,
    "E_IT": 477648800.0,
    "E_DC": 554072608.0,
    "CO2": 166221782.4
  },
  {
    "year": 2030,
    "N_train": 80000,
    "N_inference": 240500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.2,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Final year of the forecast shows a stable growth of 10% in workloads, with continued improvements in power efficiency and utilization rates. PUE is optimized based on regional advancements.",
    "grid_factor": 0.3,
    "E_IT": 533430000.0,
    "E_DC": 613444500.0,
    "CO2": 184033350.0
  }
]
```

### Oracle — Amsterdam, Netherlands

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 8000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.25,
  "notes": "Amsterdam has a mature infrastructure with a renewable-heavy grid, leading to lower emissions and efficient cooling. Utilization rates are higher due to the region's established tech ecosystem."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency (1% for training and 2.5% for inference). Utilization rates increase slightly due to optimizations. PUE is expected to improve slightly due to the renewable-heavy grid.",
    "grid_factor": 0.25,
    "E_IT": 390890500.0,
    "E_DC": 465159695.0,
    "CO2": 116289923.75
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing the trend, a 10% growth in N_train and N_inference is assumed, with a 1% improvement in power efficiency. Utilization rates continue to rise slightly. PUE improves due to ongoing optimizations and renewable energy usage.",
    "grid_factor": 0.25,
    "E_IT": 444547950.0,
    "E_DC": 524566581.0,
    "CO2": 131141645.25
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming another 10% growth in N_train and N_inference, with a 1% improvement in power efficiency. Utilization rates increase slightly. PUE continues to improve due to the established tech ecosystem in Amsterdam.",
    "grid_factor": 0.25,
    "E_IT": 505274220.0,
    "E_DC": 591170837.4,
    "CO2": 147792709.35
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Continuing the growth trend, another 10% increase in N_train and N_inference is expected, with a 1% improvement in power efficiency. Utilization rates rise. PUE improves due to ongoing enhancements in infrastructure.",
    "grid_factor": 0.25,
    "E_IT": 573931920.0,
    "E_DC": 665761027.1999999,
    "CO2": 166440256.79999998
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241600,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Assuming a final 10% growth in N_train and N_inference, with a 1% improvement in power efficiency. Utilization rates reach optimal levels. PUE continues to improve, reflecting advancements in the renewable energy grid.",
    "grid_factor": 0.25,
    "E_IT": 651588000.0,
    "E_DC": 749326200.0,
    "CO2": 187331550.0
  }
]
```

### Oracle — Riyadh, Saudi Arabia

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.65,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.4,
  "grid_factor_tCO2_per_MWh": 0.6,
  "notes": "Riyadh's climate is hot, leading to higher cooling demands, thus a higher PUE. The grid is moderately renewable, resulting in a grid emission factor of 0.6 tCO2/MWh. Utilization rates are adjusted for the emerging market context."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 50000,
    "N_inference": 150000,
    "P_avg_train": 0.55,
    "P_avg_inference": 0.2,
    "u_train": 0.75,
    "u_inference": 0.65,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.42,
    "notes": "Assuming a 1.5% increase in PUE due to higher cooling demands in Riyadh's hot climate.",
    "grid_factor": 0.6,
    "E_IT": 260250000.0,
    "E_DC": 369555000.0,
    "CO2": 221733000.0
  },
  {
    "year": 2027,
    "N_train": 52500,
    "N_inference": 157500,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.66,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.44,
    "notes": "Assuming a 1.5% increase in PUE due to continued cooling demands and operational efficiency improvements.",
    "grid_factor": 0.6,
    "E_IT": 283232250.0,
    "E_DC": 407854440.0,
    "CO2": 244712664.0
  },
  {
    "year": 2028,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.67,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.46,
    "notes": "Assuming a 1.5% increase in PUE due to persistent cooling needs and slight improvements in energy efficiency.",
    "grid_factor": 0.6,
    "E_IT": 307345500.0,
    "E_DC": 448724430.0,
    "CO2": 269234658.0
  },
  {
    "year": 2029,
    "N_train": 57500,
    "N_inference": 172500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.68,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.48,
    "notes": "Assuming a 1.5% increase in PUE reflecting ongoing cooling demands and operational adjustments.",
    "grid_factor": 0.6,
    "E_IT": 332614500.0,
    "E_DC": 492269460.0,
    "CO2": 295361676.0
  },
  {
    "year": 2030,
    "N_train": 60000,
    "N_inference": 180000,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.69,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.5,
    "notes": "Assuming a 1.5% increase in PUE due to sustained cooling requirements and gradual improvements in efficiency.",
    "grid_factor": 0.6,
    "E_IT": 359064000.0,
    "E_DC": 538596000.0,
    "CO2": 323157600.0
  }
]
```

### Oracle — Tokyo, Japan

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.25,
  "notes": "Tokyo's climate allows for efficient cooling, leading to a lower PUE. The grid is increasingly powered by renewables, resulting in a lower carbon intensity. Utilization rates are higher due to the maturity of the infrastructure and demand for services."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 50000,
    "N_inference": 150000,
    "P_avg_train": 0.55,
    "P_avg_inference": 0.2,
    "u_train": 0.75,
    "u_inference": 0.85,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Assuming a slight improvement in PUE due to ongoing efficiency measures and the use of renewable energy sources.",
    "grid_factor": 0.25,
    "E_IT": 302250000.0,
    "E_DC": 356655000.0,
    "CO2": 89163750.0
  },
  {
    "year": 2027,
    "N_train": 52500,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.198,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "N_train and N_inference increased by 10% and 10% respectively; slight decrease in power consumption efficiency due to increased load.",
    "grid_factor": 0.25,
    "E_IT": 325949400.0,
    "E_DC": 378101304.0,
    "CO2": 94525326.0
  },
  {
    "year": 2028,
    "N_train": 57750,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.196,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.14,
    "notes": "Continued growth in N_train and N_inference; further efficiency improvements in power consumption.",
    "grid_factor": 0.25,
    "E_IT": 358052310.0,
    "E_DC": 408179633.4,
    "CO2": 102044908.35
  },
  {
    "year": 2029,
    "N_train": 63525,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.194,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.12,
    "notes": "Further growth in utilization rates and power efficiency; PUE continues to improve due to technological advancements.",
    "grid_factor": 0.25,
    "E_IT": 393184176.0,
    "E_DC": 440366277.12000006,
    "CO2": 110091569.28000002
  },
  {
    "year": 2030,
    "N_train": 69877,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.192,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.1,
    "notes": "Projected continued growth and efficiency improvements; PUE reflects ongoing renewable energy integration.",
    "grid_factor": 0.25,
    "E_IT": 431615338.20000005,
    "E_DC": 474776872.0200001,
    "CO2": 118694218.00500003
  }
]
```

### Oracle — Madrid, Spain

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.2,
  "notes": "Madrid has a mature infrastructure and a favorable climate for cooling, allowing for a lower PUE. The grid in Spain is increasingly reliant on renewables, contributing to a low grid emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency and utilization due to optimization. PUE is expected to decrease slightly due to improved cooling efficiency in Madrid.",
    "grid_factor": 0.2,
    "E_IT": 344074500.0,
    "E_DC": 406007910.0,
    "CO2": 81201582.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Continuing the trend of 10% growth in N_train and N_inference, with further improvements in power efficiency and utilization. PUE continues to decrease with advancements in cooling technology.",
    "grid_factor": 0.2,
    "E_IT": 391441050.0,
    "E_DC": 454071617.99999994,
    "CO2": 90814323.6
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.14,
    "notes": "Forecasting a 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization. PUE is expected to further decrease due to ongoing advancements in infrastructure.",
    "grid_factor": 0.2,
    "E_IT": 445059780.0,
    "E_DC": 507368149.1999999,
    "CO2": 101473629.83999999
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.12,
    "notes": "Maintaining a growth rate of 10% for N_train and N_inference, with slight improvements in power efficiency and utilization. PUE continues to decrease as cooling technologies improve.",
    "grid_factor": 0.2,
    "E_IT": 505729422.00000006,
    "E_DC": 566416952.6400001,
    "CO2": 113283390.52800003
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.1,
    "notes": "Forecasting a 10% growth in N_train and N_inference, with ongoing improvements in power efficiency and utilization. PUE is projected to decrease further due to enhanced cooling and renewable energy utilization.",
    "grid_factor": 0.2,
    "E_IT": 574345980.0,
    "E_DC": 631780578.0,
    "CO2": 126356115.60000001
  }
]
```

### Oracle — Abilene, Texas, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 7200,
  "H_inference": 8400,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Abilene, Texas has a warm climate which allows for efficient cooling, leading to a moderate PUE. The grid is relatively clean with a mix of renewables, thus a lower emission factor. Utilization rates are higher due to the increasing demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.202,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 7200,
    "H_inference": 8400,
    "PUE": 1.18,
    "notes": "Assuming a 10% growth in N_train and N_inference, slight improvements in power efficiency, and a stable PUE due to efficient cooling in Abilene.",
    "grid_factor": 0.4,
    "E_IT": 407206800.0,
    "E_DC": 480504024.0,
    "CO2": 192201609.60000002
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.204,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 7200,
    "H_inference": 8400,
    "PUE": 1.16,
    "notes": "Continuing 10% growth in N_train and N_inference, with further slight improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 457075080.0,
    "E_DC": 530207092.79999995,
    "CO2": 212082837.12
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.208,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 7200,
    "H_inference": 8400,
    "PUE": 1.14,
    "notes": "Assuming continued growth and efficiency improvements, with PUE slightly decreasing due to better cooling technologies.",
    "grid_factor": 0.4,
    "E_IT": 515892405.6,
    "E_DC": 588117342.384,
    "CO2": 235246936.9536
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.212,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 7200,
    "H_inference": 8400,
    "PUE": 1.12,
    "notes": "Further growth in N_train and N_inference, with stable utilization rates and improvements in power efficiency.",
    "grid_factor": 0.4,
    "E_IT": 582041894.4,
    "E_DC": 651886921.728,
    "CO2": 260754768.69120002
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 240600,
    "P_avg_train": 0.565,
    "P_avg_inference": 0.216,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 7200,
    "H_inference": 8400,
    "PUE": 1.1,
    "notes": "Final year of forecast shows continued growth and efficiency, with PUE improving due to advanced cooling and energy management strategies.",
    "grid_factor": 0.4,
    "E_IT": 654869376.0,
    "E_DC": 720356313.6,
    "CO2": 288142525.44
  }
]
```

### Oracle — Bangladesh

#### Baseline Parameters (2025)
```json
{
  "N_train": 45000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.25,
  "u_train": 0.75,
  "u_inference": 0.65,
  "H_train": 4000,
  "H_inference": 4500,
  "PUE_current": 1.35,
  "grid_factor_tCO2_per_MWh": 0.9,
  "notes": "Bangladesh is an emerging market with a developing infrastructure. The utilization rates are moderate due to potential grid reliability issues, leading to a higher PUE. The grid has a mix of renewable sources, contributing to a moderate emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 45000,
    "N_inference": 150000,
    "P_avg_train": 0.55,
    "P_avg_inference": 0.25,
    "u_train": 0.75,
    "u_inference": 0.65,
    "H_train": 4000,
    "H_inference": 4500,
    "PUE": 1.35,
    "notes": "Current parameters for 2026 based on provided data.",
    "grid_factor": 0.9,
    "E_IT": 183937500.0,
    "E_DC": 248315625.00000003,
    "CO2": 223484062.50000003
  },
  {
    "year": 2027,
    "N_train": 47250,
    "N_inference": 157500,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.253,
    "u_train": 0.76,
    "u_inference": 0.66,
    "H_train": 4000,
    "H_inference": 4500,
    "PUE": 1.34,
    "notes": "Assuming a 5% growth in N_train and N_inference, with slight improvements in power efficiency and utilization.",
    "grid_factor": 0.9,
    "E_IT": 197779995.00000003,
    "E_DC": 265025193.30000004,
    "CO2": 238522673.97000003
  },
  {
    "year": 2028,
    "N_train": 49575,
    "N_inference": 165750,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.256,
    "u_train": 0.77,
    "u_inference": 0.67,
    "H_train": 4000,
    "H_inference": 4500,
    "PUE": 1.33,
    "notes": "Continuing the trend of 5% annual growth in N_train and N_inference, with incremental improvements in efficiency.",
    "grid_factor": 0.9,
    "E_IT": 212828676.00000003,
    "E_DC": 283062139.08000004,
    "CO2": 254755925.17200005
  },
  {
    "year": 2029,
    "N_train": 52050,
    "N_inference": 174000,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.259,
    "u_train": 0.78,
    "u_inference": 0.68,
    "H_train": 4000,
    "H_inference": 4500,
    "PUE": 1.32,
    "notes": "Forecasting continued growth and efficiency improvements, maintaining stability in operational hours.",
    "grid_factor": 0.9,
    "E_IT": 228681324.0,
    "E_DC": 301859347.68,
    "CO2": 271673412.912
  },
  {
    "year": 2030,
    "N_train": 54600,
    "N_inference": 182250,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.262,
    "u_train": 0.79,
    "u_inference": 0.69,
    "H_train": 4000,
    "H_inference": 4500,
    "PUE": 1.31,
    "notes": "Final year of forecast shows ongoing growth and efficiency enhancements, with PUE reflecting regional improvements.",
    "grid_factor": 0.9,
    "E_IT": 245227429.5,
    "E_DC": 321247932.64500004,
    "CO2": 289123139.3805
  }
]
```

### Oracle — New Zealand

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4500,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.15,
  "notes": "New Zealand has a cooler climate which allows for better cooling efficiency, leading to a lower PUE. The grid is relatively clean with a high percentage of renewable energy sources, resulting in a low grid emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.198,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4500,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency and utilization.",
    "grid_factor": 0.15,
    "E_IT": 270151200.0,
    "E_DC": 321479928.0,
    "CO2": 48221989.199999996
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.196,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4500,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continuing the trend of 10% growth in N_train and N_inference, with further improvements in power efficiency and utilization.",
    "grid_factor": 0.15,
    "E_IT": 296801505.0,
    "E_DC": 350225775.9,
    "CO2": 52533866.385
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.194,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4500,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Assuming continued growth and efficiency improvements, with a slight decrease in power consumption.",
    "grid_factor": 0.15,
    "E_IT": 325972548.0,
    "E_DC": 381387881.15999997,
    "CO2": 57208182.173999995
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.192,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4500,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Forecasting a 10% growth in N_train and N_inference, with ongoing improvements in utilization and efficiency.",
    "grid_factor": 0.15,
    "E_IT": 357891192.45000005,
    "E_DC": 415153783.24200004,
    "CO2": 62273067.48630001
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576.5,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.19,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4500,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Continuing the trend of growth and efficiency improvements, with a focus on sustainability.",
    "grid_factor": 0.15,
    "E_IT": 392802489.00000006,
    "E_DC": 451722862.35,
    "CO2": 67758429.3525
  }
]
```

## Expansion Location Predictions

### 1. Kuala Lumpur, Malaysia
**Probability:** 90%
**Key Factors:** Rapidly growing demand for AI services, significant investment planned, and government support for digital economy.
**Notes:** Oracle's commitment to Malaysia as a regional hub for cloud infrastructure.

### 2. Dallas-Fort Worth, Texas, USA
**Probability:** 85%
**Key Factors:** Existing leases for data centers, high demand for cloud services, and strategic location for U.S. operations.
**Notes:** Oracle has signed leases for two data centers in this region.

### 3. Singapore
**Probability:** 80%
**Key Factors:** Established cloud market, ongoing expansion of cloud regions, and strong demand for AI infrastructure.
**Notes:** Oracle has already opened a second cloud region here.

### 4. Amsterdam, Netherlands
**Probability:** 75%
**Key Factors:** Significant investment planned, growing demand for cloud services in Europe, and existing infrastructure.
**Notes:** Oracle plans to invest $1 billion to expand its cloud infrastructure.

### 5. Riyadh, Saudi Arabia
**Probability:** 70%
**Key Factors:** Emerging cloud market, government initiatives to attract tech investments, and lack of major competitors.
**Notes:** Oracle is already establishing a cloud region in Saudi Arabia.

### 6. Tokyo, Japan
**Probability:** 65%
**Key Factors:** High demand for cloud services, existing partnerships, and government support for tech infrastructure.
**Notes:** Oracle has plans for multiple sovereign data centers in Japan.

### 7. Madrid, Spain
**Probability:** 60%
**Key Factors:** Growing demand for AI and cloud services, significant investment planned, and strategic location in Southern Europe.
**Notes:** Oracle is investing $1 billion in AI and cloud computing in Spain.

### 8. Abilene, Texas, USA
**Probability:** 55%
**Key Factors:** Part of the Stargate project, significant capacity planned, and existing infrastructure.
**Notes:** Oracle is already involved in the Stargate AI data center initiative.

### 9. Bangladesh
**Probability:** 50%
**Key Factors:** Emerging market for cloud services, government interest in tech investments, and potential for growth.
**Notes:** Oracle has plans for sovereign data centers in Bangladesh.

### 10. New Zealand
**Probability:** 45%
**Key Factors:** Government interest in tech infrastructure, potential for cloud service growth, and existing partnerships.
**Notes:** Oracle is planning multiple sovereign data centers in New Zealand.

### 11. Johor, Malaysia
**Probability:** 40%
**Key Factors:** Strategic location near Singapore, significant investment in data center infrastructure, and growing demand for cloud services.
**Notes:** Oracle has leased a data center in Yondr's Johor project.

---
# Google

## Energy Forecast

### Google — Caldwell County, North Carolina, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Caldwell County has a moderate climate which allows for efficient cooling, justifying a PUE of 1.2. The grid mix is improving with renewable energy sources, leading to a lower carbon intensity of 0.4 tCO2/MWh. Utilization rates are higher due to the site's established infrastructure and operational maturity."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.202,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates. PUE is adjusted based on regional climate and operational factors.",
    "grid_factor": 0.4,
    "E_IT": 265614800.0,
    "E_DC": 316081612.0,
    "CO2": 126432644.80000001
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.204,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates. PUE is adjusted based on regional climate and operational factors.",
    "grid_factor": 0.4,
    "E_IT": 299489520.0,
    "E_DC": 353397633.59999996,
    "CO2": 141359053.44
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.208,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates. PUE is adjusted based on regional climate and operational factors.",
    "grid_factor": 0.4,
    "E_IT": 339692496.0,
    "E_DC": 397440220.32,
    "CO2": 158976088.128
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.212,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates. PUE is adjusted based on regional climate and operational factors.",
    "grid_factor": 0.4,
    "E_IT": 385095829.20000005,
    "E_DC": 446711161.87200004,
    "CO2": 178684464.74880004
  },
  {
    "year": 2030,
    "N_train": 80520,
    "N_inference": 241576,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.216,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates. PUE is adjusted based on regional climate and operational factors.",
    "grid_factor": 0.4,
    "E_IT": 436372646.4,
    "E_DC": 501828543.35999995,
    "CO2": 200731417.34399998
  }
]
```

### Google — Singapore, Singapore

#### Baseline Parameters (2025)
```json
{
  "N_train": 45000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.15,
  "u_train": 0.75,
  "u_inference": 0.65,
  "H_train": 3000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.25,
  "notes": "Singapore has a tropical climate, which may lead to slightly higher PUE due to cooling needs. However, the grid is relatively clean with a significant share of renewables, resulting in a lower grid emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 47250,
    "N_inference": 165000,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.153,
    "u_train": 0.76,
    "u_inference": 0.66,
    "H_train": 3000,
    "H_inference": 6000,
    "PUE": 1.22,
    "notes": "Assuming a 10% growth in N_train and 10% growth in N_inference. Slight improvement in power efficiency (1% for training, 2% for inference). Utilization increases slightly due to optimizations. PUE adjusted for tropical climate.",
    "grid_factor": 0.25,
    "E_IT": 159544890.0,
    "E_DC": 194644765.79999998,
    "CO2": 48661191.449999996
  },
  {
    "year": 2027,
    "N_train": 49575,
    "N_inference": 181500,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.156,
    "u_train": 0.77,
    "u_inference": 0.67,
    "H_train": 3000,
    "H_inference": 6000,
    "PUE": 1.24,
    "notes": "Continuing 10% growth in N_train and N_inference. Power efficiency improves slightly. Utilization continues to rise. PUE reflects ongoing cooling needs.",
    "grid_factor": 0.25,
    "E_IT": 177494427.0,
    "E_DC": 220093089.48,
    "CO2": 55023272.37
  },
  {
    "year": 2028,
    "N_train": 51900,
    "N_inference": 199650,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.159,
    "u_train": 0.78,
    "u_inference": 0.68,
    "H_train": 3000,
    "H_inference": 6000,
    "PUE": 1.26,
    "notes": "Assuming continued 10% growth in N_train and N_inference. Power efficiency improves further. Utilization increases with optimizations. PUE adjusted for climate.",
    "grid_factor": 0.25,
    "E_IT": 197405262.0,
    "E_DC": 248730630.12,
    "CO2": 62182657.53
  },
  {
    "year": 2029,
    "N_train": 54300,
    "N_inference": 219600,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.162,
    "u_train": 0.79,
    "u_inference": 0.69,
    "H_train": 3000,
    "H_inference": 6000,
    "PUE": 1.28,
    "notes": "Continuing 10% growth trend. Power efficiency improves slightly. Utilization continues to rise. PUE reflects cooling needs.",
    "grid_factor": 0.25,
    "E_IT": 219605670.00000003,
    "E_DC": 281095257.6,
    "CO2": 70273814.4
  },
  {
    "year": 2030,
    "N_train": 56700,
    "N_inference": 241560,
    "P_avg_train": 0.565,
    "P_avg_inference": 0.165,
    "u_train": 0.8,
    "u_inference": 0.7,
    "H_train": 3000,
    "H_inference": 6000,
    "PUE": 1.3,
    "notes": "Assuming continued growth. Power efficiency improves slightly. Utilization increases. PUE reflects ongoing cooling needs.",
    "grid_factor": 0.25,
    "E_IT": 244286280.0,
    "E_DC": 317572164.0,
    "CO2": 79393041.0
  }
]
```

### Google — Virginia, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.2,
  "notes": "The parameters are tailored for Northern Virginia, which has a mature infrastructure and a significant renewable energy mix, leading to lower emissions and efficient cooling. Utilization rates are higher due to the established market and demand."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.2,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a slight improvement in power efficiency (1%), and a small increase in utilization rates due to optimization.",
    "grid_factor": 0.2,
    "E_IT": 339108000.0,
    "E_DC": 403538520.0,
    "CO2": 80707704.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.2,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing the trend with another 10% growth in N_train and N_inference, and a further slight improvement in power efficiency and utilization.",
    "grid_factor": 0.2,
    "E_IT": 380387700.0,
    "E_DC": 448857486.0,
    "CO2": 89771497.2
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.2,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming a continued 10% growth in N_train and N_inference, with a slight increase in power efficiency and utilization.",
    "grid_factor": 0.2,
    "E_IT": 426612120.0,
    "E_DC": 499136180.4,
    "CO2": 99827236.08
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.2,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Continuing the growth trend with 10% increase in N_train and N_inference, along with slight improvements in power efficiency and utilization.",
    "grid_factor": 0.2,
    "E_IT": 478332720.0,
    "E_DC": 554865955.1999999,
    "CO2": 110973191.03999999
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.2,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Assuming a 10% growth in N_train and N_inference, with further improvements in power efficiency and utilization.",
    "grid_factor": 0.2,
    "E_IT": 536130000.0,
    "E_DC": 616549500.0,
    "CO2": 123309900.0
  }
]
```

### Google — Tokyo, Japan

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 8000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.453,
  "notes": "Tokyo has a mature infrastructure with a significant focus on renewable energy, resulting in a lower grid emission factor. The utilization rates are higher due to the advanced technology and demand in the region. PUE is moderate due to the climate, which allows for efficient cooling."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.2,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 8000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a slight improvement in power efficiency, and a small increase in utilization rates. PUE adjusted based on regional factors and technology improvements.",
    "grid_factor": 0.453,
    "E_IT": 357544000.0,
    "E_DC": 425477360.0,
    "CO2": 192741244.08
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.2,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 8000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continuing the trend, N_train and N_inference grow by another 10%, power efficiency improves slightly, and utilization rates increase. PUE reflects ongoing optimizations.",
    "grid_factor": 0.453,
    "E_IT": 401913600.0,
    "E_DC": 474258048.0,
    "CO2": 214838895.74400002
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.2,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 8000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Forecasting another 10% growth in workloads, with continued improvements in power efficiency and utilization. PUE is adjusted for ongoing improvements in technology.",
    "grid_factor": 0.453,
    "E_IT": 451688160.0,
    "E_DC": 528475147.2,
    "CO2": 239399241.6816
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.2,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 8000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Assuming continued growth and efficiency improvements, with N_train and N_inference increasing by 10%. PUE reflects ongoing optimizations and regional factors.",
    "grid_factor": 0.453,
    "E_IT": 507515624.0,
    "E_DC": 588718123.8399999,
    "CO2": 266689310.09951997
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.2,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 8000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Final year of forecast shows continued growth in workloads and efficiency, with N_train and N_inference up by 10%. PUE reflects the best practices and technological advancements.",
    "grid_factor": 0.453,
    "E_IT": 570118080.0,
    "E_DC": 655635792.0,
    "CO2": 297003013.776
  }
]
```

### Google — Eemshaven, Netherlands

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.85,
  "u_inference": 0.75,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.05,
  "notes": "Eemshaven benefits from a renewable-heavy grid with significant investments in local energy infrastructure, leading to lower emissions and efficient cooling due to the cooler climate. Utilization rates are high due to the site's strategic importance in Europe."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.86,
    "u_inference": 0.76,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "N_train and N_inference grow by 10% and 10% respectively. P_avg_train and P_avg_inference improve by 2%. Utilization rates increase slightly due to optimization efforts.",
    "grid_factor": 0.05,
    "E_IT": 338877000.0,
    "E_DC": 403263630.0,
    "CO2": 20163181.5
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.87,
    "u_inference": 0.77,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "N_train and N_inference grow by 10% and 10% respectively. P_avg_train and P_avg_inference improve by 2%. Utilization rates increase slightly due to optimization efforts.",
    "grid_factor": 0.05,
    "E_IT": 385451550.0,
    "E_DC": 454832829.0,
    "CO2": 22741641.450000003
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.88,
    "u_inference": 0.78,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "N_train and N_inference grow by 10% and 10% respectively. P_avg_train and P_avg_inference improve by 2%. Utilization rates increase slightly due to optimization efforts.",
    "grid_factor": 0.05,
    "E_IT": 438171855.0,
    "E_DC": 512661070.34999996,
    "CO2": 25633053.5175
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.89,
    "u_inference": 0.79,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "N_train and N_inference grow by 10% and 10% respectively. P_avg_train and P_avg_inference improve by 2%. Utilization rates increase slightly due to optimization efforts.",
    "grid_factor": 0.05,
    "E_IT": 497823282.0,
    "E_DC": 577475007.12,
    "CO2": 28873750.356000002
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576.5,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.9,
    "u_inference": 0.8,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "N_train and N_inference grow by 10% and 10% respectively. P_avg_train and P_avg_inference improve by 2%. Utilization rates increase slightly due to optimization efforts.",
    "grid_factor": 0.05,
    "E_IT": 565287390.0,
    "E_DC": 650080498.5,
    "CO2": 32504024.925
  }
]
```

### Google — Kuala Lumpur, Malaysia

#### Baseline Parameters (2025)
```json
{
  "N_train": 45000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.65,
  "H_train": 3000,
  "H_inference": 5000,
  "PUE_current": 1.35,
  "grid_factor_tCO2_per_MWh": 0.222,
  "notes": "Kuala Lumpur has a tropical climate which can lead to higher cooling demands, resulting in a slightly higher PUE. The grid mix is still developing, with a moderate carbon intensity based on local data. Utilization rates are adjusted for the emerging market context."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 49500,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.21,
    "u_train": 0.76,
    "u_inference": 0.66,
    "H_train": 3000,
    "H_inference": 5000,
    "PUE": 1.37,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and slight increases in utilization rates. PUE is adjusted based on regional climate factors.",
    "grid_factor": 0.222,
    "E_IT": 177546600.0,
    "E_DC": 243238842.00000003,
    "CO2": 53999022.92400001
  },
  {
    "year": 2027,
    "N_train": 54450,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.22,
    "u_train": 0.77,
    "u_inference": 0.67,
    "H_train": 3000,
    "H_inference": 5000,
    "PUE": 1.39,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and slight increases in utilization rates. PUE is adjusted based on regional climate factors.",
    "grid_factor": 0.222,
    "E_IT": 205459815.0,
    "E_DC": 285589142.84999996,
    "CO2": 63400789.712699994
  },
  {
    "year": 2028,
    "N_train": 59900,
    "N_inference": 199500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.23,
    "u_train": 0.78,
    "u_inference": 0.68,
    "H_train": 3000,
    "H_inference": 5000,
    "PUE": 1.41,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and slight increases in utilization rates. PUE is adjusted based on regional climate factors.",
    "grid_factor": 0.222,
    "E_IT": 237305280.0,
    "E_DC": 334600444.79999995,
    "CO2": 74281298.74559999
  },
  {
    "year": 2029,
    "N_train": 65890,
    "N_inference": 219450,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.24,
    "u_train": 0.79,
    "u_inference": 0.69,
    "H_train": 3000,
    "H_inference": 5000,
    "PUE": 1.43,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and slight increases in utilization rates. PUE is adjusted based on regional climate factors.",
    "grid_factor": 0.222,
    "E_IT": 273838587.0,
    "E_DC": 391589179.40999997,
    "CO2": 86932797.82902
  },
  {
    "year": 2030,
    "N_train": 72480,
    "N_inference": 241395,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.25,
    "u_train": 0.8,
    "u_inference": 0.7,
    "H_train": 3000,
    "H_inference": 5000,
    "PUE": 1.45,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and slight increases in utilization rates. PUE is adjusted based on regional climate factors.",
    "grid_factor": 0.222,
    "E_IT": 315591825.0,
    "E_DC": 457608146.25,
    "CO2": 101589008.4675
  }
]
```

### Google — Groningen, Netherlands

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.85,
  "u_inference": 0.75,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.07,
  "notes": "Groningen has a cooler climate which supports better cooling efficiency, leading to a lower PUE. The Netherlands has a strong commitment to renewable energy, resulting in a low grid emission factor. Utilization rates are higher due to the advanced infrastructure and operational maturity in the region."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.198,
    "u_train": 0.86,
    "u_inference": 0.76,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency and utilization rates.",
    "grid_factor": 0.07,
    "E_IT": 327056400.0,
    "E_DC": 389197116.0,
    "CO2": 27243798.12
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.196,
    "u_train": 0.87,
    "u_inference": 0.77,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing growth of 10% for N_train and N_inference, with further slight improvements in power efficiency and utilization.",
    "grid_factor": 0.07,
    "E_IT": 359123160.0,
    "E_DC": 423765328.79999995,
    "CO2": 29663573.016
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.194,
    "u_train": 0.88,
    "u_inference": 0.78,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming continued growth and efficiency improvements, with a stable utilization rate.",
    "grid_factor": 0.07,
    "E_IT": 394196946.0,
    "E_DC": 461210426.82,
    "CO2": 32284729.877400003
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.192,
    "u_train": 0.89,
    "u_inference": 0.79,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Further growth and efficiency enhancements, with utilization rates continuing to rise.",
    "grid_factor": 0.07,
    "E_IT": 432544919.4000001,
    "E_DC": 501752106.50400007,
    "CO2": 35122647.455280006
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.19,
    "u_train": 0.9,
    "u_inference": 0.8,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Final year of forecast shows continued growth and improved efficiency, with a target utilization rate achieved.",
    "grid_factor": 0.07,
    "E_IT": 474454364.0,
    "E_DC": 545622518.5999999,
    "CO2": 38193576.30199999
  }
]
```

## Expansion Location Predictions

### 1. Caldwell County, North Carolina, USA
**Probability:** 90%
**Key Factors:** Established data center corridor, supportive local regulations, and availability of renewable energy sources.
**Notes:** Strong growth in tech infrastructure in the region.

### 2. Singapore, Singapore
**Probability:** 85%
**Key Factors:** Existing data center presence, reliable infrastructure, and significant market demand in Asia.
**Notes:** Expansion of the fourth data center facility planned for 2024.

### 3. Virginia, USA
**Probability:** 80%
**Key Factors:** Strong existing operations, favorable regulations, and a growing tech ecosystem.
**Notes:** Continued investment in renewable energy initiatives.

### 4. Tokyo, Japan
**Probability:** 75%
**Key Factors:** Strategic location for Asia-Pacific operations, existing infrastructure, and government support for tech investments.
**Notes:** Ongoing digital initiatives and infrastructure improvements.

### 5. Eemshaven, Netherlands
**Probability:** 70%
**Key Factors:** Established data center location, access to renewable energy, and favorable European regulations.
**Notes:** Potential for expansion due to increasing demand in Europe.

### 6. Kuala Lumpur, Malaysia
**Probability:** 60%
**Key Factors:** Recent investment by Google, growing digital economy, and favorable regulatory environment.
**Notes:** Strategic location for Southeast Asia expansion.

### 7. Groningen, Netherlands
**Probability:** 40%
**Key Factors:** Proximity to existing data centers, strong renewable energy access, and supportive local policies.
**Notes:** Potential for further development in the region.

---
# Microsoft

## Energy Forecast

### Microsoft — Northern Virginia, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.2,
  "notes": "Northern Virginia has a mature infrastructure with a strong renewable energy mix, leading to lower PUE and grid emission factors. The utilization rates are higher due to the demand for AI workloads in this region."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.19,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a growth rate of 10% for N_train and N_inference, and slight improvements in power efficiency and utilization rates.",
    "grid_factor": 0.2,
    "E_IT": 324159000.0,
    "E_DC": 385749210.0,
    "CO2": 77149842.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.18,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing growth of 10% in N_train and N_inference, with further efficiency gains.",
    "grid_factor": 0.2,
    "E_IT": 347100600.0,
    "E_DC": 409578708.0,
    "CO2": 81915741.60000001
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.17,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming continued growth and efficiency improvements, with utilization rates increasing slightly.",
    "grid_factor": 0.2,
    "E_IT": 371029560.0,
    "E_DC": 434104585.2,
    "CO2": 86820917.04
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.16,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Forecasting a steady growth pattern with ongoing improvements in power efficiency.",
    "grid_factor": 0.2,
    "E_IT": 395877999.00000006,
    "E_DC": 459218478.84000003,
    "CO2": 91843695.768
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.15,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "End of forecast period, projecting continued growth and efficiency improvements.",
    "grid_factor": 0.2,
    "E_IT": 421549320.0,
    "E_DC": 484781717.99999994,
    "CO2": 96956343.6
  }
]
```

### Microsoft — Texas, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Texas has a mature infrastructure with a mix of renewables and natural gas, leading to a moderate grid emission factor. Utilization rates are high due to demand, and the PUE reflects efficient cooling in the warmer climate."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, and a slight improvement in power efficiency and utilization rates.",
    "grid_factor": 0.4,
    "E_IT": 344074500.0,
    "E_DC": 409448655.0,
    "CO2": 163779462.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing growth trends with a 10% increase in N_train and N_inference, and slight efficiency improvements.",
    "grid_factor": 0.4,
    "E_IT": 391441050.0,
    "E_DC": 461900439.0,
    "CO2": 184760175.60000002
  },
  {
    "year": 2028,
    "N_train": 66500,
    "N_inference": 199500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming continued growth of 10% in N_train and N_inference, with minor efficiency gains.",
    "grid_factor": 0.4,
    "E_IT": 444725400.0,
    "E_DC": 520328717.99999994,
    "CO2": 208131487.2
  },
  {
    "year": 2029,
    "N_train": 73000,
    "N_inference": 219500,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Maintaining a growth rate of 10% for N_train and N_inference, with slight improvements in power efficiency.",
    "grid_factor": 0.4,
    "E_IT": 504998500.0,
    "E_DC": 585798260.0,
    "CO2": 234319304.0
  },
  {
    "year": 2030,
    "N_train": 80000,
    "N_inference": 240000,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Forecasting a 10% growth in N_train and N_inference, with continued efficiency improvements.",
    "grid_factor": 0.4,
    "E_IT": 570600000.0,
    "E_DC": 656190000.0,
    "CO2": 262476000.0
  }
]
```

### Microsoft — Loughton, UK

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.25,
  "notes": "Loughton, UK has a cooler climate which supports better cooling efficiency, leading to a lower PUE. The UK grid is increasingly renewable, resulting in a lower grid emission factor. Utilization rates are higher due to the established infrastructure and demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.198,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, slight efficiency improvements, and a stable PUE due to the cooler climate and renewable energy sources.",
    "grid_factor": 0.25,
    "E_IT": 261038800.0,
    "E_DC": 310636172.0,
    "CO2": 77659043.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.196,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continuing growth trend of 10% for N_train and N_inference, with minor efficiency improvements and stable utilization rates.",
    "grid_factor": 0.25,
    "E_IT": 289301320.0,
    "E_DC": 341375557.59999996,
    "CO2": 85343889.39999999
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.194,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Forecasting a continued 10% growth in workloads, with slight improvements in power efficiency and utilization.",
    "grid_factor": 0.25,
    "E_IT": 320574012.0,
    "E_DC": 375071594.03999996,
    "CO2": 93767898.50999999
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.192,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Assuming a consistent growth trend, with minor efficiency gains and stable utilization rates.",
    "grid_factor": 0.25,
    "E_IT": 355148832.00000006,
    "E_DC": 411972645.12000006,
    "CO2": 102993161.28000002
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.565,
    "P_avg_inference": 0.19,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Continuing the growth trend with slight improvements in efficiency and utilization, reflecting ongoing optimization efforts.",
    "grid_factor": 0.25,
    "E_IT": 393323000.0,
    "E_DC": 452321449.99999994,
    "CO2": 113080362.49999999
  }
]
```

### Microsoft — Wisconsin, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.004,
  "notes": "Wisconsin has a cooler climate, allowing for better cooling efficiency, thus a lower PUE. The grid is increasingly renewable, contributing to a low emission factor. Utilization rates are higher due to the established infrastructure."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, slight improvement in power efficiency, and stable utilization rates. PUE is slightly improved due to cooling efficiency in Wisconsin.",
    "grid_factor": 0.004,
    "E_IT": 268169000.0,
    "E_DC": 319121110.0,
    "CO2": 1276484.44
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continuing growth of 10% in N_train and N_inference, with further slight improvements in power efficiency and utilization rates. PUE remains stable.",
    "grid_factor": 0.004,
    "E_IT": 305174100.0,
    "E_DC": 360105438.0,
    "CO2": 1440421.752
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Assuming continued growth and efficiency improvements, with utilization rates rising slightly. PUE improves due to ongoing advancements in cooling technology.",
    "grid_factor": 0.004,
    "E_IT": 347071560.0,
    "E_DC": 406073725.2,
    "CO2": 1624294.9008
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Growth continues at 10% with slight efficiency gains. Utilization rates are expected to rise as optimization efforts take effect. PUE continues to improve.",
    "grid_factor": 0.004,
    "E_IT": 394460160.0,
    "E_DC": 457573785.59999996,
    "CO2": 1830295.1423999998
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Final year of forecast shows continued growth and efficiency improvements. Utilization rates are expected to stabilize. PUE reflects ongoing advancements in cooling and energy efficiency.",
    "grid_factor": 0.004,
    "E_IT": 447982500.0,
    "E_DC": 515179874.99999994,
    "CO2": 2060719.4999999998
  }
]
```

### Microsoft — Singapore

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.0004,
  "notes": "Singapore has a mature infrastructure with a significant focus on renewable energy, leading to lower grid emissions. The utilization rates are higher due to the advanced cooling systems and favorable climate conditions. PUE is moderate due to the efficient cooling strategies employed."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.2,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a 1% improvement in P_avg_train and P_avg_inference. Utilization rates increase slightly as optimization continues.",
    "grid_factor": 0.0004,
    "E_IT": 339108000.0,
    "E_DC": 403538520.0,
    "CO2": 161415.408
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.2,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing growth of 10% in N_train and N_inference, with a 1% improvement in P_avg_train and P_avg_inference. Utilization rates continue to rise.",
    "grid_factor": 0.0004,
    "E_IT": 380387700.0,
    "E_DC": 448857486.0,
    "CO2": 179542.9944
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.2,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a 1% improvement in P_avg_train and P_avg_inference. Utilization rates increase as optimization continues.",
    "grid_factor": 0.0004,
    "E_IT": 426612120.0,
    "E_DC": 499136180.4,
    "CO2": 199654.47216
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.2,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Continuing growth of 10% in N_train and N_inference, with a 1% improvement in P_avg_train and P_avg_inference. Utilization rates continue to rise.",
    "grid_factor": 0.0004,
    "E_IT": 478332720.0,
    "E_DC": 554865955.1999999,
    "CO2": 221946.38207999998
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.2,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a 1% improvement in P_avg_train and P_avg_inference. Utilization rates increase slightly as optimization continues.",
    "grid_factor": 0.0004,
    "E_IT": 536130000.0,
    "E_DC": 616549500.0,
    "CO2": 246619.80000000002
  }
]
```

### Microsoft — Narvik, Norway

#### Baseline Parameters (2025)
```json
{
  "N_train": 45000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.85,
  "u_inference": 0.75,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.005,
  "notes": "Narvik, Norway has a cooler climate which allows for better cooling efficiency, resulting in a lower PUE. The region benefits from a renewable-heavy grid, contributing to a low grid emission factor. Utilization rates are higher due to the efficient infrastructure."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 49500,
    "N_inference": 165000,
    "P_avg_train": 0.5585,
    "P_avg_inference": 0.202,
    "u_train": 0.86,
    "u_inference": 0.76,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 1.5% improvement in power efficiency, and a slight increase in utilization rates due to optimization. PUE is expected to improve slightly due to the cooler climate in Narvik, Norway.",
    "grid_factor": 0.005,
    "E_IT": 319967670.0,
    "E_DC": 380761527.3,
    "CO2": 1903807.6365
  },
  {
    "year": 2027,
    "N_train": 54450,
    "N_inference": 181500,
    "P_avg_train": 0.5671,
    "P_avg_inference": 0.204,
    "u_train": 0.87,
    "u_inference": 0.77,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 1.5% improvement in power efficiency, and a slight increase in utilization rates due to optimization. PUE is expected to improve slightly due to the cooler climate in Narvik, Norway.",
    "grid_factor": 0.005,
    "E_IT": 360756405.9,
    "E_DC": 425692558.96199995,
    "CO2": 2128462.79481
  },
  {
    "year": 2028,
    "N_train": 59900,
    "N_inference": 199500,
    "P_avg_train": 0.5758,
    "P_avg_inference": 0.208,
    "u_train": 0.88,
    "u_inference": 0.78,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 1.5% improvement in power efficiency, and a slight increase in utilization rates due to optimization. PUE is expected to improve slightly due to the cooler climate in Narvik, Norway.",
    "grid_factor": 0.005,
    "E_IT": 408677577.6,
    "E_DC": 478152765.792,
    "CO2": 2390763.82896
  },
  {
    "year": 2029,
    "N_train": 65890,
    "N_inference": 219450,
    "P_avg_train": 0.5845,
    "P_avg_inference": 0.212,
    "u_train": 0.89,
    "u_inference": 0.79,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 1.5% improvement in power efficiency, and a slight increase in utilization rates due to optimization. PUE is expected to improve slightly due to the cooler climate in Narvik, Norway.",
    "grid_factor": 0.005,
    "E_IT": 462932246.70000005,
    "E_DC": 537001406.172,
    "CO2": 2685007.0308600003
  },
  {
    "year": 2030,
    "N_train": 72480,
    "N_inference": 241395,
    "P_avg_train": 0.5933,
    "P_avg_inference": 0.216,
    "u_train": 0.9,
    "u_inference": 0.8,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 1.5% improvement in power efficiency, and a slight increase in utilization rates due to optimization. PUE is expected to improve slightly due to the cooler climate in Narvik, Norway.",
    "grid_factor": 0.005,
    "E_IT": 524204265.6,
    "E_DC": 602834905.4399999,
    "CO2": 3014174.5272
  }
]
```

### Microsoft — Poland

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.1,
  "notes": "Poland's climate allows for efficient cooling, leading to a lower PUE. The grid is increasingly renewable, contributing to a low emission factor. Utilization rates are higher due to growing demand for AI services."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.198,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Forecasting based on a 10% growth in N_train and N_inference, a 0.5% improvement in average power efficiency, and a slight increase in utilization rates due to optimization. PUE is expected to decrease slightly due to efficient cooling in Poland.",
    "grid_factor": 0.1,
    "E_IT": 261038800.0,
    "E_DC": 310636172.0,
    "CO2": 31063617.200000003
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.196,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continuing the trend with a 10% growth in N_train and N_inference, a 0.5% improvement in average power efficiency, and a slight increase in utilization rates. PUE continues to decrease due to ongoing improvements in cooling efficiency.",
    "grid_factor": 0.1,
    "E_IT": 289301320.0,
    "E_DC": 341375557.59999996,
    "CO2": 34137555.76
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.194,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Forecasting a 10% growth in N_train and N_inference, a 0.5% improvement in average power efficiency, and a slight increase in utilization rates. PUE continues to decrease as cooling technology improves.",
    "grid_factor": 0.1,
    "E_IT": 320574012.0,
    "E_DC": 375071594.03999996,
    "CO2": 37507159.404
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.192,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Continuing the trend with a 10% growth in N_train and N_inference, a 0.5% improvement in average power efficiency, and a slight increase in utilization rates. PUE continues to decrease due to ongoing improvements in cooling efficiency.",
    "grid_factor": 0.1,
    "E_IT": 355173090.8000001,
    "E_DC": 412000785.32800007,
    "CO2": 41200078.53280001
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.565,
    "P_avg_inference": 0.19,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Forecasting a 10% growth in N_train and N_inference, a 0.5% improvement in average power efficiency, and a slight increase in utilization rates. PUE continues to decrease as cooling technology and renewable energy sources improve.",
    "grid_factor": 0.1,
    "E_IT": 393446176.0,
    "E_DC": 452463102.4,
    "CO2": 45246310.24
  }
]
```

### Microsoft — Johor Bahru, Malaysia

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.65,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.1,
  "notes": "Johor Bahru is an emerging data center market, influenced by its proximity to Singapore. The parameters reflect a balance between the need for efficiency and the challenges of a developing infrastructure. Utilization rates are moderate due to the growing nature of the market, while the grid factor is low due to increasing investments in renewable energy."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.66,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, with a slight increase in power efficiency and utilization rates.",
    "grid_factor": 0.1,
    "E_IT": 227579000.0,
    "E_DC": 270819010.0,
    "CO2": 27081901.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.67,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continued growth of 10% in N_train and N_inference, with incremental improvements in power efficiency and utilization.",
    "grid_factor": 0.1,
    "E_IT": 259436100.00000003,
    "E_DC": 306134598.0,
    "CO2": 30613459.8
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.68,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Assumes a 10% growth in N_train and N_inference, with slight improvements in power efficiency and utilization.",
    "grid_factor": 0.1,
    "E_IT": 295561860.0,
    "E_DC": 345807376.2,
    "CO2": 34580737.62
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.69,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Forecast continues with a 10% growth in N_train and N_inference, with ongoing improvements in efficiency and utilization.",
    "grid_factor": 0.1,
    "E_IT": 336508744.0,
    "E_DC": 390350143.03999996,
    "CO2": 39035014.304
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.7,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Final year of forecast assumes continued growth and efficiency improvements, with a stable PUE.",
    "grid_factor": 0.1,
    "E_IT": 382897320.0,
    "E_DC": 440331917.99999994,
    "CO2": 44033191.8
  }
]
```

### Microsoft — Georgia, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7200,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Georgia has a moderate climate which allows for efficient cooling, leading to a PUE of 1.2. The state has a growing renewable energy sector, contributing to a lower grid emission factor. Utilization rates are higher due to the increasing demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.202,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a 1% improvement in power efficiency and utilization rates slightly increasing due to optimization.",
    "grid_factor": 0.4,
    "E_IT": 345071760.0,
    "E_DC": 410635394.4,
    "CO2": 164254157.76
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.204,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.18,
    "notes": "Continuing the trend with another 10% growth in N_train and N_inference, with slight improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 387338424.0,
    "E_DC": 457059340.32,
    "CO2": 182823736.12800002
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.206,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.17,
    "notes": "Assuming a consistent growth of 10% in N_train and N_inference, with power efficiency improving slightly and utilization rates increasing.",
    "grid_factor": 0.4,
    "E_IT": 434689160.4,
    "E_DC": 508586317.6679999,
    "CO2": 203434527.06719998
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.208,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.16,
    "notes": "Continuing the growth trend with a 10% increase in N_train and N_inference, with continued improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 487726262.76000005,
    "E_DC": 565762464.8016,
    "CO2": 226304985.92064
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.565,
    "P_avg_inference": 0.21,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.15,
    "notes": "Assuming a 10% growth in N_train and N_inference, with slight improvements in power efficiency and utilization rates.",
    "grid_factor": 0.4,
    "E_IT": 547120420.8,
    "E_DC": 629188483.9199998,
    "CO2": 251675393.56799996
  }
]
```

### Microsoft — Wyoming, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.3,
  "notes": "Wyoming has a cooler climate, allowing for better cooling efficiency, which results in a lower PUE. The grid is moderately renewable, leading to a lower carbon emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and slight increases in utilization.",
    "grid_factor": 0.3,
    "E_IT": 344074500.0,
    "E_DC": 409448655.0,
    "CO2": 122834596.5
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing growth trends with a 10% increase in workloads and slight improvements in efficiency and utilization.",
    "grid_factor": 0.3,
    "E_IT": 391441050.0,
    "E_DC": 461900439.0,
    "CO2": 138570131.7
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Forecasting a 10% growth in workloads with continued efficiency improvements and utilization increases.",
    "grid_factor": 0.3,
    "E_IT": 445059780.0,
    "E_DC": 520719942.59999996,
    "CO2": 156215982.77999997
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Assuming a 10% growth in workloads and continued improvements in power efficiency and utilization.",
    "grid_factor": 0.3,
    "E_IT": 505729422.00000006,
    "E_DC": 586646129.52,
    "CO2": 175993838.85599998
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576.5,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Continuing the trend of 10% growth in workloads with slight improvements in efficiency and utilization.",
    "grid_factor": 0.3,
    "E_IT": 574346688.75,
    "E_DC": 660498692.0625,
    "CO2": 198149607.61875
  }
]
```

## Expansion Location Predictions

### 1. Northern Virginia, USA
**Probability:** 90%
**Key Factors:** High demand for AI workloads, existing infrastructure, favorable tax incentives.
**Notes:** Data Center Alley is a major hub for data centers.

### 2. Texas, USA
**Probability:** 85%
**Key Factors:** Lower energy costs, strong fiber networks, and favorable business environment.
**Notes:** Texas is becoming a significant player in the data center market.

### 3. Loughton, UK
**Probability:** 80%
**Key Factors:** Partnerships for supercomputing, growing demand for cloud services in Europe.
**Notes:** UK expansion aligns with Microsoft's European digital commitments.

### 4. Wisconsin, USA
**Probability:** 75%
**Key Factors:** Recent investment in AI datacenter, supportive local regulations.
**Notes:** Wisconsin's Fairwater datacenter is a key facility for AI workloads.

### 5. Singapore
**Probability:** 70%
**Key Factors:** Strategic location in Asia, existing infrastructure, and demand for cloud services.
**Notes:** Singapore is a critical hub for Microsoft in Asia.

### 6. Narvik, Norway
**Probability:** 65%
**Key Factors:** Partnerships for AI datacenter development, renewable energy availability.
**Notes:** Norway's focus on sustainability aligns with Microsoft's goals.

### 7. Poland
**Probability:** 60%
**Key Factors:** Growing demand for cloud services in Eastern Europe, favorable regulations.
**Notes:** Poland is part of Microsoft's European expansion strategy.

### 8. Johor Bahru, Malaysia
**Probability:** 55%
**Key Factors:** Proximity to Singapore, growing demand for data centers in Southeast Asia.
**Notes:** Chinese firms are also investing in this region.

### 9. Georgia, USA
**Probability:** 50%
**Key Factors:** Favorable tax incentives, growing tech ecosystem.
**Notes:** Georgia is emerging as a data center location.

### 10. Wyoming, USA
**Probability:** 45%
**Key Factors:** Low energy costs, potential for renewable energy projects.
**Notes:** Wyoming's energy landscape is attractive for data centers.

---
# Apple

## Energy Forecast

### Apple — Maiden, North Carolina, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.25,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 8000,
  "H_inference": 8500,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Assuming Maiden, NC has a moderate climate with good cooling efficiency, leading to a PUE of 1.2. The grid in North Carolina has a growing share of renewables, resulting in a lower emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.245,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 8000,
    "H_inference": 8500,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency (1% reduction in P_avg_train and 2% in P_avg_inference), and a 1% increase in utilization.",
    "grid_factor": 0.4,
    "E_IT": 476082750.0,
    "E_DC": 566538472.5,
    "CO2": 226615389.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.24,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 8000,
    "H_inference": 8500,
    "PUE": 1.18,
    "notes": "Continuing the growth trend with another 10% increase in N_train and N_inference, with further slight improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 519646600.0,
    "E_DC": 613182988.0,
    "CO2": 245273195.20000002
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.235,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 8000,
    "H_inference": 8500,
    "PUE": 1.17,
    "notes": "Assuming a continued growth rate of 10% for N_train and N_inference, with ongoing improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 566886210.0,
    "E_DC": 663256865.6999999,
    "CO2": 265302746.27999997
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.23,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 8000,
    "H_inference": 8500,
    "PUE": 1.16,
    "notes": "Continuing the trend with another 10% increase in N_train and N_inference, with slight improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 618073475.2500001,
    "E_DC": 716965231.2900001,
    "CO2": 286786092.51600003
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 8000,
    "H_inference": 8500,
    "PUE": 1.15,
    "notes": "Final year of forecast with a 10% increase in N_train and N_inference, with continued improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 673492690.0,
    "E_DC": 774516593.4999999,
    "CO2": 309806637.4
  }
]
```

### Apple — Houston, Texas, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7200,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Houston has a warm climate, which may lead to moderate cooling efficiency, hence a PUE of 1.2. The grid mix in Texas includes a significant amount of natural gas and renewables, resulting in a moderate grid emission factor. Utilization rates are higher due to the established tech ecosystem in the area."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight increase in power efficiency and utilization rates due to optimization. PUE is slightly improved due to better cooling efficiency.",
    "grid_factor": 0.4,
    "E_IT": 349892400.0,
    "E_DC": 416371956.0,
    "CO2": 166548782.4
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.18,
    "notes": "Continuing growth trend of 10% for N_train and N_inference, with gradual improvements in power efficiency and utilization rates. PUE remains stable due to consistent cooling practices.",
    "grid_factor": 0.4,
    "E_IT": 398073060.0,
    "E_DC": 469726210.79999995,
    "CO2": 187890484.32
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.17,
    "notes": "Assuming a 10% growth in N_train and N_inference, with further enhancements in power efficiency and utilization rates. PUE improves slightly due to ongoing optimization efforts.",
    "grid_factor": 0.4,
    "E_IT": 452614536.0,
    "E_DC": 529559007.11999995,
    "CO2": 211823602.848
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.16,
    "notes": "Continuing the growth trend with a 10% increase in N_train and N_inference, with slight improvements in power efficiency and utilization rates. PUE remains stable.",
    "grid_factor": 0.4,
    "E_IT": 514329545.40000004,
    "E_DC": 596622272.664,
    "CO2": 238648909.06560004
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7200,
    "PUE": 1.15,
    "notes": "Assuming a 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization rates. PUE shows a slight improvement due to enhanced cooling strategies.",
    "grid_factor": 0.4,
    "E_IT": 584129808.0,
    "E_DC": 671749279.1999999,
    "CO2": 268699711.68
  }
]
```

### Apple — Iowa, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.85,
  "u_inference": 0.75,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Iowa has a cooler climate which allows for better cooling efficiency, leading to a lower PUE. The grid has a significant share of renewables, resulting in a lower carbon emission factor. Utilization rates are higher due to the established infrastructure in the region."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.86,
    "u_inference": 0.76,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates due to optimization. PUE is slightly reduced due to the cooler climate in Iowa.",
    "grid_factor": 0.4,
    "E_IT": 260194000.0,
    "E_DC": 309630860.0,
    "CO2": 123852344.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.87,
    "u_inference": 0.77,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continuing the trend of 10% growth in N_train and N_inference, with a 2% improvement in power efficiency and utilization rates. PUE remains low due to ongoing cooling efficiency.",
    "grid_factor": 0.4,
    "E_IT": 296099100.0,
    "E_DC": 349396938.0,
    "CO2": 139758775.20000002
  },
  {
    "year": 2028,
    "N_train": 66500,
    "N_inference": 199500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.88,
    "u_inference": 0.78,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Following the same growth patterns, with a 10% increase in N_train and N_inference, and a 2% improvement in efficiency. Utilization rates continue to rise, and PUE improves slightly.",
    "grid_factor": 0.4,
    "E_IT": 336503300.0,
    "E_DC": 393708861.0,
    "CO2": 157483544.4
  },
  {
    "year": 2029,
    "N_train": 73000,
    "N_inference": 219500,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.89,
    "u_inference": 0.79,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Maintaining the growth trajectory with a 10% increase in N_train and N_inference, and a 2% improvement in power efficiency. Utilization rates increase, and PUE remains favorable.",
    "grid_factor": 0.4,
    "E_IT": 382223800.0,
    "E_DC": 443379607.99999994,
    "CO2": 177351843.2
  },
  {
    "year": 2030,
    "N_train": 80000,
    "N_inference": 240000,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.9,
    "u_inference": 0.8,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Final year of the forecast shows a continued 10% growth in N_train and N_inference, with a 2% efficiency improvement. Utilization rates reach optimal levels, and PUE continues to decrease.",
    "grid_factor": 0.4,
    "E_IT": 432000000.0,
    "E_DC": 496799999.99999994,
    "CO2": 198720000.0
  }
]
```

### Apple — Oregon, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.1,
  "notes": "Oregon has a favorable climate for cooling, allowing for a lower PUE. The grid is heavily reliant on renewables, leading to a low carbon emission factor. The utilization rates are higher due to the established infrastructure and demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates due to optimization.",
    "grid_factor": 0.1,
    "E_IT": 268169000.0,
    "E_DC": 316439420.0,
    "CO2": 31643942.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates due to optimization.",
    "grid_factor": 0.1,
    "E_IT": 305174100.0,
    "E_DC": 354001956.0,
    "CO2": 35400195.6
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.14,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates due to optimization.",
    "grid_factor": 0.1,
    "E_IT": 347071560.0,
    "E_DC": 395661578.4,
    "CO2": 39566157.839999996
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.12,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates due to optimization.",
    "grid_factor": 0.1,
    "E_IT": 394460160.0,
    "E_DC": 441795379.20000005,
    "CO2": 44179537.92000001
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241600,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.1,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization rates due to optimization.",
    "grid_factor": 0.1,
    "E_IT": 448104000.0,
    "E_DC": 492914400.00000006,
    "CO2": 49291440.00000001
  }
]
```

### Apple — Arizona, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Arizona has a warm climate, which may lead to higher cooling demands, resulting in a PUE of 1.2. The grid is moderately renewable, leading to a grid emission factor of 0.4 tCO2/MWh. Utilization rates are higher due to the growing demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.19,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.21,
    "notes": "Assumed a 10% growth in N_train and N_inference. Slight improvement in power efficiency (P_avg_train and P_avg_inference) by 1%. Utilization rates increased slightly due to optimization. PUE increased slightly due to higher cooling demands in Arizona.",
    "grid_factor": 0.4,
    "E_IT": 252054000.0,
    "E_DC": 304985340.0,
    "CO2": 121994136.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.18,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.22,
    "notes": "Assumed a 10% growth in N_train and N_inference. Continued slight improvement in power efficiency (P_avg_train and P_avg_inference) by another 1%. Utilization rates increased slightly due to optimization. PUE increased slightly due to higher cooling demands in Arizona.",
    "grid_factor": 0.4,
    "E_IT": 269297600.0,
    "E_DC": 328543072.0,
    "CO2": 131417228.80000001
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.17,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.23,
    "notes": "Assumed a 10% growth in N_train and N_inference. Continued slight improvement in power efficiency (P_avg_train and P_avg_inference) by another 1%. Utilization rates increased slightly due to optimization. PUE increased slightly due to higher cooling demands in Arizona.",
    "grid_factor": 0.4,
    "E_IT": 287176560.0,
    "E_DC": 353227168.8,
    "CO2": 141290867.52
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.16,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.24,
    "notes": "Assumed a 10% growth in N_train and N_inference. Continued slight improvement in power efficiency (P_avg_train and P_avg_inference) by another 1%. Utilization rates increased slightly due to optimization. PUE increased slightly due to higher cooling demands in Arizona.",
    "grid_factor": 0.4,
    "E_IT": 305595360.0,
    "E_DC": 378938246.4,
    "CO2": 151575298.56
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.15,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.25,
    "notes": "Assumed a 10% growth in N_train and N_inference. Continued slight improvement in power efficiency (P_avg_train and P_avg_inference) by another 1%. Utilization rates increased slightly due to optimization. PUE increased slightly due to higher cooling demands in Arizona.",
    "grid_factor": 0.4,
    "E_IT": 324415000.0,
    "E_DC": 405518750.0,
    "CO2": 162207500.0
  }
]
```

### Apple — Nevada, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Nevada has a relatively mature infrastructure with a moderate climate, allowing for efficient cooling and a reasonable PUE. The grid has a significant share of renewables, resulting in a lower carbon intensity."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.195,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a 2% improvement in power efficiency and slight increases in utilization.",
    "grid_factor": 0.4,
    "E_IT": 329125500.0,
    "E_DC": 391659345.0,
    "CO2": 156663738.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.191,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing the trend with another 10% growth in N_train and N_inference, and a further 2% improvement in power efficiency.",
    "grid_factor": 0.4,
    "E_IT": 359259285.0,
    "E_DC": 423925956.29999995,
    "CO2": 169570382.51999998
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.187,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 391936908.0,
    "E_DC": 458566182.35999995,
    "CO2": 183426472.944
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.183,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Maintaining the growth trend with 10% increases in N_train and N_inference, and further improvements in efficiency.",
    "grid_factor": 0.4,
    "E_IT": 427346632.35,
    "E_DC": 495722093.526,
    "CO2": 198288837.41040003
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.179,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Continuing the growth pattern with 10% increases in N_train and N_inference, with slight improvements in power efficiency and utilization.",
    "grid_factor": 0.4,
    "E_IT": 465685255.20000005,
    "E_DC": 535538043.48,
    "CO2": 214215217.39200002
  }
]
```

### Apple — California, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.15,
  "notes": "California has a mature infrastructure with a strong emphasis on renewable energy, leading to lower emissions and efficient cooling. Utilization rates are higher due to the advanced technology ecosystem."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 1% improvement in power efficiency, and slight increases in utilization rates.",
    "grid_factor": 0.15,
    "E_IT": 344074500.0,
    "E_DC": 409448655.0,
    "CO2": 61417298.25
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing growth trends with a 10% increase in N_train and N_inference, and further improvements in power efficiency and utilization.",
    "grid_factor": 0.15,
    "E_IT": 391441050.0,
    "E_DC": 461900439.0,
    "CO2": 69285065.85
  },
  {
    "year": 2028,
    "N_train": 66500,
    "N_inference": 199500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming another 10% growth in N_train and N_inference, with continued efficiency and utilization improvements.",
    "grid_factor": 0.15,
    "E_IT": 444725400.0,
    "E_DC": 520328717.99999994,
    "CO2": 78049307.69999999
  },
  {
    "year": 2029,
    "N_train": 73000,
    "N_inference": 219500,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Forecasting a 10% growth in N_train and N_inference, with ongoing enhancements in power efficiency and utilization.",
    "grid_factor": 0.15,
    "E_IT": 504998500.0,
    "E_DC": 585798260.0,
    "CO2": 87869739.0
  },
  {
    "year": 2030,
    "N_train": 80000,
    "N_inference": 240500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Continuing the trend with a 10% growth in N_train and N_inference, and further improvements in power efficiency and utilization.",
    "grid_factor": 0.15,
    "E_IT": 571308750.0,
    "E_DC": 657005062.5,
    "CO2": 98550759.375
  }
]
```

### Apple — Michigan, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.3,
  "notes": "Michigan has a moderate climate which allows for efficient cooling, leading to a lower PUE. The grid has a significant portion of renewables, resulting in a lower emission factor. Utilization rates are higher due to the established infrastructure."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, slight improvement in power efficiency, and stable utilization rates. PUE is adjusted based on regional climate efficiency.",
    "grid_factor": 0.3,
    "E_IT": 268169000.0,
    "E_DC": 316439420.0,
    "CO2": 94931826.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, slight improvement in power efficiency, and stable utilization rates. PUE is adjusted based on regional climate efficiency.",
    "grid_factor": 0.3,
    "E_IT": 305174100.0,
    "E_DC": 354001956.0,
    "CO2": 106200586.8
  },
  {
    "year": 2028,
    "N_train": 66500,
    "N_inference": 199500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.14,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, slight improvement in power efficiency, and stable utilization rates. PUE is adjusted based on regional climate efficiency.",
    "grid_factor": 0.3,
    "E_IT": 346810800.0,
    "E_DC": 395364311.99999994,
    "CO2": 118609293.59999998
  },
  {
    "year": 2029,
    "N_train": 73000,
    "N_inference": 219500,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.12,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, slight improvement in power efficiency, and stable utilization rates. PUE is adjusted based on regional climate efficiency.",
    "grid_factor": 0.3,
    "E_IT": 393969800.0,
    "E_DC": 441246176.00000006,
    "CO2": 132373852.80000001
  },
  {
    "year": 2030,
    "N_train": 80000,
    "N_inference": 240000,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.1,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, slight improvement in power efficiency, and stable utilization rates. PUE is adjusted based on regional climate efficiency.",
    "grid_factor": 0.3,
    "E_IT": 445200000.0,
    "E_DC": 489720000.00000006,
    "CO2": 146916000.0
  }
]
```

### Apple — Washington, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 8000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.3,
  "notes": "Washington has a cooler climate which allows for better cooling efficiency, resulting in a lower PUE. The region has a significant amount of renewable energy sources, leading to a lower grid emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.21,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Assumed a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization due to optimization.",
    "grid_factor": 0.3,
    "E_IT": 395857000.0,
    "E_DC": 467111260.0,
    "CO2": 140133378.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.22,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Assumed a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization due to optimization.",
    "grid_factor": 0.3,
    "E_IT": 455601300.0,
    "E_DC": 528497507.99999994,
    "CO2": 158549252.39999998
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.23,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.14,
    "notes": "Assumed a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization due to optimization.",
    "grid_factor": 0.3,
    "E_IT": 523721880.0,
    "E_DC": 597042943.1999999,
    "CO2": 179112882.95999998
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.24,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.12,
    "notes": "Assumed a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization due to optimization.",
    "grid_factor": 0.3,
    "E_IT": 601294080.0,
    "E_DC": 673449369.6,
    "CO2": 202034810.88
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.25,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 8000,
    "H_inference": 7000,
    "PUE": 1.1,
    "notes": "Assumed a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a slight increase in utilization due to optimization.",
    "grid_factor": 0.3,
    "E_IT": 689482500.0,
    "E_DC": 758430750.0000001,
    "CO2": 227529225.00000003
  }
]
```

## Expansion Location Predictions

### 1. Maiden, North Carolina, USA
**Probability:** 90%
**Key Factors:** Significant expansion plans already announced, part of $500 billion investment, strong local support for renewable energy.
**Notes:** North Carolina is a key focus for Apple's data center strategy.

### 2. Houston, Texas, USA
**Probability:** 80%
**Key Factors:** New server manufacturing facility planned, strong investment in advanced manufacturing, proximity to existing infrastructure.
**Notes:** Houston's role in server production may lead to data center expansion.

### 3. Iowa, USA
**Probability:** 70%
**Key Factors:** Part of Apple's announced expansion plans, favorable regulations for data centers, and renewable energy availability.
**Notes:** Iowa's supportive environment for tech infrastructure is promising.

### 4. Oregon, USA
**Probability:** 70%
**Key Factors:** Existing data center presence, commitment to renewable energy, and expansion plans mentioned.
**Notes:** Oregon's renewable energy resources are attractive for data center operations.

### 5. Arizona, USA
**Probability:** 60%
**Key Factors:** Part of the expansion strategy, favorable climate for data centers, and existing infrastructure.
**Notes:** Arizona's environment is conducive to data center operations.

### 6. Nevada, USA
**Probability:** 60%
**Key Factors:** Included in Apple's expansion plans, favorable regulations, and renewable energy initiatives.
**Notes:** Nevada's regulatory environment supports tech infrastructure.

### 7. California, USA
**Probability:** 50%
**Key Factors:** Existing presence and infrastructure, but high competition and regulatory challenges.
**Notes:** California's market is saturated, but still a potential area for growth.

### 8. Michigan, USA
**Probability:** 50%
**Key Factors:** Investment in advanced manufacturing and training, potential for tech infrastructure growth.
**Notes:** Michigan's focus on manufacturing may support data center expansion.

### 9. Washington, USA
**Probability:** 40%
**Key Factors:** Existing tech infrastructure, but high competition and regulatory challenges.
**Notes:** Washington's market is competitive, but still a viable option.

---
# Nebius

## Energy Forecast

### Nebius — New Jersey, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.04,
  "notes": "New Jersey has a mature infrastructure and a mix of renewable energy sources, leading to a lower grid emission factor. The utilization rates are higher due to the demand for AI workloads, and the PUE is slightly lower due to favorable cooling conditions."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.197,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency and utilization rates.",
    "grid_factor": 0.04,
    "E_IT": 258013800.0,
    "E_DC": 307036422.0,
    "CO2": 12281456.88
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.194,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continuing growth at 10% for N_train and N_inference, with ongoing efficiency improvements.",
    "grid_factor": 0.04,
    "E_IT": 282561620.0,
    "E_DC": 333422711.59999996,
    "CO2": 13336908.464
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.191,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Assuming continued growth and improvements in efficiency and utilization.",
    "grid_factor": 0.04,
    "E_IT": 309313752.0,
    "E_DC": 361897089.84,
    "CO2": 14475883.5936
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.188,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Further growth and efficiency improvements assumed.",
    "grid_factor": 0.04,
    "E_IT": 338453068.8,
    "E_DC": 392605559.80799997,
    "CO2": 15704222.39232
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241577,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.185,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Continuing trends of growth and efficiency improvements.",
    "grid_factor": 0.04,
    "E_IT": 370175423.0,
    "E_DC": 425701736.45,
    "CO2": 17028069.458
  }
]
```

### Nebius — Kansas City, Missouri, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.045,
  "notes": "Kansas City has a moderate climate which allows for efficient cooling, leading to a PUE of 1.2. The grid mix includes a significant portion of renewables, resulting in a low grid emission factor. Utilization rates are higher due to the established infrastructure and demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.553,
    "P_avg_inference": 0.202,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assumed a 10% growth in N_train and N_inference. Power efficiency improves by 0.5% for training and 1% for inference. Utilization rates increase slightly due to optimization efforts. PUE is expected to remain stable due to the moderate climate and efficient cooling.",
    "grid_factor": 0.045,
    "E_IT": 264444400.0,
    "E_DC": 314688836.0,
    "CO2": 14160997.62
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.556,
    "P_avg_inference": 0.204,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continued growth of 10% in N_train and N_inference. Power efficiency improves by 0.5% for training and 1% for inference. Utilization rates continue to rise slightly. PUE remains stable.",
    "grid_factor": 0.045,
    "E_IT": 296880760.0,
    "E_DC": 350319296.79999995,
    "CO2": 15764368.355999997
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.559,
    "P_avg_inference": 0.206,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Assumed a 10% growth in N_train and N_inference. Power efficiency improves by 0.5% for training and 1% for inference. Utilization rates increase slightly. PUE remains stable.",
    "grid_factor": 0.045,
    "E_IT": 333223836.0,
    "E_DC": 389871888.12,
    "CO2": 17544234.9654
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.562,
    "P_avg_inference": 0.208,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Continued growth of 10% in N_train and N_inference. Power efficiency improves by 0.5% for training and 1% for inference. Utilization rates continue to rise slightly. PUE remains stable.",
    "grid_factor": 0.045,
    "E_IT": 373911456.0,
    "E_DC": 433737288.96,
    "CO2": 19518178.0032
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.565,
    "P_avg_inference": 0.21,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Assumed a 10% growth in N_train and N_inference. Power efficiency improves by 0.5% for training and 1% for inference. Utilization rates increase slightly. PUE remains stable.",
    "grid_factor": 0.045,
    "E_IT": 419405000.0,
    "E_DC": 482315749.99999994,
    "CO2": 21704208.749999996
  }
]
```

### Nebius — Keflavik, Iceland

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 7000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.02,
  "notes": "Keflavik, Iceland benefits from a cooler climate, leading to better cooling efficiency and a lower PUE. The grid is primarily renewable, resulting in a low grid emission factor. Utilization rates are higher due to the demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.21,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 2% improvement in P_avg_train and P_avg_inference, and a slight increase in utilization rates due to optimization.",
    "grid_factor": 0.02,
    "E_IT": 349041000.0,
    "E_DC": 415358790.0,
    "CO2": 8307175.8
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.22,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.18,
    "notes": "Continuing the trend with a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and further optimization in utilization.",
    "grid_factor": 0.02,
    "E_IT": 402494400.0,
    "E_DC": 474943392.0,
    "CO2": 9498867.84
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.23,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.17,
    "notes": "Assuming a similar growth pattern with 10% increase in N_train and N_inference, and slight improvements in power efficiency and utilization.",
    "grid_factor": 0.02,
    "E_IT": 463507440.0,
    "E_DC": 542303704.8,
    "CO2": 10846074.095999999
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.24,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.16,
    "notes": "Continuing the growth trajectory with 10% increase in N_train and N_inference, and gradual improvements in power efficiency and utilization.",
    "grid_factor": 0.02,
    "E_IT": 533057040.0,
    "E_DC": 618346166.4,
    "CO2": 12366923.328
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.25,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 7000,
    "PUE": 1.15,
    "notes": "Assuming a 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization.",
    "grid_factor": 0.02,
    "E_IT": 612202500.0,
    "E_DC": 704032875.0,
    "CO2": 14080657.5
  }
]
```

### Nebius — Amsterdam, Netherlands

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.25,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.04,
  "notes": "Amsterdam has a mature data center market with good cooling efficiency due to its climate, leading to a lower PUE. The grid is increasingly renewable, resulting in a low carbon intensity."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.25,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Assumed a growth rate of 10% for N_train and N_inference, slight improvement in power efficiency (1%), and a small increase in utilization rates.",
    "grid_factor": 0.04,
    "E_IT": 303138000.0,
    "E_DC": 360734220.0,
    "CO2": 14429368.8
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.25,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Continued growth of 10% for N_train and N_inference, with a further 1% improvement in power efficiency and utilization.",
    "grid_factor": 0.04,
    "E_IT": 335617700.0,
    "E_DC": 396028886.0,
    "CO2": 15841155.44
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.25,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Assumed 10% growth for N_train and N_inference, with continued slight improvements in power efficiency and utilization.",
    "grid_factor": 0.04,
    "E_IT": 371508720.0,
    "E_DC": 434665202.4,
    "CO2": 17386608.096
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.25,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Maintained growth of 10% for N_train and N_inference, with a 1% improvement in power efficiency and utilization.",
    "grid_factor": 0.04,
    "E_IT": 411163203.0,
    "E_DC": 476949315.47999996,
    "CO2": 19077972.6192
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.25,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Projected continued growth of 10% for N_train and N_inference, with further improvements in power efficiency and utilization.",
    "grid_factor": 0.04,
    "E_IT": 454967600.0,
    "E_DC": 523212739.99999994,
    "CO2": 20928509.599999998
  }
]
```

### Nebius — Toronto, Ontario, Canada

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 8000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.03,
  "notes": "Toronto has a mature infrastructure and a cooler climate, allowing for efficient cooling and a lower PUE. The grid is increasingly reliant on renewable energy, contributing to a low carbon intensity. Utilization rates are high due to the demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.21,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.19,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 2% improvement in P_avg_train and P_avg_inference, a 1% increase in utilization rates, stable hours, and a slight reduction in PUE due to improved cooling efficiency.",
    "grid_factor": 0.03,
    "E_IT": 378840000.0,
    "E_DC": 450819600.0,
    "CO2": 13524588.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.22,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.18,
    "notes": "Continuing with a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a 1% increase in utilization rates.",
    "grid_factor": 0.03,
    "E_IT": 437233500.0,
    "E_DC": 515935530.0,
    "CO2": 15478065.899999999
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.23,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.17,
    "notes": "Forecasting a 10% growth in N_train and N_inference, with a 2% improvement in power efficiency and a 1% increase in utilization rates.",
    "grid_factor": 0.03,
    "E_IT": 503916600.0,
    "E_DC": 589582422.0,
    "CO2": 17687472.66
  },
  {
    "year": 2029,
    "N_train": 73205,
    "N_inference": 219615,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.24,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.16,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a 1% increase in utilization rates.",
    "grid_factor": 0.03,
    "E_IT": 580003215.0,
    "E_DC": 672803729.4,
    "CO2": 20184111.882
  },
  {
    "year": 2030,
    "N_train": 80525,
    "N_inference": 241576,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.25,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.15,
    "notes": "Continuing the trend with a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and a 1% increase in utilization rates.",
    "grid_factor": 0.03,
    "E_IT": 666748800.0,
    "E_DC": 766761120.0,
    "CO2": 23002833.599999998
  }
]
```

## Expansion Location Predictions

### 1. New Jersey, USA
**Probability:** 90%
**Key Factors:** Significant capacity expansion planned, strategic location for US market, existing infrastructure.
**Notes:** Nebius has already committed to a new data center here.

### 2. Kansas City, Missouri, USA
**Probability:** 70%
**Key Factors:** Incremental capacity additions at existing facility, favorable regulations, and energy availability.
**Notes:** Nebius is expanding its current operations here.

### 3. Keflavik, Iceland
**Probability:** 60%
**Key Factors:** New colocation deployment, abundant geothermal energy, and growing demand for AI infrastructure in Europe.
**Notes:** Iceland's energy resources are a significant advantage.

### 4. Amsterdam, Netherlands
**Probability:** 50%
**Key Factors:** Headquarters location, strong tech ecosystem, and potential for AI infrastructure growth.
**Notes:** Proximity to existing operations and market demand.

### 5. Toronto, Ontario, Canada
**Probability:** 40%
**Key Factors:** Growing tech market, favorable regulations, and energy availability.
**Notes:** Potential for expansion into North America.

---
# Meta

## Energy Forecast

### Meta — Dallas, Texas, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.12,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Dallas, Texas has a moderate climate allowing for efficient cooling, leading to a lower PUE. The grid mix includes a significant amount of natural gas and renewables, resulting in a lower carbon emission factor. Utilization rates are higher due to the mature infrastructure and demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.11,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 2% improvement in power efficiency, and slight increases in utilization rates. PUE remains stable due to efficient cooling in Dallas.",
    "grid_factor": 0.4,
    "E_IT": 268169000.0,
    "E_DC": 297667590.0,
    "CO2": 119067036.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.1,
    "notes": "Continuing growth of 10% in N_train and N_inference, with a 2% efficiency improvement and gradual increase in utilization. PUE slightly decreases due to continued optimization.",
    "grid_factor": 0.4,
    "E_IT": 305174100.0,
    "E_DC": 335691510.0,
    "CO2": 134276604.0
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.09,
    "notes": "Assuming a 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization. PUE remains stable as cooling efficiency is maintained.",
    "grid_factor": 0.4,
    "E_IT": 347071560.0,
    "E_DC": 378308000.40000004,
    "CO2": 151323200.16000003
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.08,
    "notes": "Continuing trends with 10% growth in N_train and N_inference, slight improvements in power efficiency, and utilization rates. PUE continues to decrease slightly.",
    "grid_factor": 0.4,
    "E_IT": 394460160.0,
    "E_DC": 426016972.8,
    "CO2": 170406789.12
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.07,
    "notes": "Assuming a 10% growth in N_train and N_inference, with continued efficiency improvements and utilization increases. PUE remains low due to effective cooling strategies.",
    "grid_factor": 0.4,
    "E_IT": 447982500.0,
    "E_DC": 479341275.0,
    "CO2": 191736510.0
  }
]
```

### Meta — Northern Virginia, Virginia, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.12,
  "grid_factor_tCO2_per_MWh": 0.3,
  "notes": "Northern Virginia has a mature infrastructure and a reliable grid, allowing for higher utilization rates. The region's cooler climate contributes to a lower PUE. The grid is increasingly powered by renewables, resulting in a lower carbon emission factor."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.195,
    "u_train": 0.76,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.11,
    "notes": "Assuming a 10% growth in N_train and N_inference, slight improvement in power efficiency (1% decrease in P_avg), and a small increase in utilization rates due to optimization.",
    "grid_factor": 0.3,
    "E_IT": 258241500.0,
    "E_DC": 286648065.0,
    "CO2": 85994419.5
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.19,
    "u_train": 0.77,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.1,
    "notes": "Continuing the trend with another 10% growth in N_train and N_inference, further 1% decrease in P_avg, and continued optimization leading to higher utilization.",
    "grid_factor": 0.3,
    "E_IT": 280841000.0,
    "E_DC": 308925100.0,
    "CO2": 92677530.0
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.185,
    "u_train": 0.78,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.09,
    "notes": "Assuming a 10% growth in N_train and N_inference, another 1% decrease in P_avg, and continued improvement in utilization rates.",
    "grid_factor": 0.3,
    "E_IT": 305204955.0,
    "E_DC": 332673400.95000005,
    "CO2": 99802020.28500001
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.18,
    "u_train": 0.79,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.08,
    "notes": "Continuing the trend with 10% growth in N_train and N_inference, 1% decrease in P_avg, and further optimization of utilization.",
    "grid_factor": 0.3,
    "E_IT": 331420320.00000006,
    "E_DC": 357933945.6000001,
    "CO2": 107380183.68000002
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241500,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.175,
    "u_train": 0.8,
    "u_inference": 0.91,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.07,
    "notes": "Assuming a 10% growth in N_train and N_inference, 1% decrease in P_avg, and continued improvements in utilization rates.",
    "grid_factor": 0.3,
    "E_IT": 359553250.0,
    "E_DC": 384721977.5,
    "CO2": 115416593.25
  }
]
```

### Meta — Phoenix, Arizona, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 6000,
  "H_inference": 8000,
  "PUE_current": 1.09,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Phoenix has a warm climate which allows for efficient cooling, resulting in a lower PUE. The grid in Arizona has a significant share of renewable energy, contributing to a lower carbon intensity. Utilization rates are higher due to the demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.5635,
    "P_avg_inference": 0.206,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.08,
    "notes": "Assuming a 10% growth in N_train and N_inference, a 1% improvement in power efficiency, and slight increases in utilization rates due to optimization.",
    "grid_factor": 0.4,
    "E_IT": 375177000.0,
    "E_DC": 405191160.0,
    "CO2": 162076464.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.577,
    "P_avg_inference": 0.212,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.07,
    "notes": "Continuing growth trends with a 10% increase in N_train and N_inference, 2% improvement in power efficiency, and further optimization in utilization rates.",
    "grid_factor": 0.4,
    "E_IT": 429084150.0,
    "E_DC": 459120040.5,
    "CO2": 183648016.20000002
  },
  {
    "year": 2028,
    "N_train": 66050,
    "N_inference": 199650,
    "P_avg_train": 0.5915,
    "P_avg_inference": 0.218,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.06,
    "notes": "Forecasting a 10% growth in N_train and N_inference, with a 2% improvement in power efficiency and continued optimization in utilization rates.",
    "grid_factor": 0.4,
    "E_IT": 489247779.0,
    "E_DC": 518602645.74,
    "CO2": 207441058.296
  },
  {
    "year": 2029,
    "N_train": 72650,
    "N_inference": 219600,
    "P_avg_train": 0.606,
    "P_avg_inference": 0.224,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.05,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a 2% improvement in power efficiency and further increases in utilization rates.",
    "grid_factor": 0.4,
    "E_IT": 558918414.0000001,
    "E_DC": 586864334.7000002,
    "CO2": 234745733.88000008
  },
  {
    "year": 2030,
    "N_train": 79915,
    "N_inference": 241560,
    "P_avg_train": 0.621,
    "P_avg_inference": 0.23,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 6000,
    "H_inference": 8000,
    "PUE": 1.04,
    "notes": "Continuing the trend with a 10% growth in N_train and N_inference, a 3% improvement in power efficiency, and further optimization in utilization rates.",
    "grid_factor": 0.4,
    "E_IT": 638233992.0,
    "E_DC": 663763351.6800001,
    "CO2": 265505340.67200005
  }
]
```

### Meta — Oregon, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.85,
  "u_inference": 0.75,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.12,
  "grid_factor_tCO2_per_MWh": 0.15,
  "notes": "Oregon has a cooler climate which allows for better cooling efficiency, resulting in a lower PUE. The region also has a significant share of renewable energy sources, contributing to a lower grid emission factor. Utilization rates are high due to the mature infrastructure and demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.54,
    "P_avg_inference": 0.195,
    "u_train": 0.86,
    "u_inference": 0.76,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.11,
    "notes": "Assuming a 10% growth in N_train and N_inference, with a slight improvement in power efficiency (1% decrease in P_avg), and a small increase in utilization rates.",
    "grid_factor": 0.15,
    "E_IT": 248886000.0,
    "E_DC": 276263460.0,
    "CO2": 41439519.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.53,
    "P_avg_inference": 0.191,
    "u_train": 0.87,
    "u_inference": 0.77,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.1,
    "notes": "Continuing growth of 10% in N_train and N_inference, with a further 1% improvement in power efficiency and utilization rates.",
    "grid_factor": 0.15,
    "E_IT": 271745430.0,
    "E_DC": 298919973.0,
    "CO2": 44837995.949999996
  },
  {
    "year": 2028,
    "N_train": 66550,
    "N_inference": 199650,
    "P_avg_train": 0.52,
    "P_avg_inference": 0.187,
    "u_train": 0.88,
    "u_inference": 0.78,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.09,
    "notes": "Assuming continued growth of 10% in N_train and N_inference, with a 1% improvement in power efficiency and utilization rates.",
    "grid_factor": 0.15,
    "E_IT": 296538814.0,
    "E_DC": 323227307.26000005,
    "CO2": 48484096.08900001
  },
  {
    "year": 2029,
    "N_train": 73200,
    "N_inference": 219600,
    "P_avg_train": 0.51,
    "P_avg_inference": 0.183,
    "u_train": 0.89,
    "u_inference": 0.79,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.08,
    "notes": "Continuing 10% growth in N_train and N_inference, with further improvements in power efficiency and utilization rates.",
    "grid_factor": 0.15,
    "E_IT": 323387352.0,
    "E_DC": 349258340.16,
    "CO2": 52388751.024000004
  },
  {
    "year": 2030,
    "N_train": 80500,
    "N_inference": 241560,
    "P_avg_train": 0.5,
    "P_avg_inference": 0.179,
    "u_train": 0.9,
    "u_inference": 0.8,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.07,
    "notes": "Assuming 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization rates.",
    "grid_factor": 0.15,
    "E_IT": 352448352.0,
    "E_DC": 377119736.64000005,
    "CO2": 56567960.49600001
  }
]
```

### Meta — Atlanta, Georgia, USA

#### Baseline Parameters (2025)
```json
{
  "N_train": 50000,
  "N_inference": 150000,
  "P_avg_train_kW": 0.55,
  "P_avg_inference_kW": 0.2,
  "u_train": 0.75,
  "u_inference": 0.85,
  "H_train": 4000,
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Atlanta has a moderate climate, which allows for efficient cooling, leading to a PUE of 1.2. The region's grid has a significant renewable energy component, reducing the carbon intensity. Utilization rates are high due to the demand for AI workloads."
}
```

#### Forecast Results (2026 – 2030)
```json
[
  {
    "year": 2026,
    "N_train": 55000,
    "N_inference": 165000,
    "P_avg_train": 0.56,
    "P_avg_inference": 0.205,
    "u_train": 0.76,
    "u_inference": 0.86,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.19,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, with a slight increase in power efficiency and utilization rates. PUE is slightly improved due to ongoing operational efficiencies.",
    "grid_factor": 0.4,
    "E_IT": 268169000.0,
    "E_DC": 319121110.0,
    "CO2": 127648444.0
  },
  {
    "year": 2027,
    "N_train": 60500,
    "N_inference": 181500,
    "P_avg_train": 0.57,
    "P_avg_inference": 0.21,
    "u_train": 0.77,
    "u_inference": 0.87,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.18,
    "notes": "Forecast assumes a further 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization rates. PUE reflects ongoing operational improvements.",
    "grid_factor": 0.4,
    "E_IT": 305174100.0,
    "E_DC": 360105438.0,
    "CO2": 144042175.20000002
  },
  {
    "year": 2028,
    "N_train": 66500,
    "N_inference": 199500,
    "P_avg_train": 0.58,
    "P_avg_inference": 0.215,
    "u_train": 0.78,
    "u_inference": 0.88,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.17,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, with slight improvements in power efficiency and utilization rates. PUE continues to improve due to better operational practices.",
    "grid_factor": 0.4,
    "E_IT": 346810800.0,
    "E_DC": 405768636.0,
    "CO2": 162307454.4
  },
  {
    "year": 2029,
    "N_train": 73000,
    "N_inference": 219500,
    "P_avg_train": 0.59,
    "P_avg_inference": 0.22,
    "u_train": 0.79,
    "u_inference": 0.89,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.16,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, with continued improvements in power efficiency and utilization rates. PUE reflects ongoing advancements in operational efficiency.",
    "grid_factor": 0.4,
    "E_IT": 393969800.0,
    "E_DC": 457004967.99999994,
    "CO2": 182801987.2
  },
  {
    "year": 2030,
    "N_train": 80000,
    "N_inference": 240000,
    "P_avg_train": 0.6,
    "P_avg_inference": 0.225,
    "u_train": 0.8,
    "u_inference": 0.9,
    "H_train": 4000,
    "H_inference": 6000,
    "PUE": 1.15,
    "notes": "Forecast assumes a 10% growth in N_train and N_inference, with slight improvements in power efficiency and utilization rates. PUE continues to improve due to enhanced operational efficiencies.",
    "grid_factor": 0.4,
    "E_IT": 445200000.0,
    "E_DC": 511979999.99999994,
    "CO2": 204792000.0
  }
]
```

## Expansion Location Predictions

### 1. Dallas, Texas, USA
**Probability:** 90%
**Key Factors:** High demand for data centers, favorable regulatory environment, and existing infrastructure.
**Notes:** Texas is a leading state for data center growth due to its energy availability and supportive legislation.

### 2. Northern Virginia, Virginia, USA
**Probability:** 85%
**Key Factors:** Established data center hub, strong demand, and proximity to major tech companies.
**Notes:** Northern Virginia remains a focal point for data center expansion due to its existing infrastructure.

### 3. Phoenix, Arizona, USA
**Probability:** 80%
**Key Factors:** Growing demand, favorable climate for cooling, and supportive local policies.
**Notes:** Phoenix is becoming increasingly attractive for data centers due to its climate and energy costs.

### 4. Oregon, USA
**Probability:** 75%
**Key Factors:** Strong renewable energy resources, existing data center infrastructure, and favorable regulations.
**Notes:** Oregon's commitment to renewable energy makes it a viable option for sustainable data center operations.

### 5. Atlanta, Georgia, USA
**Probability:** 70%
**Key Factors:** Growing tech ecosystem, favorable energy costs, and increasing demand for data services.
**Notes:** Atlanta's tech growth and energy availability position it well for future data center expansion.

---
# Amazon

## Expansion Location Predictions

### 1. Columbus, Ohio, USA
**Probability:** 90%
**Key Factors:** Significant investment of $23 billion planned by AWS, existing infrastructure, and favorable local regulations.
**Notes:** Expansion contingent on energy service agreements.

### 2. Taipei, Taiwan
**Probability:** 85%
**Key Factors:** New AWS Asia/Pacific Region launched, high demand for cloud services, and existing AWS presence.
**Notes:** Strong growth in cloud services expected in the region.

### 3. Milan, Italy
**Probability:** 75%
**Key Factors:** Investment of $1.3 billion planned, existing AWS cloud region, and growing demand for cloud services in Europe.
**Notes:** Part of broader European expansion strategy.

### 4. Bangkok, Thailand
**Probability:** 70%
**Key Factors:** New AWS Region planned, increasing cloud adoption in Southeast Asia, and strategic location for regional services.
**Notes:** Potential for significant growth in cloud services.

### 5. Kuala Lumpur, Malaysia
**Probability:** 65%
**Key Factors:** New AWS Region planned, growing demand for cloud services, and strategic location in Southeast Asia.
**Notes:** Part of AWS's expansion in the Asia Pacific region.

### 6. Marysville, Ohio, USA
**Probability:** 60%
**Key Factors:** New data center development announced, part of significant investment in Ohio, and local government support.
**Notes:** Expected to create new jobs and boost local economy.

### 7. Sunbury, Ohio, USA
**Probability:** 55%
**Key Factors:** Planned $2 billion data center campus, part of broader Ohio investment strategy, and favorable local regulations.
**Notes:** Expected to enhance AWS's infrastructure in the region.

### 8. Fayette County, Ohio, USA
**Probability:** 40%
**Key Factors:** Acquisition of land for data center development, part of Ohio expansion strategy, and local government support.
**Notes:** Expected to go live by 2026.

---
# CoreWeave

## Expansion Location Predictions

### 1. Lancaster, Pennsylvania, USA
**Probability:** 90%
**Key Factors:** Significant investment of $6 billion for a large-scale AI data center, existing infrastructure, and skilled workforce availability.
**Notes:** Lancaster is strategically located near major markets and has supportive local regulations.

### 2. Barcelona, Spain
**Probability:** 85%
**Key Factors:** Investment of $2.2 billion in Europe, existing job openings indicating operational plans, and growing demand for AI infrastructure.
**Notes:** Barcelona's location is favorable for serving Southern Europe.

### 3. Norway
**Probability:** 80%
**Key Factors:** Part of the $2.2 billion investment in Europe, focus on renewable energy, and favorable regulations for data centers.
**Notes:** Norway's energy resources are abundant and sustainable.

### 4. Sweden
**Probability:** 75%
**Key Factors:** Included in the European expansion plans, strong focus on sustainability, and favorable energy policies.
**Notes:** Sweden is known for its renewable energy initiatives.

### 5. Côte d'Ivoire
**Probability:** 60%
**Key Factors:** Emerging market for data centers, recent establishment of a data center by ST Digital indicating growth potential.
**Notes:** Côte d'Ivoire is becoming a hub for tech investments in West Africa.

### 6. Luzerne County, Pennsylvania, USA
**Probability:** 40%
**Key Factors:** Part of AWS's $20 billion investment in Pennsylvania, with plans for multiple advanced data center campuses.
**Notes:** Luzerne County's infrastructure and workforce are being developed to support tech growth.

### 7. Bucks County, Pennsylvania, USA
**Probability:** 35%
**Key Factors:** Included in AWS's significant investment in Pennsylvania, aiming to create tech clusters and job opportunities.
**Notes:** Bucks County is strategically positioned to support AWS's expansion efforts.
