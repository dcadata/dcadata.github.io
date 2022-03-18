"""DSB 6100 Marketing Analytics - Goodbelly Case Assignment"""

### CREATE THE MODELS! ###

### IMPORTS ###

# Import relevant project variables - details on each variable included in respective modules
from goodbelly.dataset import df, df_log
from goodbelly.variables import results_dir, explanatory_model
from goodbelly.model_functions import condensed_summary
# Import pandas, the module that handles dataframes
import pandas as pd
# Import statistics modules for explanatory modeling
import statsmodels.formula.api as smf
# Import codecs module to save results to text file
import codecs

### CHECKS ###

# No scaling needed because all X/independent variables are already binary (0/1). Don't need to worry about shape of distribution or outliers.

# Check for potential balance issues in the dataset... Is the 1/1/1 "quadrant" too small?
# len(df[(df.sales_rep == 1) & (df.endcap == 1) & (df.demo == 1)])# = 165, so no - the dataset is relatively well balanced.

### MODEL ###

# Explanatory model - OLS model with intercept
# Do both standard and log transformed to see which works better.

# stage1-substage1 formulae generation list
big3 = ['demo', 'sales_rep', 'endcap'] # These are the 3 main IVs we're using in stage1.
s11 = [['endcap'], ['sales_rep'], ['demo'],
       ['demo', 'sales_rep'],
       big3]
# stage1-substage2 formulae generation list
s12 = [big3 + ['demo13'],
       big3 + ['demo45'],
       big3 + ['demo13', 'demo45'],
       big3 + ['natural'],
       big3 + ['fitness'],
       big3 + ['natural', 'fitness'],
       big3 + ['demo13', 'natural'],
       big3 + ['demo13', 'fitness'],
       big3 + ['demo13', 'natural', 'fitness']]
# stage2 formulae generation list
s2 = [big3 + ['arp'],
      big3 + ['arp', 'demo13'],
      big3 + ['arp', 'demo45'],
      big3 + ['arp', 'demo13', 'demo45'],
      big3 + ['arp', 'natural', 'fitness'],
      big3 + ['demo13', 'demo45', 'natural', 'fitness'],
      big3 + ['demo13', 'demo45', 'arp', 'natural', 'fitness']]

# Which stage to run for?
STAGE = s2

# Use for loop to run all the models for that stage in succession
for x_features in [' * '.join(s) for s in STAGE]:

    formula = 'sales_volume ~ ' + x_features # This is the R-style formula
    model, summary = explanatory_model(smf, df_log, formula)
    output, filename = condensed_summary(pd, formula, summary)
    # Output model details to text file for saving
    with codecs.open(results_dir + filename, 'w', encoding='utf-8') as f:
        f.write(output)
        f.close()


#########################################
#########################################


### NOTES FROM TESTING ###


### TEST WITH ML ###

# # Fit explanatory model using ML module sklearn (this is only to confirm the explanatory model above because this module isn't optimal for explanatory modeling)
# # Set up X and Y as numpy arrays
# X, Y = splitXY(df, x_cols)
# # Also do the log version so you can test both
# Xlog, Ylog = splitXY(df_log, x_cols)
# # Model
# model, score, intercept, coeffs = explanatory_model_ML(LinearRegression, X, Y)
# modellog, scorelog, interceptlog, coeffslog = explanatory_model_ML(LinearRegression, Xlog, Ylog)
# # Confirms same R2 in both standard and log transformed