"""Module for fitting data in a pandas DataFrame to a given model."""

import inspect
from dataclasses import dataclass
from typing import Dict, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


class ColumnNotFoundError(Exception):
    def __init__(self, column):
        self.column = column
        self.message = f"Column '{column}' not found in DataFrame."


@dataclass
class Parameter:
    """Data class for a parameter and its bounds."""

    value: float = 1
    fixed: bool = False
    min: float = -np.inf
    max: float = np.inf
    err: float = 0

    def __post_init__(self):
        if self.min > self.max:
            raise ValueError("Minimum value must be less than maximum value.")

        if self.min > self.value or self.value > self.max:
            raise ValueError("Value must be within the bounds.")

        if self.err < 0:
            raise ValueError("Error must be non-negative.")

        if self.fixed:
            self.min = self.value - np.finfo(float).eps
            self.max = self.value + np.finfo(float).eps

    def __call__(self) -> float:
        return self.value

    def __repr__(self):
        if self.fixed:
            return f"(value={self.value:.10f}, fixed=True)"
        return f"(value={self.value} ± {self.err}, bounds=({self.min}, {self.max}))"

    def random(self) -> float:
        """Returns a valid random value within the bounds."""
        param = np.random.normal(self.value, min(self.err, 1))
        return np.clip(param, self.min, self.max)


@dataclass
class Model:
    """Data class for a model function and its parameters."""

    func: callable
    params: dict[str:Parameter] | None = None
    pnames: list[str] | None = None
    residuals: np.ndarray | None = None
    𝜒2: float | None = None
    r𝜒2: float | None = None

    def __post_init__(self, params=None):
        """Generate a list of parameters from the function signature."""
        if self.params is None:
            self.params = {}
        input_params = self.params.copy()
        self.params = {}
        for i, name in enumerate(inspect.signature(self.func).parameters):
            if i == 0:
                continue
            self.params[name] = (
                Parameter()
                if name not in input_params
                else Parameter(**input_params[name])
            )

    def __call__(self, x) -> tuple[np.ndarray, np.ndarray, np.ndarray] | np.ndarray:
        """Evaluate the model at the given x values."""
        nominal = self.func(x, **self.kwargs())
        return nominal

    def __repr__(self):
        name = self.func.__name__
        params = "\n".join([f"{v} : {param}" for v, param in self.params.items()])
        return f"{name}:\n𝜒2: {self.𝜒2}\nreduced 𝜒2: {self.r𝜒2}\n{params}"

    def __getitem__(self, key) -> Parameter:
        return self.params[key]

    def __setitem__(self, key, value: tuple[float, float]):
        self.params[key].value = value[0]
        self.params[key].err = value[1]

    def __iter__(self) -> tuple[str, Parameter]:
        yield from [(n, val) for n, val in self.params.items()]

    def values(self) -> list[float]:
        """Yield the model parameters as a list."""
        return [param.value for _, param in iter(self)]

    def bounds(self) -> tuple[list[float], list[float]]:
        """Yield the model parameter bounds as a tuple of lists."""
        return (
            [param.min for _, param in iter(self)],
            [param.max for _, param in iter(self)],
        )

    def kwargs(self) -> dict:
        """Return the model parameters as a dictionary."""
        return {k: v.value for k, v in self.params.items()}

    def random(self, x):
        """Returns a valid random value within the bounds."""
        params = np.array([param.random() for param in self.params.values()])
        return self.func(x, *params)


@pd.api.extensions.register_dataframe_accessor("fit")
class FitAccessor:
    """Fitting accessor for pandas DataFrames."""

    def __init__(self, df):
        self._df = df

    def __call__(
        self,
        model: callable,
        x: str,
        y: str,
        yerr: str | None = None,
        plot: bool = True,
        plot_kwargs: dict = {"data_kwargs": {}, "model_kwargs": {}},
        **parameters: dict[str, Parameter],
    ) -> Model | tuple[Model, plt.Axes | None]:
        model = self.fit(model, x, y, yerr, **parameters)
        if plot:
            ax = plt.gca()
            self.plot(x, y, model, yerr, ax, **plot_kwargs)
            plt.show()
            return model, ax
        return model, None

    def fit(
        self,
        model: callable,
        x: str,
        y: str,
        yerr: str | None = None,
        **parameters: dict[str, Parameter],
    ):
        """Fit the data in the DataFrame to the given model.

        Parameters
        ----------
        model : Model
            The model to fit the data to.
        x : str
            The column name of the independent variable.
        y : str
            The column name of the dependent variable.
        **kwargs
            Additional keyword arguments to pass to `curve_fit`.

        Returns
        -------
        Model
            The fitted model.
        """
        if x not in self._df.columns:
            raise ColumnNotFoundError(x)

        if y not in self._df.columns:
            raise ColumnNotFoundError(y)

        if yerr is not None and yerr not in self._df.columns:
            raise ColumnNotFoundError(yerr)

        xdata = self._df[x].values
        ydata = self._df[y].values
        yerr = self._df[yerr].values if yerr is not None else [1] * len(xdata)

        data_model = Model(model, parameters)
        p0 = data_model.values()
        bounds = data_model.bounds()
        print(p0, bounds)

        popt, pcov, infodict, _, _ = curve_fit(
            data_model.func,
            xdata,
            ydata,
            p0=p0,
            sigma=yerr,
            bounds=bounds,
            absolute_sigma=True,
            full_output=True,
        )

        for i, (name, _) in enumerate(data_model):
            data_model[name] = popt[i], np.sqrt(pcov[i, i])

        data_model.residuals = infodict["fvec"]
        data_model.𝜒2 = np.sum(data_model.residuals**2)
        dof = len(xdata) - len(popt)
        data_model.r𝜒2 = data_model.𝜒2 / dof

        return data_model

    def plot(
        self,
        x: str,
        y: str,
        model: Model,
        yerr: str = None,
        ax=None,
        data_kwargs: Optional[Dict] = None,
        model_kwargs: Optional[Dict] = None,
    ):
        """Plot the data and the model on the given axis.

        Parameters
        ----------
        x : str
            The column name of the independent variable.
        y : str
            The column name of the dependent variable.
        model : Model
            The model to plot.
        ax : matplotlib.axes.Axes
            The axis to plot on.
        **kwargs
            Additional keyword arguments to pass to `plot`.

        Returns
        -------
        matplotlib.axes.Axes
            The axis with the plot.
        """
        if data_kwargs is None:
            data_kwargs = {}
        if model_kwargs is None:
            model_kwargs = {}

        if ax is None:
            ax = plt.gca()

        if x not in self._df.columns:
            raise ColumnNotFoundError(x)

        if y not in self._df.columns:
            raise ColumnNotFoundError(y)

        if yerr is not None and yerr not in self._df.columns:
            raise ColumnNotFoundError(yerr)

        # Extract data
        xdata = self._df[x].values
        ydata = self._df[y].values
        yerr_values = self._df[yerr].values if yerr is not None else None

        ax.errorbar(
            xdata, ydata, yerr=yerr_values, fmt=".", color="C0", label=y, **data_kwargs
        )
        nominal = model(xdata)

        ax.plot(xdata, nominal, color="C1", label="Model", **model_kwargs)
        #  add residuals plotted on new axis below
        ax_res = ax.inset_axes([0, -0.2, 1, 0.2])
        ax_res.plot(xdata, model.residuals, linestyle="", marker=".", color="C2")
        ax_res.axhline(0, color="grey", linewidth=plt.rcParams["lines.linewidth"])

        # Labels and legend
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.legend()
        return ax
