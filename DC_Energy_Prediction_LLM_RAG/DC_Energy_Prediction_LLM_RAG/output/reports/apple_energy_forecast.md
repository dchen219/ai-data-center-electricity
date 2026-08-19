# Apple — Data Center Energy Forecast

## Apple — Maiden, North Carolina, USA

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Apple — Houston, Texas, USA

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
  "H_inference": 7200,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Houston has a warm climate, which may lead to moderate cooling efficiency, hence a PUE of 1.2. The grid mix in Texas includes a significant amount of natural gas and renewables, resulting in a moderate grid emission factor. Utilization rates are higher due to the established tech ecosystem in the area."
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

## Apple — Iowa, USA

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Apple — Oregon, USA

### Baseline Parameters (2025)
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

## Apple — Arizona, USA

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Apple — Nevada, USA

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
  "notes": "Nevada has a relatively mature infrastructure with a moderate climate, allowing for efficient cooling and a reasonable PUE. The grid has a significant share of renewables, resulting in a lower carbon intensity."
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

## Apple — California, USA

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
  "grid_factor_tCO2_per_MWh": 0.15,
  "notes": "California has a mature infrastructure with a strong emphasis on renewable energy, leading to lower emissions and efficient cooling. Utilization rates are higher due to the advanced technology ecosystem."
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

## Apple — Michigan, USA

### Baseline Parameters (2025)
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

## Apple — Washington, USA

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
  "grid_factor_tCO2_per_MWh": 0.3,
  "notes": "Washington has a cooler climate which allows for better cooling efficiency, resulting in a lower PUE. The region has a significant amount of renewable energy sources, leading to a lower grid emission factor."
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
