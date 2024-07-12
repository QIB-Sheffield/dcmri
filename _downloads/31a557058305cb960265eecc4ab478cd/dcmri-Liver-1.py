import matplotlib.pyplot as plt
import dcmri as dc
#
# Use `fake_tissue` to generate synthetic test data:
#
time, aif, roi, gt = dc.fake_tissue(CNR=100, agent='gadoxetate', R10=1/dc.T1(3.0,'liver'))
#
# Build a tissue model and set the constants to match the experimental conditions of the synthetic test data:
#
model = dc.Liver(
    aif = aif,
    dt = time[1],
    Hct = 0.45,
    agent = 'gadoxetate',
    TR = 0.005,
    FA = 20,
    n0 = 10,
)
#
# Train the model on the ROI data:
#
model.train(time, roi)
#
# Plot the reconstructed signals (left) and concentrations (right) and compare the concentrations against the noise-free ground truth:
#
model.plot(time, roi, testdata=gt)
