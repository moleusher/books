Proof. Theorem 5.1 and p. 129 in [44].

Examples 1.6. (i) Consider the backward difference operator (1.4). An easy computation shows that

 $$ \begin{array}{r l r l}{\|\nabla\|_{\rho,\alpha}}&{\leq}&{1+\frac{1}{\sqrt{\rho}}\;,\quad}&{\alpha\geq0\;,}\\ {\|\nabla\|_{\rho,\alpha}}&{\leq}&{1+\frac{1}{\sqrt{\rho(1+\alpha)}}\;,\quad&{-1<\alpha<0\;.}\end{array} $$ 

(ii) The norm of the forward difference operator  $ \Delta $ can be estimated by

using the norm  $ M_{+} $ of the forward shift operator

 $$ \left\|\Delta\right\|_{\rho,\alpha}\leq1+M_{+} $$ 

 $$ (S_{+}u)(s):=u(s+1) $$ 

given by

 $$ \|S_{+}\|_{\rho,\alpha}\leq M_{+}:=\left\{\begin{array}{l l}\sqrt{\rho(1+\alpha/2)}&,\quad\alpha\geq0,\\ \sqrt{\rho}&,\quad-1<\alpha<0.\end{array}\right. $$ 

(iii) A degradation process in polymer chemistry

 $$ u^{\prime}(t)=A_{D}u(t),u(0)=\varphi, $$ 

– similar to the summary system (1.7) in Example 1.2 – can be formulated in terms of the operator  $ A_{D} $:

 $$ \begin{array}{r c l}{(A_{D}\;u)_{s}}&{:=}&{-(s-1)\;u_{s}+2\displaystyle\sum_{r=1}^{\infty}u_{r}}\\ {}&{=}&{-(s-1)\;u_{s}+2\;\left(\displaystyle\sum_{r=1}^{\infty}(S_{+})^{r}\;u\right)_{s}.}\\ \end{array} $$ 

Using (1.41) the infinite sum of operators on the right-hand side of (1.42) converges uniformly for

 $$ \rho(1+\alpha/2)<1 $$ 

(a condition which will play an important role in Example 5.3):

 $$ \sum_{r=1}^{\infty}\left\|\left(S_{+}\right)^{r}\right\|_{\rho,\alpha}\leq\sum_{r=1}^{\infty}\left\|S_{+}\right\|_{\rho,\alpha}^{r}\leq\sum_{r=1}^{\infty}M_{+}^{r}<\infty. $$ 