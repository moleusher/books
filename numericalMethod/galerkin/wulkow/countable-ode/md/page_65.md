## 5 NUMERICAL EXAMPLES

In this chapter some numerical results are presented featuring the following items:

• Adaptivity of the parameters  $ \rho $,  $ \alpha $

• Adaptivity of the the truncation index n

• Treatment of general problems and control of the truncation error

• Numerical preprocessing using the adaptive multilevel algorithm SUMMATOR

• Treatment of non-linear problems by means of the semi-implicit Euler discretization

All examples are excerpts from real life problems, in particular from polymer chemistry. All computations have been performed on a SPARC–station 1+ using double precision. The computing times (CPU) are given in seconds.

Example 5.1: Backward difference equation. The equation

 $$ u^{\prime}(t)=-\nabla u(t)\;,\;u(0)=\varphi $$ 

appears as a basic step in many applications in chemistry and is called chain addition process or propagation process there. It can also be considered as a stochastic process (e.g. random walk). As the operator  $ \nabla $ is bounded in  $ H_{\rho,\alpha} $ (compare Example 1.6 (i)), the problem is solved by use of the explicit Euler scheme.

The projections  $ \mathcal{P}_n^{\rho,\alpha} $ can be performed in every time step (with variable truncation index  $ n $) using (3.14).

The process is started with the geometric distribution  $ \varphi = \Psi_{\rho,0} $,  $ \rho_0 $ given. The choice  $ \rho_0 = 0.3 $ is made here to illustrate the parameter control of the algorithm. From (1.5) the solution  $ u(t) $ is expected to be similar to a Poisson distribution with parameter  $ \lambda = t $. As the weight function  $ \Psi_{\rho,\alpha} $ tends to such a Poisson distribution for  $ \rho \to 0 $ and  $ \alpha = t/\rho $ (Section 3.2), we can expect to obtain Galerkin approximations in spaces  $ H_{\rho,\alpha} $ with  $ \rho \ll \rho_0 $ and  $ \alpha $ large. The algorithm has to transfer the initial geometric distribution to the (moving) Poisson distribution.

The system has been integrated up to $T = 50$ sec. It turns out, that the parameter $\rho$ decreases to $\rho(T) = 3.6 \cdot 10^{-3}$, whereas the parameter $\alpha$ increases from zero to $\alpha(T) = 13844.4 - \text{this is presented in Figure 1.1 (logarithmic scale).}$ Note that $\rho(T)\alpha(T) \approx T$ as predicted in Section 3.2.