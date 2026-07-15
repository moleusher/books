However, the first term of  $ A_{D} $ leads to difficulties. In order to analyze the situation (let  $ \alpha = 0 $) we define an operator  $ A_{1} $ by

 $$ (A_{1}\;u)_{s}:=-(s-1)\;u_{s}\;,\;s\in\mathbb{N}. $$ 

 $ A_{1} $ is not bounded in  $ H_{\rho} $, but we can derive that

 $$ \left\|A_{1}u\right\|_{\rho}\leq\frac{C}{\epsilon}\left\|u\right\|_{\rho-\varepsilon},\epsilon>0, $$ 

i.e.  $ A_{1} $ is Lipschitz continuous as a map from the ‘smaller’ space  $ H_{\rho-\varepsilon} $ to the ‘larger’ space  $ H_{\rho} $. The solution of

 $$ u^{\prime}(t)=A_{1}u(t),u(0)\in H_{\rho-\varepsilon}, $$ 

is seen to be

 $$ u_{s}(t)=u_{s}(0)e^{-(s-1)t},~s\in\mathbb{N}~, $$ 

and  $ u(t) \in H_\rho $ for all  $ t > 0 $. An explanation of this behavior can be gained by use of semigroup theory (compare the remark to Corollary 1.12), but a more appropriate description in the present context seems to be Theorem 1.9, which is based on Lipschitz conditions of the form (1.45). Assertion and proof of this result follow Theorem 15.7 in the textbook of DEIMLING [13] and have been converted from certain weighted  $ l^1 $ – spaces to the  $ H_{\rho,\alpha} $ – spaces considered here. Additionally, a parameter  $ \gamma $ has been introduced, which allows the treatment of more general problems than in [13] ( $ \gamma = 1 $). For example, the convolution operator  $ A_c $ (1.14) requires  $ \gamma = 1/2 $ (Example 1.7), whereas  $ \gamma = 1 $ in (1.45). Theorem 1.9 supplies existence and uniqueness of solutions of nonlinear ODE's in  $ H_\rho $ (for simplicity the  $ \alpha $ – scale is omitted again and we write  $ \|\cdot\|_p $ instead of  $ \|\cdot\|_{\rho,\alpha} $).

THEOREM 1.9. Consider a sub-scale of  $ H_\rho $ - spaces for  $ \rho \in [\rho_0, 1) $,  $ 0 < \rho_0 < 1 $. Let  $ J = [0, T_f] \subset \mathbb{R} $ and assume:

(a) The operator

(1.47)

 $$ F:J\times H_{\rho}\longrightarrow H_{\bar{\rho}} $$ 

is continuous for  $ \bar{\rho} > \rho $ and  $ F(t,0) \in H_{\rho_0} $ on  $ J $.

(b) There exists a constant M such that

 $$ \begin{array}{r}{||F(t,u)-F(t,v)||_{\bar{\rho}}\leq\frac{M}{(\bar{\rho}-\rho)^{\gamma}}||u-v||_{\rho}\;,\;0<\gamma\leq1\;,}\end{array} $$ 

for  $ t \in J $,  $ \bar{\rho} > \rho $ and  $ u, v \in H_{\rho} $.