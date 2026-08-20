import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. Read data
# =========================
file_path = r"Holder\regional_outputs\regional_power_stress_index_2030v2.xlsx"   # 改成你的文件名
sheet_name = 0                 # 如果有特定sheet，可以改成sheet名

df = pd.read_excel(file_path, sheet_name=sheet_name)

# =========================
# 2. Keep needed rows
# =========================
# 根据你的数据调整 scenario 名称
year_target = 2030
scenario_target = "conservative"   # 如果实际值不是这个，请改掉

# 有些表里 scenario 可能被截断或大小写不一致，所以这里更稳一点
df["scenario"] = df["scenario"].astype(str).str.strip().str.lower()

plot_df = df[
    (df["year"] == year_target) &
    (df["scenario"].str.contains(scenario_target.lower()))
].copy()

# =========================
# 3. Sort by EDPI/psi
# =========================
# 这里假设你的 EDPI 列名叫 psi
plot_df = plot_df.sort_values(by="psi", ascending=False).reset_index(drop=True)

# =========================
# 4. Compute percentiles
# =========================
p75 = plot_df["psi"].quantile(0.75)
p90 = plot_df["psi"].quantile(0.90)

print(f"P75 = {p75:.4f}")
print(f"P90 = {p90:.4f}")

# =========================
# 5. Draw figure
# =========================
fig, ax = plt.subplots(figsize=(14, 7))

bars = ax.bar(
    plot_df["region"],
    plot_df["psi"],
    edgecolor="black",
    linewidth=1.1
)

# 让高值颜色更深，低值更浅
norm = plt.Normalize(plot_df["psi"].min(), plot_df["psi"].max())
for bar, val in zip(bars, plot_df["psi"]):
    bar.set_facecolor(plt.cm.Reds(norm(val)))

# Add percentile lines
ax.axhline(
    y=p75,
    linestyle="--",
    linewidth=1.5,
    label=f"Upper quantile group (P75 = {p75:.2f})"
)

ax.axhline(
    y=p90,
    linestyle="--",
    linewidth=1.5,
    label=f"Top quantile group (P90 = {p90:.2f})"
)

# =========================
# 6. Labels and style
# =========================
ax.set_title(f"Regional Electricity Demand Pressure Index ({year_target} - {scenario_target.capitalize()} Scenario)",
             fontsize=15, fontweight="bold")
ax.set_ylabel("Electricity Demand Pressure Index (EDPI)", fontsize=12)
ax.set_xlabel("")

plt.xticks(rotation=45, ha="right", fontsize=15)
ax.legend(frameon=False)
ax.spines["top"].set_visible(True)
ax.spines["right"].set_visible(True)

plt.tight_layout()
svg_path = r"Holder\regional_outputs\regional_power_stress_index_2030v3.svg"
fig.savefig(svg_path, format="svg")
print(f"Saved SVG to: {svg_path}")
plt.show()