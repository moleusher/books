We suppose that at t = 0 there are N molecules of C and no molecules of A or B such that the initial distribution is given by

 $$ \begin{array}{l l l}{P(0,x_{1},x_{2})}&{=}&{\left\{\begin{array}{l l}{1}&{\mathrm{i f~}x_{1}=x_{2}=0,}\\ {0}&{\mathrm{e l s e.}}\end{array}\right.}\\ \end{array} $$ 

It is easy to see that in the limit  $ t \longrightarrow 0 $ all molecules of C disappear and that the exchange between A and B reaches an equilibrium. In the special case

 $$ c_{1}=\cdots=c_{5}=1, $$ 

it can be shown that the stationary distribution is the uniform distribution on the line  $ \left\{(x_1, x_2) \in \mathbf{N}^2 : x_1 + x_2 = N\right\} $, i.e.

 $$ \bar{P}(x_{1},x_{2})=\lim_{t\to\infty}P(t,x_{1},x_{2})=\left\{\begin{array}{cc}1/(N+1)&if x_{1}+x_{2}=N,\\0&else.\end{array}\right. $$ 

This distribution is the worst case for any tensor product ansatz, because an exact representation of  $ \bar{P} $ requires  $ N+1 $ basis functions although  $ \bar{P} $ contains only  $ N+1 $ nonzero elements. Moreover, all nonzero elements have the same value such that any truncation produces the same error.

Figure 7 (upper panel) shows the result for N=100 at t=5 computed with TOL = 0.02. At that time, the distribution is nearly reduced to the line  $ x_{1} + x_{2} = N $, and obviously this leads to difficulties regarding the domain decomposition into reactangles, cf. the lower panel of Figure 7. About 2500 variables are necessary to compute the solution. In comparison to the maximum number of about 10000, this is not a convincing reduction, and for smaller N, the reduction is even less efficient. However, if we do not try to approximate the final end of the process, but stop a bit earlier, the pay-off can be drastically. Figure 8 shows the solution at t=4, but with N increased to N = 10000. To obtain a tolerance of TOL = 0.05 on the state space with  $ 10000 \times 10000 $ states, only about 2600 variables are required, which corresponds to a reduction of 0.999974%! A 3d-plot shot from the top (cf. the lower panel in Figure 8) shows how narrow even then the front already is.

## Conclusion

We present an adaptive discrete Galerkin method for use in the chemical master equation (CME). In one state space dimension, such methods have