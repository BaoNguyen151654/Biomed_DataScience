# Nanomaterial Cytotoxicity Classification Task

I have uploaded 3 Excel files containing samples of nanomaterials.

Your task is to classify the cytotoxicity status for **every** sample in the dataset. You need to learn from `X_train_cyto` and `y_train_binary_cyto`, then make predictions on `X_test_cyto`.

## Classification Requirements

1. Predict the cytotoxicity status of every sample.
2. Use the following binary classification threshold based on Cell Viability (%):
   - **Cell Viability < 70%:** Cytotoxic (1).
   - **Cell Viability ≥ 70%:** Non-cytotoxic (0).
3. Use only the input features available in the dataset.
4. Preserve the original `sn` values exactly.
5. Do not omit or duplicate samples.
6. Do not search the internet or use external datasets.
7. Predict the classification of each sample independently.
8. Return binary numerical predictions only (0 or 1).
9. Do not fabricate missing input features.

## Inference-Time Measurement

Use an external timer if available.

- Record the start timestamp immediately before beginning predictions.
- Record the end timestamp after all predictions are completed.
- Report total elapsed time in seconds.
- Report the number of samples.
- Calculate average elapsed time per sample.

Do not invent or estimate inference time. If you cannot measure it reliably, explicitly state that.

## Output

Generate and provide a downloadable CSV file named:

`Gpt_Cytotox_Classification.csv`

The CSV must contain exactly these columns:

- `sn`
- `predicted_cytotoxicity`

The `predicted_cytotoxicity` column must contain:
- `1` = Cytotoxic
- `0` = Non-cytotoxic

## Final Validation

Before exporting:

- Verify that the output contains exactly as many rows as the input.
- Verify that every `sn` appears exactly once.
- Verify that all predictions are numeric integers.
- Verify that all predictions belong to the set `{0, 1}`.
- Confirm that `sn` was used only for sample identification and output alignment.
- Confirm that no samples were omitted or duplicated.
- Confirm that the classification threshold is consistent: Cell Viability < 70% = Cytotoxic (1), and Cell Viability ≥ 70% = Non-cytotoxic (0).

Do not merely display a table in the conversation. Generate the actual CSV file.
