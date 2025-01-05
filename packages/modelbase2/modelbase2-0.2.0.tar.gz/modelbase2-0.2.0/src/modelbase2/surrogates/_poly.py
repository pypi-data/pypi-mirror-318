from collections.abc import Iterable
from dataclasses import dataclass

import numpy as np
import pandas as pd
from numpy.polynomial.polynomial import Polynomial

from modelbase2.types import AbstractSurrogate, ArrayLike

__all__ = ["PolySurrogate", "train_polynomial_surrogate"]


@dataclass(kw_only=True)
class PolySurrogate(AbstractSurrogate):
    model: Polynomial

    def predict_raw(self, y: np.ndarray) -> np.ndarray:
        return self.model(y)


def train_polynomial_surrogate(
    feature: ArrayLike,
    target: ArrayLike,
    degrees: Iterable[int] = (1, 2, 3, 4, 5, 6, 7),
    surrogate_args: list[str] | None = None,
    surrogate_stoichiometries: dict[str, dict[str, float]] | None = None,
) -> tuple[PolySurrogate, pd.DataFrame]:
    """Train a polynomial surrogate model.

    Args:
        feature: Input data as a numpy array.
        target: Output data as a numpy array.
        degrees: Degrees of the polynomial to fit to the data.
        surrogate_args: Additional arguments for the surrogate model.
        surrogate_stoichiometries: Stoichiometries for the surrogate model.

    Returns:
        PolySurrogate: Polynomial surrogate model.

    """
    feature = np.array(feature, dtype=float)
    target = np.array(target, dtype=float)

    models = [Polynomial.fit(feature, target, degree) for degree in degrees]
    predictions = np.array([model(feature) for model in models], dtype=float)
    errors = np.sqrt(np.mean(np.square(predictions - target.reshape(1, -1)), axis=1))
    log_likelihood = -0.5 * np.sum(
        np.square(predictions - target.reshape(1, -1)), axis=1
    )
    score = 2 * np.array(degrees) - 2 * log_likelihood

    # Choose the model with the lowest AIC
    model = models[np.argmin(score)]
    return (
        PolySurrogate(
            model=model,
            args=surrogate_args if surrogate_args is not None else [],
            stoichiometries=surrogate_stoichiometries
            if surrogate_stoichiometries is not None
            else {},
        ),
        pd.DataFrame(
            {"models": models, "error": errors, "score": score},
            index=pd.Index(np.array(degrees), name="degree"),
        ),
    )
