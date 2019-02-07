#%% [markdown]
## Homework 5
#%%
import numpy as np
import matplotlib.pyplot as plt

import os
import sys
# adding path of smithplot
sys.path.append(os.path.join(os.getcwd(),"smithplot"))
from smithplot import SmithAxes

fig = plt.figure()


# # Making some test data
# thetas = np.linspace(0,2*np.pi,100)
# S = 0.316*np.exp(1j*thetas)

#%% [markdown]
## Construcing the plot
# Now that we have our $R_{lo}$, we can find all of the impedances corresponding to the
# -2 dB contour by drawing the "football" corresponding to all impedances of 
# the form  $Z = R_{lo} + jX$ on the left and $ Y = \frac1{R_{lo}} + jB $ on the left (before they 
# intercept each other). 
# This can easily be done and then plotted once you have the two points where these lines intersect.

#%%
ax = plt.subplot(1,1,1,projection='smith')

R_lo = 40                                   # Lower resistance which gives the desired attenuation 
X = 10000                                   # Plotting a large sweep of these impedances
ctr_left = R + 1j*np.linspace(-X,X,100)     # Broadcasts to sweep
ctr_right = R_L_opt**2/ctr_left # flippy dippy

plt.plot(ctr_left,datatype=SmithAxes.Z_PARAMETER,markersize=0.2,color='r')
plt.plot(ctr_right,datatype=SmithAxes.Z_PARAMETER,markersize=0.2,color='b')
plt.show()


#%%
# Plot the Cripps contour for Z0 = R_L_opt Ω
R_L_opt = 100
Z0 = R_L_opt
ax = plt.subplot(1,1,1,projection='smith',axes_impedance=Z0)
R = 40 # Lower resistance which gives the desired attenuation, must be < Z0
X = np.sqrt(R_L_opt**2-R**2) # Result shown in previous cell
ctr_left = R + 1j*np.linspace(-X,X,100) # Broadcasts to sweep
ctr_right = R_L_opt**2/ctr_left # flippy dippy
ctr = np.concatenate((ctr_left,ctr_right))

plt.plot(ctr,datatype=SmithAxes.Z_PARAMETER,markersize=0.2,color='r')
plt.show()
#%%
# Plot the Cripps contour given a resistance for Z0 = 50 Ω
ax = plt.subplot(1,1,1,projection='smith',axes_impedance=50)

plt.plot(ctr,datatype=SmithAxes.Z_PARAMETER,markersize=0.2,color='r')
plt.show()
