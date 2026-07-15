## Chapter 4

## Adaptive Rothe Method

The method of lines (MOL) approach to the discrete Galerkin method as described in the preceding section works efficiently in quite a number of realistic applications including those of industrial relevance [7]. Further studies on possible improvements of this variant have been made by Canu and Ray [8]. However, in view of its applicability to a larger class of practical problems, the MOL variant has nevertheless several disadvantages, the most important of which are:

● Choice of weight function. The MOL requires an a priori decision about the choice of  $ \Psi $, which in turn determines the choice of

the basis for the Galerkin approximation. Apart from the Schulz–Flory distribution, which generates the discrete Laguerre polynomials, the paper [13] also mentions the Poisson distribution, which generates the Charlier polynomials. A “wrong” choice of weight function may result in an undesirably large necessary truncation index n.

● Adaptive control of the truncation index. In the MOL approach the truncation error is only monitored rather than controlled. In fact, if the truncation error estimate indicates an untolerable error, then the whole run must be repeated with a larger truncation index to be chosen ad hoc.

In order to overcome these drawbacks, Wulkow [18, 19] presented a much improved variant of the discrete Galerkin method, which avoids the above difficulties.

First, he designed a two parameter weight function, which covers both the Schulz–Flory distribution and the Poisson distribution under its roof. It reads

 $$ \Psi_{\rho,\alpha}(s)=\left(1-\rho\right)^{1-\alpha}\binom{s-1+\alpha}{s-1}\rho^{s-1}\quad0<\rho<1\quad\alpha>-1\quad. $$ 

Such a weight function had been constructed earlier by Wulkow and Deuflhard in [20], but there for a different reason with  $ |\alpha| < 1 $ only. The associated polynomials are the so-called modified discrete Laguerre polynomials

 $$ l_{k}(s;\rho,\alpha)=\sum_{j=0}^{k}\rho^{k-j}(\rho-1)^{j}\binom{k-\alpha}{k-j}\binom{s-1}{j}\quad. $$ 