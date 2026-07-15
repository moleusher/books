Example 1.5. A degradation process in polymer chemistry (compare Example 4.2) can be written as  $ (s = 1, 2, \ldots) $

 $$ u^{\prime}(t)=A_{D}u(t):=-(s-1)u(s)+2\left(\sum_{r=1}^{\infty}\left(S_{+}\right)^{r}u\right)(s),u(0)=\varphi, $$ 

in terms of the forward shift operator

 $$ (S_{+}u)(s):=u(s+1)\enspace. $$ 

The operator  $ S_{+} $ is bounded in  $ H_{\rho,\alpha} $ with the norm

 $$ \|S_{+}\|_{\rho,\alpha}\leq M_{+}:=\left\{\begin{array}{l l}{\sqrt{\rho(1+\alpha/2)}}&{,\quad\alpha\geq0,}\\ {\sqrt{\rho}}&{,\quad-1<\alpha<0.}\end{array}\right. $$ 

Thus the infinite sum of operators on the right-hand side of (1.14) converges uniformly to a bounded operator for

 $$ \rho(1+\alpha/2)<1 $$ 

(a condition which plays a role in Example 4.2). However, the first term of  $ A_{D} $ leads to difficulties. Let  $ \alpha = 0 $ and define an operator  $ A_{1} $ by

 $$ (A_{1}\;u)_{s}:=-(s-1)\;u_{s}\;,\;s\in\mathbb{N}. $$ 

 $ A_{1} $ is not bounded in  $ H_{\rho,0} $, but a short calculation yields

 $$ \left\|A_{1}u\right\|_{\rho,0}\leq\frac{C}{\epsilon}\left\|u\right\|_{\rho-\varepsilon,0},\;\epsilon>0, $$ 

i.e.  $ A_1 $ is Lipschitz continuous as a map from the ‘smaller’ space  $ H_{\rho-\varepsilon,0} $ to the ‘larger’ space  $ H_{\rho,0} $. The estimate (1.17) is the motivation for the following theorem, which follows Theorem 15.7 in the textbook [14] and has been converted from certain weighted  $ l^1 $-spaces to the  $ H_{\rho,\alpha} $-spaces. Theorem 1.7 supplies existence and uniqueness of solutions of nonlinear ODEs in  $ H_{\rho,0} $ (for simplicity the  $ \alpha $-scale is omitted and we write  $ \|\cdot\|_\rho $ instead of  $ \|\cdot\|_{\rho,\alpha} $).

THEOREM 1.7. Consider a sub-scale of  $ H_\rho $ - spaces for  $ \rho \in [\rho_0, 1) $,  $ 0 < \rho_0 < 1 $. Let  $ J = [0, T_f] \subset \mathbb{R} $ and assume:

(a) The operator

 $$ F:J\times H_{\rho}\longrightarrow H_{\bar{\rho}} $$ 

is continuous for  $ \bar{\rho} > \rho $ and  $ F(t,0) \in H_{\rho_0} $ on  $ J $.