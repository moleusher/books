Combination of (4.13) and (4.3) then leads to the differential equations  $ (j=2,3,\ldots) $:

 $$ \begin{array}{r c l}{{)}}&{{a_{0}^{\prime}}}&{{=}}&{{-\frac{k_{p}}{2}a_{0}^{2}}}\\ {{)}}&{{\cdot}}&{{}}&{{}}\\ {{)}}&{{\rho^{\prime}}}&{{=}}&{{\frac{k_{p}}{2}(1-\rho)a_{0}}}\\ {{}}&{{}}&{{}}&{{}}\\ {{}}&{{}}&{{a_{j}^{\prime}}}&{{=}}&{{\frac{k_{p}}{2}\left[\frac{j a_{0}}{\rho}(a_{j-1}-a_{j})+\displaystyle\sum_{m=1}^{j-1}a_{m}a_{j-m}-\frac{1}{\rho}\displaystyle\sum_{m=0}^{j-1}a_{m}a_{j-1-m}\right]}}\end{array} $$ 

For general initial values  $ N_{s}(0) $, the representations (4.2) and (2.8) are directly evaluated (compare [7, 8]). In [18], the degenerate case

 $$ N_{s}(0)=N_{10}\delta_{s,1} $$ 

has been prescribed. As in the preceding model problem, a singularity arises in (4.14.c), which can be removed by setting the initial values

 $$ a_{j}(0):=a_{j-1}(0)-\frac{1}{j a_{0}(0)}\sum_{m=0}^{j-1}a_{m}(0)a_{j-1-m}(0),\quad j=2,3,\ldots $$ 

With  $ a_{0}(0)=N_{10} $,  $ a_{1}(0)=0 $ repeated induction in (4.16) readily yields

 $$ a_{j}(0)=0\quad,\quad j=2,3,\dots. $$ 

In order to start the integration, one needs the right-hand side

 $$ a_{j}^{\prime}(0)=\frac{j-2}{j+1}a_{j-1}^{\prime}(0)\quad,\quad j=2,3,\ldots\quad, $$ 

which, with  $ a_{1}^{\prime}(0)=0 $, directly leads to

 $$ a_{j}^{\prime}(0)=0\qquad,\qquad j=2,3,\dots. $$ 

As it turns out, these initial values imply

 $$ a_{j}(t)\equiv0\qquad,\qquad j=1,2,\dots. $$ 

Summarizing, only one generalized moment and a moving Schulz-Flory weight function is sufficient to describe this mechanism! This structure is, of course, modified in the cases, when either the initial values (4.15) are different or the polyreaction mechanism is part of a larger reaction scheme. In any case, the above derivation confirms that the discrete Galerkin-Laguerre method is particularly well-suited for this kind of mechanism.