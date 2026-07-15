Polymer degradation. In this paper, only the method for the homogeneous model (1.7) with (1.8.a) is presented. The treatment of the heterogeneous cases = (1.8.b, c) will be given elsewhere. As in the two preceding model problems, one has to calculate

 $$ \frac{1}{k_{p}}\left\langle l_{j}\right.,\left.\dot{N}_{s}^{\prime}\right\rangle=-\left\langle(s-1)l_{j}\right.,\left.N_{s}\right\rangle+2\left\langle l_{j},\sum_{i=s+1}^{\infty}N_{i}\right\rangle $$ 

The first term on the right-hand side just requires the application of the three-term-recurrence (3.3.a, b). For the second term, the relations (3.12) and (3.9.b) together with a proper reordering of summations are employed. This leads to the result

 $$ \rho^{-j}\left\langle l_{j},N_{s}^{\prime}\right\rangle=\frac{k_{p}}{1-\rho}\left[j(a_{j-1}-a_{j})+\rho(j-1)(a_{j+1}-a_{j})\right]\quad\textcircled{4}\frac{1}{2}\frac{\partial^{2}}{\partial x\partial y} $$ 

Insertion of (4.21) into (4.3) then yields the differential equations

 $$ \begin{align*}\mathbf{a})\quad&a_{0}^{\prime}=\quad\frac{k_{p}\rho}{1-\rho}\;a_{0}\\\mathbf{b})\quad&\rho^{\prime}\quad=\quad-k_{p}\;\rho\\\mathbf{c})\quad&a_{j}^{\prime}\quad=\quad\frac{k_{p}\rho}{1-\rho}(j-1)\;(a_{j+1}-a_{j})\quad,\quad j=2,\;3,\;\ldots\quad.\end{align*} $$ 

Note that the system (4.22) is open, which requires a truncation rule such as  $ a_{N+1} := 0 $ for truncation index N.

Initial values  $ P_s(0) \sim sN_s(0) $ from experimental measurements are plotted in Figure 4, [2], or in Figure 13.6, [11]. In view of these experimental data, the following model initial values seem to be realistic:

 $$ N_{s}(0)=\frac{s}{r}\;e^{-s/r}\quad. $$ 

With this choice, the maximum of the distribution  $ N_{s}(0) $ roughly occurs at s = r. From (4.23), the initial value

 $$ 1-\rho(0):=\frac{1-\bar{\rho}}{1+\bar{\rho}}\quad,\quad\bar{\rho}:=e^{-1/\tau}. $$ 

can be obtained, which then allows to compute the a₀(0), a₂(0), … from (2.8).

### 4.2 Preprocessing by Charlier Polynomials

With the weight function  $ \Psi $ from (3.20) the associated representation for the polymer distribution reads

 $$ P_{s}(t):=e^{-\lambda}\frac{\lambda^{s-1}}{(s-1)!}\sum_{k=0}^{\infty}a_{k}(t)c_{k}(s)\quad,\quad\lambda>0 $$ 

where  $ \{c_{k}\} $ denotes the set of Charlier polynomials as introduced in Section 3.2.