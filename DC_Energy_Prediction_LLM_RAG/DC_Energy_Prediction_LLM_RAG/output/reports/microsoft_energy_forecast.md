# Microsoft — Data Center Energy Forecast

## Microsoft — Northern Virginia, USA

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
  "notes": "Northern Virginia has a mature infrastructure with a strong renewable energy mix, leading to lower PUE and grid emission factors. The utilization rates are higher due to the demand for AI workloads in this region."
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

## Microsoft — Texas, USA

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
  "notes": "Texas has a mature infrastructure with a mix of renewables and natural gas, leading to a moderate grid emission factor. Utilization rates are high due to demand, and the PUE reflects efficient cooling in the warmer climate."
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

## Microsoft — Loughton, UK

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
  "grid_factor_tCO2_per_MWh": 0.25,
  "notes": "Loughton, UK has a cooler climate which supports better cooling efficiency, leading to a lower PUE. The UK grid is increasingly renewable, resulting in a lower grid emission factor. Utilization rates are higher due to the established infrastructure and demand for AI workloads."
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

## Microsoft — Wisconsin, USA

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
  "grid_factor_tCO2_per_MWh": 0.004,
  "notes": "Wisconsin has a cooler climate, allowing for better cooling efficiency, thus a lower PUE. The grid is increasingly renewable, contributing to a low emission factor. Utilization rates are higher due to the established infrastructure."
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

## Microsoft — Singapore

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
  "grid_factor_tCO2_per_MWh": 0.0004,
  "notes": "Singapore has a mature infrastructure with a significant focus on renewable energy, leading to lower grid emissions. The utilization rates are higher due to the advanced cooling systems and favorable climate conditions. PUE is moderate due to the efficient cooling strategies employed."
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

## Microsoft — Narvik, Norway

### Baseline Parameters (2025)
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

### Forecast Results (2026 – 2030)
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

## Microsoft — Poland

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
  "notes": "Poland's climate allows for efficient cooling, leading to a lower PUE. The grid is increasingly renewable, contributing to a low emission factor. Utilization rates are higher due to growing demand for AI services."
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

## Microsoft — Johor Bahru, Malaysia

### Baseline Parameters (2025)
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

## Microsoft — Georgia, USA

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
  "notes": "Georgia has a moderate climate which allows for efficient cooling, leading to a PUE of 1.2. The state has a growing renewable energy sector, contributing to a lower grid emission factor. Utilization rates are higher due to the increasing demand for AI workloads."
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

## Microsoft — Wyoming, USA

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
  "notes": "Wyoming has a cooler climate, allowing for better cooling efficiency, which results in a lower PUE. The grid is moderately renewable, leading to a lower carbon emission factor."
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
