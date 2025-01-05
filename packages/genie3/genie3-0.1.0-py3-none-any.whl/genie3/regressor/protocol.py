from typing import Any, Dict, Protocol

from numpy.typing import NDArray


class RegressorProtocol(Protocol):
    def fit(
        self, X: NDArray, y: NDArray, **fit_kwargs: Dict[str, Any]
    ) -> Any: ...

    @property
    def feature_importances(self) -> NDArray:
        if not hasattr(self, "_feature_importances"):
            raise ValueError(
                "Model has not been fitted yet. Therefore, no feature importances available."
            )
        return self._feature_importances

    @feature_importances.setter
    def feature_importances(self, value: NDArray) -> None:
        self._feature_importances = value
