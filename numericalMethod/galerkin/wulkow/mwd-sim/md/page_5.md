applied to the converted discrete systems. However, the continuous equivalents to countable systems are partial integro-differential equations with convection and diffusion and for this class of problems (in particular when more than one polymer species has to be treated in a model) efficient and flexible numerical techniques are also missing (see the review article $ ^{15} $).

## Statistical methods

The statistical simulation of polyreaction kinetics has been tried for several years and is still quite popular. These methods are relatively flexible concerning the form of the arising distributions, but are rather time-consuming $ ^{3)} $, even if additional assumptions comparable to the QSSA are employed $ ^{16)} $. Moreover, there is no reliable error estimate controlling the truncation of the number of molecules or of the number of events. A recent thesis $ ^{17)} $ presents a comparison between Monte-Carlo-simulations and the Galerkin h-p-method for the polymer degradation of polylactid and it shows that the results are quite the same in this case, but the computing times differ by a factor of about 20.

## Approximations by means of moments

Actually, the method of moments is not an approach to compute distributions, but only describes certain aspects of distributions expressed in terms of the statistical moments  $ \mu_{k} $:

 $$ \mu_{k}(t)\left[P\right]:=\sum_{s=1}^{\infty}s^{k}P_{s}(t)\qquad k=0,1,\cdots $$ 

Nevertheless, the method of moments is the most popular approach and reflects some of the basic problems of polyreactions, e.g. analytical preprocessing, closing problem, method of lines (see below).

In general, the complete distribution can only be reconstructed by its moments, if all (infinite) moments are known. Otherwise, additional assumptions are required, which are usually based on the expected type of the molecular weight distribution. The choice of a basic distribution is the crucial point in such a method, of course. Thus, the moments are mainly used to compute the different mean values of a distribution. However, there are situations, where the method of moments can be a tool:

There is a theoretical evidence that the considered reaction scheme leads to a certain type of distribution. For example, a living polymerization leads to a Poisson distribution for long reaction times, in a radical polymerization the living polymer is close to a Schulz-Flory distribution over wide ranges of the process.

● There is practical experience (e.g. from measurements) that the solution is “close” to a chosen distribution function.

● An analysis of the mean values lets expect a distribution of a certain type.

If there are hints that some of the assumptions above are valid and if the moments of a given system can be computed (which is not always the case), only a few differential equations (sometimes numerically ill-conditioned) have to be solved.