Example 1.1: Backward difference equation. Consider the equation

 $$ u^{\prime}(t)=-\nabla u(t)\;,\;u(0)=\varphi\;, $$ 

given in some sequence space, where ∇ defined by

 $$ (\nabla u)_{s}=u_{s}-u_{s-1}\;,\;(\nabla u)_{1}=u_{1}\;, $$ 

denotes the backward difference operator. Equation (1.3) appears as a basic module in many problems. For an initial sequence  $ \varphi $ the solution of (1.3) can be written as

 $$ u_{s}(t)=(T(t)\varphi)(s) $$ 

in terms of a semigroup (compare Section 1.4)  $ T(t) $ given by

 $$ (T(t)\varphi)(s)=e^{-t}\sum_{r=1}^{s}\frac{t^{s-r}}{(s-r)!}\varphi(r)\;. $$ 

Specializing  $ \varphi_{s}=\delta_{s,1} $,  $ \delta_{s,r} $ the Kronecker symbol, for fixed t the solution  $ u(t) $ reduces to a Poisson distribution with parameter t:

 $$ u_{s}(t)=e^{-t}\frac{t^{s-1}}{(s-1)!}. $$ 

Thus in general  $ u(t) $ can be considered as a convolution of Poisson distributions. In [18] the problem (1.3) has been treated as a chain addition polymerization in a space essentially spanned by Charlier polynomials. These polynomials are orthogonal with respect to a scalar product induced by the Poisson distribution.

Example 1.2: Summatory systems. Equations of this type have been studied by HILLE [30] and can be regarded as special settings of mathematical models of polymer degradation processes [4], which have been solved numerically by use of the discrete Galerkin method in [18] and [52]. Let us consider the following special summary system

 $$ u_{s}^{\prime}(t)=-(s-1)u_{s}(t)+\sum_{r=s+1}^{\infty}u_{r}(t)\;,\;u_{s}(0)=\varphi_{s}\;,\;s\in\mathbb{N}\;. $$ 

Suppose that for a given initial value  $ \varphi \in l^1 $ the equation (1.7) has at least one solution  $ u(t) \in C^1((0,T], l^1) $, defined for positive values of  $ t $ such that  $ u_s(t) \to \varphi_s $ for  $ t \to 0 $. We define

 $$ v_{s}(t):=\sum_{r=s}^{\infty}u_{r}(t)~. $$ 