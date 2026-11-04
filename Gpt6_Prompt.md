# Nanomaterial MIC Prediction Prompt

I have uploaded 3 Excel files containing samples of nanomaterials.

Your task is to predict the Minimum Inhibitory Concentration (MIC) for EVERY sample in the dataset. You need to learn from the "X_train_sel", "y_train_sel" and make predictions on "X_test_sel".

## Prediction requirements

1. Predict MIC in µg/mL.
2. Use only the input features available in the dataset.
3. Do not use the actual MIC target column, even if it exists in the file.
4. Do not use `sn` as a predictive feature. It is only a sample identifier.
5. Preserve the original `sn` values exactly.
6. Do not omit or duplicate samples.
7. Do not search the internet or use external datasets.
8. Predict each sample independently.
9. Return positive numerical MIC predictions.
10. Do not fabricate missing input features.

## Inference-time measurement

Use an external timer if available.

- Record the start timestamp immediately before beginning predictions.
- Record the end timestamp after all predictions are completed.
- Report total elapsed time in seconds.
- Report the number of samples.
- Calculate average elapsed time per sample.

Do not invent or estimate inference time. If you cannot measure it reliably, explicitly state that.

## Output

Generate and provide a downloadable CSV file named:

`ChatGPT_MIC_Predictions.csv`

The CSV must contain exactly these columns:

- sn
- predicted_mic

## Final validation

Before exporting:

- Verify that the output contains exactly as many rows as the input.
- Verify that every `sn` appears exactly once.
- Verify that all predictions are numeric and positive.
- Confirm that the actual MIC values were not used during prediction.

Do not merely display a table in the conversation. Generate the actual CSV file.
