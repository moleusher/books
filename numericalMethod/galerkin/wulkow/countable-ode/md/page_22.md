Then for every  $ \rho \in (\rho_0, 1) $ the initial value problem

 $$ u^{\prime}(t)=F(t,u(t)),u(0)=\varphi\in H_{\rho_{0}}, $$ 

has a unique solution

 $$ u:[0,\delta(\bar{\rho}-\rho)^{\gamma})\longrightarrow H_{\rho_{0}}, $$ 

with $\delta = \min\{T_f, (Md_\gamma)^{-1}\}$. The constant $d_\gamma > 1$ can be computed in concrete cases, e.g. $d_1 = e$, $d_{1/2} = 2\sqrt{3}/3$.

Proof. The proof is based on a fixed point iteration in a scale of Hilbert spaces. We consider the successive approximation

 $$ u_{k}(t)=u_{0}+\int_{0}^{t}F(s,u_{k-1}(s))\mathrm{d}s,k\geq1,u_{0}=\varphi. $$ 

Due to the condition (a) and  $ \varphi \in H_{\rho_0} $, the iterate  $ u_k : J \to H_\rho $ is continuous for  $ \rho > \rho_0 $. We will show by induction, that

 $$ \|u_{k}(t)-u_{k-1}(t)\|_{\bar{\rho}}\leq C_{\rho_{0}}(t)\left(\frac{M t d_{\gamma}}{\left(\bar{\rho}-\rho_{0}\right)^{\gamma}}\right)^{k}\mathrm{f o r}\bar{\rho}>\rho_{0}, $$ 

where  $ C_{\rho_0}(t) := \|\varphi\|_{\rho_0} + \frac{(1 - \rho_0)}{M} \max_{s \in [0, t]} \|F(s, 0)\|_{\rho_0} $.

In a first step we get

 $$ \begin{array}{r c l}{\displaystyle\|u_{1}(t)-u_{0}\|_{\bar{\rho}}}&{\leq}&{\displaystyle\int_{0}^{t}\|F(s,u_{0})\|_{\bar{\rho}}\mathrm{d}s}\\ {}&{\leq}&{\displaystyle\frac{t M}{(\bar{\rho}-\rho_{0})^{\gamma}}C_{\rho_{0}}(t)\;,}\\ \end{array} $$ 

using  $ \|u\|_{\bar{\rho}} \leq \|u\|_{\rho_{0}} $ for  $ \rho_{0} \leq \bar{\rho} $. Now the induction step yields

 $$ \begin{align*}\|u_{k+1}(t)-u_{k}(t)\|_{\bar{\rho}}&\leq\quad\int_{0}^{t}\|F(s,u_{k}(s))-F(s,u_{k-1}(s))\|_{\bar{\rho}}\mathrm{d}s\\&\leq\quad\frac{M}{\varepsilon^{\gamma}}\int_{0}^{t}\|u_{k}(s)-u_{k-1}(s)\|_{\bar{\rho}-\varepsilon}\mathrm{d}s\\&\leq\quad\frac{M}{\varepsilon^{\gamma}}\int_{0}^{t}C_{\rho_{0}}(t)\frac{(s M d_{\gamma})^{k}}{(\bar{\rho}-\varepsilon-\rho_{0})^{k\gamma}}\mathrm{d}s\\&=\quad\frac{C_{\rho_{0}}(t)}{\varepsilon^{\gamma}}\frac{M^{k+1}t^{k+1}d_{\gamma}^{k}}{(\bar{\rho}-\varepsilon-\rho_{0})^{\gamma k}}\frac{1}{k+1},\end{align*} $$ 