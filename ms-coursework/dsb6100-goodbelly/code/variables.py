"""DSB 6100 Marketing Analytics - Goodbelly Case Assignment"""

### DEFINE PROJECT VARIABLES AND FUNCTIONS FOR USE THROUGHOUT PROJECT ###

### PROJECT VARIABLES ###

# Project directory
directory = 'D:\\python\\goodbelly\\'

# Location of the file containing the provided GB dataset
dataset = directory + 'dataset.csv'

# Location of the results files
results_dir = directory + 'outputs\\'

### PROJECT FUNCTIONS ###

# Define function to return explanatory model
def explanatory_model(statsmodels_api, data, formula):
    """Function to return explanatory model"""
    model = statsmodels_api.ols(formula, data=data).fit()
    summary = model.summary()
    return model, summary