"""Arquivo de teste de predict."""

import model_xpto.main
import numpy as np
from sklearn.metrics import accuracy_score
import time
import pytest

@pytest.mark.repeat(5) 
def test_predict_gt_70()->None:
    """Este teste valida retorno >=70%."""
    y_pred=model_xpto.main.predict(model_xpto.main.model, model_xpto.main.x_test)
    assert accuracy_score(model_xpto.main.y_test,y_pred) >= 0.7  # noqa: PLR2004, RUF100

    time.sleep(3)
