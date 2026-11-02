import pandas as pd
from sklearn.model_selection import train_test_split

cytotox = pd.read_csv('Cytotox_filter.csv')
seltox = pd.read_csv('SelTox_filter.csv')

cytotox_train, cytotox_test = train_test_split(
    cytotox,
    test_size=0.2,
    random_state=42
)

seltox_train, seltox_test = train_test_split(
    seltox,
    test_size=0.2,
    random_state=42
)

cytotox_train.to_csv("cytotox_train.csv", index=False)
cytotox_test.to_csv("cytotox_test.csv", index=False)

seltox_train.to_csv("seltox_train.csv", index=False)
seltox_test.to_csv("seltox_test.csv", index=False)