Rather, a limiting process

 $$ a_{j}(0):=\operatorname*{l i m}_{t\to0^{+}}a_{j}(t) $$ 

must be performed. Examination of the right-hand side in (4.7.c) shows that a regular solution  $ a_{j} $ is only possible under the necessary algebraic conditions

 $$ a_{j}(0)=a_{j-1}(0)-\frac{1}{j}\sum_{m=0}^{j-1}a_{m}(0)\qquad,\qquad j=2,3,\cdots, $$ 

which are seen to determine the missing initial values. Under this assumption,  $ (4.7.c) $ has a removable singularity: by means of Taylor expansion around  $ t = 0 $ one easily verifies that the initial right-hand side

 $$ a_{j}^{\prime}(0)=\frac{1}{j+1}\left[j a_{j-1}^{\prime}(0)-\sum_{m=0}^{j-1}a_{m}^{\prime}(0)\right] $$ 

must be used to start the numerical integration.

Coagulation and polycondensation. This mechanism is modelled by the differential equations (1.9) in terms of the number  $ N_s(t) $ of polymers of length s. Of course,  $ N_s(t) $ now replaces  $ P_s(t) $ in the representation (4.1). Moreover, for illustration purposes, the specification (1.10) for the Smoluchowski model is made. Once more, the relation (4.3) requires the calculation of

 $$ \left\langle l_{j},N_{s}^{\prime}\right\rangle=\frac{k_{p}}{2}\left\langle l_{j},\sum_{r=1}^{s-1}N_{r}N_{s-r}\right\rangle-\dot{k}_{p}\left\langle l_{j},N_{s}\sum_{r=1}^{\infty}N_{r}\right\rangle $$ 

Upon using the relations (2.30) and (1.13), rearranging the order of summation and applying the properties of Section 3.1, one obtains

 $$ \begin{array}{r c l}{\langle l_{j},N_{s}^{\prime}\rangle}&{=}&{\displaystyle\frac{k_{p}}{2}\sum_{k=0}^{\infty}a_{k}\sum_{m=0}^{\infty}a_{m}\sum_{s=1}^{\infty}(1-\rho)^{2}\rho^{s-2}l_{j}(s)\sum_{r=1}^{s-1}l_{k}(r)l_{m}(s-r)-}\\ {}&{}&{\displaystyle-k_{p}a_{0}\sum_{k=0}^{\infty}a_{k}\sum_{s=1}^{\infty}(1-\rho)\rho^{s-1}l_{j}(s)l_{k}(s)=}\\ {}&{=}&{\displaystyle\frac{k_{p}}{2}\rho^{j}\left[\sum_{m=1}^{j-1}a_{m}a_{j-m}-\frac{1}{\rho}\sum_{m=0}^{j-1}a_{m}a_{j-1-m}\right]}\\ \end{array} $$ 