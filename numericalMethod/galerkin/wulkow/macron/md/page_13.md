to increase NPROJ by steps of about five using the error prediction formula described below.

Starting the simulation with an initial distribution. To start the simulation with an initial chain length distribution, the user has several possibilities. If there exists a (for example measured) distribution on a separate file, it can be related to a macromolecular species using the input block *GALERKIN PROJECTION. The program approximates the data by a polynomial expansion used as initial value of a simulation. The truncation index can be prescribed by the user, otherwise it will be chosen by the program. Moreover, some standard distributions can be defined. A skillful user may also enter initial values for every weight function parameter and the associated expansion coefficients separately.

Use of the Error Estimation. The most important tool to discuss the quality of a Galerkin approximation is the error estimate given at the end of each simulation. In the following, we point out some possibilities to work with this device. We use three simple but illustrative test examples and approximate only given distributions (as if they had been obtained by a simulation). Possible limitations and difficulties are emphasized. In ‘good’ examples, the approximation will often show a similar behavior to Test 1.

Theorem 2.14 in [13] implies, that under some assumptions the (relative) error  $ \tilde{\epsilon}_{n} $ of a Galerkin approximation  $ u_{s}^{n} $ behaves like

 $$ \bar{\epsilon}_{n}\approx C n^{\gamma} $$ 

where $C$ and $\gamma$ are at least locally independent of $n$. Assume now, that two expansions (of the same distribution) have the errors $\bar{\epsilon}_{n_{1}}$ and $\bar{\epsilon}_{n_{2}}$ with $n_{1} < n_{2}$. If the user is interested in reaching a given tolerance, a plausible prediction for $\bar{\epsilon}_{n_{3}} \quad (n_{3} > n_{2})$ is

 $$ \begin{array}{r}{\overline{{\epsilon}}_{n_{3}}\approx\left(\frac{\left(\overline{{\epsilon}}_{n_{2}}\right)^{n_{3}-n_{1}}}{\left(\overline{{\epsilon}}_{n_{1}}\right)^{n_{3}-n_{2}}}\right)^{1/\left(n_{2}-n_{1}\right)}\quad.}\end{array} $$ 

This can be verified by using the binomial theorem and by omitting  $ O(1/n) $ terms. For  $ n_{2}=n_{1}+1 $,  $ n_{3}=n_{2}+1 $ formula (2.3) reduces to

 $$ \bar{\epsilon}_{n+2}=\frac{\bar{\epsilon}_{n+1}^{2}}{\bar{\epsilon}_{n}}. $$ 

In practical examples, the true error  $ \epsilon_n $ of an approximation is not available, therefore it is replaced by a well-tried error estimate  $ \epsilon_n $.