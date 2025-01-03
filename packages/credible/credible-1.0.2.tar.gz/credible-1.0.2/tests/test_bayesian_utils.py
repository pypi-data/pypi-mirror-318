# SPDX-FileCopyrightText: Copyright © 2023 Idiap Research Institute <contact@idiap.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import itertools

import credible.bayesian.utils
import numpy
import scipy.special
import scipy.stats


def test_bayesian_precision_comparison():
    # system 1 performance
    tp1 = 10
    # fn1 = 5
    # TN1 = 5
    fp1 = 10

    # system 2 performance
    tp2 = 3
    # fn2 = 3
    # TN1 = 4
    fp2 = 2

    nb_samples = 10000  # Sample size, higher makes it more precise
    lambda_ = 0.5  # use 1.0 for a flat prior, or 0.5 for Jeffrey's prior

    rng = numpy.random.default_rng(42)
    prob = credible.bayesian.utils.compare_beta_posteriors(
        tp2, fp2, tp1, fp1, lambda_, nb_samples, rng
    )

    assert numpy.allclose(prob, 0.6592)


def test_bayesian_recall_comparison():
    # system 1 performance
    tp1 = 10
    fn1 = 5
    # TN1 = 5
    # fp1 = 10

    # system 2 performance
    tp2 = 3
    fn2 = 3
    # TN1 = 4
    # fp2 = 2

    nb_samples = 10000  # Sample size, higher makes it more precise
    lambda_ = 0.5  # use 1.0 for a flat prior, or 0.5 for Jeffrey's prior

    # recall: TP / TP + FN, k=TP, l=FN

    # now we calculate what is the probability that system 2's recall
    # measurement is better than system 1
    rng = numpy.random.default_rng(42)
    prob = credible.bayesian.utils.compare_beta_posteriors(
        tp2, fn2, tp1, fn1, lambda_, nb_samples, rng
    )

    assert numpy.allclose(prob, 0.2376)


def test_bayesian_f1_comparison():
    # system 1 performance
    tp1 = 10
    fn1 = 5
    # TN1 = 5
    fp1 = 10

    # system 2 performance
    tp2 = 3
    fn2 = 3
    # TN1 = 4
    fp2 = 2

    nb_samples = 100000  # Sample size, higher makes it more precise
    lambda_ = 0.5  # use 1.0 for a flat prior, or 0.5 for Jeffrey's prior

    # now we calculate what is the probability that system 2's recall
    # measurement is better than system 1
    rng = numpy.random.default_rng(42)
    prob = credible.bayesian.utils.compare_f1_scores(
        tp2, fp2, fn2, tp1, fp1, fn1, lambda_, nb_samples, rng
    )

    assert numpy.allclose(prob, 0.42618)


def test_bayesian_system_comparison():
    rng = numpy.random.default_rng(1234)
    nb_samples = 50

    # expected output of the system
    labels = numpy.ones(nb_samples, dtype=bool)
    ratio = 0.2
    labels[: int(numpy.ceil(ratio * nb_samples))] = 0
    rng.shuffle(labels)

    # system1 has 10% error, so we flip its bits by that amount randomly
    flip_probability = rng.choice(
        [False, True], p=[0.9, 0.1], size=labels.shape
    )
    system1_output = numpy.logical_xor(labels, flip_probability)
    system1_acc = numpy.count_nonzero(
        ~numpy.logical_xor(system1_output, labels)
    ) / len(labels)

    # system2 has 20% error, so we flip its bits by that amount randomly
    flip_probability = rng.choice(
        [False, True], p=[0.85, 0.15], size=labels.shape
    )
    system2_output = numpy.logical_xor(labels, flip_probability)
    system2_acc = numpy.count_nonzero(
        ~numpy.logical_xor(system2_output, labels)
    ) / len(labels)

    assert numpy.allclose(system1_acc, 0.90)
    assert numpy.allclose(system2_acc, 0.84)

    # calculate when systems agree and disagree
    n1 = numpy.count_nonzero(
        (~numpy.logical_xor(system1_output, labels))  # correct for system 1
        & numpy.logical_xor(system2_output, labels)  # incorrect for system 2
    )
    n2 = numpy.count_nonzero(
        (~numpy.logical_xor(system2_output, labels))  # correct for system 2
        & numpy.logical_xor(system1_output, labels)  # incorrect for system 1
    )
    n3 = nb_samples - n1 - n2
    assert n1 == 8
    assert n2 == 5
    assert n3 == 37
    assert n1 + n2 + n3 == nb_samples
    prob = credible.bayesian.utils.compare_systems(
        [n1, n2, n3], [0.5, 0.5, 0.5], 1000000, rng
    )
    assert numpy.allclose(prob, 0.79668)


def test_beta_coverage():
    # tests if the returned value by beta() corresponds to the correct total
    # requested area using scipy.special.beatinc()

    a_list = [50, 10, 1000]
    b_list = [100, 5, 100]
    prior_list = [1.0, 0.5]
    coverage_list = [0.80, 0.90, 0.95]

    # just does a bunch of different combinatorics and check our implementation
    for a, b, prior, coverage in itertools.product(
        a_list, b_list, prior_list, coverage_list
    ):
        # print(a, b, prior, coverage)

        _, _, lower, upper = credible.bayesian.utils.beta(a, b, prior, coverage)

        # scipy.special.betainc should return a very similar result
        area_low = scipy.special.betainc(a + prior, b + prior, lower)
        area_high = scipy.special.betainc(a + prior, b + prior, upper)
        assert numpy.isclose(
            (area_low, area_high), ((1 - coverage) / 2, (1 + coverage) / 2)
        ).all()
