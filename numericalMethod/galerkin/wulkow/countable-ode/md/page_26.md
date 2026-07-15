THEOREM 1.10. (HAIRER/LUBICH) Given a (possibly) nonlinear CODE

 $$ u^{\prime}(t)=A(t)u(t),u(0)=\varphi, $$ 

with A Lipschitz continuous on H and unique solution in H. The implicit (explicit) Euler approximation converges for all  $ \varphi \in H $ to this solution and the global error of the discretization has an asymptotic expansion

 $$ u_{\tau}(t)-u(t)=e_{1}(t)\tau+\ldots+e_{N}(t)\tau^{N}+E_{N+1}(t;\tau)\tau^{N+1}. $$ 

The  $ e_j(t) $ are solutions of certain linear, inhomogeneous differential equations, the remainder  $ E_{N+1}(t;\tau) $ is bounded on compact sets.

Proof. Because of the boundedness (Lipschitz continuity) of A, we repeat the arguments from ODE theory. By Taylor expansion we conclude that the Euler schemes are consistent with order one. The consistency of the Euler schemes implies the convergence of the schemes analogue e.g to the proof of Theorem 7.3 in [27]. Then the asymptotic expansions follow from [26], Theorem 1.

Things are more difficult for unbounded operators. Assume the explicit Euler scheme applied to a linear equation with operator A, which is bounded in the  $ \rho $-scale. For ODE's the order of consistency p is given by

 $$ u(t+\tau)-u(t)-\tau A u(t)=\mathcal{O}(\tau^{p+1})\;. $$ 

The question is, in what sense we can speak of consistency now. Let $\rho$ be given and $u(0) \in H_{\rho_0}$, $\rho_0 < \rho$. Assuming the validity of a Lipschitz condition (1.48), we know from Theorem 1.9 that (1.58) is defined in $H_\rho$ for $t$ small enough, leading to $p = 1$ for the explicit Euler scheme. Even the expression $u_n(t)$ from (1.55) is defined in $H_\rho$ by stepping in $n$ spaces between $H_{\rho_0}$ and $H_\rho$. But an estimation which allows the limit $n \to \infty$ is not possible here, because the insertion of infinite many spaces between $H_{\rho_0}$ and $H_\rho$ leads to unbounded Lipschitz constants. As mentioned in Remark (iii) to Theorem 1.9, the same reason prevents the proof of a stability result, which possibly could be applied to prove convergence of consistent discretization schemes as in standard ODE theory. As a consequence we can use the explicit Euler scheme only for the bounded case.

The examination of the implicit Euler discretization requires assumptions which can be naturally formulated in terms of semigroup theory. We only study linear (homogeneous) problems in detail. Nonlinear equations will be attacked by a semi-implicit discretization (see Chapter 4.1, (6.1)), which is the implicit Euler scheme in the linear case, of course.