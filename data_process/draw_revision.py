import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D
from pathlib import Path
import numpy as np


def scenario_analysis_2():
    # === Load data ===
    hist = pd.read_excel(r"Holder\dc_consumption_history.xlsx")
    forecast = pd.read_excel(r"Holder\firm_total_energy_forecast_2025_2030_update4.xlsx")

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
    # === Define Color Map (one tone per firm) ===    plt.savefig("Holder/Fig1_firm_panels.png", dpi=300, bbox_inches="tight")    plt.savefig("Holder/Fig1_firm_panels.png", dpi=300, bbox_inches="tight")
# === Define Color Map (one tone per firm) ===
    base_colors = {
        "Amazon": "#1f77b4",      # 蓝
        "Apple": "#d62728",       # 橙
        "Google": "#2ca02c",      # 绿
        "Meta": "#9467bd",        # 紫
        "Msft": "#ff7f0e",        # 红
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
    fig, axes = plt.subplots(3, 2, figsize=(15, 12))

    # Define firms and display names
    firms = ["Amazon", "Msft", "Google", "Meta", "Oracle", "Apple"]
    display_names = ["Amazon", "Microsoft", "Google", "Meta", "Oracle", "Apple"]

    # === Firm-level forecast (6 panels) ===
    for i, (firm, disp) in enumerate(zip(firms, display_names)):
        ax = axes.flat[i]
        firm_forecast = forecast[forecast["firm"] == firm]

        for scen, style in zip(["conservative", "neutral", "optimistic"], ["--", "-.", ":"]):
            scen_df = firm_forecast[firm_forecast["scenario"] == scen]
            if scen_df.empty:
                continue

            scen_stats = scen_df.groupby("year", as_index=False)["e_total_twh"].agg(
                e_mean_twh="mean",
                e_min_twh="min",
                e_max_twh="max"
            )

            ax.fill_between(
                scen_stats["year"],
                scen_stats["e_min_twh"],
                scen_stats["e_max_twh"],
                color=color_map[firm][scen],
                alpha=0.2,
                label=f"{scen.title()} band"
            )

            ax.plot(
                scen_stats["year"],
                scen_stats["e_mean_twh"],
                linestyle=style,
                marker='o',
                markersize=5,
                color=color_map[firm][scen],
                markeredgecolor='black',
                markeredgewidth=0.6,
                linewidth=1.8,
                label=f"{scen.title()} mean"
            )

        ax.set_title(f"({chr(97+i)}) {disp}")
        ax.set_ylabel("Energy (TWh)")
        ax.legend(fontsize=7)
        ax.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    # plt.show()
    plt.savefig("Holder/Fig2_firm_panels.svg", dpi=300, bbox_inches="tight")


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
    df_ai = pd.read_excel(r"full_firm_forecast.xlsx")            # 未来各 AI 站点（含 Location、year、E_AI_DC）
    df_ai.columns = df_ai.columns.str.strip().str.lower()

        # === 读取 datacenter.xlsx ===
    df_hist_sites = pd.read_excel(r"datacenter.xlsx")            # 历史站点（仅站点与公司，或可含年份）
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
    
    df_total = pd.read_excel(r"firm_total_energy_forecast_2025_2030_update4.xlsx")  # 你情景函数输出
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
    # ai_alloc.to_csv(r"regional_outputs\\ai_alloc_temp.csv", index=False)
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
    # region_alloc.to_csv(r"regional_outputs\\region_alloc_preid.csv", index=False)
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
    # region_year_scen.to_csv(r"regional_outputs\region_year_scenario_global.csv", index=False)

    # === 1️⃣ Top-15地区 (按情景) ===
    top15_2030 = (
        region_year_scen[region_year_scen["year"]==2030]
        .sort_values(["scenario","e_region_total_twh"], ascending=[True, False])
        .groupby("scenario")
        .head(30)
    )
    # top15_2030.to_excel(r"regional_outputs\region_top15_2030_50.xlsx", index=False)

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
        "Amazon": "#005693",   # 同 scenario_analysis_2 (Amazon 蓝)
        "Apple": "#cd0000",    # 同 scenario_analysis_2 (Apple 橙)
        "Google": "#509f50",   # 同 scenario_analysis_2 (Google 绿)
        "Meta": "#8566a2",     # 同 scenario_analysis_2 (Meta 紫)
        "Msft": "#ff7b08",     # 同 scenario_analysis_2 (Microsoft 红)
        "Oracle": "#a76b5f",   # 同 scenario_analysis_2 (Oracle 棕)
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
    ax.set_title(f"Data Center Electricity Demand by Firm and Region ({year_target})", fontsize=13, fontweight="bold")

    ax.grid(axis="x", linestyle="--", alpha=0.4)
    ax.legend(title="Firm", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    # plt.savefig(f"region_firm_with_errorbar_{year_target}_v2.svg", dpi=400)
    plt.show()


if __name__ == "__main__":
    # scenario_analysis_2()
    energy_gap_analysis()