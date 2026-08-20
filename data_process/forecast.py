import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import matplotlib.colors as mcolors

def forecasts():
    # === Step 1. 文件路径 ===
    history_file = "dc_consumption_history.xlsx"
    forecast_file = "full_firm_forecast.xlsx"

    # === Step 2. 读取历史能耗 (2015–2024) ===
    df_hist = pd.read_excel(history_file)
    df_hist.columns = df_hist.columns.str.strip().str.lower()

    # 自动检测可能的列
    firm_cols = [c for c in df_hist.columns if "firm" in c or "company" in c]
    year_cols = [c for c in df_hist.columns if "year" in c]
    energy_cols = [c for c in df_hist.columns if "energy" in c]

    if not energy_cols:
        raise ValueError("❌ 历史文件中未找到包含 'energy' 的列，请检查列名（如 'Energy Consumption (TWh)'）")

    # 自动重命名标准列
    df_hist = df_hist.rename(columns={
        firm_cols[0]: "firm",
        year_cols[0]: "year",
        energy_cols[0]: "E_total_TWh"
    })

    df_hist = df_hist[["firm", "year", "E_total_TWh"]]
    df_hist = df_hist.dropna(subset=["E_total_TWh"])
    df_hist["E_total_TWh"] = pd.to_numeric(df_hist["E_total_TWh"], errors="coerce")

    # === Step 3. 读取 LLM 预测文件 ===
    # 自动检测所有 sheet
    xls = pd.ExcelFile(forecast_file)
    sheet_to_use = xls.sheet_names[0]  # 默认第一个
    df_fore = pd.read_excel(forecast_file, sheet_name=sheet_to_use)
    df_fore.columns = df_fore.columns.str.strip().str.lower()

    # === Step 3b. 处理重复列，自动识别能耗列 ===
    energy_cols = [c for c in df_fore.columns if "e_dc" in c or "energy" in c]
    
    if not energy_cols:
        raise ValueError("❌ 未找到包含 'E_DC' 或 'energy' 的列，请检查 forecast 文件。")

    if len(energy_cols) > 1:
        print(f"⚠️ 检测到多个能耗列：{energy_cols}，将优先选第一个非空列。")
        for col in energy_cols:
            if df_fore[col].notna().sum() > 0:
                df_fore["E_DC"] = df_fore[col]
                break
    else:
        df_fore["E_DC"] = df_fore[energy_cols[0]]

    # === Step 3c. 标准化列名 ===
    rename_map2 = {}
    for c in df_fore.columns:
        if "firm" in c or "company" in c: rename_map2[c] = "firm"
        if "year" in c: rename_map2[c] = "year"
    df_fore = df_fore.rename(columns=rename_map2)
    df_fore = df_fore.dropna(subset=["firm", "year", "E_DC"])

    df_fore["E_DC"] = pd.to_numeric(df_fore["E_DC"], errors="coerce")
    df_fore = df_fore.dropna(subset=["E_DC"])

    # === Step 4. 聚合得到 2026 基准 AI 数据中心能耗 ===
    base_year = 2026
    df_base = (
        df_fore[df_fore["year"] == base_year]
        .groupby("firm", as_index=False)["E_DC"]
        .sum()
    )
    df_base = df_base.rename(columns={"E_DC": "E_AI_base_TWh"})
    df_base["E_AI_base_TWh"] = df_base["E_AI_base_TWh"].astype(float)
    print("\n✅ 2026年各公司基准AI能耗（TWh）:")
    print(df_base)

    # === Step 5. 参数设定 ===
    beta = 0.6
    growth_scenarios = {"conservative": 0.15, "neutral": 0.25, "optimistic": 0.35}

    p_ai = {
        "Meta": {"conservative": 0.35, "neutral": 0.50, "optimistic": 0.60},
        "Microsoft": {"conservative": 0.30, "neutral": 0.45, "optimistic": 0.55},
        "Google": {"conservative": 0.25, "neutral": 0.40, "optimistic": 0.50},
        "Amazon": {"conservative": 0.15, "neutral": 0.25, "optimistic": 0.40},
        "Oracle": {"conservative": 0.20, "neutral": 0.35, "optimistic": 0.50},
        "Apple": {"conservative": 0.08, "neutral": 0.15, "optimistic": 0.25},
    }

    # === Step 6. 未来情景预测 ===
    records = []
    for _, row in df_base.iterrows():
        firm = str(row["firm"])
        e_base = float(row["E_AI_base_TWh"])

        for scen, gN in growth_scenarios.items():
            for year in range(2025, 2031):
                e_ai = (e_base / beta) * ((1 + gN) ** (year - base_year))
                p_val = p_ai.get(firm, {}).get(scen, 0.3)
                e_total = e_ai / p_val
                records.append({
                    "firm": firm,
                    "scenario": scen,
                    "year": year,
                    "E_AI_TWh": round(e_ai, 2),
                    "E_Total_TWh": round(e_total, 2),
                })

    df_future = pd.DataFrame(records)

    # === Step 7. 合并历史与未来 ===
    # === Step 7. 合并历史与未来 ===
    # === Step 7. 合并历史与未来 ===
    # 确保列名统一
    df_hist.columns = [c.lower() for c in df_hist.columns]

    # 处理列命名差异
    if "firm" not in df_hist.columns:
        df_hist = df_hist.rename(columns={df_hist.columns[0]: "firm"})
    if "year" not in df_hist.columns:
        year_col = [c for c in df_hist.columns if "year" in c][0]
        df_hist = df_hist.rename(columns={year_col: "year"})
    if "e_total_twh" not in df_hist.columns:
        energy_col = [c for c in df_hist.columns if "energy" in c][0]
        df_hist = df_hist.rename(columns={energy_col: "e_total_twh"})

    # 新增缺失列
    if "scenario" not in df_hist.columns:
        df_hist["scenario"] = "historical"
    if "E_AI_TWh" not in df_hist.columns and "e_ai_twh" not in df_hist.columns:
        df_hist["E_AI_TWh"] = None

    # 重命名能耗列（统一格式）
    df_hist = df_hist.rename(columns={"e_total_twh": "E_Total_TWh"})

    # 确保列存在后再重排
    expected_cols = ["firm", "year", "scenario", "E_AI_TWh", "E_Total_TWh"]
    for col in expected_cols:
        if col not in df_hist.columns:
            df_hist[col] = None

    df_hist = df_hist[expected_cols]
    df_all = pd.concat([df_hist, df_future], ignore_index=True)
    df_all = df_all.sort_values(["firm", "year"])

    # === Step 8. 生成 Global Summary ===
    df_global = (
        df_all[df_all["scenario"] != "historical"]
        .groupby(["year", "scenario"], as_index=False)[["E_AI_TWh", "E_Total_TWh"]]
        .sum()
    )
    
    # # === Step 8b. 扩展信息计算 ===
    # print("🧮 正在计算扩展信息列...")

    # # === g_N (站点数量增长率) ===
    # gN_map = {"conservative": 0.15, "neutral": 0.25, "optimistic": 0.35}
    # df_all["g_N"] = df_all["scenario"].map(gN_map)

    # # === p_AI 三情景占比 ===
    # pAI_map = {
    #     "Amazon": (0.15, 0.25, 0.40),
    #     "Apple": (0.08, 0.15, 0.25),
    #     "Google": (0.25, 0.40, 0.50),
    #     "Meta": (0.35, 0.50, 0.60),
    #     "Microsoft": (0.30, 0.45, 0.55),
    #     "Oracle": (0.20, 0.35, 0.50)
    # }
    # df_all["p_AI_conservative"] = df_all["firm"].map(lambda f: pAI_map.get(f, (None, None, None))[0])
    # df_all["p_AI_neutral"] = df_all["firm"].map(lambda f: pAI_map.get(f, (None, None, None))[1])
    # df_all["p_AI_optimistic"] = df_all["firm"].map(lambda f: pAI_map.get(f, (None, None, None))[2])

    # # === LLM 预测的 E_DC 与 AI 站点数 ===
    # df_fore = pd.read_excel(forecast_file)
    # df_fore.columns = df_fore.columns.str.strip().str.lower()
    # if "e_dc" in df_fore.columns:
    #     df_fore = df_fore.rename(columns={"e_dc": "E_DC_predicted"})
    # elif "energy" in df_fore.columns:
    #     df_fore = df_fore.rename(columns={"energy": "E_DC_predicted"})

    # df_all = df_all.merge(
    #     df_fore[["firm", "E_DC_predicted"]].drop_duplicates(),
    #     on="firm", how="left"
    # )

    # # === AI 站点数 (若文件无提供，则按 g_N 复利增长计算) ===
    # df_all["AI_sites_predicted"] = np.where(
    #     df_all["g_N"].notna(),
    #     7 * (1 + df_all["g_N"]) ** (df_all["year"] - 2025),
    #     np.nan
    # )

    # # === 扩展系数（以 2025 为基准） ===
    # base_2025 = df_all[df_all["year"] == 2025][["firm", "E_Total_TWh"]].rename(
    #     columns={"E_Total_TWh": "Base_Total_TWh"}
    # )
    # df_all = df_all.merge(base_2025, on="firm", how="left")
    # df_all["Expansion_factor"] = df_all["E_Total_TWh"] / df_all["Base_Total_TWh"]

    # # === 清理输出列 ===
    # df_all["Expansion_factor"] = df_all["Expansion_factor"].round(3)
    # df_all["AI_sites_predicted"] = df_all["AI_sites_predicted"].round(2)

    # print("✅ 已添加扩展信息列（g_N、p_AI、Expansion_factor、E_DC_predicted、AI_sites_predicted）")

    
    
    # === Step 9. 输出 Excel ===
    out_path = Path("dc_energy_full_scenario_full.xlsx")
    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        df_all.to_excel(writer, index=False, sheet_name="Full_Series")
        df_global.to_excel(writer, index=False, sheet_name="Global_Summary")
    print(f"\n✅ 已生成完整数据文件：{out_path}")

    # === Step 10. 绘制公司级图表 ===
    firms = df_all["firm"].unique()
    for firm in firms:
        plt.figure(figsize=(8,5))
        firm_data = df_all[df_all["firm"] == firm]

        hist = firm_data[firm_data["scenario"] == "historical"]
        plt.plot(hist["year"], hist["E_Total_TWh"], "k--", label="Historical Total")

        for scen, color in zip(["conservative","neutral","optimistic"], ["#8da0cb","#66c2a5","#fc8d62"]):
            sub = firm_data[firm_data["scenario"] == scen]
            plt.plot(sub["year"], sub["E_Total_TWh"], color=color, linewidth=2, label=f"Total ({scen})")
            plt.plot(sub["year"], sub["E_AI_TWh"], color=color, linestyle=":", linewidth=2, label=f"AI ({scen})")

        plt.title(f"{firm}: Data Center Energy (2015–2030)")
        plt.xlabel("Year")
        plt.ylabel("Energy (TWh)")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(f"{firm}_energy_trend.png", dpi=300)
        plt.close()

    # === Step 11. 全球总量图 ===
    plt.figure(figsize=(9,5))
    for scen, color in zip(["conservative","neutral","optimistic"], ["#8da0cb","#66c2a5","#fc8d62"]):
        sub = df_global[df_global["scenario"] == scen]
        plt.plot(sub["year"], sub["E_Total_TWh"], color=color, linewidth=2, label=f"Total ({scen})")
        plt.plot(sub["year"], sub["E_AI_TWh"], color=color, linestyle=":", linewidth=2, label=f"AI ({scen})")

    hist_total = df_hist.groupby("year", as_index=False)["E_Total_TWh"].sum()
    plt.plot(hist_total["year"], hist_total["E_Total_TWh"], "k--", label="Historical Total")

    plt.title("🌍 Global Data Center Energy Consumption (2015–2030)")
    plt.xlabel("Year")
    plt.ylabel("Energy Consumption (TWh)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig("Global_energy_summary.png", dpi=300)
    plt.close()

    print("\n🌍 已生成全球总能耗图表：Global_energy_summary.png")

def forcast_extend():
    df_hist = pd.read_excel("dc_consumption_history.xlsx")
    df_fore = pd.read_excel("full_firm_forecast.xlsx")

    # === Step 2. Load LLM AI DC forecast (per-firm site data) ===
    df_ai = pd.read_excel("dc_energy_full_scenario_full.xlsx", sheet_name="Full_Series")

    # === Step 3. Normalize column names ===
    df_ai.columns = [c.strip() for c in df_ai.columns]
    df_hist.columns = [c.strip().lower() for c in df_hist.columns]
    df_ai.columns = [c.strip().lower() for c in df_ai.columns]

    # === Step 4. Add scenario growth rate mapping ===
    gN_map = {"conservative": 0.15, "neutral": 0.25, "optimistic": 0.35}
    df_ai["g_N"] = df_ai["scenario"].map(gN_map)

    # === Step 5. Define AI ratio parameters (p_AI) ===
    pAI_map = {
        "Amazon": (0.10, 0.25, 0.45),
        "Apple": (0.05, 0.15, 0.25),
        "Google": (0.25, 0.40, 0.55),
        "Meta": (0.35, 0.50, 0.65),
        "Microsoft": (0.30, 0.45, 0.60),
        "Oracle": (0.20, 0.35, 0.50)
    }
    df_ai["p_AI_conservative"] = df_ai["firm"].map(lambda f: pAI_map.get(f, (None, None, None))[0])
    df_ai["p_AI_neutral"] = df_ai["firm"].map(lambda f: pAI_map.get(f, (None, None, None))[1])
    df_ai["p_AI_optimistic"] = df_ai["firm"].map(lambda f: pAI_map.get(f, (None, None, None))[2])

    # === Step 6. Merge LLM DC power data ===
    df_fore = df_fore.rename(columns={"E_DC": "E_DC_predicted", "N_site": "AI_sites_predicted"})
    df_ai = df_ai.merge(df_fore[["firm", "E_DC_predicted"]].drop_duplicates(), on="firm", how="left")

    # === Step 7. Compute Expansion_factor (base year = 2025) ===
    base_2025 = df_ai[df_ai["year"] == 2025][["firm", "total_twh"]].rename(columns={"total_twh": "Base_Total_TWh"})
    df_ai = df_ai.merge(base_2025, on="firm", how="left")
    df_ai["Expansion_factor"] = df_ai["total_twh"] / df_ai["Base_Total_TWh"]

    # === Step 8. Estimate AI site count (if not provided) ===
    df_ai["AI_sites_predicted"] = np.where(
        df_ai["AI_sites_predicted"].isna(),
        7 * (1 + df_ai["g_N"].fillna(0)) ** (df_ai["year"] - 2025),
        df_ai["AI_sites_predicted"]
    )

    # === Step 9. Output full extended dataset ===
    df_out = df_ai[[
        "firm", "year", "scenario", "e_ai_twh", "total_twh",
        "E_DC_predicted", "AI_sites_predicted", "Expansion_factor", "g_N",
        "p_AI_conservative", "p_AI_neutral", "p_AI_optimistic"
    ]]
    df_out.to_excel("dc_energy_full_scenario_extended.xlsx", index=False)
    print("✅ Extended dataset saved as dc_energy_full_scenario_extended.xlsx")

    # === Step 10. Global summary ===
    df_global = df_ai.groupby(["year", "scenario"], as_index=False)[["e_ai_twh", "total_twh"]].sum()

    # === Step 11. Auto-scale units (fix 1e9 issue) ===
    if df_global["total_twh"].mean() > 1e6:
        df_global[["e_ai_twh", "total_twh"]] /= 1e9
        df_hist["total_twh"] = df_hist["total_twh"] / 1e9
        unit_label = "Energy Consumption (TWh)"
    else:
        unit_label = "Energy Consumption (TWh)"

    # === Step 12. Plot Global Energy Consumption ===
    plt.figure(figsize=(9,5))
    colors = {"conservative": "#8da0cb", "neutral": "#66c2a5", "optimistic": "#fc8d62"}

    for scen in ["conservative", "neutral", "optimistic"]:
        sub = df_global[df_global["scenario"] == scen]
        plt.plot(sub["year"], sub["total_twh"], color=colors[scen], linewidth=2, label=f"Total ({scen})")
        plt.plot(sub["year"], sub["e_ai_twh"], color=colors[scen], linestyle=":", linewidth=2, label=f"AI ({scen})")

    plt.plot(df_hist["year"], df_hist["total_twh"], "k--", label="Historical Total")

    plt.xlabel("Year")
    plt.ylabel(unit_label)
    plt.title("🌐 Global Data Center Energy Consumption (2015–2030)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("Global_energy_summary.png", dpi=400)
    plt.show()

    print("🌍 Global Energy Consumption chart saved as Global_energy_summary.png")

def scenario_analysis():
    # ==========================================================
    # 1. PARAMETERS
    # ==========================================================
    # Annual stock growth rate for existing data centers
    g_stock = 0.10

    # Scenario-specific new-site growth rates
    g_map = {"conservative": 0.15, "neutral": 0.25, "optimistic": 0.35}

    # AI share by firm (pAI)
    pAI = {
        "Amazon": (0.3, 0.4, 0.6),
        "Apple": (0.25, 0.3, 0.35),
        "Google": (0.35, 0.4, 0.6),
        "Meta": (0.35, 0.5, 0.6),
        "Msft": (0.35, 0.45, 0.6),
        "Oracle": (0.25, 0.35, 0.5),
    }

    def get_pAI(firm, year):
        """Firm-specific AI share schedule."""
        if firm not in pAI:
            return None
        if year == 2025:
            return pAI[firm][0]
        elif year in [2026, 2027]:
            return pAI[firm][1]
        elif year in [2028, 2029, 2030]:
            return pAI[firm][2]
        else:
            return pAI[firm][2]

    # ==========================================================
    # 2. READ INPUT FILES
    # ==========================================================
    hist = pd.read_excel("dc_consumption_history.xlsx")
    forecast = pd.read_excel("full_firm_forecast.xlsx")

    # Clean columns
    hist.columns = hist.columns.str.strip().str.lower()
    forecast.columns = forecast.columns.str.strip().str.lower()

    # Basic renaming
    if "firm" not in forecast.columns:
        if "location" in forecast.columns:
            forecast = forecast.rename(columns={"location": "firm"})
        else:
            raise ValueError("Missing 'firm' or 'location' column.")

    # Required columns
    if "e_ai_dc" not in forecast.columns:
        raise ValueError("Missing 'E_AI_DC' column in forecast file.")

    # ==========================================================
    # 3. STOCK BASELINE (EXISTING DC)
    # ==========================================================
    # Find each firm's 2024 total electricity
    hist_2024 = hist[hist["year"] == 2024].copy()
    if "e_total_twh" not in hist_2024.columns:
        raise ValueError("Your history file must contain a column 'E_Total_TWh'.")

    stock_baseline = hist_2024[["firm", "e_total_twh"]].rename(columns={"e_total_twh": "stock_2024"})
    print("\nBaseline stock (2024):\n", stock_baseline)
    
    # ==========================================================
    # 4. NEW SITE ELECTRICITY (AI + non-AI)
    # ==========================================================
    agg_new = forecast.groupby(["firm", "year"], as_index=False)["e_ai_dc"].sum()
    print("\nAggregated new site AI electricity:\n", agg_new)
    
    
    # ==========================================================
    # 5. COMBINE STOCK + NEW SITE FORECAST
    # ==========================================================
    records = []
    for _, row in agg_new.iterrows():
        firm = row["firm"]
        base_year = int(row["year"])
        e_ai_base = float(row["e_ai_dc"])

        # Baseline stock for this firm
        stock_row = stock_baseline[stock_baseline["firm"] == firm]
        base_stock = float(stock_row["stock_2024"]) if not stock_row.empty else 0

        for scen, g_new in g_map.items():
            # Initialize new AI for first forecast year
            e_ai = e_ai_base* (1 + g_new)
            for year in range(base_year, 2031):
                # === Stock roll-forward ===
                years_since_2024 = year - 2024
                e_stock = base_stock * ((1 + g_stock) ** years_since_2024)

                # === New site AI & non-AI ===
                p = get_pAI(firm, year)
                if not p:
                    continue
                e_new_total = e_ai / p
                e_new_nonai = e_new_total - e_ai

                # === Combine totals ===
                e_total = e_stock + e_new_total

                records.append({
                    "firm": firm,
                    "year": year,
                    "scenario": scen,
                    "growth_stock": g_stock,
                    "growth_new": g_new,
                    "pAI": p,
                    "E_stock_TWh": round(e_stock, 3),
                    "E_AI_new_TWh": round(e_ai, 3),
                    "E_nonAI_new_TWh": round(e_new_nonai, 3),
                    "E_new_total_TWh": round(e_new_total, 3),
                    "E_total_combined_TWh": round(e_total, 3)
                })

                # compound new AI growth for next year
                e_ai *= (1 + g_new)

    # ==========================================================
    # 6. OUTPUT
    # ==========================================================
    df_out = pd.DataFrame(records)
    output_path = "firm_total_energy_forecast_2025_2030_update4.xlsx"
    df_out.to_excel(output_path, index=False)

    print(f"\n✅ Final forecast (stock + new) saved to: {output_path}")
    print(df_out.head(10))

def scenario_analysis_2():
    # === Load data ===
    hist = pd.read_excel("dc_consumption_history.xlsx")
    forecast = pd.read_excel("firm_total_energy_forecast_2025_2030_update4.xlsx")

    # === Clean columns ===
    hist.columns = hist.columns.str.strip().str.lower()
    forecast.columns = forecast.columns.str.strip().str.lower()

    # Rename for consistency
    if "energy consumption(twh)" in hist.columns:
        hist = hist.rename(columns={"energy consumption(twh)": "e_total_twh"})
    elif "energy consumption (twh)" in hist.columns:
        hist = hist.rename(columns={"energy consumption (twh)": "e_total_twh"})

    hist = hist.rename(columns={"firm": "firm", "year": "year"})
    forecast = forecast.rename(columns={"firm": "firm", "year": "year"})

    # === Combine for global plotting ===
    hist["scenario"] = "historical"
    forecast["e_total_twh"] = forecast["e_total_combined_twh"]
    combined = pd.concat([hist[["firm","year","scenario","e_total_twh"]],
                        forecast[["firm","year","scenario","e_total_twh"]]],
                        ignore_index=True)
    # === Define Color Map (one tone per firm) ===
# === Define Color Map (one tone per firm) ===
    base_colors = {
        "Amazon": "#1f77b4",      # 蓝
        "Apple": "#ff7f0e",       # 橙
        "Google": "#2ca02c",      # 绿
        "Meta": "#9467bd",        # 紫
        "Msft": "#d62728",        # 红
        "Oracle": "#8c564b",      # 棕
    }
    # 生成由深到浅的三种情景颜色
    def generate_shades(base_color):
        r, g, b = mcolors.to_rgb(base_color)
        shades = [
            mcolors.to_hex((r * 0.6, g * 0.6, b * 0.6)),                         # conservative (深)
            mcolors.to_hex((r, g, b)),                                           # neutral (中)
            mcolors.to_hex((min(r * 1.4, 1), min(g * 1.4, 1), min(b * 1.4, 1)))  # optimistic (浅)
        ]
        return dict(zip(["conservative", "neutral", "optimistic"], shades))

    color_map = {firm: generate_shades(color) for firm, color in base_colors.items()}

    # === Create Figure ===
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    # === (1) Firm-level forecast ===
    for firm in forecast["firm"].unique():
        for scen, style in zip(["conservative", "neutral", "optimistic"], ["--", "-.", ":"]):
            sub = forecast[(forecast["firm"] == firm) & (forecast["scenario"] == scen)]
            axes[0].plot(
                sub["year"],
                sub["e_total_twh"],
                linestyle=style,
                marker='o',
                color=color_map[firm][scen],
                label=f"{firm} ({scen})"
            )

    axes[0].set_title("Firm-level Data Center Energy Forecast (2025–2030)")
    axes[0].set_ylabel("Energy (TWh)")
    axes[0].legend(fontsize=7, ncol=2)
    axes[0].grid(True, linestyle="--", alpha=0.6)
    # === (2) Global total energy trend ===
    # hist_global = hist.groupby("year", as_index=False)["e_total_twh"].sum()
    # forecast_global = forecast.groupby(["year","scenario"], as_index=False)["e_total_twh"].sum()

    # axes[1].plot(hist_global["year"], hist_global["e_total_twh"], "k--", linewidth=2, label="Historical")
    # for scen, color in zip(["conservative","neutral","optimistic"], ["#1f77b4","#2ca02c","#ff7f0e"]):
    #     sub = forecast_global[forecast_global["scenario"] == scen]
    #     axes[1].plot(sub["year"], sub["e_total_twh"], color=color, linewidth=2, label=f"{scen.title()}")
    # axes[1].set_title("Global Data Center Energy (2015–2030)")
    # axes[1].set_ylabel("Total Energy (TWh)")
    # axes[1].legend()
    # axes[1].grid(True, linestyle="--", alpha=0.6)
    # === (2) Global total energy trend with uncertainty band ===
    # === 1️⃣ 历史总量 ===
    
    # hist_global = hist_global[hist_global["year"] >= 2018]
    hist_global = hist.groupby("year", as_index=False)["e_total_twh"].sum()
    print("\n✅ 历史总量数据:\n", hist_global)
    # 只保留 2016 年及以后的历史数据
    # === 2️⃣ 给每家公司每年每情景路径编号（例如 conservative1, conservative2...） ===
    # 说明：如果同一 firm-year-scenario 有多条记录，就给它们编号
    forecast["path_id"] = (
        forecast.groupby(["firm", "year", "scenario"]).cumcount() + 1
    )
    print("\n✅ 已添加路径编号 path_id:\n", forecast[["firm","year","scenario","path_id"]].head())

    # === 3️⃣ 每家公司内部路径合并（同一公司多地合并） ===
    firm_year_scen_sum = (
        forecast.groupby(["firm", "year", "scenario", "path_id"], as_index=False)["e_total_twh"]
        .sum()
    )
    print("\n✅ 公司层路径合并结果:\n", firm_year_scen_sum.head())

    # === 4️⃣ 计算每年每情景每条路径的全球总能耗 ===
    global_by_scenario_path = (
        firm_year_scen_sum
        .groupby(["year", "scenario", "path_id"], as_index=False)["e_total_twh"]
        .sum()
        .rename(columns={"e_total_twh": "E_global_TWh"})
    )
    print("\n✅ 全球路径汇总结果:\n", global_by_scenario_path.head())

    # === 5️⃣ 对每年每情景求均值、最小、最大路径能耗 ===
    forecast_stats = (
        global_by_scenario_path
        .groupby(["year", "scenario"], as_index=False)["E_global_TWh"]
        .agg(E_mean_TWh="mean", E_min_TWh="min", E_max_TWh="max")
    )
    print("\n✅ 各情景统计结果（每年均值/区间）:\n", forecast_stats.head())

    # === 6️⃣ 跨情景求整体范围（optional，全局带状图） ===
    # 如果你想把三种情景的整体区间也画出来，可用下面这一段：
    forecast_range = (
        forecast_stats
        .groupby("year", as_index=False)[["E_min_TWh","E_max_TWh","E_mean_TWh"]]
        .agg(E_min_TWh=("E_min_TWh","min"), E_max_TWh=("E_max_TWh","max"), E_mean_TWh=("E_mean_TWh","mean"))
    )
    print("\n✅ 不同情景总体区间:\n", forecast_range)

    # === 7️⃣ 检查衔接点 ===
    print("\n2024历史总量:", hist_global.loc[hist_global["year"] == 2024, "e_total_twh"].sum())
    print("2025预测区间(跨情景):", forecast_range.query("year==2025")[["E_min_TWh","E_max_TWh","E_mean_TWh"]])

    # === 历史部分（从2016开始） ===
    hist_global = hist_global[hist_global["year"] >= 2015]
    print("\n✅ 历史数据年份范围:")
    print(hist_global["year"].unique())

    # === 添加 2024→2025 衔接点 ===
    last_hist_year = 2024
    last_hist_value = hist_global.loc[hist_global["year"] == last_hist_year, "e_total_twh"].sum()
    # === 为每个情景增加衔接点（用 2024 历史末值对齐） ===
    for scen in ["conservative", "neutral", "optimistic"]:
        first_forecast_year = forecast_stats[forecast_stats["scenario"] == scen]["year"].min()
        # 用历史末值作为 2024 的预测起点
        new_row = pd.DataFrame({
            "year": [last_hist_year],
            "scenario": [scen],
            "E_mean_TWh": [last_hist_value],
            "E_min_TWh": [last_hist_value],
            "E_max_TWh": [last_hist_value]
        })
        forecast_stats = pd.concat([forecast_stats, new_row], ignore_index=True)
        forecast_stats = forecast_stats.sort_values(["scenario", "year"])

    colors = {
        "conservative": "#1f77b4",  # 蓝
        "neutral": "#2ca02c",       # 绿
        "optimistic": "#ff7f0e"     # 橙
    }

    # 历史部分 (实线)
    # === 历史部分（2016–2024）——黑色实线 ===
    hist_cut = hist_global[(hist_global["year"] >= 2015) & (hist_global["year"] <= 2024)]
    print("\n✅ 历史数据用于绘图:\n", hist_cut)
    axes[1].plot(hist_cut["year"], hist_cut["e_total_twh"],
                color="black", linewidth=2.2, linestyle="-", label="Historical")

    # === 绘制三情景预测 ===
    for scen, color in colors.items():
        sub = forecast_stats[forecast_stats["scenario"] == scen]

        # 历史衔接段（到2024的部分）——实线
        sub_hist = sub[sub["year"] <= 2025]
        if not sub_hist.empty:
            axes[1].plot(sub_hist["year"], sub_hist["E_mean_TWh"],
                        color=color, linewidth=2.2, linestyle="-")

        # 未来预测段（从2025开始）——虚线
        sub_future = sub[sub["year"] >= 2025]
        axes[1].plot(sub_future["year"], sub_future["E_mean_TWh"],
                    color=color, linewidth=2.2, linestyle="--", label=f"{scen.title()} (mean)")

        # 阴影区 (未来范围)
        axes[1].fill_between(sub_future["year"], sub_future["E_min_TWh"], sub_future["E_max_TWh"],
                            color=color, alpha=0.2, linewidth=0, label=f"{scen.title()} range")

    axes[1].set_xlim(2017, 2030)
    axes[1].set_ylim(20, 300)
    axes[1].set_title("Global Data Center Energy (2015–2030) — Scenario Path Aggregation")
    axes[1].set_ylabel("Total Energy (TWh)")
    axes[1].legend(fontsize=8, ncol=2)
    axes[1].grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("AI_DataCenter_Dashboard.pdf")
    plt.show()
    # # === (3) AI vs Non-AI share ===
    # ai_share = forecast.groupby(["year","scenario"], as_index=False)[["e_ai_new_twh","e_nonai_new_twh"]].sum()
    # ai_share["AI_share"] = ai_share["e_ai_new_twh"] / (ai_share["e_ai_new_twh"] + ai_share["e_nonai_new_twh"])

    # for scen, style in zip(["conservative","neutral","optimistic"], ["--","-.",":"]):
    #     sub = ai_share[ai_share["scenario"] == scen]
    #     axes[2].plot(sub["year"], sub["AI_share"]*100, linestyle=style, marker='o', label=f"{scen.title()}")

    # axes[2].set_title("AI Share of Data Center Energy (2025–2030)")
    # axes[2].set_ylabel("AI Share (%)")
    # axes[2].set_xlabel("Year")
    # axes[2].legend()
    # axes[2].grid(True, linestyle="--", alpha=0.6)




def dc_region_analysis():

    df = pd.read_excel("full_firm_forecast.xlsx")

    # === 2. Keep key columns ===
    df = df[["Firm", "Location", "year", "E_AI_DC"]]

    # === 3. Define function: extract region name ===
    def extract_region(loc):
        """
        Extract state (for USA) or country (for others)
        Example:
        - 'Columbus, Ohio, USA' -> 'Ohio'
        - 'Milan, Italy' -> 'Italy'
        - 'Tokyo, Japan' -> 'Japan'
        """
        if pd.isna(loc):
            return None
        parts = [p.strip() for p in str(loc).split(",")]
        if len(parts) == 3 or (len(parts) == 2 and parts[-1] == "USA"):
            # e.g. Columbus, Ohio, USA
            return parts[-2]
        elif len(parts) >= 2:
            # Non-US (e.g. Milan, Italy)
            return parts[-1]
        else:
            return parts[0]

    df["Region"] = df["Location"].apply(extract_region)

    # === 4. Filter target year ===
    df_2030 = df[df["year"] == 2030].copy()

    # === 5. Aggregate total electricity by region ===
    region_firm = (
        df_2030.groupby(["Region", "Firm"], as_index=False)["E_AI_DC"]
        .sum()
    )

    # === 5. Pivot for stacked bar chart ===
    pivot_df = region_firm.pivot(index="Region", columns="Firm", values="E_AI_DC").fillna(0)
    # === 6. Sort descending & select top 15 (for overview) ===
    # === 6. Sort by total descending ===
    pivot_df["Total"] = pivot_df.sum(axis=1)
    pivot_df = pivot_df.sort_values("Total", ascending=False).head(15)  # top 10
    pivot_df = pivot_df.drop(columns="Total")
    # top15 = region_energy.sort_values("E_Total_TWh", ascending=False).head(15)

    # === 7. Print output ===
    print("\n=== Top 15 U.S. States or International Regions by 2030 AI DC Energy ===")
    print(pivot_df.to_string(index=False))
    
    
    # === 7. 自定义和谐配色（柔和且区分度高） ===
    color_map = {
        "Amazon": "#F36D21",    # 柔和蓝
        "Apple": "#5C2D8B",     # 柔和绿
        "Google": "#F2B261",    # 蓝灰
        "Meta": "#BFA2CC",      # 柔黄
        "Msft": "#9AC2DA",      # 紫蓝
        "Oracle": "#3d67a0"     # 浅青
    }
    # === 7. Plot stacked bar chart ===
    plt.figure(figsize=(10, 6))
    pivot_df[list(color_map.keys())].plot(
        kind="barh",
        stacked=True,
        color=color_map,
        ax=plt.gca(),
    )
    plt.xlabel("Electricity Demand (TWh, 2030)")
    plt.ylabel("Region (U.S. State ≈ Country)")
    plt.title("AI Data Center Electricity Demand by Firm and Region (2030)", fontsize=13, pad=15)
    plt.legend(title="Firm", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=9)
    plt.grid(alpha=0.3, linestyle="--", axis="x")
    plt.gca().invert_yaxis()  # 从高到低排列
    plt.tight_layout()
    plt.savefig("Top10_Regions_FirmStacked_2030.png", dpi=400)
    plt.show()
    
    
    
    
    
    # # === 8. Visualization ===
    # plt.figure(figsize=(10, 6))
    # plt.barh(top15["Region"], top15["E_Total_TWh"], color="royalblue")
    # plt.gca().invert_yaxis()
    # plt.xlabel("Electricity Demand (TWh, 2030)")
    # plt.ylabel("Region / State / Country")
    # plt.title("Top 15 Regions by AI Data Center Electricity Demand (2030)")
    # plt.grid(alpha=0.3, linestyle="--")
    # plt.tight_layout()
    # plt.savefig("Top15_AI_DC_Regions_US_and_Global.png", dpi=400)
    # plt.show()

    # === 9. Optional: classify into 'US' vs. 'International' ===
    # df_2030["CountryType"] = df_2030["Location"].apply(lambda x: "US" if str(x).endswith("USA") else "International")
    # summary = df_2030.groupby("CountryType")["E_AI_DC"].sum().reset_index()
    # summary["Share_%"] = summary["E_AI_DC"] / summary["E_AI_DC"].sum() * 100

    # print("\n=== U.S. vs. International AI Data Center Electricity Split (2030) ===")
    # print(summary)

def energy_gap_analysis():
    # --- 1) 公共：提取地区（州/国家） ---
    def extract_region(loc):
        if pd.isna(loc):
            return None
        parts = [p.strip() for p in str(loc).split(",")]
        # US: "City, State, USA"  或 "State, USA"
        if len(parts) >= 2 and parts[-1].upper() == "USA":
            return parts[-2]  # 州
        # 非 US：取最后一段为国家
        if len(parts) >= 2:
            return parts[-1]
        return parts[0]

    # --- 2) 读取数据 ---
    df_ai = pd.read_excel("full_firm_forecast.xlsx")            # 未来各 AI 站点（含 Location、year、E_AI_DC）
    df_ai.columns = df_ai.columns.str.strip().str.lower()

        # === 读取 datacenter.xlsx ===
    df_hist_sites = pd.read_excel("datacenter.xlsx")            # 历史站点（仅站点与公司，或可含年份）
    df_hist_sites.columns = df_hist_sites.columns.str.strip().str.lower()
    print("✅ 读取 datacenter.xlsx，列名：", df_hist_sites.columns.tolist())
    # === 自动拼接 Location 字段 ===
    # === 自动拼接 Location 字段（适配 datacenter.xlsx 实际列名） ===
    # === 自动拼接 Location 字段（最终稳定版） ===
    cols = [c.lower().strip() for c in df_hist_sites.columns]
    print("✅ 读取 datacenter.xlsx, 列名:", cols)

    # 兼容多种表头组合
    if "location" not in cols:
        if "city" in cols and "state or province" in cols and "country or region" in cols:
            # 美国和国际都能兼容
            df_hist_sites["location"] = (
                df_hist_sites["city"].astype(str).str.strip() + ", " +
                df_hist_sites["state or province"].astype(str).str.strip() + ", " +
                df_hist_sites["country or region"].astype(str).str.strip()
            )

        elif "city" in cols and "country or region" in cols:
            df_hist_sites["location"] = (
                df_hist_sites["city"].astype(str).str.strip() + ", " +
                df_hist_sites["country or region"].astype(str).str.strip()
            )

        elif "city" in cols and "country" in cols:
            df_hist_sites["location"] = (
                df_hist_sites["city"].astype(str).str.strip() + ", " +
                df_hist_sites["country"].astype(str).str.strip()
            )

        else:
            print("❌ 当前列名:", df_hist_sites.columns.tolist())
            raise ValueError("无法构造 Location 字段，请确认 datacenter.xlsx 是否包含 City, State or Province, Country or Region")

    print("✅ 成功构造 Location 字段示例:\n", df_hist_sites["location"].head())
    print(df_hist_sites.columns.tolist())
    
    df_total = pd.read_excel("firm_total_energy_forecast_2025_2030_update4.xlsx")  # 你情景函数输出
    df_total.columns = df_total.columns.str.strip().str.lower()

    # --- 3) 统一公司名（避免 "Msft" vs "Microsoft" 之类不一致）---
    name_map = {
        "msft": "msft",
        "microsoft corp": "msft",
        "alphabetInc": "google",
        "meta platforms": "meta",
        "amazon": "amazon",
        "apple": "apple",
    }
    for col in ["firm"]:
        df_ai[col] = df_ai[col].astype(str).str.strip()
        df_hist_sites[col] = df_hist_sites[col].astype(str).str.strip()
        df_total[col] = df_total[col].astype(str).str.strip()
        df_ai[col] = df_ai[col].str.lower().replace(name_map).str.title()
        df_hist_sites[col] = df_hist_sites[col].str.lower().replace(name_map).str.title()
        df_total[col] = df_total[col].str.lower().replace(name_map).str.title()

    # --- 4) 补齐必要列并构造地区 ---
    if "location" in df_ai.columns:
        df_ai["region"] = df_ai["location"].apply(extract_region)
    else:
        raise ValueError("full_firm_forecast.xlsx 缺少 Location 列。")

    if "location" in df_hist_sites.columns:
        df_hist_sites["region"] = df_hist_sites["location"].apply(extract_region)
    else:
        raise ValueError("datacenter.xlsx 缺少 Location 列。")

    # --- 5) 计算 AI 站点地区权重（按 firm-year） ---
    # E_AI_DC 有单位差异时请先统一（此处假定已统一）
    ai_region = (
        df_ai.groupby(["firm", "year", "region"], as_index=False)["e_ai_dc"].sum()
    )
    ai_region["w_ai_region"] = ai_region.groupby(["firm", "year"])["e_ai_dc"] \
                                        .transform(lambda x: x / x.sum())

    # --- 6) 计算历史站点地区权重（按 firm），用于 Non-AI 与 Stock 分配 ---
    # 如果 datacenter.xlsx 没有每站能耗列，就按“站点数量”求权重
    hist_region = (
        df_hist_sites.groupby(["firm", "region"], as_index=False)
                    .size()
                    .rename(columns={"size": "site_count"})
    )
    hist_region["w_hist_region"] = hist_region.groupby("firm")["site_count"] \
                                            .transform(lambda x: x / x.sum())

    # --- 7) 为缺失权重的情况做兜底（避免 NaN）---
    # 若某 firm 的某 year 在 AI 没有任何站点，则用其历史权重兜底；如果历史也没有，退回均匀分布
    def ensure_weights(df_weights, key_cols, weight_col):
        # 规范化避免浮点残差
        df_weights[weight_col] = df_weights[weight_col].fillna(0.0)
        # 归一化
        df_weights[weight_col] = df_weights.groupby(key_cols)[weight_col] \
                                        .transform(lambda x: 0 if x.sum()==0 else x/x.sum())
        return df_weights

    ai_region = ensure_weights(ai_region, ["firm","year"], "w_ai_region")
    hist_region = ensure_weights(hist_region, ["firm"], "w_hist_region")

    # 构造一个“均匀分布”权重以绝对兜底（公司范围内）
    all_regions = pd.DataFrame({"region": pd.concat([ai_region["region"], hist_region["region"]]).dropna().unique()})

    def build_uniform_weights(df_firms):
        rows = []
        for firm in df_firms["firm"].unique():
            regs = pd.concat([
                ai_region.loc[ai_region["firm"]==firm, "region"],
                hist_region.loc[hist_region["firm"]==firm, "region"],
            ]).dropna().unique()
            if len(regs)==0:
                regs = all_regions["region"].values
            w = 1/len(regs)
            for r in regs:
                rows.append((firm, r, w))
        uni = pd.DataFrame(rows, columns=["firm","region","w_uniform"])
        return uni

    uni_region = build_uniform_weights(df_total[["firm"]].drop_duplicates())

    # --- 8) 把三块权重准备好，合并到公司情景总量表，进行地理分配 ---
    # df_total 里应有：firm, year, scenario, e_stock_twh, e_ai_new_twh, e_nonai_new_twh
    need_cols = {"firm","year","scenario","e_stock_twh","e_ai_new_twh","e_nonai_new_twh","e_total_combined_twh"}
    missing = need_cols - set(df_total.columns)
    if missing:
        raise ValueError(f"你的情景输出缺少列：{missing}。请在导出时保留这些列。")

    # AI 权重并上公司-年份对齐，历史权重对齐到公司
    # 先做笛卡尔扩展到有 region 维度，再填权重
    firms_years = df_total[["firm","year"]].drop_duplicates()
    print("✅ 公司-年份组合示例:\n", firms_years.head())
    regions_by_firmyear = (ai_region[["firm","year","region"]]
                        .drop_duplicates()
                        .merge(firms_years, on=["firm","year"], how="outer"))
    regions_by_firm = (hist_region[["firm","region"]]
                    .drop_duplicates()
                    .merge(df_total[["firm"]].drop_duplicates(), on=["firm"], how="outer"))
    print("✅ 公司-年份-地区组合示例:\n", regions_by_firmyear.head())
    # 合并权重
    # AI: firm-year-region
    w_ai = regions_by_firmyear.merge(ai_region[["firm","year","region","w_ai_region"]],
                                    on=["firm","year","region"], how="left")
    print("✅ AI 权重合并示例:\n", w_ai.head())
    # hist: firm-region
    w_hist = regions_by_firm.merge(hist_region[["firm","region","w_hist_region"]],
                                on=["firm","region"], how="left")
    print("✅ 历史权重合并示例:\n", w_hist.head())
    # uniform：firm-region
    w_uni = uni_region.copy()

    # 归一化兜底
    w_ai["w_ai_region"] = w_ai["w_ai_region"].fillna(0.0)
    w_hist["w_hist_region"] = w_hist["w_hist_region"].fillna(0.0)

    # --- 9) 地理分配：Stock & Non-AI 用历史权重，AI 用 AI 权重 ---
    # 先把 df_total 与地区维度合并（两套：按 firm-year-region / 按 firm-region）
    base_ai = df_total.merge(w_ai, on=["firm","year"], how="left")
    base_ai = base_ai.dropna(subset=["region"])  # 只保留有 region 的

    base_hist = df_total.merge(w_hist, on=["firm"], how="left")
    base_hist = base_hist.dropna(subset=["region"])

    # 若某公司在某年 AI 权重全 0，则用 uniform 补
    tmp = df_total.merge(w_uni, on=["firm"], how="left")
    tmp = tmp.dropna(subset=["region"])

    # 计算各项地区电量
    ai_part = base_ai.copy()
    ai_part["e_region_ai_twh"] = ai_part["e_ai_new_twh"] * ai_part["w_ai_region"]
    print("✅ AI 地区分配示例:\n", ai_part.head())
    hist_part = base_hist.copy()
    hist_part["e_region_stock_twh"]  = hist_part["e_stock_twh"]   * hist_part["w_hist_region"]
    hist_part["e_region_nonai_twh"]  = hist_part["e_nonai_new_twh"] * hist_part["w_hist_region"]
    print("✅ 历史与 Non-AI 地区分配示例:\n", hist_part.head(20))
    hist_part_agg = (
    hist_part
    .groupby(["firm", "year", "scenario", "region"], as_index=False)
    .agg({
        "e_region_stock_twh": "mean",
        "e_region_nonai_twh": "mean"  # 或 sum，看你定义
        })
    )

    print("✅ 聚合后 hist_part 行数:", len(hist_part_agg))
    print(hist_part_agg.head())
    # hist_part.to_csv("regional_outputs\\hist_part_temp.csv", index=False)
    # 兜底：AI 权重为 0 的公司-年份，用 uniform 权重分配 AI 新增（极少数情况）
    ai_zero_mask = (ai_part.groupby(["firm","year"])["w_ai_region"].transform("sum") == 0)
    if ai_zero_mask.any():
        ai_part_fallback = df_total.merge(w_uni, on=["firm"], how="left")
        ai_part_fallback["e_region_ai_twh"] = ai_part_fallback["e_ai_new_twh"] * ai_part_fallback["w_uniform"]
        # 仅保留缺失的 firm-year
        keys = ai_part.loc[ai_zero_mask, ["firm","year"]].drop_duplicates()
        ai_part_fallback = ai_part_fallback.merge(keys, on=["firm","year"], how="inner")
    else:
        ai_part_fallback = ai_part.iloc[0:0].copy()  # 空

    # 汇总三个部分
    keep_ai = ai_part[~ai_zero_mask][["firm","year","scenario","region","e_region_ai_twh"]]
    ai_alloc = pd.concat([keep_ai, ai_part_fallback[["firm","year","scenario","region","e_region_ai_twh"]]], ignore_index=True)
    print("✅ AI 分配汇总示例:\n", ai_alloc.head())
    ai_alloc.to_csv("regional_outputs\\ai_alloc_temp.csv", index=False)
    region_alloc = (
        ai_alloc
        .merge(hist_part_agg[["firm","year","scenario","region","e_region_stock_twh","e_region_nonai_twh"]],
            on=["firm","year","scenario","region"], how="outer")
        .fillna(0.0)
    )
    region_alloc["e_region_total_twh"] = (region_alloc["e_region_stock_twh"]
                                        + region_alloc["e_region_nonai_twh"]
                                        + region_alloc["e_region_ai_twh"])
    print("✅ 地区分配最终示例:\n", region_alloc.head())
    region_alloc.to_csv("regional_outputs\\region_alloc_preid.csv", index=False)
    # === 为每个公司-年份-地区-情景生成唯一编号 ===
    region_alloc = region_alloc.copy()
    region_alloc["scenario_id"] = (
        region_alloc.groupby(["firm", "year", "region"])
        .cumcount() + 1
    )

    # === 聚合每公司-年份-地区-情景的均值 ===
    region_alloc_mean = (
        region_alloc
        .groupby(["firm", "year", "scenario", "region"], as_index=False)
        .agg({
            "e_region_ai_twh": "mean",
            "e_region_stock_twh": "mean",
            "e_region_nonai_twh": "mean",
            "e_region_total_twh": "mean"  # 如果有该列
        })
    )
    # region_alloc_mean.to_csv("regional_outputs\\region_alloc_mean.csv", index=False)
    #     # 或者如果你希望是全局唯一编号（不分公司）
    # region_alloc["global_id"] = (
    #     region_alloc.groupby(["year", "region", "scenario"])
    #     .ngroup() + 1
    # )

    # print("\n✅ 已生成唯一情景编号示例:")
    # print(region_alloc[["firm", "year", "region", "scenario", "scenario_id", "global_id"]].head(10))
    # region_alloc.to_csv("regional_outputs\\region_alloc.csv", index=False)
    # --- 10) 得到【地区 × 年份 × 情景】合计与 Top-15 ---
   # === 0️⃣ 汇总地区-情景数据 ===
    region_year_scen = (
        region_alloc_mean
        .groupby(["region","year","scenario"], as_index=False)[
            ["e_region_ai_twh","e_region_nonai_twh","e_region_stock_twh","e_region_total_twh"]
        ].sum()
    )
    region_year_scen.to_csv("regional_outputs/region_year_scenario_global.csv", index=False)

    # === 1️⃣ Top-15地区 (按情景) ===
    top15_2030 = (
        region_year_scen[region_year_scen["year"]==2030]
        .sort_values(["scenario","e_region_total_twh"], ascending=[True, False])
        .groupby("scenario")
        .head(30)
    )
    top15_2030.to_excel("regional_outputs/region_top15_2030_50.xlsx", index=False)

    # === 2️⃣ Firm-level堆叠数据 (neutral 情景)
    year_target = 2030
    firm_df = (
        region_alloc_mean[
            (region_alloc_mean["year"] == year_target)
            & (region_alloc_mean["scenario"] == "neutral")
        ]
        .groupby(["region", "firm"], as_index=False)["e_region_total_twh"]
        .sum()
    )
    pivot_df = firm_df.pivot(index="region", columns="firm", values="e_region_total_twh").fillna(0)

    # === 3️⃣ 情景上下限 ===
    scen_df = region_year_scen[region_year_scen["year"] == year_target]
    scen_summary = (
        scen_df.groupby(["region","scenario"])["e_region_total_twh"]
        .mean().unstack().fillna(0)
    )
    scen_summary["neutral"] = scen_summary.get("neutral", 0)
    scen_summary["yerr_min"] = scen_summary["neutral"] - scen_summary["conservative"]
    scen_summary["yerr_max"] = scen_summary["optimistic"] - scen_summary["neutral"]

    # === 4️⃣ 排序并对齐 ===
    region_order = scen_summary.sort_values("neutral", ascending=True).index
    pivot_df = pivot_df.reindex(region_order)
    scen_summary = scen_summary.reindex(region_order)

    # === 5️⃣ 绘图 ===
    fig, ax = plt.subplots(figsize=(10, 6))
    firm_colors = {
        "Amazon": "#ED985C",   # warm orange
        "Apple": "#5D3A9B",    # deep purple
        "Google": "#FFB964",   # light orange
        "Meta": "#B2ABD2",     # soft lavender
        "Msft": "#80CDC1",     # mint green
        "Oracle": "#018571",   # teal green
    }
    pivot_df.plot(kind="barh", stacked=True,
                color=[firm_colors.get(f, "#CCCCCC") for f in pivot_df.columns],
                ax=ax, width=0.7, legend=True)

    # === 6️⃣ 添加误差条 (Scenario range) ===
    y_positions = np.arange(len(scen_summary))
    ax.errorbar(
        x=scen_summary["neutral"],
        y=y_positions,
        xerr=[scen_summary["yerr_min"], scen_summary["yerr_max"]],
        fmt='none', ecolor='black', elinewidth=1.3, capsize=3, capthick=1.2,
        label="Scenario Range"
    )

    # === 7️⃣ 美化 ===
    ax.set_yticks(y_positions)
    ax.set_yticklabels(region_order)
    ax.set_xlabel(f"Electricity Demand (TWh, {year_target})")
    ax.set_ylabel("Region (U.S. State ≈ Country)")
    ax.set_title(f"AI Data Center Electricity Demand by Firm and Region ({year_target})", fontsize=13, fontweight="bold")

    ax.grid(axis="x", linestyle="--", alpha=0.4)
    ax.legend(title="Firm", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(f"regional_outputs/region_firm_with_errorbar_{year_target}.svg", dpi=400)
    plt.show()
    
    
def region_psi():
    """
    基于 region_top15_2030.xlsx 计算地区级电力压力指数 (PSI)
    """
    print("📂 读取 region_top15_2030.xlsx ...")
    df = pd.read_excel("regional_outputs/regional_top15_2030.xlsx")
    df.columns = df.columns.str.strip().str.lower()
    # print(df.head())
    required_cols = {"region", "year", "scenario", "e_region_total_twh"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"❌ 文件缺少必要列: {required_cols}")
    
    # ==============================================================
    # 1️⃣ 构建地区供电能力表（若无真实数据）
    # ==============================================================
    print("⚙️ 构造假设供电能力...")
    df_supply = (
        df.groupby("region", as_index=False)["e_region_total_twh"]
          .mean()
          .rename(columns={"e_region_total_twh": "capacity_twh"})
    )

    # 初始供电能力为平均耗电量的 10 倍
    df_supply["capacity_twh"] *= 10

    expanded = []
    for year in range(2025, 2031):
        temp = df_supply.copy()
        temp["year"] = year
        # 假设供电每年增长 2.5%
        temp["capacity_twh"] = temp["capacity_twh"] * ((1.025) ** (year - 2025))
        expanded.append(temp)
    df_supply = pd.concat(expanded, ignore_index=True)

    # ==============================================================
    # 2️⃣ 合并并计算 PSI
    # ==============================================================
    merged = pd.merge(df, df_supply, on=["region", "year"], how="left")
    merged["psi"] = merged["e_region_total_twh"] / merged["capacity_twh"]
    merged["psi_gap"] = (merged["e_region_total_twh"] - merged["capacity_twh"]) / merged["capacity_twh"]

    # ==============================================================
    # 3️⃣ 输出结果与 Top15
    # ==============================================================
    out_dir = Path("regional_outputs")
    out_dir.mkdir(exist_ok=True)

    merged.to_excel(out_dir / "region_psi_all.xlsx", index=False)

    # 取 2030 年结果
    top15 = (
        merged[merged["year"] == 2030]
        .sort_values("psi", ascending=False)
        .groupby("scenario")
        .head(15)
    )
    top15.to_excel(out_dir / "region_psi_top15_2030.xlsx", index=False)

    print("✅ 已生成 PSI 表格: region_psi_all.xlsx 和 region_psi_top15_2030.xlsx")

    # ==============================================================
    # 4️⃣ 可视化：不同情景下的前15地区 PSI 对比
    # ==============================================================
    plt.figure(figsize=(10, 6))
    colors = {"conservative": "#1f77b4", "neutral": "#2ca02c", "optimistic": "#ff7f0e"}

    for scen in ["conservative", "neutral", "optimistic"]:
        sub = top15[top15["scenario"] == scen]
        plt.barh(sub["region"], sub["psi"], label=scen.title(), color=colors[scen], alpha=0.7)

    plt.xlabel("Power Stress Index (PSI)")
    plt.ylabel("Region")
    plt.title("Top 15 Regions by Power Stress Index (2030)")
    plt.legend()
    plt.gca().invert_yaxis()
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(out_dir / "region_psi_top15_2030.png", dpi=300)
    plt.show()

    print(f"📊 已生成图表: {out_dir}/region_psi_top15_2030.png")

def region_forecast_2025():
    """
    提取 2025 年全企业区域预测，计算 e_region_total_twh by scenario
    """
    print("📂 读取 full_firm_forecast.xlsx 和 firm_total_energy_forecast_2025_2030_update4.xlsx ...")
    
    # === Step 1. 读取原始位置数据 ===
    df_locations = pd.read_excel(r"Holder\full_firm_forecast.xlsx")
    df_locations.columns = df_locations.columns.str.strip().str.lower()
    
    # === Step 2. 定义地区提取函数 ===
    def extract_region(loc):
        if pd.isna(loc):
            return None
        parts = [p.strip() for p in str(loc).split(",")]
        # US: "City, State, USA" 或 "State, USA"
        if len(parts) >= 2 and parts[-1].upper() == "USA":
            return parts[-2]  # 州
        # 非 US：取最后一段为国家
        if len(parts) >= 2:
            return parts[-1]
        return parts[0]
    
    df_locations["region"] = df_locations["location"].apply(extract_region)
    df_locations = df_locations[["firm", "region"]].drop_duplicates()
    
    # === Step 3. 读取情景预测数据（含 2025 年） ===
    df_forecast = pd.read_excel(r"Holder\firm_total_energy_forecast_2025_2030_update4.xlsx")
    df_forecast.columns = df_forecast.columns.str.strip().str.lower()
    
    # === Step 4. 过滤 2025 年数据 ===
    df_2025 = df_forecast[df_forecast["year"] == 2025].copy()
    print(f"✅ 读取 {len(df_2025)} 行 2025 年预测数据")
    
    # === Step 5. 合并区域信息 ===
    df_2025 = df_2025.merge(df_locations, on="firm", how="left")
    df_2025 = df_2025.dropna(subset=["region"])
    
    # === Step 6. 按区域和情景聚合 ===
    region_2025 = (
        df_2025
        .groupby(["region", "year", "scenario"], as_index=False)
        .agg({
            "e_total_combined_twh": "sum"
        })
        .rename(columns={"e_total_combined_twh": "e_region_total_twh"})
    )
    
    print(f"✅ 按区域聚合后 {len(region_2025)} 行数据")
    print(region_2025.head(10))
    
    # === Step 7. 保存结果 ===
    output_dir = Path("regional_outputs")
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "region_top15_2025_30.xlsx"
    region_2025.to_excel(output_file, index=False)
    print(f"✅ 已保存 2025 年区域预测: {output_file}")
    
    return region_2025

def extract_2025_conservative():
    """
    从 region_year_scenario_global.csv 提取 2025 年 neutral 情景数据
    返回 (region, e_region_total_twh) 对
    """
    print("📂 读取 region_year_scenario_global.csv ...")
    
    # === Step 1. 读取全局区域-年份-情景数据 ===
    df = pd.read_csv(r"Holder\regional_outputs\region_year_scenario_global.csv")
    print(f"✅ 读取 {len(df)} 行数据，列名：{df.columns.tolist()}")
    
    # === Step 2. 过滤 2025 年 conservative 情景 ===
    df_2025_neutral = df[
        (df["year"] == 2025) & 
        (df["scenario"].str.lower() == "neutral")
    ].copy()
    
    print(f"\n✅ 过滤后 {len(df_2025_neutral)} 行数据 (2025, neutral)")
    print(df_2025_neutral[["region", "year", "scenario", "e_region_total_twh"]])
    
    # === Step 3. 保存结果 ===
    output_dir = Path(r"Holder\regional_outputs")
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "region_2025_neutral.xlsx"
    df_2025_neutral.to_excel(output_file, index=False)
    print(f"\n✅ 已保存 2025 neutral 数据: {output_file}")
    
    return df_2025_neutral

if __name__ == "__main__":
    # forecasts()
    # forcast_extend()
    # scenario_analysis()
    # scenario_analysis_2()
    # dc_region_analysis()
    # energy_gap_analysis()
    # region_psi()
    extract_2025_conservative()
    