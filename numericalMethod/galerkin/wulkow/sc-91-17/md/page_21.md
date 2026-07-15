## 3 APPROXIMATION OF COUNTABLE SYSTEMS

The numerical treatment of countable systems with the algorithm CODEX consists of two main parts:

(i) the time discretization and step-size control in  $ H_{\rho,\alpha} $

(ii) the solver for stationary problems in  $ H_{\rho,\alpha} $

The countable system is discretized in time first (i). The arising stationary problem is then solved by a Galerkin method (ii) within an accuracy supplied by the step-size control. The results of (ii) are also used to obtain a time error estimate of the approximation after a time step (ii). Finally, the solution is transformed to a space  $ H_{\tilde{\rho},\tilde{\alpha}} $ in order to minimize the number of degrees of freedom of the approximation (i).

The above order of the discretizations – first in time, then in ‘space’ – is called Rothe’s method [37] and has been introduced by BORNEMANN [6] for the numerical solution of parabolic differential equations.

### 3.1 DISCRETIZATION IN TIME

We discuss, how and under which conditions a countable system can be discretized in time by a given scheme and consider first an abstract (linear) Cauchy problem in  $ H_{\rho,\alpha} $:

 $$ u^{\prime}(t)=A u(t)+f(t),u(0)\mathrm{g i v e n}. $$ 

THEOREM 3.1. (Hersh/Kato [27], Brenner/Thomee [9]) Let the operator A be the generator of a $C_0$-semigroup of contractions. For each A-acceptable rational approximation $r$ of $e^z$ of order $p$, there are constants $C$ and $\kappa$, such that

 $$ \|r^{n}(\tau A)v-e^{n\tau A}v\|\leq C t\tau^{p}\|A^{p+1}v\|,\quad{f o r~}t=n\tau,v\in D(A^{p+1}). $$ 

Proof. Theorem 3 in [9].

It remains to check here, when  $ v \in D(A^{p+1}) $ is valid for a given p.

COROLLARY 3.2. Let $A$ additionally satisfy the conditions of Theorem 1.7 in $H_{\rho,\alpha}$ and let $v \in H_{\rho-\varepsilon,\alpha}$. Then $v \in D(A^p)$ for all fixed $p \in \mathbb{N}$.