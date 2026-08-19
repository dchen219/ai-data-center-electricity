# Meta — Data Center Energy Forecast

## Meta — Dallas, Texas, USA

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
  "PUE_current": 1.12,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Dallas, Texas has a moderate climate allowing for efficient cooling, leading to a lower PUE. The grid mix includes a significant amount of natural gas and renewables, resulting in a lower carbon emission factor. Utilization rates are higher due to the mature infrastructure and demand for AI workloads."
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

## Meta — Northern Virginia, Virginia, USA

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
  "PUE_current": 1.12,
  "grid_factor_tCO2_per_MWh": 0.3,
  "notes": "Northern Virginia has a mature infrastructure and a reliable grid, allowing for higher utilization rates. The region's cooler climate contributes to a lower PUE. The grid is increasingly powered by renewables, resulting in a lower carbon emission factor."
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

## Meta — Phoenix, Arizona, USA

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
  "H_inference": 8000,
  "PUE_current": 1.09,
  "grid_factor_tCO2_per_MWh": 0.4,
  "notes": "Phoenix has a warm climate which allows for efficient cooling, resulting in a lower PUE. The grid in Arizona has a significant share of renewable energy, contributing to a lower carbon intensity. Utilization rates are higher due to the demand for AI workloads."
}
```

### Forecast Results (2026 – 2030)
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

## Meta — Oregon, USA

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
  "PUE_current": 1.12,
  "grid_factor_tCO2_per_MWh": 0.15,
  "notes": "Oregon has a cooler climate which allows for better cooling efficiency, resulting in a lower PUE. The region also has a significant share of renewable energy sources, contributing to a lower grid emission factor. Utilization rates are high due to the mature infrastructure and demand for AI workloads."
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

## Meta — Atlanta, Georgia, USA

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
  "notes": "Atlanta has a moderate climate, which allows for efficient cooling, leading to a PUE of 1.2. The region's grid has a significant renewable energy component, reducing the carbon intensity. Utilization rates are high due to the demand for AI workloads."
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
