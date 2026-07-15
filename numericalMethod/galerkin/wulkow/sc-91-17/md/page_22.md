Proof. Define  $ \varepsilon_k := \varepsilon/k $,  $ 1 \leq k \leq p $. Then  $ A $ is bounded from  $ H_{\rho-\varepsilon_k, \alpha} $ to  $ H_{\rho-\varepsilon_{k+1}, \alpha} $.

As noted in Section 1.2, the condition  $ v \in H_{\rho-\varepsilon,\alpha} $ is crucial for guaranteeing senseful numerical approximations anyway.

Discretization scheme for the linear case. Starting at time t, we use the implicit Euler scheme leading to an approximation  $ u^1 $ of  $ u(t + \tau) $. The task is then to get an estimation of the time error  $ \|u^1 - u(t + \tau)\| $ for predicting a new reasonable step-size  $ \bar{\tau} $. This is usually done by computing a ‘better’ approximation  $ u^2 $ and then taking the difference  $ \|u^2 - u^1\| $ as an estimate of the time error. However, in the case of partial differential equations or countable systems,  $ u^1 $ and  $ u^2 $ can only be approximated. It turned out [6], that their approximation error has to be comparatively small for not perturbing the time error estimation. In order to avoid this disadvantage, BORNEMANN developed a so-called multiplicative error correction scheme [7], which allows the direct estimation of the time error. The accuracy requirements for the  $ u^1 $ and  $ u^2 $ are then less restrictive than in the case described above. For linear problems (3.1) the discretization scheme looks as follows (for details see [7]):

Let  $ \varphi = \bar{u}(t) $ the exact solution of (3.1) at time  $ t $. In order to perform a time step  $ \tau $ we compute:

 $$ \begin{array}{rcl}u^{1}&=&(I-\tau A)^{-1}\left(\varphi+\tau f(t)\right)\quad(implicit Euler step),\\&\eta^{1}&=&\frac{1}{2}\tau(I-\tau A)^{-1}\left(A(\varphi-u^{1})-(f(\tau)-f(0))\right),\\&u^{2}&=&u^{1}+\eta^{1}\end{array} $$ 

The approximation $u^{2}$ is of order $p=2$ and the rational function of the scheme is A-acceptable. Note, that only one type of stationary subproblem has to be solved in a global time step (in contrary to the application of extrapolation ([6], [39]), where problems with different $\tau$ appear).

In [7] it is pointed out, that  $ u^{1} $ has to be computed with an accuracy

 $$ \mathrm{e p s}=\frac{1}{8}\mathrm{T O L}\quad, $$ 

TOL the required global tolerance for  $ u(t) $, to ensure the reliable working of the time step control.

Remark. Due to the multiplicative error correction this requirement is much weaker than in the case of extrapolation used in [6] and [39].