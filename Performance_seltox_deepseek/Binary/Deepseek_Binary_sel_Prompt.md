# Nanomaterial Binary Classification and Prediction Task

I have uploaded 3 Excel files containing nanomaterial samples and their
corresponding binary target labels.

Your task is to train your understanding using `X_train_sel` and
`y_train_binary_sel`, then predict the binary class for **every** sample
in `X_test_sel`.

## Classification Requirements

1.  Perform binary classification for each sample.
2.  Use `X_train_sel` as the training input features.
3.  Use `y_train_binary_sel` as the training target.
4.  Predict labels for `X_test_sel`.
5.  The target represents:
    -   `1`: MIC \< 64 µg/mL
    -   `0`: MIC ≥ 64 µg/mL
6.  Use only the input features available in the training and test
    datasets.
7.  Do not use the actual MIC target column, even if it exists in any
    uploaded file.
8.  Do not use `sn` as a predictive feature. It is only a sample
    identifier.
9.  Preserve the original `sn` values exactly.
10. Do not omit or duplicate samples.
11. Do not search the internet or use external datasets.
12. Predict each sample independently.
13. Do not fabricate missing input features.
14. Return only binary predictions (`0` or `1`).

## Inference-Time Measurement

Use an external timer if available.

-   Record the start timestamp immediately before beginning predictions.
-   Record the end timestamp after all predictions are completed.
-   Report total elapsed time in seconds.
-   Report the number of test samples.
-   Calculate average elapsed time per sample.

Do not invent or estimate inference time. If you cannot measure it
reliably, explicitly state that.

## Output

Generate and provide a downloadable CSV file named:

`DeepSeek_Binary_Predictions.csv`

The CSV must contain exactly these columns:

-   `sn`
-   `predicted_class`

Where:

-   `predicted_class = 1` means MIC \< 64 µg/mL.
-   `predicted_class = 0` means MIC ≥ 64 µg/mL.

## Final Validation

Before exporting:

-   Verify that the output contains exactly as many rows as
    `X_test_sel`.
-   Verify that every `sn` appears exactly once.
-   Verify that all predictions are valid binary labels (`0` or `1`).
-   Confirm that the actual MIC values were not used during prediction.
-   Confirm that `sn` was excluded from the predictive features.
-   Confirm that the model learned exclusively from `X_train_sel` and
    `y_train_binary_sel`.

Do not merely display a table in the conversation. Generate the actual
CSV file.
