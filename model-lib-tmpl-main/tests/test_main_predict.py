"""Arquivo de teste de predict."""
# from model_xpto.main import predict  # noqa: ERA001
import random

import model_xpto.main
import numpy as np


def test_predict__42()->None:
    """Este teste valida retorno = 42."""
    x = np.linspace(0,10,100)
    index = random.randint(1,100)  # noqa: S311
    y_hipotetic = x[index]*2 + 1

    assert abs(model_xpto.main.predict(x) - y_hipotetic) < 1  # noqa: PLR2004, RUF100
