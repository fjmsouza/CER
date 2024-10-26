"""Implementation of the XPTO model."""

# import cython as cy  # noqa: ERA001
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


def train (x_train,y_train):  # noqa: ANN001, ANN201, D417
    """Train the model using the given data.

    Args:
    ----
        data (Pandas DataFrame): The input data.

    Returns:
    -------
        Any: The trained model.

    """
    # TODO (@someone): Implement the training logic.

    model= SVC(gamma='auto', random_state=1)

    model.fit(x_train,y_train.to_numpy().ravel())

    return model

def predict(model, x_test):  # noqa: ANN001, ANN201, D417
    """Predict the output for the given data.

    Args:
    ----
        data (Pandas DataFrame): The input data.

    Returns:
    -------
        float (Cython Float): The predicted output.

    """
    # TODO (@someone): Implement the prediction logic.
    # return 42  # noqa: ERA001
    return model.predict(x_test)



diabetes = pd.read_csv('dataset/diabetes.csv')
inputs=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
output=['Outcome']

x=diabetes[inputs]
y=diabetes[output]

normalized=MinMaxScaler()
normalized_inputs=normalized.fit_transform(x)
x_train,x_test,y_train,y_test = train_test_split(normalized_inputs,y, test_size=0.2, random_state=42)
model = train(x_train,y_train)
