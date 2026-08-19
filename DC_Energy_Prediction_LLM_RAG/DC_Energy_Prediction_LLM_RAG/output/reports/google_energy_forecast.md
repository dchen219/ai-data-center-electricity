# Google — Data Center Energy Forecast

## Google — Caldwell County, North Carolina, USA

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
  "notes": "Caldwell County has a moderate climate which allows for efficient cooling, justifying a PUE of 1.2. The grid mix is improving with renewable energy sources, leading to a lower carbon intensity of 0.4 tCO2/MWh. Utilization rates are higher due to the site's established infrastructure and operational maturity."
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

## Google — Singapore, Singapore

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Google — Virginia, USA

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
  "notes": "The parameters are tailored for Northern Virginia, which has a mature infrastructure and a significant renewable energy mix, leading to lower emissions and efficient cooling. Utilization rates are higher due to the established market and demand."
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

## Google — Tokyo, Japan

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
  "H_inference": 6000,
  "PUE_current": 1.2,
  "grid_factor_tCO2_per_MWh": 0.453,
  "notes": "Tokyo has a mature infrastructure with a significant focus on renewable energy, resulting in a lower grid emission factor. The utilization rates are higher due to the advanced technology and demand in the region. PUE is moderate due to the climate, which allows for efficient cooling."
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

## Google — Eemshaven, Netherlands

### Baseline Parameters (2025)
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

## Google — Kuala Lumpur, Malaysia

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Google — Groningen, Netherlands

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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
