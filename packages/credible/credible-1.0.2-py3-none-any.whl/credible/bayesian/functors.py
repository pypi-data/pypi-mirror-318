# SPDX-FileCopyrightText: Copyright © 2023 Idiap Research Institute <contact@idiap.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Functors with standard credible region parameterisation."""

import typing

import numpy
import numpy.typing

from ..utils import CIArrayFunctor, CIFunctor
from . import utils


def make_functor(fun, lambda_=1.0, coverage=0.95) -> CIFunctor:
    r"""Decorate a function to operate across the library, with scalar inputs.

    Parameters
    ----------
    fun
        Function to be decorated.
    lambda_
        The parameterisation of the Beta prior to consider. Use
        :math:`\lambda=1` for a flat prior.  Use :math:`\lambda=0.5` for
        Jeffrey's prior.  Changes in this value do not significantly affect the
        outcome, unless ``tp`` or ``fp`` are very small (close to 1).
    coverage
        A floating-point number between 0 and 1.0 indicating the coverage
        you're expecting.  A value of 0.95 will ensure 95% of the area under
        the probability density of the posterior is covered by the returned
        equal-tailed interval.

    Returns
    -------
        The decorated function.
    """

    def inner(s: int, f: int) -> tuple[float, float, float]:
        retval = fun(s, f, lambda_=lambda_, coverage=coverage)
        return retval[1:]

    return inner


def make_array_functor(fun, lambda_=1.0, coverage=0.95) -> CIArrayFunctor:
    r"""Decorate a function to operate across the library, with array inputs.

    Parameters
    ----------
    fun
        Function to be decorated.
    lambda_
        The parameterisation of the Beta prior to consider. Use
        :math:`\lambda=1` for a flat prior.  Use :math:`\lambda=0.5` for
        Jeffrey's prior.  Changes in this value do not significantly affect the
        outcome, unless ``tp`` or ``fp`` are very small (close to 1).
    coverage
        A floating-point number between 0 and 1.0 indicating the coverage
        you're expecting.  A value of 0.95 will ensure 95% of the area under
        the probability density of the posterior is covered by the returned
        equal-tailed interval.

    Returns
    -------
        The decorated function.
    """

    def inner(
        s: typing.Iterable[int], f: typing.Iterable[int]
    ) -> tuple[
        numpy.typing.NDArray[numpy.double],
        numpy.typing.NDArray[numpy.double],
        numpy.typing.NDArray[numpy.double],
    ]:
        retval = fun(s, f, lambda_=lambda_, coverage=coverage)
        return retval[1:]

    return inner


bayesian_flat: CIFunctor = make_functor(utils.beta)
bayesian_flat_array: CIArrayFunctor = make_array_functor(utils.beta_array)
bayesian_jeffreys: CIFunctor = make_functor(utils.beta, lambda_=0.5)
bayesian_jeffreys_array: CIArrayFunctor = make_array_functor(
    utils.beta_array, lambda_=0.5
)
