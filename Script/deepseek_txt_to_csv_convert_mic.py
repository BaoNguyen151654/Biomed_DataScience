import pandas as pd

files_to_convert = [
    {
        "input": "deepseek_csv_20261106_37c82f.txt",
        "output": "deepseek_MIC_predictions.csv"
    },
    {
        "input": "deepseek_csv_20261107_6f40c7.txt",
        "output": "deepseek_binary_predictions.csv"
    }
]

for file_info in files_to_convert:
    print(f"Processing: {file_info['input']}...")
    df = pd.read_csv(file_info['input'])
    df.to_csv(file_info['output'], index=False)
    print(f"Saved: {file_info['output']}")
    print(df.head())
    print("-" * 50)
