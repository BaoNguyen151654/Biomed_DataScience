# Nanomaterial Cell Viability Prediction Task

I have uploaded 3 Excel files containing samples of nanomaterials. Your
task is to predict the Cell Viability (%) for **every** sample in the
dataset. You need to learn from `X_train_cyto` and `y_train_cyto`, then
make predictions on `X_test_cyto`. \## Prediction Requirements 1.
Predict Cell Viability in percentage (%). 2. Use only the input features
available in the dataset. 3. Do not use the actual Cell Viability target
column, even if it exists in the file. 4. Do not use `sn` as a
predictive feature. It is only a sample identifier. 5. Preserve the
original `sn` values exactly. 6. Do not omit or duplicate samples. 7. Do
not search the internet or use external datasets. 8. Predict each sample
independently. 9. Return numerical Cell Viability predictions. 10. Do
not fabricate missing input features. 11. All predicted Cell Viability
values must be non-negative (≥ 0%). 12. Do not impose an upper limit of
100%, since Cell Viability may exceed 100% in experimental data. \##
Inference-Time Measurement Use an external timer if available. - Record
the start timestamp immediately before beginning predictions. - Record
the end timestamp after all predictions are completed. - Report total
elapsed time in seconds. - Report the number of samples. - Calculate
average elapsed time per sample. Do not invent or estimate inference
time. If you cannot measure it reliably, explicitly state that. \##
Output Generate and provide a downloadable CSV file named:
`Grok_Cytotox_Predictions.csv` The CSV must contain exactly these
columns: - `sn` - `predicted_cell_viability` \## Final Validation Before
exporting: - Verify that the output contains exactly as many rows as the
input. - Verify that every `sn` appears exactly once. - Verify that all
predictions are numeric. - Verify that all predictions are non-negative
(≥ 0%). - Allow predictions greater than 100%. - Confirm that the actual
Cell Viability values were not used during prediction. - Confirm that
`sn` was used only for sample identification and output alignment. -
Confirm that no samples were omitted or duplicated. Do not merely
display a table in the conversation. Generate the actual CSV file.
