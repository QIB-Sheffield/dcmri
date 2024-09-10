import matplotlib.pyplot as plt
import numpy as np
import dcmri as dc
#
# Create an array of time points over 30 minutes
#
t = np.arange(0, 30*60, 0.1)
#
# Generate the rat input function for these time points:
#
cp = dc.aif_tristan_rat(t)
#
# Plot the result:
#
plt.plot(t/60, 1000*cp, 'r-')
plt.title('TRISTAN rat AIF')
plt.xlabel('Time (min)')
plt.ylabel('Plasma concentration (mM)')
plt.show()
