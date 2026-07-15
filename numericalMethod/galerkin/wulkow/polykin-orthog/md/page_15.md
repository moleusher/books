By definition, one knows that

 $$ b_{k k}\neq0\qquad,\qquad k=0,1,\dots. $$ 

Upon inserting (2.20) and (2.7) into the definition (1.13), one obtains

 $$ \mu_{k}(t)=\langle s^{k},P_{s}(t)\rangle=\sum_{m=0}^{k}b_{k m}\sum_{r=0}^{\infty}a_{r}(t)(l_{m},l_{r})=\sum_{m=0}^{k}b_{k m}a_{m}(t)\gamma_{m}\;. $$ 

This leads to an infinite-dimensional recursive linear system of the form

 $$ \begin{aligned}&\begin{aligned}\\ &\mu_{0}&=b_{00}\gamma_{0}a_{0}\\&\mu_{1}&=b_{10}\gamma_{0}a_{0}+b_{11}\gamma_{1}a_{1}\\&\vdots\\ &\end{aligned}\\ \end{aligned} $$ 

Because of

 $$ b_{k k}\;\gamma_{k}\;\neq\;0\;, $$ 

the generalized moments $a_0$, $a_1$, ... can be recursively computed from the statistical moments $\mu_0$, $\mu_1$, ... This fact nicely reflects the basic structure of the Stieltjes problem already mentioned in Section 1.2. If the infinite sequence $\{u_k\}$ is bounded and given, then the infinite sequence $\{a_k\}$ can be obtained, which, in turn, defines the polymer distribution $P_s(t)$ via the representation (2.7) — for any choice of weight function $\Psi$ subject to the condition (2.6). If, however, only a finite number $N$ of statistical moments is given, then only $N$ generalized moments are determined — which, in turn, define associated Galerkin approximations $P_s^{(N)}$. However, variation of the weight function may produce a possibly rather wide variation of $P_s^{(N)}$ — this fact is illustrated in Section 5 below.

Summarizing, the mere computation of just a few statistical moments will only be useful in special situations such as:

(a) investigations concerning physical properties that only depend on, say,  $ \mu_{0} $,  $ \mu_{1} $, or  $ \mu_{2} $,

(b) comparisons with experimental data, which anyway arise in the form of statistical moments,

(c) estimation of relaxation times — as in [12].

Even in these cases, the statistical moment treatment appears to be unsatisfactory, if one of the following situations occurs:

(a) fractional powers of s arise in the reaction rate coefficients (compare (1.8))—here approximation techniques of unclear domain of applicability are in common use [11, 13],