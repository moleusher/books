The following disadvantages argue against a computation of distributions from moments:

● Distributions obtained by the method of moments do not permit an estimation, whether an assumed basis distribution has been correctly selected. A parameterized basis function always looks very smooth — even if it is absolutely wrong.

● The method of moments can only be recommended, if the considered process is already well studied and thus no surprises are to be expected. However, this is just not the case for models to be developed.

● A distribution computed by moments contains the moment information only. Additional findings cannot be obtained.

● Sometimes the differential equations for the moments cannot be derived in a closed form $ ^{1)} $.

Summarizing, the method of moments is helpful to adjust parameters of a model and for a first overview, but is problematic for reaction schemes resulting in complicated distributions and for chain-length dependent reaction steps of any kind.

## The discrete weighted Galerkin method

The development of this method in ref. $ ^{8} $ was based on the following considerations

● the polymer degree s is a discrete variable,

● the chain length distributions in typical processes are looking like familiar probability distributions,

• degrees of freedom have to be reduced as far as possible,

● an error estimation is required.

Starting point is an expansion of a chain length distribution  $ P_{s} $ into certain orthogonal polynomials, which are constructed by means of a weight function:

 $$ P_{s}(t)=\psi(s;\rho)\sum_{k=0}^{\infty}a_{k}(t)l_{k}(s;\rho) $$ 

The weight function  $ \psi $, depending on one or more parameters  $ \rho $, is chosen to describe the solution  $ P_{s} $ as well as possible. Then a truncation of Eq. (5) at an index m leads to a Galerkin approximation

 $$ P_{s}^{m}(t)=\psi(s,\rho)\sum_{k=0}^{\infty}a_{k}(t)l_{k}(s,\rho) $$ 

which should be close to $P_s$ for small $m$ (small means here: <20–50). The expansion coefficients $a_k(t)$ (called generalized moments) are computed by means of differential equations, which are derived by use of analytical relations of the polynomials $l_k(s; \rho)$. Defining a weighted inner product

 $$ \left(f,g\right)_{\psi}:=\sum_{s=1}^{\infty}f(s)g\left(s\right)\psi\left(s\right)^{-1} $$ 

the related orthogonal polynomials fulfill