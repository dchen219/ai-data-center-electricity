# Nebius — Data Center Energy Forecast

## Nebius — New Jersey, USA

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
  "grid_factor_tCO2_per_MWh": 0.04,
  "notes": "New Jersey has a mature infrastructure and a mix of renewable energy sources, leading to a lower grid emission factor. The utilization rates are higher due to the demand for AI workloads, and the PUE is slightly lower due to favorable cooling conditions."
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

## Nebius — Kansas City, Missouri, USA

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
  "grid_factor_tCO2_per_MWh": 0.045,
  "notes": "Kansas City has a moderate climate which allows for efficient cooling, leading to a PUE of 1.2. The grid mix includes a significant portion of renewables, resulting in a low grid emission factor. Utilization rates are higher due to the established infrastructure and demand for AI workloads."
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

## Nebius — Keflavik, Iceland

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
  "grid_factor_tCO2_per_MWh": 0.02,
  "notes": "Keflavik, Iceland benefits from a cooler climate, leading to better cooling efficiency and a lower PUE. The grid is primarily renewable, resulting in a low grid emission factor. Utilization rates are higher due to the demand for AI workloads."
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

## Nebius — Amsterdam, Netherlands

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Nebius — Toronto, Ontario, Canada

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
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.03,
  "notes": "Toronto has a mature infrastructure and a cooler climate, allowing for efficient cooling and a lower PUE. The grid is increasingly reliant on renewable energy, contributing to a low carbon intensity. Utilization rates are high due to the demand for AI workloads."
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
