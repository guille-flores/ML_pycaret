# PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows. \
# install with pip install pycaret

# We will use the `insurance` dataset in this example. It is a regression use-case for predicting medical charges based on age, sex, BMI, and region. 


from pycaret.datasets import get_data
from pycaret.regression import *

data = get_data("insurance")

# we get a list og people's age, sex, # children, if they smoke, region and the insurance charge (target/label).
# setup from pycaret help us prepare the data (remove outliers, fill missing or NULL values, etc)
s = setup(data, target = 'charges')


# Once the setup is finished, we can start model training and selection with just one line of code:
# `compare_models`. Through the use of cross-validation, this function trains and evaluates the model 
# performance of all estimators within the model library
best = compare_models() #this gives us a list of the best model (less error)
create_api (best, 'insurance_prediction_model')
