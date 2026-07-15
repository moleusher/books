### 2. Discrete Galerkin Method

The method to be proposed herein aims at preserving the advantages of both the statistical moment treatment and the continuous Galerkin method (Section 1.2) and, at the same time, to avoid the intrinsic disadvantages of these approaches. Starting point is the fact that, after all, the polymer degree (or chain length) is a discrete variable.

### 2.1 Basic Approximation Scheme

The key to the construction of the basic scheme is the introduction of a discrete inner product

 $$ (f,g):=\sum_{s=1}^{\infty}f(s)g(s)\Psi(s) $$ 

where $f$, $g$ are grid functions defined only on the grid $\{1, 2, \ldots\}$ and $\Psi$ is a given weight function with

 $$ \Psi(s)>0\qquad s=1,2,\dots<\infty $$ 

which characterizes the inner product  $ \left(\cdot,\cdot\right) $. This inner product induces the norm

 $$ \parallel f\parallel_{\Psi}:=(f,\;f)^{1/2} $$ 

and an associated Hilbert space  $ H_{\Psi} $. In  $ H_{\Psi} $, there exists an orthogonal polynomial basis  $ \{l_{j}(s)\}\;j=0,\;1,\;\ldots $ satisfying

 $$ (l_{i},~l_{j})=\gamma_{j}\delta_{i j}~,\quad\gamma_{j}>0~,\quad i,j=0,1,2,\ldots $$ 

with  $ \delta_{ij} $ the Kronecker symbol. For ease of the subsequent presentation, the (Euclidean) inner product

 $$ \langle u,v\rangle:=\sum_{s=1}^{\infty}u(s)v(s)\;, $$ 

will also be used, where u, v are grid functions such that  $ \langle u, v \rangle $ is bounded. Assume that

 $$ \bar{P}_{s}(t):=\frac{P_{s}(t)}{\Psi(s)}\in H_{\Psi}. $$ 

Then there exists a unique representation

 $$ P_{s}(t)=\Psi(s)\sum_{k=0}^{\infty}\alpha_{k}(t)l_{k}(s)\;. $$ 