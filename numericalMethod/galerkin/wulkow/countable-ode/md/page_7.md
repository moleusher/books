## 1 Countable Systems of Ordinary Differential Equations

Following the notation of DEIMLING [12] essentially, this work will be concerned with scalar initial value problems of the type (CODE)

 $$ u_{s}^{\prime}(t)=f_{s}(t,u_{1}(t),u_{2}(t),\dots),u_{s}(0)=\varphi_{s},s\in\mathbb{N}(s\geq1), $$ 

where the functions

 $$ f_{s}:[0,T_{f}]\times D\to\mathbb{R}~,~D\subset\mathbb{R}^{\mathbb{N}}~,~s\in\mathbb{N}~, $$ 

and the initial value

 $$ \varphi=(\varphi_{s})\in\mathbb{R}^{\mathbb{N}}, $$ 

are given. The actual sequence space will be specified later on. The prime denotes the derivative with respect to the time t. The ‘space’ variable, i.e. the index of the sequence, will usually be called s in this work, in imitation of the notations used in applications. For ease of writing we will alternate between the notations  $ u_s(t) $ and  $ u(s,t) $ for the s-component of the sequence (grid function) u at time t. As far as the context is clear, the time-dependence will be omitted, such that  $ u(s) $ or  $ u_s $ means  $ u(s,t) $.

 $$ u:[0,T]\to D\quad,\quad T\in(0,T_{f}]\quad, $$ 

is called a solution of (1.1), if  $ u_s(0) = \varphi_s $,  $ u_s \in C^1((0,T]) $ and  $ u'_s = f_s(t,u) $ in  $ [0,T] $ for each  $ s \in \mathbb{N} $. In connection with time discretization and extrapolation in Hilbert spaces, we will mainly feature the linear case

 $$ u^{\prime}(t)=A(t)u(t)+h(t),u(0)=\varphi,t\in(0,T_{f}], $$ 

with A a linear operator on certain sequence spaces and h a sequence-valued  $ L^{1} $ - function. Problem (1.2) is a (linear) evolution problem. The existence and uniqueness theory will be given for the general nonlinear case.

Before we will be engaged in the theory of such problems, we will discuss some examples first, which will draw our attention to typical difficulties occurring with CODE's, showing that CODE's are not just ODE's.

### 1.1 INTRODUCTORY CONSIDERATIONS

This section serves as a motivation of the theory developed in the following parts of Chapter 1. Thus some details of the presentation will be specified in later sections. We study first typical examples of countable systems of ordinary differential equations.