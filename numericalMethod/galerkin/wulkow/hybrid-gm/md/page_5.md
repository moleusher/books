## Ensemble of Chains

As described before, within the hybrid algorithm we solve the kinetic rate equations and in parallel compute single realizations of the CME with MC method, i.e., a modification of the SSA algorithm. Therefore each distribution  $ P^i $ is not only represented by the  $ d_i $ degrees of freedom of the deterministic method, but also by an ensemble  $ E $ consisting of  $ m_i $ chains  $ e $ with chain-length  $ e_s $ and further properties  $ e_1, e_2, \ldots $. This number  $ m_i $ can be fixed or chosen adaptively. A main task of the present algorithm is to keep  $ m_i $ “small,” e.g., at values between  $ 10^2 $ and  $ 10^3 $. This implies, that a typical chain-length distribution from radical polymerization, where the maximal chain-lengths range up to  $ 10^4 $ or even  $ 10^6 $ will not be approximated sufficiently well by the MC ensemble, but this does not matter in the hybrid approach, where dependencies on the chain-length axis are treated by the deterministic part of the algorithm.

The complexity of the information of one chain can be chosen in view of the problem to be considered. Typical numbers are chain length, number of monomers of all types, number of branches, length of branches, position of active unit, etc., but also the full chain could be stored as linear or branched structure. Another important aspect is the definition of concentrations in the context of the MC method. Usually a control volume V is taken and the molar concentrations of the single species are given by:

 $$ c_{i}=\frac{n_{i}}{V N_{A}}. $$ 

Since the new approach should be used in a technical reactor setting, the volume might be in the range of liters or more, such that even for low-concentrated radical polymers (e.g.,  $ 10^{-8} $ mol l $ ^{-1} $) more than  $ 10^{15} $ chains have to be considered. Since the total number of MC chains is limited by storage and computer speed, the control volume is often set to very small values. Then it can happen, that certain populations (like radical polymer chains) are represented by a few MC chains only. Here we use a different approach: for each distribution  $ P_s^i $ we know the overall concentration from the deterministic method and assign it to the MC ensemble. Thus in the present approach a natural choice is to use a reasonable, even equal number  $ m_i $ for all distributions  $ P_s^i $ and scale all interactions with respect to the assigned, time-dependent concentration level obtained by the deterministic part of the algorithm.

## Time Discretization

The MC method is used within the time discretization scheme of the deterministic approach. There, time steps  $ \tau $ are chosen, such that the overall accuracy is kept within a prescribed tolerance. At first, the full deterministic system is solved using the approximation method for chain-length distribution (Rothe's method, see Figure 3 in ref.[1] Within such a time step, many single reactions take place and have to be performed by the MC method in parallel. Both — the deterministic and the stochastic part — use the results of the previous time step of the global time evolution. For example, starting with a chain-length distribution  $ P_s(t) $ at time  $ t $, described by a h-p-grid  $ \Delta_t $ and a MC ensemble  $ E_t $, the time step  $ \tau $ leads to an approximation  $ P_s(t+\tau) $ and an updated MC ensemble  $ E_{t+\tau} $.



For the MC part we follow the algorithm by Gillespie as used in ref. $ ^{[7]} $ At time t stochastic time intervals  $ \Delta t_k $ are consecutively computed in terms of the total rate of reactions  $ r_T $:

 $$ \Delta t_{k}=\frac{1}{r_{T}}\ln\left(\frac{1}{z_{k}}\right) $$ 

with random numbers  $ z_k \in (0, 1) $. A total number of MC steps  $ n_{MC} $ for the outer time step  $ \tau $ at time  $ t $ is chosen such that:

 $$ \sum_{k=1}^{n_{MC}}\Delta t_{k}<\tau and\sum_{k=1}^{n_{MC}+1}\Delta t_{k}\geq\tau. $$ 

This means, that two tasks have to be solved:

• Computation of the total rate.

• Selection of one operation in the single MC steps.

Computation of Total Rate and Selection of Reaction

In a bimolecular reaction  $ R_{\mu} $ with species A and B and rate constant  $ k_{i} $ the MC rate is given by (see ref. $ ^{[7]} $):

 $$ r_{\mu}=\frac{k_{\mu}}{V N_{A}}n_{A}n_{B}. $$ 

The actual total rates for the most important reaction types are listed in Table 2 below. At start of a τ-step, the individual reaction rates and the sum  $ r_T = \sum r_\mu $ are computed and assigned to sub-intervals  $ I_\mu $ of  $ [0, 1] $ given by:

 $$ I_{\mu}=(\sum_{l}^{\mu-1}\frac{r_{l}}{r_{T}},\sum_{l}^{\mu}\frac{r_{l}}{r_{T}}]. $$ 

In a MC time step  $ \Delta t_k $ a reaction  $ R_\mu $ is selected, if  $ z \in I_\mu $ for a random number  $ z \in (0, 1] $. All this is quite similar to the algorithm used in ref. $ ^{[7]} $ By the above scheme, the MC part of the algorithm is treated in an explicit way. This means, that