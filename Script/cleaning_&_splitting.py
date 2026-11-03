import pandas as pd
from sklearn.model_selection import train_test_split
import zipfile

cyto = pd.read_csv('Cytotox.csv')
sel = pd.read_csv('SelTox.csv')

# Remove all null in the target features
cyto = cyto.dropna(subset=['viability_%'])
sel = sel.dropna(subset=['mic_np_µg_ml'])
# Drop all research indicators. core_nm have no value, so it is better to remove it too
cyto = cyto.drop(columns=[
    'doi',
    'article_list',
    'journal_name',
    'publisher',
    'year',
    'title',
    'journal_is_oa',
    'is_oa',
    'oa_status',
    'pdf',
    'access',
    'core_nm'
])
sel = sel.drop(columns=[
    'doi',
    'article_list',
    'journal_name',
    'publisher',
    'year',
    'title',
    'journal_is_oa',
    'is_oa',
    'oa_status',
    'pdf',
    'access',
    'reference'
])

# Remove samples that do not have "MIC" as method. While all values are method, it is better to remove the column 'method.
sel = sel[sel['method'] == 'MIC'].copy()
sel = sel.drop(columns=['concentration','zoi_np_mm','method'])

# Train-test split (80-20)
cyto_train, cyto_test = train_test_split(
    cyto,
    test_size=0.2,
    random_state=42,
    shuffle=True
)
sel_train, sel_test = train_test_split(
    sel,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

print("Cyto:", cyto_train.shape, cyto_test.shape)
print("Sel:", sel_train.shape, sel_test.shape)

# CYTO - Cell Viability
X_train_cyto = cyto_train.drop(columns=['viability_%'])
y_train_cyto = cyto_train['viability_%']

X_test_cyto = cyto_test.drop(columns=['viability_%'])
y_test_cyto = cyto_test['viability_%']


# SEL - MIC
X_train_sel = sel_train.drop(columns=['mic_np_µg_ml'])
y_train_sel = sel_train['mic_np_µg_ml']

X_test_sel = sel_test.drop(columns=['mic_np_µg_ml'])
y_test_sel = sel_test['mic_np_µg_ml']

print("CYTO:")
print(X_train_cyto.shape, y_train_cyto.shape)
print(X_test_cyto.shape, y_test_cyto.shape)

print("\nSEL:")
print(X_train_sel.shape, y_train_sel.shape)
print(X_test_sel.shape, y_test_sel.shape)

# Save 4 datasets
cyto_train.to_csv('cyto_train.csv', index=False)
cyto_test.to_csv('cyto_test.csv', index=False)
sel_train.to_csv('sel_train.csv', index=False)
sel_test.to_csv('sel_test.csv', index=False)

datasets = {
    'X_train_cyto': X_train_cyto,
    'X_test_cyto': X_test_cyto,
    'y_train_cyto': y_train_cyto,
    'y_test_cyto': y_test_cyto,
    'X_train_sel': X_train_sel,
    'X_test_sel': X_test_sel,
    'y_train_sel': y_train_sel,
    'y_test_sel': y_test_sel
}

# Save all files into ZIP (X-y pairs)
with zipfile.ZipFile('ML_datasets.zip', 'w') as zipf:
    for name, data in datasets.items():
        data.to_csv(f'{name}.csv', index=False)
        zipf.write(f'{name}.csv')
