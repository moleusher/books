### 5. Numerical Experiments

In this section, the approach derived above is now illustrated. Because of the different convergence theory, a splitting between self-closing and open systems is made. On the basis of Section 2.2 it is clear that, whenever the differential equations for the statistical moments are self-closing, then this property is inherited for any generalized moments arising in the discrete Galerkin method.

### 5.1 Self-closing Systems

Among the polyreaction processes treated herein (Section 1.1), the chain addition polymerization and the coagulation (or polycondensation) with the Smoluchowski specification lead to a self-closing differential equation system (compare Section 4).

Chain addition polymerization. The preprocessing of model (1.4) by Charlier polynomials showed that the exact analytic solution for the initial values (1.4.b) is just the moving Poisson distribution with time dependent amplitude

 $$ P_{s}(t)=a_{0}(t)e^{-\lambda(t)}\frac{(\lambda(t))^{s-1}}{(s-1)!} $$ 

This means that the discrete Galerkin-Charlier method is exact already for truncation index  $ \tilde{N}=1 $. (Of course, (5.1) has already been derived otherwise [18].) From (4.31) and (4.32) the direct analytic solution

 $$ a_{0}(t)=P_{10},\lambda(t)=t $$ 

can be calculated. Note, however, that for general initial values  $ P_s(0) $ the truncation index N for a reasonable approximation  $ P_s^{(N)} $ will be greater than 1. Nevertheless, the Poisson distribution as weight function  $ \Psi $ seems to fit particularly well with this special polyreaction mechanism.

Things turn out to be different when the Schulz-Flory distribution is chosen as weight function  $ \Psi $ for the discrete Galerkin method (Section 4.1). This fact is illustrated in Figure 1, where the discrete Galerkin-Laguerre approximation for  $ N = 1, 10, 30 $ and  $ t = 5 $ is depicted. At the same time, these Figures visualize the comments about the Stieltjes problem for finite truncaton index  $ N $, that have been made in Section 2.2: recall that due to the self-closing property of the system (4.7) the first  $ \hat{N} + 1 $ statistical moments can be correctly computed via (2.22).