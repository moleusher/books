## 1 Countable Systems of Ordinary Differential Equations

### 1.1 MODEL PROBLEMS

We consider scalar initial value problems of the type (CODE)

 $$ u_{s}^{\prime}(t)=f_{s}(t,u_{1}(t),u_{2}(t),\dots),u_{s}(0)=\varphi_{s},s\in\mathbb{N}(s\geq1), $$ 

where the functions

 $$ f_{s}:[0,T_{f}]\times D\to\mathbb{R}\;,\;D\subset\mathbb{R}^{\mathbb{N}}\;,\;s\in\mathbb{N}\;, $$ 

and the initial value

 $$ \varphi=(\varphi_{s})\in\mathbb{R}^{\mathbb{N}}, $$ 

are given. The actual sequence space will be specified later on. The prime denotes the derivative with respect to the time t. The index of the sequence will usually be called s. For ease of writing we will alternate between the notations  $ u_s(t) $ and  $ u(s,t) $ for the s-component of the sequence (grid function) u at time t. As far as the context is clear the time dependence will be omitted, such that  $ u(s) $ or  $ u_s $ means  $ u(s,t) $.

 $$ u:[0,T]\to D\quad,\quad T\in(0,T_{f}]\quad, $$ 

is called a solution of (1.1), if  $ u_s(0) = \varphi_s $,  $ u_s \in C^1((0,T]) $ and  $ u_s' = f_s(t,u) $ in  $ [0,T] $ for each  $ s \in \mathbb{N} $.

Example 1.1: Backward difference equation. Consider the equation

 $$ u^{\prime}(t)=-\nabla u(t)\;,\;u(0)=\varphi\;, $$ 

where the backward difference operator  $ \nabla $ is defined by

 $$ (\nabla u)_{1}=u_{1}\;,\;(\nabla u)_{s}=u_{s}-u_{s-1}\;,\;s=2,3,\ldots. $$ 

Equation (1.2) appears as a basic module in many problems (e.g. as chain addition  $ P_{s} + M \rightarrow P_{s+1} $ in polymerization models). For an initial sequence  $ \varphi $ the solution of (1.2) can be written as

 $$ u_{s}(t)=(T(t)\varphi)(s) $$ 

in terms of a semigroup  $ T(t) $ given by

 $$ (T(t)\varphi)(s)=\epsilon^{-t}\sum_{r=1}^{s}\frac{t^{s-r}}{(s-r)!}\varphi(r)\;. $$ 