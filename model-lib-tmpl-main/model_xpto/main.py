"""Implementation of the XPTO model."""

# import cython as cy  # noqa: ERA001
import numpy as np
from sklearn.linear_model import LinearRegression

model=LinearRegression(fit_intercept=True)

# def predict(data: pd.DataFrame) -> cy.float:
def predict(xfit):  # noqa: ANN001, ANN201, D417
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

    return model.predict(xfit[:, np.newaxis])



# def train(data: pd.DataFrame) -> any:
def train (x,y):  # noqa: ANN001, ANN201, D417
    """Train the model using the given data.

    Args:
    ----
        data (Pandas DataFrame): The input data.

    Returns:
    -------
        Any: The trained model.

    """
    # TODO (@someone): Implement the training logic.

    model.fit(x[:,np.newaxis], y)

    # return {'model': 'xpto'}  # noqa: ERA001
    return model



np.random.seed(0)  # noqa: NPY002
n=20   # Number of data points
x=np.linspace(0, 10, n)
y=x*2 + 1 + 1*np.random.Generator(n) # Standard deviation 1
model = train(x,y)



