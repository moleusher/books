Then for the global error of the implicit Euler scheme the asymptotic expansion

 $$ u_{\tau}(t)-u(t)=e_{1}(t)\tau+\cdots+e_{N}(t)\tau^{N}+E_{N+1}(t;\tau)\tau^{N+1} $$ 

is valid in X. Furthermore the estimates

 $$ \begin{array}{l l l}{a)}&{\|e_{k}(t)\|\leq C t~,}&{1\leq k\leq N~,}\\ {b)}&{\|E_{N+1}(t;\tau)\|\leq C t}&{}\\ \end{array} $$ 

hold for every $t \in [0, T_f]$ , $\tau \in [0, \tau_0]$ . The constant $C$ depends only on $T_f$, $\tau_0$, $N$ and $\varphi$. For general $C_0$ semigroups there is an additional time-step bound $\tau < 1/\omega$.

Proof. See [7], Theorem 2.13.

In the present context, the important condition  $ \varphi \in D(A^{2N+2}) $ characterizing the consistency of initial data can be gained from

COROLLARY 1.14. Let $A$ be an operator satisfying the conditions of Theorem 1.9 in $H_{\rho,\alpha}$ and let $\varphi \in H_{\rho-\varepsilon,\alpha}$. Then $\varphi \in D(A^N)$ for all fixed $N \in \mathbb{N}$.

Proof. Define  $ \varepsilon_k := \varepsilon/k $,  $ 1 \leq k \leq N $. Then  $ A $ is bounded from  $ H_{\rho-\varepsilon_k, \alpha} $ to  $ H_{\rho-\varepsilon_{k+1}, \alpha} $.