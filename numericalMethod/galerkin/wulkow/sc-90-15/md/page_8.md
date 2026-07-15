## 3 Discrete Galerkin Method II – CODEX

The concept of a method of lines realized in MACRON and the restricted choice of the weight function has some conceptual limitations :

– missing analytical properties (e.g. for reaction steps with chain length dependent rate coefficients) cannot be replaced by numerical approximations, because this induces perturbations on the right-hand side of the differential equations for the Galerkin coefficients  $ a_{k} $ and destroys the order- and time-step control of a numerical integration code.

- expensive approximation (i.e. large truncation index n in (4)) arises for processes with a solution ‘far’ from the Schulz-Flory distribution, i.e. for very peaked or very broad distributions.

The new approach to be presented here is based on two concepts, which are related to the above two points. In order to overcome the first difficulty we apply a so-called outer time discretization of a linear countable system:

 $$ u^{\prime}(t)=A u(t),u(0)=u_{0}, $$ 

with  $ u(t) = (u_1(t), u_2(t), \ldots) $ the distribution to be computed and A a very large, possibly infinite matrix, which is typically not sparse. The discretization of (5) at time t by means of the well-known implicit Euler scheme with step-size  $ \tau $ leads to a countable system of algebraic equations (CAE)

 $$ \left(I-\tau A\right)\tilde{u}(t+\tau)=u(t) $$ 

The solution  $ \hat{u}(t+\tau) $ of this (generally infinite) system is the approximation of the exact solution u at time  $ t+\tau $. If one can compute  $ \tilde{u}(t+\tau) $ exactly, then a time-control of the complete system (5) – as known in algorithms for the solution of ordinary differential equations – will be possible. Fortunately it turns out, that (6) needs to be solved only up to an accuracy TOL, which is prescribed by the outer time discretization. If this accuracy TOL is achieved, the order- and time-step control, even with extrapolation in time, is not affected. This strategy has been developed by BORNEMANN [2] for parabolic partial differential equations (PDE's) and applied to CODE's in [6]. As a consequence, the solution  $ \tilde{u}(t+\tau) $ in each time-step may be represented by an appropriate Galerkin approximation  $ \tilde{u}^* $. Note that the type of this approximation is open at this point. In the following one possible choice will be discussed.

The modified weight function

 $$ \Psi_{\rho,\alpha}(s)=\left(1-\rho\right)^{1+\alpha}\binom{s-1+\alpha}{s-1}\rho^{s-1}, $$ 