"""Arquivo de teste de predict."""
from model_xpto.main import predict


def test_predict_eq_42()->None:
    """Este teste valida retorno = 42."""
    assert predict(None)==42  # noqa: PLR2004
