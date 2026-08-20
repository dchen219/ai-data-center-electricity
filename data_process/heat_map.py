import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import altair as alt
import geopandas as gpd
import matplotlib.patches as mpatches

def heat_map():
    # === Data: Firm–Determinant Intensity (1–5 scale) ===
    data = {
        'Firm': ['Google', 'Amazon', 'Meta', 'Microsoft', 'Oracle', 'Apple'],
        'Energy Access & Sustainability': [5, 3, 5, 4, 3, 5],
        'Policy & Regulatory Environment': [3, 5, 2, 5, 5, 3],
        'Infrastructure Maturity': [4, 4, 4, 3, 2, 3],
        'Market Demand Potential': [3, 5, 3, 3, 4, 3],
        'Corporate Integration & Synergy': [2, 2, 2, 3, 3, 5],
        'Network Connectivity & Latency': [4, 5, 4, 3, 3, 3]
    }

    df = pd.DataFrame(data)
    df.set_index('Firm', inplace=True)

    # === Normalize to 0–1 ===
    df_norm = df / 5.0


    # === Set Seaborn style ===
    sns.set_theme(style="whitegrid", font="Arial")
    plt.figure(figsize=(10, 5))

    # === Draw Heatmap ===
    ax = sns.heatmap(
        df_norm,
        cmap="cividis",
        annot=df,             # show raw 1–5 values
        fmt="d",
        linewidths=0.6,
        vmin=0, vmax=1,
        cbar_kws={'label': 'Determinant Emphasis (normalized 0–1)'}
    )

    # === Titles and labels ===
    plt.title(
        "Firm–Determinant Intensity Matrix of AI Data Center Expansion (2025–2030)",
        fontsize=13, weight="bold", pad=15
    )
    plt.xlabel("")
    plt.ylabel("")
    plt.xticks(rotation=25, ha="right", fontsize=10)
    plt.yticks(fontsize=10)

    # === Refine colorbar ===
    cbar = ax.collections[0].colorbar
    cbar.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    cbar.set_ticklabels(["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"])
    cbar.ax.tick_params(labelsize=9, width=0.6, length=3)
    cbar.outline.set_linewidth(0.6)
    cbar.set_label(
        "Determinant Emphasis (0 = Low / Blue → 1 = High / Red)",
        fontsize=11, weight="bold", labelpad=12, rotation=270
    )

    plt.tight_layout()

    # === Optional: Save High-Resolution Version ===
    plt.savefig("firm_determinant_matrix_blue_to_red2.svg", dpi=600, bbox_inches="tight", transparent=True)

    plt.show()
def heat_map2():
    # === Data: Firm–Determinant Intensity (1–5 scale) ===
    data = {
        'Firm': ['Google', 'Amazon', 'Meta', 'Microsoft', 'Oracle', 'Apple'],
        'Energy Access & Sustainability': [5, 3, 5, 4, 3, 5],
        'Policy & Regulatory Environment': [3, 5, 2, 5, 5, 3],
        'Infrastructure Maturity': [4, 4, 4, 3, 2, 3],
        'Market Demand Potential': [3, 5, 3, 3, 4, 3],
        'Corporate Integration & Synergy': [2, 2, 2, 3, 3, 5],
        'Network Connectivity & Latency': [4, 5, 4, 3, 3, 3]
    }

    df = pd.DataFrame(data)
    df.set_index('Firm', inplace=True)

    # === Normalize to 0–1 ===
    df_norm = df / 5.0

    # === Set Seaborn style ===
    sns.set_theme(style="white", font="Arial")
    plt.figure(figsize=(10, 5))

    # === Draw Heatmap ===
    ax = sns.heatmap(
        df_norm,
        cmap="viridis",              # perceptually uniform sequential palette
        annot=df,                    # show raw 1–5 values
        fmt="d",
        linewidths=0.6,
        linecolor="white",
        vmin=0,
        vmax=1,
        cbar_kws={
            'label': 'Relative Determinant Emphasis'
        }
    )

    # === Titles and labels ===
    plt.title(
        "Firm–Determinant Intensity Matrix of AI Data Center Expansion",
        fontsize=13,
        weight="bold",
        pad=15
    )

    plt.xlabel("")
    plt.ylabel("")

    plt.xticks(
        rotation=25,
        ha="right",
        fontsize=10
    )

    plt.yticks(
        rotation=0,
        fontsize=10
    )

    # === Refine colorbar ===
    cbar = ax.collections[0].colorbar

    cbar.set_ticks([
        0.0, 0.2, 0.4, 0.6, 0.8, 1.0
    ])

    cbar.set_ticklabels([
        "0.0", "0.2", "0.4", "0.6", "0.8", "1.0"
    ])

    cbar.ax.tick_params(
        labelsize=9,
        width=0.6,
        length=3
    )

    cbar.outline.set_linewidth(0.6)

    cbar.set_label(
        "Relative Determinant Emphasis\n(0 = Low, 1 = High)",
        fontsize=10,
        labelpad=14,
        rotation=270,
        va="bottom"
    )

    plt.tight_layout()

    # === Save high-resolution version ===
    plt.savefig(
        "firm_determinant_matrix_cividis.svg",
        dpi=600,
        bbox_inches="tight",
        transparent=True
    )

    plt.show()

def line_chart():
    # === Load data ===
    df = pd.read_excel("currentenergy_consumption.xlsx")
    print(df.head())
    # Clean column names
    df.columns = df.columns.str.strip()

    # Drop irrelevant or empty columns
    df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors="ignore")

    # Rename columns to standard ones for Altair
    df = df.rename(columns={
        "Firm": "symbol",
        "Year": "date",
        "Energy Consumption(TWh)": "price"
    })

    # Convert year to datetime for x-axis
    df["date"] = pd.to_datetime(df["date"], format="%Y")

    # === Build chart ===
    base = alt.Chart(df).encode(
        alt.Color("symbol:N").legend(None)
    ).properties(width=600)

    # Line for each firm
    line = base.mark_line().encode(
        x="date:T",
        y="price:Q"
    )

    # Last value marker
    last_price = base.mark_circle().encode(
        alt.X("last_date['date']:T"),
        alt.Y("last_date['price']:Q")
    ).transform_aggregate(
        last_date="argmax(date)",
        groupby=["symbol"]
    )

    # Firm labels
    company_name = last_price.mark_text(
        align="left", dx=5
    ).encode(
        text="symbol:N"
    )

    # Combine all layers
    chart = (line + last_price + company_name).encode(
        x=alt.X("date:T", title="Year"),
        y=alt.Y("price:Q", title="Energy Consumption (TWh)")
    )

    # Save SVG
    chart.save("energy_consumption_chart2.svg")
    print("✅ Saved as energy_consumption_chart.svg")

def update_data():
# === Load your Excel file ===
    df = pd.read_excel("currentenergy_consumption.xlsx")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Drop unnecessary columns (like 'Unnamed')
    df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors="ignore")

    # Rename columns for consistency
    df = df.rename(columns={
        "Firm": "symbol",  # company name
        "Year": "date",    # year column
        "Energy Consumption(TWh)": "price"  # numeric column
    })

    # Convert 'date' column to datetime (for time axis)
    df["date"] = pd.to_datetime(df["date"], format="%Y")

    # === Build the base chart ===
    base = alt.Chart(df).encode(
        alt.Color("symbol:N").legend(title="Firm")
    ).properties(
        width=700,
        height=400,
        title="Energy Consumption of Major Tech Firms (2015–2024)"
    )

    # === Line for each firm ===
    line = base.mark_line(point=True, strokeWidth=2).encode(
        x=alt.X(
            "date:T",
            title="Year",
            axis=alt.Axis(
                values=["2015-01-01", "2017-01-01", "2021-01-01", "2024-01-01"],
                format="%Y",
                labelAngle=0
            )
        ),
        y=alt.Y("price:Q", title="Energy Consumption (TWh)")
    )

    # === Optional: add labels at the last data point ===
    last_point = base.mark_text(
        align="left", dx=5, dy=0
    ).encode(
        text="symbol:N"
    ).transform_aggregate(
        last_date="argmax(date)",
        groupby=["symbol"]
    )

    # Combine the layers
    chart = (line + last_point)

    # === Save the chart ===
    chart.save("energy_consumption_linechart.svg")

def main():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load data
    df = pd.read_excel("currentenergy_consumption.xlsx")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Drop irrelevant or empty columns
    df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors="ignore")

    # Rename columns
    df = df.rename(columns={
        "Firm": "Firm",
        "Year": "Year",
        "Energy Consumption(TWh)": "Energy"
    })

    # Filter only 2015, 2017, 2021, 2024
    df = df[df["Year"].isin([2015, 2017, 2021, 2024])]

    # Plot
    plt.figure(figsize=(8, 5))
    for firm in df["Firm"].unique():
        subset = df[df["Firm"] == firm]
        plt.plot(subset["Year"], subset["Energy"], marker="o", label=firm)

    plt.title("Energy Consumption (TWh) by Firm (Selected Years)")
    plt.xlabel("Year")
    plt.ylabel("Energy Consumption (TWh)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save as SVG
    output_path = "energy_consumption_selected_years.svg"
    plt.savefig(output_path, format="svg", dpi=600, bbox_inches="tight")

def map():
    # === 1. 读取数据 ===
    df = pd.read_excel("Site_unique_with_citytier_gdp.xlsx")

    # === 2. 构建 GeoDataFrame ===
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["y"], df["x"]), crs="EPSG:4326")


    # === 2. 读取城市底图 ===
    cities = gpd.read_file(r"D:\Financial_Carbon\Holder\data\ne_10m_populated_places.zip")
    cities = cities[cities.geometry.notnull()].copy()
    cities = cities.to_crs("EPSG:4326")

    # === 3. 定义颜色映射 ===
    tier_colors = {"Tier 1": "#e41a1c", "Tier 2": "#ff7f00", "Tier 3": "#377eb8", "Tier 4": "#999999"}
    firm_colors = {"Amazon": "#1f77b4", "Google": "#ff7f0e", "Oracle": "#2ca02c", "Meta": "#d62728", "Apple": "#9467bd"}

    # === 4. 合并城市与数据中心（按最近城市匹配） ===
    # 用空间连接找到每个数据中心最近的城市
    joined = gpd.sjoin_nearest(gdf, cities, how="left", distance_col="dist_km")

    # 计算每个城市对应的最高等级 Tier
    tier_map = {"Tier 1": 1, "Tier 2": 2, "Tier 3": 3, "Tier 4": 4}
    inv_tier_map = {v: k for k, v in tier_map.items()}
    city_tier = joined.groupby("NAME")["City_Tier"].apply(
        lambda x: inv_tier_map[min([tier_map[t] for t in x if t in tier_map])]
    ).reset_index()
    cities = cities.merge(city_tier, on="NAME", how="left")

    # === 5. 绘图 ===
    fig, ax = plt.subplots(figsize=(18, 9))
    ax.set_aspect("equal")

    # 底图按城市等级着色
    cities["color"] = cities["City_Tier"].map(tier_colors)
    cities.plot(ax=ax, color=cities["color"].fillna("lightgray"), markersize=10, alpha=0.5)

    # 绘制数据中心点
    for _, r in gdf.iterrows():
        ax.scatter(
            r.geometry.x,
            r.geometry.y,
            s=r["estimated_probability"] * 600,
            color=firm_colors.get(r["Firm"], "black"),
            edgecolor=tier_colors.get(r["City_Tier"], "black"),
            linewidth=1.2,
            alpha=0.9
        )

    # 图例
    firm_patches = [mpatches.Patch(color=c, label=f) for f, c in firm_colors.items()]
    tier_patches = [mpatches.Patch(color=c, label=t) for t, c in tier_colors.items()]
    legend1 = ax.legend(handles=firm_patches, title="Firm", loc="lower left", fontsize=10)
    ax.add_artist(legend1)
    ax.legend(handles=tier_patches, title="City Tier", loc="lower right", fontsize=10)

    ax.set_xlim(-180, 180)
    ax.set_ylim(-60, 85)
    ax.set_title("Global AI Data Centers and City-Level Distribution", fontsize=17, weight="bold")
    ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
    ax.set_facecolor("whitesmoke")
    plt.tight_layout()
    plt.savefig("global_ai_dc_city_tier_map.png", dpi=400, bbox_inches="tight")
    plt.show()

def map_up():
    import os
    import urllib.request
    import pandas as pd
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.colors import ListedColormap, BoundaryNorm
    from adjustText import adjust_text

    # ============================================================
    # 1. 路径与下载
    # ============================================================
    DATA_DIR = r"D:\Financial_Carbon\Holder\data"
    os.makedirs(DATA_DIR, exist_ok=True)

    STATE_PATH = os.path.join(DATA_DIR, "ne_50m_admin_1_states_provinces.zip")
    if not os.path.exists(STATE_PATH):
        print("Downloading province/state shapefile...")
        url = "https://naturalearth.s3.amazonaws.com/50m_cultural/ne_50m_admin_1_states_provinces.zip"
        urllib.request.urlretrieve(url, STATE_PATH)
        print("✅ Province/state shapefile downloaded successfully.")

    # ============================================================
    # 2. 读取数据中心文件与底图（含CRS修正）
    # ============================================================
    df = pd.read_excel("Site_unique_with_citytier_gdp.xlsx")
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["y"], df["x"]), crs="EPSG:4326")

    states = gpd.read_file(STATE_PATH)

    # --- 坐标系修正 ---
    if states.crs is None:
        print("⚠️ No CRS found. Setting to EPSG:4326 (WGS84).")
        states.set_crs(epsg=4326, inplace=True)
    elif states.crs.to_string().lower() not in ["epsg:4326", "urn:ogc:def:crs:epsg::4326"]:
        print(f"⚠️ Detected CRS: {states.crs}. Converting to EPSG:4326.")
        states = states.to_crs(epsg=4326)

    print(f"✅ CRS confirmed: {states.crs}")
    states = states[states["iso_a2"].notna()].copy()  # 去除非主权区

    # 自动检测省份名称字段
    state_name_col = None
    for c in ["name", "name_en", "nameascii", "NAME"]:
        if c in states.columns:
            state_name_col = c
            break
    if not state_name_col:
        raise ValueError("❌ Province/State name field not found.")
    print(f"✅ State name column detected: {state_name_col}")

    # ============================================================
    # 3. 定义配色与色阶
    # ============================================================
    tier_order = ["Tier 1", "Tier 2", "Tier 3", "Tier 4"]
    tier_colors = {
        "Tier 1": "#d73027",  # 红
        "Tier 2": "#fc8d59",  # 橙
        "Tier 3": "#91bfdb",  # 蓝
        "Tier 4": "#cccccc",  # 灰
    }
    tier_numeric = {"Tier 1": 1, "Tier 2": 2, "Tier 3": 3, "Tier 4": 4}

    firm_colors = {
        "Amazon": "#1f77b4",
        "Google": "#ff7f0e",
        "Oracle": "#2ca02c",
        "Meta": "#d62728",
        "Apple": "#9467bd",
    }

    # ============================================================
    # 4. 空间匹配 + 动态右表字段识别
    # ============================================================
    print("Matching data centers to nearest provinces/states...")
    joined = gpd.sjoin_nearest(gdf, states, how="left", distance_col="dist_km")

    possible_names = [state_name_col, f"{state_name_col}_right"]
    valid_col = [c for c in possible_names if c in joined.columns]
    if not valid_col:
        raise KeyError(f"No state name column found in joined DataFrame. Available columns: {joined.columns}")
    group_col = valid_col[0]

    tier_map = {"Tier 1": 1, "Tier 2": 2, "Tier 3": 3, "Tier 4": 4}
    inv_tier_map = {v: k for k, v in tier_map.items()}

    # 按省级聚合
    state_tier = (
        joined.groupby(group_col)["City_Tier"]
        .apply(lambda x: inv_tier_map[min([tier_map[t] for t in x if t in tier_map])])
        .reset_index()
    )
    state_tier.columns = [state_name_col, "City_Tier"]

    states = states.merge(state_tier, on=state_name_col, how="left")
    matched_count = states["City_Tier"].notna().sum()
    print(f"✅ Matched {matched_count} provinces/states with AI data center tiers.")

    # ============================================================
    # 5. 绘图
    # ============================================================
    fig, ax = plt.subplots(figsize=(18, 9))
    ax.set_aspect("equal")

    # --- 基础底图 ---
    states["TierNum"] = states["City_Tier"].map(tier_numeric)
    cmap = ListedColormap([tier_colors[t] for t in tier_order])
    norm = BoundaryNorm([0.5, 1.5, 2.5, 3.5, 4.5], cmap.N)

    states.plot(
        ax=ax,
        column="TierNum",
        cmap=cmap,
        norm=norm,
        linewidth=0.3,
        edgecolor="white",
        alpha=0.9,
    )

    # --- 数据中心点 ---
    for _, r in gdf.iterrows():
        ax.scatter(
            r.geometry.x,
            r.geometry.y,
            s=r["estimated_probability"] * 600,
            color=firm_colors.get(r["Firm"], "black"),
            edgecolor=tier_colors.get(r["City_Tier"], "black"),
            linewidth=1.2,
            alpha=0.9,
        )

    # --- Tier 1/2 标签 ---
    texts = []
    for _, row in states.iterrows():
        if row.get("City_Tier") in ["Tier 1", "Tier 2"]:
            centroid = row.geometry.representative_point()
            texts.append(
                ax.text(
                    centroid.x,
                    centroid.y,
                    row[state_name_col],
                    fontsize=7,
                    color="black",
                    ha="center",
                    va="center",
                    weight="bold",
                    alpha=0.8,
                )
            )
    adjust_text(texts, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))

    # ============================================================
    # 6. 图例与色带
    # ============================================================
    firm_patches = [mpatches.Patch(color=c, label=f) for f, c in firm_colors.items()]
    legend1 = ax.legend(handles=firm_patches, title="Firm", loc="lower left", fontsize=9)
    ax.add_artist(legend1)

    # 连续色带 colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    cbar = plt.colorbar(sm, ax=ax, orientation="horizontal", fraction=0.03, pad=0.05)
    cbar.set_label("Province/State Tier (1–4)", fontsize=10)
    cbar.set_ticks([1, 2, 3, 4])
    cbar.set_ticklabels(tier_order)

    ax.set_xlim(-180, 180)
    ax.set_ylim(-60, 85)
    ax.set_title(
        "Global AI Data Centers and Province-Level Tier Distribution",
        fontsize=17,
        weight="bold",
        pad=15,
    )
    ax.set_xlabel("Longitude", fontsize=11)
    ax.set_ylabel("Latitude", fontsize=11)
    ax.set_facecolor("whitesmoke")

    plt.tight_layout()
    OUTPUT_PATH = "global_ai_dc_state_tier_map_final_with_colorbar.png"
    plt.savefig(OUTPUT_PATH, dpi=400, bbox_inches="tight")
    plt.show()

    print(f"✅ Map saved successfully to: {OUTPUT_PATH}")

def forecasts():
    # === Step 1. 自动读取文件所有 sheet ===
    file_path = "full_firm_forecast.xlsx"
    excel_file = pd.ExcelFile(file_path)

    # 自动检测包含“firm”和“E_DC”关键列的 sheet
    target_sheets = []
    for sheet in excel_file.sheet_names:
        df_temp = pd.read_excel(file_path, sheet_name=sheet, nrows=3)
        cols = [c.lower().strip() for c in df_temp.columns]
        if any("firm" in c for c in cols) and any("e_dc" in c or "energy" in c for c in cols):
            target_sheets.append(sheet)

    if not target_sheets:
        raise ValueError("⚠️ 未找到包含 firm / E_DC 列的 sheet，请检查文件。")
    else:
        print(f"✅ 检测到以下候选 sheet: {target_sheets}")

    # === Step 2. 读取目标 sheet（默认取第一个匹配项） ===
    df = pd.read_excel(file_path, sheet_name=target_sheets[0])
    df.columns = df.columns.str.strip()
    print(f"✅ 读取 {target_sheets[0]}，共 {len(df)} 行")

    # === Step 3. 统一列名并清洗 ===
    rename_map = {}
    for c in df.columns:
        c_low = c.lower()
        if "firm" in c_low: rename_map[c] = "firm"
        if "year" in c_low: rename_map[c] = "year"
        if "e_dc" in c_low or "energy" in c_low: rename_map[c] = "E_DC"
    df = df.rename(columns=rename_map)

    # === Step 4. 汇总 2026 基准数据 ===
    base_year = 2026
    df_base = df[df["year"] == base_year].groupby("firm", as_index=False)["E_DC"].sum()
    df_base = df_base.rename(columns={"E_DC": "E_AI_2026"})
    print("✅ 成功汇总 2026 年基准 AI 数据中心能耗：")
    print(df_base)

    # === Step 5. 参数设定 ===
    beta = 0.6  # 预测覆盖率
    growth_scenarios = {"conservative": 0.15, "neutral": 0.25, "optimistic": 0.35}

    # 各公司 AI 占比
    p_ai = {
        "Meta": {"conservative": 0.35, "neutral": 0.50, "optimistic": 0.60},
        "Microsoft": {"conservative": 0.30, "neutral": 0.45, "optimistic": 0.55},
        "Google": {"conservative": 0.25, "neutral": 0.40, "optimistic": 0.50},
        "Amazon": {"conservative": 0.15, "neutral": 0.25, "optimistic": 0.40},
        "Oracle": {"conservative": 0.20, "neutral": 0.35, "optimistic": 0.50},
        "Apple": {"conservative": 0.08, "neutral": 0.15, "optimistic": 0.25},
    }

    # === Step 6. 计算未来各年能耗 ===
    records = []
    for _, row in df_base.iterrows():
        firm, e_base = row["firm"], row["E_AI_2026"]
        for scenario, gN in growth_scenarios.items():
            for year in range(2026, 2031):
                e_ai = (e_base / beta) * ((1 + gN) ** (year - base_year))
                p_val = p_ai.get(firm, {}).get(scenario, 0.3)
                e_total = e_ai / p_val
                records.append({
                    "firm": firm,
                    "scenario": scenario,
                    "year": year,
                    "gN": gN,
                    "p_AI": p_val,
                    "E_AI_TWh": e_ai / 1e6,
                    "E_Total_TWh": e_total / 1e6,
                })

    df_out = pd.DataFrame(records)

    # === Step 7. 导出结果 ===
    out_path = "ai_dc_energy_scenarios_auto.xlsx"
    df_out.to_excel(out_path, index=False)
    print(f"✅ 已输出结果至 {out_path}")
def pie_chart():
    # ========== 数据定义 ==========
    regions = ["North America", "Europe", "Asia-Pacific", "Middle East", "Nordic"]
    labels = [
        ["Renewable Energy", "Climate Advantage (Cool Climate)", "Policy Incentives", "Connectivity (Mature Infrastructure)"],
        ["Renewable Energy", "Sustainability Alignment", "Market Demand"],
        ["Market Demand", "Government Investment", "Connectivity (Mature Infrastructure)"],
        ["Government Investment", "Land Availability", "Energy Contract"],
        ["Renewable Energy", "Climate Advantage (Cool Climate)", "Sustainability Alignment"],
    ]
    weights = [
        [0.3, 0.2, 0.3, 0.2],
        [0.4, 0.35, 0.25],
        [0.45, 0.35, 0.2],
        [0.5, 0.3, 0.2],
        [0.45, 0.35, 0.2],
    ]

    color_map = {
        "Renewable Energy": "#4daf4a",
        "Climate Advantage (Cool Climate)": "#377eb8",
        "Policy Incentives": "#984ea3",
        "Connectivity (Mature Infrastructure)": "#ff7f00",
        "Sustainability Alignment": "#e41a1c",
        "Market Demand": "#984ea3",
        "Government Investment": "#4daf4a",
        "Land Availability": "#a65628",
        "Energy Contract": "#fdb462",
    }

    # ========== 绘制圆环图 ==========
    fig, axs = plt.subplots(1, 5, figsize=(18, 5))

    for i, ax in enumerate(axs):
        wedges, texts, autotexts = ax.pie(
            weights[i],
            labels=None,
            colors=[color_map.get(l, "#cccccc") for l in labels[i]],
            autopct="%1.0f%%",
            textprops={"fontsize": 8},
            wedgeprops={"width": 0.4, "edgecolor": "white"}
        )
        ax.set_title(regions[i], fontsize=10, fontweight="bold")

    # ========== 添加图例 ==========
    all_labels = list({lbl for sub in labels for lbl in sub})
    fig.legend(
        handles=[plt.Line2D([0], [0], marker='o', color='w', label=l,
                            markerfacecolor=color_map.get(l, "#cccccc"), markersize=8)
                 for l in all_labels],
        labels=all_labels,
        loc='lower center',
        ncol=4,
        bbox_to_anchor=(0.5, -0.05),
        fontsize=8
    )

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2)
    plt.savefig("regional_determinants_donutcharts_with_legend.svg", dpi=300, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    heat_map2()
    # line_chart()
    # update_data()
    # main()
    # map()
    # map_up()
    # forecasts()
    # pie_chart()