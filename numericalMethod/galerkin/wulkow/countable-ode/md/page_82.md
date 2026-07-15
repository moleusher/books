As pointed out in the Chapters 3 and 5, the evaluation of scalar products in  $ H_{\rho,\alpha} $ sometimes has to be done numerically. The task is the computation of sums of the form

arising from the Galerkin method based on modified discrete Laguerre polynomials, or of sums

 $$ \sum_{s=1}^{s_{\max}}u_{s}l_{j}(s;\rho,\alpha) $$ 

in general for a given grid function  $ f(s) $,  $ s \in [s_{\min}, s_{\max}] $,  $ s \in \mathbb{N} $. In order to obtain an approximation of (6.2) a so-called SUMMATOR has been developed. The idea is the construction of a sequence of grids

 $$ \sum_{s=s_{\min}}^{s_{\max}}f(s) $$ 

 $$ \Delta^{0}\subset\Delta^{1}\subset\ldots\subset\Delta^{j}\subset\left[s_{\mathrm{m i n}}\;,\;s_{\mathrm{m a x}}\right]\;, $$ 

which should reflect the behavior of the grid function f. Therefore we need local summation formulas, a local error estimation and a refinement strategy. The algorithm might have applications apart from the context of this work.

Discrete Interpolation. Interpolation of a sequence (grid function)  $ f(s) $ only makes sense, if we assume an underlying smoothness of  $ f $. The error of polynomial interpolation for functions  $ f \in C^k[a,b] $ can be described by means of the  $ k $-th derivative of  $ f $. In the discrete case we have to replace the derivative by a finite difference. Thus the interpolation error will contain all values of a grid function  $ f(s) $. For a given subset

 $$ I:=\left\{s_{\mathrm{m i n}},s_{\mathrm{m i n}}+1,\ldots,s_{\mathrm{m a x}}\right\}\subset\mathbb{N} $$ 

let

 $$ \Delta:=\left\{s_{\min}=s_{0}<s_{1}<\cdots<s_{n}=s_{\max}\right\}\subset I $$ 

a sub-grid, where the discrete interpolation polynomial  $ D_n(s) = D_n^{s_0}, \ldots, s_n(s) $ of degree  $ n $ is defined by the conditions

 $$ D_{n}^{s_{0},\ldots,s_{n}}(s_{i})=f(s_{i}),\;s_{i}\in\Delta\;. $$ 

As in the continuous case  $ D^n(s) $ can be constructed by means of divided differences  $ f[s_i, \ldots, s_{i+k}] $ [51]. The polynomial  $ D_n(s) $ then reads

 $$ \begin{array}{r c l}{D_{n}^{s_{0},\ldots,s_{n}}(s)}&{=}&{\displaystyle\sum_{j=0}^{n}\omega_{j}(s)\;f[s_{0},\ldots,s_{j}]~,}\\ {\omega_{j}(s)}&{:=}&{\left(s-s_{0}\right)\cdot\ldots\cdot\left(s-s_{j-1}\right)~,}\\ \end{array} $$ 

for  $ s \in \Delta $.