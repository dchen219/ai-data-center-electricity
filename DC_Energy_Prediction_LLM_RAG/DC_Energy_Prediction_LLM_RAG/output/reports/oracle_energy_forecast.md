# Oracle — Data Center Energy Forecast

## Oracle — Kuala Lumpur, Malaysia

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Dallas-Fort Worth, Texas, USA

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Singapore

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Amsterdam, Netherlands

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Riyadh, Saudi Arabia

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Tokyo, Japan

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Madrid, Spain

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Abilene, Texas, USA

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — Bangladesh

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Oracle — New Zealand

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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
