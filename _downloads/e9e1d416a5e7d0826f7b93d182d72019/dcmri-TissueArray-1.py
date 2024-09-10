import dcmri as dc
#
# Use `fake_brain` to generate synthetic test data:
#
n=8
time, signal, aif, gt = dc.fake_brain(n)
#
# Build a tissue array model and set the constants to match the experimental conditions of the synthetic test data:
#
shape = (n,n)
model = dc.TissueArray(
    shape = shape,
    aif = aif,
    dt = time[1],
    agent = 'gadodiamide',
    TR = 0.005,
    FA = np.full(shape, 20),
    R10 = 1/gt['T1'],
    n0 = 15,
    kinetics = '2CX',
)
#
# Train the model on the ROI data:
#
model.train(time, signal)
#
# Plot the reconstructed maps, along with their standard deviations and the ground truth for reference:
#
model.plot(time, signal, ref=gt)
#
# As the left panel shows, the measured signals are accurately reconstructed by the model. However, while these simulated data are noise-free, they are temporally undersampled (dt = 1.5 sec). As a result the reconstruction of the parameter maps (right panel) is not perfect - as can be seen by comparison against the ground truth, or, in the absence of a ground truth, by inspecting the standard deviations. PS for instance is showing some areas where the value is overestimated and the standard deviations large.
