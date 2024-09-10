import matplotlib.pyplot as plt
import numpy as np
import dcmri as dc
#
# Generate a population-average input function:
#
t = np.arange(0, 300, 1.5)
ca = dc.aif_parker(t, BAT=20)
#
# Define some tissue parameters:
#
Fp, vp, PS, ve = 0.01, 0.05, 0.005, 0.4
Ktrans = PS*Fp/(PS+Fp)
#
# Set up a plot to show concentrations:
#
fig, (ax0, ax1) = plt.subplots(1,2,figsize=(12,5))
#
# Generate plasma and extravascular tissue concentrations with the 2CX model and add to the plot:
#
C = dc.conc_tissue(ca, Fp, vp, PS, ve, t=t, sum=False, kinetics='2CX')
ax0.set_title('2-compartment exchange model')
ax0.plot(t/60, 1000*C[0,:], linestyle='--', linewidth=3.0, color='darkred', label='Plasma')
ax0.plot(t/60, 1000*C[1,:], linestyle='--', linewidth=3.0, color='darkblue', label='Extravascular, extracellular space')
ax0.plot(t/60, 1000*(C[0,:]+C[1,:]), linestyle='-', linewidth=3.0, color='grey', label='Tissue')
ax0.set_xlabel('Time (min)')
ax0.set_ylabel('Tissue concentration (mM)')
ax0.legend()
#
# Generate plasma and extravascular tissue concentrations with the WV model and add to the plot:
#
C = dc.conc_tissue(ca, Ktrans, ve, t=t, sum=False, kinetics='WV')
ax1.set_title('Weakly vascularised model')
ax1.plot(t/60, 1000*C[0,:], linestyle='--', linewidth=3.0, color='darkred', label='Plasma (WV)')
ax1.plot(t/60, 1000*C[1,:], linestyle='--', linewidth=3.0, color='darkblue', label='Extravascular, extracellular space (WV)')
ax1.plot(t/60, 1000*(C[0,:]+C[1,:]), linestyle='-', linewidth=3.0, color='grey', label='Tissue (WV)')
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Tissue concentration (mM)')
ax1.legend()
plt.show()
