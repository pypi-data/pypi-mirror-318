# SPDX-FileCopyrightText: Copyright © 2023 Idiap Research Institute <contact@idiap.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later
import credible.bayesian.utils
import numpy
from matplotlib import pyplot as plt

# system 1 performance
TP1 = 10
FN1 = 5
TN1 = 5
FP1 = 10

# system 2 performance
TP2 = 3
FN2 = 3
TN1 = 4
FP2 = 2

nb_samples = 100000  # Sample size, higher makes it more precise
lambda_ = 0.5  # use 1.0 for a flat prior, or 0.5 for Jeffrey's prior

# now we calculate what is the probability that system 2's recall
# measurement is better than system 1
rng = numpy.random.default_rng(42)
prob = credible.bayesian.utils.compare_f1_scores(
    TP2, FP2, FN2, TP1, FP1, FN1, lambda_, nb_samples, rng
)

# we then visualize the posteriors of the F1-score for both systems
# together with the probability that system 1 is better than system 2
pdf1 = credible.bayesian.utils.f1_posterior(
    TP1, FP1, FN1, lambda_, nb_samples, rng
)
pdf2 = credible.bayesian.utils.f1_posterior(
    TP2, FP2, FN2, lambda_, nb_samples, rng
)
h1 = plt.hist(
    pdf1, bins=200, alpha=0.3, label=f"TP1 = {TP1}, FP1 = {FP1}, FN1 = {FN1}"
)
plt.hist(pdf1, bins=200, color=h1[2][0].get_facecolor()[:3], histtype="step")
h2 = plt.hist(
    pdf2, bins=200, alpha=0.3, label=f"TP2 = {TP2}, FP1 = {FP1}, FN2 = {FN2}"
)
plt.hist(pdf2, bins=200, color=h2[2][0].get_facecolor()[:3], histtype="step")
plt.title(
    f"Posterior F1-Score - Monte Carlo - "
    f"($\\mathbb{{P}}(F1_2>F1_1)$: {(100*prob):.0f}%)"
)
plt.grid()
plt.legend()
plt.show()
