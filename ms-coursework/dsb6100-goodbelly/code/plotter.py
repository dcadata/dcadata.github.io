"""DSB 6100 Marketing Analytics - Goodbelly Case Assignment"""

### DRAW 3D PLOTS! ###

### IMPORTS ###

# Import relevant project variables - details on each variable included in respective modules
from goodbelly.dataset import df_log as df
from goodbelly.variables import explanatory_model
from goodbelly.model_functions import summary2df, get_coefficients, get_coefficient
# Import pandas, the module that handles dataframes
import pandas as pd
# Import statistics modules for explanatory modeling
import statsmodels.formula.api as smf
# Import numpy functions for array handling
from numpy import arange, meshgrid
# Import modules for 3D plotting
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Import tool to get combinations of IVs from list
from itertools import combinations

### PLOTTING ###

# Select IVs to include in the 3D plot
ALL_Xs = ['demo', 'sales_rep', 'endcap', 'arp']
Ylabel = 'sales_volume'

# We are limited to 2 IVs in a 3D plot, so choose 2.
for Xs in list(combinations(ALL_Xs, 2)):

    # Create labels
    X1label, X2label = Xs

    # Create dataframes with Xs and Y data
    X1data = df[X1label]
    X2data = df[X2label]
    Ydata = df[Ylabel]

    # Create model to plot
    formula = '{} ~ {} * {}'.format(Ylabel, X1label, X2label)
    _, summary = explanatory_model(smf, df, formula)

    # Get coefficients from model
    dfc = get_coefficients(summary2df(pd, summary)[2])
    B0 = get_coefficient(dfc, 'Intercept')
    B1 = get_coefficient(dfc, X1label)
    B2 = get_coefficient(dfc, X2label)

    # Get min and max for plot mesh dimensions
    Xmax = max(X1data.max(), X2data.max())
    Xmin = min(X1data.min(), X2data.min())
    # Create plot mesh
    X1surf = X2surf = arange(Xmin, Xmax, (Xmax - Xmin)/20)
    X1surf, X2surf = meshgrid(X1surf, X2surf)
    # Create Y surface for plotting
    Ysurf = B0 + B1*X1surf + B2*X2surf

    # Set up 3D grid for both plots - surface and scatter
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Surface plot of regression equation
    ax.plot_surface(X1surf, X2surf, Ysurf, rstride=1, cstride=1, alpha=0.5, cmap='coolwarm')
    # Scatter plot of points
    ax.scatter(X1data, X2data, Ydata, c='g', marker='o', alpha=0.5)
    # Set labels and title of plot
    ax.set_xlabel('log ' + X1label)
    ax.set_ylabel('log ' + X2label)
    ax.set_zlabel('log ' + Ylabel)
    plt.title('{} & {} vs. {}'.format(X1label, X2label, Ylabel).upper())
    # Adjust plot's layout
    fig.tight_layout()
    # Show plot
    plt.show()