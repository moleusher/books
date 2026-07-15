### 1.3 THEORY OF COUNTABLE SYSTEMS

Results about existence and uniqueness of solutions of countable systems of ordinary differential equations have been derived by several authors, an extensive survey can be found in the monograph [12] by DEIMLING. He uses a classification of the problem (1.1) into  $ (s = 1, 2, \ldots) $:

(i) lower diagonal systems:  $ f_{s}(t, u_{1}(t), \ldots) = f_{s}(t, u_{1}(t), \ldots, u_{s}(t)) $,

(ii) row-finite systems:  $ f_{s}(t, u_{1}(t), \ldots) = f_{s}(t, u_{1}(t), \ldots, u_{\kappa(s)}(t)) $,  $ \kappa(s) < \infty $,

(iii) general systems,

and proves results by means of extensions of ODE techniques (Lipschitz conditions, fixed point iterations). In Section 3.1 we will introduce another classification in the context of the spaces  $ H_{\rho,\alpha} $. Most results in [12] are valid for the classical sequence spaces  $ l^p $,  $ 1 \leq p \leq \infty $. Linear problems are often considered in terms of infinite matrices and conditions on the matrix entries are derived. This ‘matrix point of view’ (which is also an ‘ODE view’) has also been used by other authors, e.g. SHAW [50] for  $ l^1 $ and BELLMANN [6] for  $ l^p $ spaces. MCLURE/WONG [40] could weaken the conditions for solutions in  $ l^1 $ by means of semigroup theory. In [43] solutions of general degradation processes (see Examples 1.2 and 5.3) are obtained by putting strong conditions on the matrix entries. Many further references can be found in [12]. This work will take a different view. The approach suggested herein is motivated by the (expected) qualitative behavior of the solutions. The attention is directed to the (efficient) approximation of solutions of given problems and the spaces  $ H_{\rho,\alpha} $ seem to be promising for this task. In view of the considerations in Section 1.1, we study CODE’s only in these spaces as operator equations.

It will turn out, that the operators studied in this work are Lipschitz continuous as operators on a fixed  $ H_{p,\alpha} $ - space or on the scale of these spaces. For the bounded case we can state the well known result:

THEOREM 1.8. For  $ 0 \leq t \leq T_f $ let  $ A(t) $ be a bounded linear operator on  $ H_{\rho,\alpha} $. Let the function  $ t \to A(t) $ be continuous in the uniform operator topology and  $ h(t) $ an continuous  $ H_{\rho,\alpha} $-valued  $ L^1 $-function. Then for every  $ \varphi \in H_{\rho,\alpha} $ the initial value problem

 $$ u^{\prime}(t)=A(t)u(t)+h(t),u(0)=\varphi, $$ 

has a unique solution u in  $ H_{\rho,\alpha} $ for  $ t \in [0, T_{f}] $.