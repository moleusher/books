butions, reaction steps and additional effects. For a formal approach we write Eq. (2) in the form of a countable system of ordinary differential equations

 $$ u_{s}^{\prime}(t)=f_{s}(u_{1}(t),\ldots,u_{s_{\mathrm{t o t}}^{-}}(t))\qquad\quad s=1,\ldots s_{\mathrm{t o t}} $$ 

The vector of the  $ u_s(t) $ will be called  $ u(t) $. In the above example the variables  $ u_s(t) $ are the concentrations of macromolecules  $ P_r $ and  $ D_r $ with chain length  $ r $ at a time  $ t $ and the concentrations of initiator and monomer. In contrast to ordinary differential equations the upper index  $ s_{\text{tot}} $ (i.e. the dimension of the complete system) may be very large ( $ 10^3 - 10^6 $ in practical examples). If for computational reasons such a large system has to be truncated at a smaller chain length  $ s_{\text{max}} $, a suitable value is rarely known a priori and may vary with time  $ t $ by orders of magnitude (closing problem). Thus a system (3) cannot be treated by standard numerical methods for ordinary differential equations in general. The theory of countable systems shows that their behavior is quite different from that of a high dimensional system of ordinary differential equations. The theoretical techniques for providing existence and uniqueness of solutions — in particular the choice of appropriate function spaces — resembles more the theoretical treatment of partial differential equations. A survey on this field is given in ref. $ ^9 $

## The modular approach — some reaction steps

As pointed out in the introduction, the aim of this research was to solve problems with arbitrary reaction steps leading to arbitrary distributions. Thus it should be possible to combine reaction steps from a comprehensive list. The following Tab. 1 shows typical reaction patterns and their difficulties. An algorithm has to be measured by its capability to treat such modules.

## Approaches to polyreaction kinetics — the way to the discrete h-p-method

A review of methods for the computation of molecular weight distributions has to consider efficiency and flexibility. We will give a brief, incomplete survey on popular and recent methods here. For all approaches details may be found in the literature. Thus we will only present some structural information, which lead to the motivation of the proposed Galerkin method of this article. Our selection of references only wants to give some hints. There are many important contributions which are not mentioned here.

## Model reduction by additional assumptions — quasi-steady-state assumption

Whenever it is known that the complete reaction system — or at least components of the system — can be considered as quasi-stationary (i.e. the respective derivatives can be set to zero), the kinetic equations may be simplified. For example, in radical polymerization the computation of the molecular weight distributions can be reduced to a quadrature of selected fractions (concentrations of the distribution at certain nodes of the chain length axis) of the dead polymer  $ {}^{13} $. Between the fractions the result can