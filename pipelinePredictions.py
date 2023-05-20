import pandas as pd
import pickle

# Load the fitted pipeline from the file
with open('fitted_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Load the data to be predicted from the CSV file
data = pd.read_csv('./Abandono_teste.csv', delimiter=';')

# Extract the features from the data
X = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)  # Exclude unused columns

# Make predictions using the fitted pipeline
predictions = pipeline.predict(X)

# Create a new DataFrame with the row numbers (starting from 1) and predicted values
output_data = pd.DataFrame({'rowNumber': range(1, X.shape[0] + 1), 'predictedValues': predictions})

# Save the predictions to a CSV file
output_data.to_csv('predictions.csv', index=False)
