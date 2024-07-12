import dcmri as dc
#
# Use the AortaLiver model to fit the **tristan1scan** data:
#
data = dc.fetch('tristan1scan')
#
# Fit the baseline visit for the first subject:
#
data_subj = data['baseline']['001']
model = dc.AortaLiver(**data_subj['params'])
model.train(data_subj['xdata'], data_subj['ydata'], xtol=1e-3)
#
# Plot the results to check that the model has fitted the data:
#
model.plot(data_subj['xdata'], data_subj['ydata'])
