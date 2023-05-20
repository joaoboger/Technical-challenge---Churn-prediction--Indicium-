# Churn Prediction Project

This repository contains code and files related to the churn prediction project for a financial institution.

## Notebooks

The `notebooks` directory contains Jupyter notebooks for exploratory data analysis (EDA) and machine learning model development.

- [churn_eda_ml.ipynb](notebooks/churn_eda_ml.ipynb): Notebook for EDA and ML model development.

## Pipeline

The `pipeline` directory contains scripts and files related to the churn prediction pipeline.

- [churn_pipeline.py](pipeline/churn_pipeline.py): Python script for running the churn prediction pipeline and making predictions on new data.

## Dataset

The `data` directory stores the dataset used for churn prediction.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/joaoboger/TechnicalChallenge-ChurnPrediction
```

2. Prepare the input data:
   - Rename the desired data file to be predicted as `Abandono_teste.csv`.
   - Move the `Abandono_teste.csv` file to the `data` directory within the repository.

3. Run the churn prediction pipeline:
   - Open a terminal or command prompt and navigate to the root directory of the cloned repository.
   - Execute the following command to run the `churn_pipeline.py` script:

```bash
python pipeline/churn_pipeline.py
```

4. Check the output predictions:
   - After running the script, the predicted churn results will be generated.
   - Locate the output predictions file named `predictions.csv`.
   - Find the `predictions.csv` file in the `output` directory within the repository.
   - The file will have two columns: the first column represents the row numbers, and the second column contains the predicted churn values.
