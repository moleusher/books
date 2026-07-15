a while. Even though in some cases  $ P_s(t) $ cannot be represented well by a series (1.22) for a (short) time with  $ \Psi $ the geometric distribution, it turns out that the information contained in the expansion coefficients is sufficient (or not necessary) to ensure good approximations for  $ t \gg 1 $.

As a consequence we make the demand:

- Find weight functions  $ \Psi $ which allow the treatment of processes containing different types of basic probability distributions.

Further we note, that there are models in polymer chemistry as well as in smog simulation or in statistics with reaction coefficients (transfer probabilities) depending on the present sequence index s itself. It seems very difficult (or impossible) to find a weight function and associated polynomials with appropriate properties for a sufficient general case. For special heterogeneous reactions an attempt has been made in [52], but there analytical properties of the orthogonal polynomials have been used again. Therefore our second requirement is:

• Give an algorithm which allows a numerical preprocessing of a CODE.

However, there are at least two things which seem to prevent such a numerical preprocessing: First, the numerical evaluation of scalar products as needed in (1.24) requires the time consuming summation over a very large or infinite domain. Secondly, even if we can compute a numerical approximation of the right-hand side of the ODE for the expansion coefficients, a sophisticated ODE solver will become inefficient or will fail, since it will detect a defect of smoothness. Besides that, a method of lines has the disadvantage of not looking at the problem in the ‘right’ space, but only in an  $ \mathbb{R}^n $-setting (even if an Hilbert space error-norm and special scalings are used).

The above considerations have entered the following rough outline of the algorithm to be developed herein.

Outline of the algorithm. Consider a (linear) CODE as an ordinary differential equation in a special Hilbert space:

 $$ u^{\prime}(t)=A u(t),u(0)given. $$ 

Discretizing this equation at time t with e.g. the implicit Euler scheme with step size  $ \tau $ leads to a countable system of algebraic equations (CAE)

 $$ \left(I-\tau A\right)u_{\tau}(t+\tau)=u(t), $$ 

with  $ u_{\tau}(t+\tau) $ the Euler approximation at time  $ t+\tau $ and  $ u(t) $ given. In order to apply extrapolation in time, we need an asymptotic expansion of the implicit