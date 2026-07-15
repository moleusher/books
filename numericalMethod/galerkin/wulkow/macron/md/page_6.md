## 1 NUMERICAL CONCEPTS

The numerical heart of MACRON is the discrete Galerkin method. Details and examples of this approach can be found in [8], [2] or [13] and will not be repeated here. Only the following items will be sketched below:

- Galerkin approximation

– Analytical preprocessing

- Moving weight function

- Error estimation

which are all related to the discrete Galerkin method itself. Further, some partly new

– Numerical devices

will be mentioned.

Galerkin approximation. Let  $ u_s(t) $ be the concentration of a molecule of chain length (degree, index)  $ s $ at time  $ t $. The sequence  $ u_1(t) $,  $ u_2(t) $, ..., can be considered as a chain length distribution (CLD). This CLD is approximated by a truncated expansion  $ u_s^n(t) $ of certain orthogonal polynomials of a discrete variable  $ l_j(s; \rho) $ multiplied by a parameter dependent weight function  $ \Psi_\rho(s) $:

 $$ u_{s}^{n}(t)=\Psi_{\rho}(s)\sum_{j=0}^{n}a_{j}(t)l_{j}(s;\rho)~. $$ 

Note, that this is a global representation, i.e. the range of s is not restricted. In the present version of MACRON the weight function  $ \Psi_{\rho} $ is set to be the Schulz-Flory distribution

 $$ \Psi_{\rho}(s)=\left(1-\rho\right)\rho^{s-1}\;,\;0<\rho<1\;. $$ 

The associated polynomials are the discrete Laguerre polynomials. Obviously we are interested in obtaining good approximations for small truncation index n. This depends in a crucial way on the parameter  $ \rho $. Hence, an adaptive procedure, referred to as moving weight function concept, is introduced in [8]. Based on this idea, in MACRON a single-step parameter selection can be performed. In this case, after each time step a possibly new value of the parameter is adapted. (For an alternative see the Appendix)