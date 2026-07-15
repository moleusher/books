## Chapter 3

## Method of Lines Approach

In this section we start from the mathematical model directly. Let  $ u_s(t) $ denote the concentration of macromolecules of chain length  $ s $ at time  $ t $. The sequence  $ u_1(t), u_2(t), \ldots $ can be written in short hand notation as distribution  $ u(t) = (u_s(t), s = 1, 2, \ldots) $. As illustrated above, the kinetics of a macromolecular reaction process can be represented by a countable system of ordinary differential equations (abbreviated as CODE) of the form

 $$ u_{s}^{\prime}(t)=(A u(t))_{s} $$ 

with given initial distribution  $ u_{s}(0) $. For simplicity, the linear special case is treated here with A denoting a linear, possibly unbounded operator. The changes to the general nonlinear case, which in fact is treated in the below mentioned software, are marginal. Starting point for the construction of the discrete Galerkin method in [13] was the introduction of a discrete inner product to take care of the discrete nature of the variable s. Formally, it can be written as

 $$ (f,g):=\sum_{s=1}^{\infty}f(s)g(s)\Psi(s) $$ 

where $f, g$ are functions of the discrete variable $s = 1, 2, \ldots$ and $\Psi$ is a given (positive) weight function. This product induces an associated norm

 $$ \left|\left|f\right|\right|:=(f,f)^{1/2} $$ 

and an associated orthogonal basis $\{l_j(s), j = 0, 1, 2, \ldots\}$ of polynomials of the discrete variable $s$ with

 $$ (l_{j},l_{k})=\gamma_{j}\delta_{j k}\qquad,\qquad\gamma_{j}>0\qquad j,k=0,1,2,\dots. $$ 

With these preparations a natural ansatz for the unknown distribution  $ u_{s}(t) $ will be

 $$ u_{s}(t)=\Psi(s)\sum_{k=0}^{\infty}a_{k}(t)l_{k}(s). $$ 

Truncation of this expansion after  $ n+1 $ terms leads to the Galerkin approximation

 $$ u_{s}^{(n)}(t):=\Psi(s)\sum_{k=0}^{n}a_{k}^{(n)}(t)l_{k}(s) $$ 

in terms of the truncation index n. Note that whenever the system has the already mentioned open loop property, then the upper index  $ (n) $ in the expansion coefficients  $ a_{k} $ cannot be ignored.