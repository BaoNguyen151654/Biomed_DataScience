import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from scipy.stats import skew
import re

csv_url = "https://huggingface.co/datasets/QueHayRich/NanoAntimicrobialDB/resolve/main/Ag_MIC_Database.csv"
NanoAntimicrobialDB_2024 = pd.read_csv(csv_url)
cytotox = pd.read_csv("Cytotox_filtered.csv")
seltox = pd.read_csv("Seltox_filtered.csv")
ditox = pd.read_csv("dataset_3090.csv")
nanopar = pd.read_csv("Nanoparticles_MIC.csv")

def clean_mic_value(val):
    if pd.isna(val):
        return np.nan
    val_str = str(val).strip()

    range_match = re.match(r'^([0-9.]+)\s*[–\-]\s*([0-9.]+)$', val_str)
    if range_match:
        try:
            low = float(range_match.group(1))
            high = float(range_match.group(2))
            return (low + high) / 2
        except:
            pass

    num_match = re.search(r'([0-9.]+)', val_str)
    if num_match:
        try:
            return float(num_match.group(1))
        except:
            return np.nan
    return np.nan

mic_col_name = [col for col in NanoAntimicrobialDB_2024.columns if 'MIC' in col][0]
cleaned_mic = NanoAntimicrobialDB_2024[mic_col_name].apply(clean_mic_value)

datasets_to_analyze = {
    'Cytotox (Chem X)': (cytotox['viability_%'], 'Viability (%)'),
    'Seltox (Chem X)': (seltox['mic_np_µg_ml'], 'MIC (µg/mL)'),
    'Ditox': (ditox['Viability (%)'], 'Viability (%)'),
    'NanoAntimicrobialDB_2024': (cleaned_mic, 'MIC (µg/mL)'),
    'Nanoparticle-Antibacterial-Dataset': (nanopar['MIC (µg/mL)'], 'MIC (µg/mL)')
}

results = []
for name, (series, endpoint) in datasets_to_analyze.items():
    numeric_series = pd.to_numeric(series, errors='coerce')

    skew_val = numeric_series.skew()
    kurt_val = numeric_series.kurtosis()
    valid_samples = numeric_series.notna().sum()

    results.append({
        'Dataset (Column)': name,
        'End point': endpoint,
        'Skewness': skew_val,
        'Kurtosis': kurt_val,
        'Valid Samples': valid_samples
    })

results_df = pd.DataFrame(results)
display(results_df)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 15
})

sns.set_style("white")
fig, axes = plt.subplots(3, 2, figsize=(14, 16))
axes = axes.flatten()

plot_data = [
    ('Cytotox (Chem X)', cytotox['viability_%'], 'Viability (%)', '#1f77b4'),
    ('Ditox', ditox['Viability (%)'], 'Viability (%)', '#2ca02c'),
    ('Seltox (Chem X)', pd.to_numeric(seltox['mic_np_µg_ml'], errors='coerce'), 'MIC (µg/mL)', '#d62728'),
    ('NanoAntimicrobialDB_2024', cleaned_mic, 'MIC (µg/mL)', '#ff7f0e'),
    ('Nanoparticle-Antibacterial-Dataset', pd.to_numeric(nanopar['MIC (µg/mL)'], errors='coerce'), 'MIC (µg/mL)', '#9467bd')]

for i, (name, series, label, color) in enumerate(plot_data):
    ax = axes[i]
    clean_series = series.dropna()
    sns.histplot(clean_series, kde=True, ax=ax, color=color, stat="density", alpha=0.3, edgecolor=color, linewidth=1)
    ax.set_title(name, fontsize=13, fontweight='bold', pad=10)
    ax.set_xlabel(label, fontsize=11)
    ax.set_ylabel("Probability Density", fontsize=11)
    ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='#cccccc')
    ax.xaxis.grid(False)
    sns.despine(ax=ax, top=True, right=True)

fig.delaxes(axes[5])

plt.tight_layout()
plt.show()
