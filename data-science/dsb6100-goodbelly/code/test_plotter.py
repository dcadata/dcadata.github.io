"""DSB 6100 Marketing Analytics - Goodbelly Case Assignment"""

### PLOT THE PREDICTED VS. ACTUAL TO CHECK FIT ###

### IMPORTS ###

# Import relevant project variables - details on each variable included in respective modules
from goodbelly.dataset import df, df_log
from goodbelly.variables import explanatory_model
from goodbelly.model_functions import condensed_summary
# Import pandas, the module that handles dataframes
import pandas as pd
# Import statistics modules for explanatory modeling
import statsmodels.formula.api as smf
# Import numpy and matplotlib to set up plots
from numpy import ravel
import matplotlib.pyplot as plt

### MODEL ###

# Explanatory model - OLS model with intercept
# Do both standard and log transformed to see which works better.

big3 = ['demo', 'sales_rep', 'endcap'] # These are the 3 main IVs we're using in stage1.

formula = 'sales_volume ~ ' + ' * '.join(big3) # This is the R-style formula
model, summary = explanatory_model(smf, df, formula)

### PLOT ###

# Plot the predictions vs. actuals to check fit

predictions = model.predict()
Yactuals = ravel(df.sales_volume)

plt.scatter(predictions, Yactuals) #you can see the curvature still present in this plot, showing that the true relationship is probably nonlinear
plt.show()