# A Hybrid Galerkin–Monte-Carlo Approach to Higher-Dimensional Population Balances in Polymerization Kinetics

Christof Schütte,* Michael Wulkow*

Population balance models describing not only the chain-length distribution of a polymer but also additional properties like branching or composition are still difficult to solve numerically. For simulation of such systems two essentially different approaches are discussed in the

Population balance models describing not only the also additional properties like branching or compo For simulation of such systems two essentially literature: deterministic solvers based on rate equations and stochastic Monte-Carlo (MC) strategies based on chemical master equations. The paper presents a novel hybrid approach to polymer reaction kinetics that combines the best of these two worlds. We discuss the theoretical conditions of the algorithm, describe its numerical realization, and show that, if applicable, it is more efficient than full-scale MC approaches and leads to more detailed information in additional property indices than deterministic solvers.

<div style="text-align: center;"><img src="imgs/img_in_image_box_665_584_1101_909.jpg" alt="Image" width="36%" /></div>


## Introduction

The modeling and simulation of polymer reactions still bears various challenges regarding formulation and numerical solution of the underlying population balances. A recent overview is given in ref. $ ^{[1]} $ An issue of special interest of such systems is the treatment of more than one property coordinate, i.e., a description of polymer chains including not only the chain length, but also composition, branching, etc. Even then it is straightforward to derive rate equations, however, these systems will form a higher-dimensional set of countable systems prohibitively complex for more than two or three independent properties. Apart from direct higher-dimensional discretization approaches for such systems, $ ^{[1-3]} $ a special calculus (based on so-called balance distributions or distributed moments) has been developed in the context of the discrete Galerkin h-p-method, $ ^{[4,5]} $ where the additional properties are computed as averages with respect to chain-length. This leads to very detailed and often sufficient information within reasonable computation times, since the original n-dimensional system can be replaced by n one-dimensional countable systems (where a countable system itself is represented by an infinite or very large set of differential equations). A disadvantage of this approach is the fact, that the preparation of such distributed moment systems requires some insight regarding the population balances and a sophisticated use of the discretization method handling the single reaction steps. Regarding the results, sometimes it would be helpful to get information not only on chain-length dependent mean values of additional properties, but full distributions of such, e.g.,



in order to examine a composition drift in a copolymer system.

Therefore for a long while as an alternative to the deterministic approaches sketched above, stochastic methods are applied to polymer systems  $ [6-8] $ to name very few). The advantage of the resulting Monte-Carlo (MC) methods is, that they are (or at least seem to be) relatively simple to implement and provide quite general information. However, even on modern, parallelized systems, stochastic results of a sufficient accuracy (something which is naturally required from deterministic methods), still cost a lot of computing time. $ ^{[8]} $ Furthermore, error controls for MC methods are hardly to obtain without lengthy convergence tests. On the other hand, deterministic methods are superior in view of identification and optimization purposes, where it is necessary to deal with smooth, differentiable structures.

Summarizing we can state, that there are accurate deterministic (very efficient for one property) and comprehensive stochastic methods available, but mostly applied used in a quite separated manner. One exception is the work described in ref. $ ^{[9]} $, where a MC simulation is used as a postprocessing to results obtained by the balance distribution approach. In contrast to that approach, in this paper we will apply deterministic and stochastic methods in parallel, sometimes even depending on each other. We will show, how a skillful combination of both types of techniques can overcome the disadvantages of the single approaches and lead to detailed and efficient simulations. One basic idea is, that for polymer systems there is one special property — the chain length. There will always be more, often much more, monomer units along a polymer chain than counts for any other property. In our hybrid algorithm, the chain-length axis and the related chain-length distributions are treated by means of a deterministic approach, whereas all other property coordinates are represented by an ensemble of molecules of a MC method. As a consequence, only a relative small number of chains is necessary for the MC method, since the reaction rates can be obtained from the deterministic results within high accuracy. In order to develop this algorithm on a mathematical basis, the coupling has to be done by carefully studying the underlying chemical master equations (CMEs). Then — using certain limit processes — we can derive the coupling between deterministic and stochastic parts of the algorithm.

In contrast to refs. $ ^{[6-8]} $ and other comparable approaches, where the aim is to calculate the polymer chain length distribution (and sometimes additional properties) from probabilistic models, the hybrid approach suggested herein addresses the distribution of other properties (e.g., branching) by MC techniques. The chain length distribution, however, is computed by reaction kinetics using PREDICI or similar solvers.

In Section Theoretical Considerations of this article, the mathematical basics of master and rate equations for polymer kinetics are summarized and the theory of the coupling is derived. The distinction between the basic objects of master equation and reaction kinetics is essential for the comprehension of the hybrid approach; in particular it is essential to understand that the entire chain length distribution is the first (marginal) moment of the probability distribution underlying the master equation. Our hybrid approach contains the full chain length distribution and the associated marginal probability distribution for the other properties. It thus, at least in principle, allows to compute, e.g., all the moments of the chain length distribution as well as all the moments of the distributions of other properties. In order to work this out as clearly as possible, we added an overview over the basic aspects of the different modeling layers at the end of Section Hybrid Model.



In Section Algorithm, some technical issues of the algorithm, already implemented in a prototypical version of the program package Predici, are discussed. Finally some illustrative examples are presented in Section Numerical Experiments.

## Theoretical Considerations

Modeling polymer reaction kinetics basically means to describe certain phenomena occurring on a microscopic level and affecting the single monomeric units of a polymer chain — for example, the process of adding a monomer to a polymer molecule. The probability of such a single reaction, the position along the chain, the type of monomer and chain, etc., are all under consideration. The common notation for a propagation reaction:

 $$ P_{s}+M\stackrel{k_{p}}{\rightarrow}P_{s+1},s=1,2,\ldots $$ 

refers to the types of molecules involved:  $ P_s $ to the type polymer of chain length  $ s $,  $ M $ to the type monomer. If one wants to distinguish between polymers of type chain length  $ s $ with different additional properties, one has to add additional property indices. For example, we can distinguish between polymers with different branching index  $ j $ by introducing the polymer type  $ P_{sj} $. For a given instance in time let us denote the number of copies of polymers of type  $ P_{sj} $ by  $ n_{sj} $. Summation over the branching index  $ j $ yields the copy number  $ N_s = \sum_j n_{sj} $ of polymers of type  $ P_s $. If required, we can introduce several additional property indices  $ j_1, \ldots, j_m $ and different types of polymers  $ P^k $ such that in general we would have to consider molecular types  $ P_{sj_1, \ldots, j_m}^k $. For the sake of simplicity we will however restrict the following considerations to types  $ P_{sj} $ or  $ P_s $.

At time $t$ the ensemble of molecules is completely characterized by the state $n = (n_{s,j})_{s \geq 1, j \geq 0}$ of all copy numbers of all types of polymers. The reactions that change the state of the ensemble happen statistically such that the temporal evolution of the state is a stochastic process. Consequently, we in general cannot assume to know the present state of the ensemble but just the probability $\mathbb{P}_t(n)$ to find the ensemble at time $t$ in state $n$. The Chemical Master equation (CME) describes the evolution of this probability. It is driven by the possible reactions $R_\mu = (a_\mu, v_\mu)$, where $\mu$ is the index that enumerates the reactions, $a_\mu$ is the reaction rate of reaction $R_\mu$ (the so-called propensity function), and $v_\mu$ the associated stoichiometric vector. The CME then has the following form:

 $$ \begin{align*}\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}_{t}(n)&=\sum_{\mu}(\alpha_{\mu}(n-\nu_{\mu})\mathbb{P}_{t}(n-\nu_{\mu})\\&\quad-\alpha_{\mu}(n)\mathbb{P}_{t}(n)).\end{align*} $$ 

This means, with rate  $ a_{\mu}(n - \nu_{\mu}) $ the reaction  $ R_{\mu} $ happens in a state  $ n - \nu_{\mu} $ of the ensemble that has probability  $ \mathbb{P}_t(n - \nu_{\mu}) $ and brings the ensemble to state  $ n $ and thus increases  $ \mathbb{P}_t(n) $. Simultaneously the same reaction, if happening in state  $ n $ with rate  $ a_{\mu}(n) $, generates a state  $ n + \nu_{\mu} $ thus decreasing  $ \mathbb{P}_t(n) $. Consequently, the solution of the CME is a probability distribution on an enormously large state space that contains all possible combinations of copy numbers  $ n_{s,j} $. For example, the typically considered polymer chain length distributions are just one expectation value of  $ \mathbb{P}_t(n) $:

 $$ c_{t}(P_{s})=\frac{1}{V}\sum_{s\mathrm{f i x e d}}n_{s,j}\mathbb{P}_{t}(n_{s,j})=\frac{1}{V}\sum_{N_{s}}N_{s}\mathbb{P}_{t}(N_{s}), $$ 

where V is the reference volume. For molar concentrations as mostly used in polymer reactions we would have to divide  $ c_{t}(P_{s}) $ by the Avogadro number, but this does not matter here.

For the case of the simple reaction scheme (1), the state is  $ N = (N_s)_{s \geq 1} $ and the possible reactions consist of one reaction  $ R_s = (a_s, v_s) $ per polymer type  $ P_s $ where the stoichiometric vector  $ v_s = e_s $ has just one nonzero entry at position  $ s $, while the reaction rate has the form  $ a_s(n) = N_s k_p M $ (assumption:  $ k_p M = \text{const} $, unit 1/s) such that the CME reads:

 $$ \begin{aligned}\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}_{t}(N)&=k_{p}M\sum_{s}\left((N_{s}-1)\mathbb{P}_{t}(N-e_{s})\right.\\&\left.-N_{s}\mathbb{P}_{t}(N)\right)\end{aligned} $$ 

This is easily understood: the change  $ d\mathbb{P}_t(N)/\text{dt} $ in the probability that the copy number vector is  $ N $, results from all the reactions  $ P_s + M \rightarrow P_{s+1} $ for all  $ s $. For fixed  $ s $ this reaction shifts the copy number vector from  $ N $ to  $ N + e_s $ (death of particle  $ P_s $) with rate  $ N_s k_p M $ and probability  $ \mathbb{P}_t(N) $ (second term on the RHS) and simultaneously from  $ N - e_s $ to  $ N $ (birth of particle  $ P_s $) with probability  $ \mathbb{P}_t(N - e_s) $ and rate  $ (N_s - 1) k_p M $ (first term on RHS).



In terms of simulations, a solution of the CME for many different types of molecules (here polymers of all possible chain lengths) is infeasible. The Stochastic Simulation Algorithm (SSA) as going back to Gillespie  $ (^{[10,11]} $ does not solve (2) but simulates single realizations of the stochastic process underlying the CME. Consequently, the solution  $ \mathbb{P}_t(n) $ of the CME strictly speaking can only be approximated by many SSA simulations. Even in view of SSA simulations, the CME approach is rather unrealistic in applications where  $ 10^{15} - 10^{23} $ molecules of one type of molecules have to be taken into account and several types of molecules are present. Fortunately, one can show that for large reaction rate  $ a_\mu $ (more precisely for  $ a_\mu \to \infty $), the solution of the CME gets the form of a delta distribution in state space that evolves along the deterministic solution of the associated reaction kinetics. In order to express this in more detail let us consider the polymer types  $ P_s $ again and assume that (as in the example above) the reaction rates  $ a_\mu(N) $ scales with the copy numbers  $ N $ as follows: let  $ N_0 $ denote some reference number, then  $ a_\mu(N) = N_0 a_\mu(N/N_0) $, i.e., the reaction rates are large for large copy numbers. Then, if the copy numbers of a system are large, we can expand the CME (2) in powers of the small number  $ 1/N_0 $ and consider just the terms in lowest order in  $ 1/N_0 $. In lowest order, i.e., in the limit of large copy number  $ N_0 $, the probability distribution is just a delta distribution in state space:

 $$ \mathbb{P}_{t}(N)=\delta(N-V c_{t}(P_{s})), $$ 

that evolves along the concentration trajectory  $ c_{t}(P_{s}) $ that is given by:

 $$ \frac{\mathrm{d}}{\mathrm{d}t}c_{t}(P_{s})=\sum_{\mu}\nu_{\mu}\alpha_{\mu}\big(c_{t}(P_{s})\big), $$ 

where  $ \alpha_{\mu} $ results from the reaction rate  $ a_{\mu} $ by switching from copy numbers to concentrations,  $ \alpha_{\mu}(c) = a_{\mu}(Vc)/V $. For the above example, this results in the rate equation:

 $$ \frac{\mathrm{d}}{\mathrm{d}t}c_{t}(P_{s})=k_{p}M c_{t}(P_{s-1})-k_{p}M c_{t}(P_{s}). $$ 

Taking higher orders in  $ 1/N_0 $ into account leads to further resolution of the probability distribution, e.g., the next order results in information on the variance of  $ \mathbb{P}_t(N_s) $ around its mean  $ Vc_t(P_s) $.

## Hybrid Model

In general we cannot assume that all copy numbers in a system are large. For example, this may be true if additional property indices like the branching index are considered. We will now consider cases in which the state  $ (n_{sj})_{s \geq 1, j \geq 0} $ of the ensemble can be partitioned into two different parts, in the sense that the state of the ensemble can be written in the form  $ n = (x, y) $. Later we will consider cases in which the copy numbers in the  $ y $-part are large while the copy numbers in the  $ x $-part are low (or, in general, cannot be assumed to be large). For example, we could consider in the notation used above,  $ y = (N_s)_{s \geq 1} $, and  $ x = (n_{sj})_{s \geq 1, j \geq 0} $.

Due to the laws of conditional probabilities we can write:

 $$ \mathbb{P}_{t}(x,y)=\mathbb{P}_{t}(x|y)\mathbb{P}_{t}(y), $$ 

where  $ \mathbb{P}_t(x|y) $ denotes the probability of state  $ x $ conditional on  $ y $. Inserting this into the CME (2) we get:

 $$ \begin{align*}\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}_{t}(x,y)=\mathbb{P}_{t}(y)\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}_{t}(x|y)+\mathbb{P}_{t}(x|y)\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}_{t}(y)\\=\sum_{\mu}\left[\alpha_{\mu}(x-v_{\mu},y-\xi_{\mu})\mathbb{P}_{t}(x-v_{\mu}|y-\xi_{\mu})\mathbb{P}_{t}(y-\xi_{\mu})\right.\\ \left.\quad-\alpha_{\mu}(x,y)\mathbb{P}_{t}(x|y)\mathbb{P}_{t}(y)\right],\end{align*} $$ 

where we split the stoichiometric vectors  $ \nu_{\mu} = (v_{\mu}, \xi_{\mu}) $ in analogy to the splitting  $ n = (x, y) $. Because of  $ \sum_{x} \mathbb{P}_t(x|y) = 1 $, we get directly from (9) by summing both sides over  $ x $ and using  $ (\mathrm{d}/\mathrm{d}t) \sum_{x} \mathbb{P}_t(x|y) = 0 $:

 $$ \begin{align*}\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}_{t}(y)&=\sum_{\mu}[\overline{\alpha}_{\mu}(y-\xi_{\mu})\mathbb{P}_{t}(y-\xi_{\mu})\\&\quad-\overline{\alpha}_{\mu}(y)\mathbb{P}_{t}(y)],\end{align*} $$ 

with averaged rates:

 $$ \overline{{a}}_{\mu}(y)=\sum_{x}a_{\mu}(x,y)\mathbb{P}_{t}(x|y). $$ 

Now, we assume that for the y-part the limit of large copy numbers is justified such that in the limit of large copy numbers we get  $ \mathbb{P}_t(y) = \delta_{VC_t}(y) $ with a concentration trajectory  $ C_t $ given by the rate equation:

 $$ \frac{\mathrm{d}}{\mathrm{d}t}C_{t}=\sum_{\mu}\xi_{\mu}\overline{\alpha}_{\mu}(t,C_{t}). $$ 

The usual properties of the delta distribution  $ \delta_{VC_t}(y) $ allow to compute expectation values in y in the sense of  $ \sum_y f(y)\delta_{VC_t}(y) = f(VC_t) $ for all smooth enough functions  $ f $; we can use this particularly to introduce:



 $$ \sum_{y}\mathbb{P}_{t}(x|y)\delta_{VC_{t}}(y)=\mathbb{P}_{t}(x|C_{t}). $$ 

When inserting these results back into (9) we find:

 $$ \begin{align*}\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}_{t}(x|C_{t})\\=&\sum_{\mu}\left[a_{\mu}(x-v_{\mu},VC_{t}-\xi_{\mu})\mathbb{P}_{t}(x-v_{\mu}|C_{t})\right.\\&\left.-a_{\mu}(x,VC_{t})\mathbb{P}_{t}(x|C_{t})\right],\end{align*} $$ 

which in turn implies for the averaged rates:

 $$ \begin{align*}\overline{\alpha}_{\mu}(y,t)&=\sum_{x}\alpha_{\mu}(x,y)\mathbb{P}_{t}(x|C_{t}),\\\overline{\alpha}(t,C_{t})&=\overline{\alpha}(VC_{t},t)/V.\end{align*} $$ 

In particular, if there are rates that do not depend on the low copy number part of state space, we simply get:

 $$ \overline{\alpha}_{\mu}(y)=\alpha_{\mu}. $$ 

Summarizing one gets a system of two coupled equations, a rate equation (12) for the concentrations of the large copy number particles in y that does depend on the low copy numbers in x just via the averaged rates and the CME (13) for the low copy number particles that depends on the concentrations  $ C_t $. This allows to restrict the stochastic CME simulations via SSA to the dimension of the low copy number variables while the large copy number particles can be handled much more efficiently via deterministic rate equation solvers like Predici.

## Overview Over the Different Modeling Layers

Table 1 shows the different description layers. The basic quantity  $ \mathbb{P}_t(n_{s,j}) $ of the CME layer is the probability distribution over all possible copy numbers  $ n_{s,j} $ of chains with property  $ (s,j) $. Its marginal moments  $ \mu_t^{(m)}(s) $ for s thus are averages over an ensemble of chains with identical property s distributed according to  $ \mathbb{P}_t(n_{s,j}) $. In deterministic reaction kinetics the basic quantity is the chain length distribution  $ c_t(P_s) $ that is proportional to the first of the marginal moments of the CME, i.e.,  $ \mu_t^{(1)}(s) $. Moments of the chain length distribution are thus averages over the property s (and not averages over copy number distributions since those have already been partially averaged out by switching to chain length distributions).

The hybrid model layer considers the marginal probability distribution of copy numbers conditioned to the chain length distribution being fixed. Its basic quantities are the full chain length distribution (no moments taken w.r.t. the chain length property) and the remaining

<div style="text-align: center;">Table 1. Overview over the different modeling layers.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Models</td><td style='text-align: center; word-wrap: break-word;'>Basic quantities</td><td style='text-align: center; word-wrap: break-word;'>Algorithms</td><td style='text-align: center; word-wrap: break-word;'>Moments</td></tr><tr><td rowspan="2">CME</td><td style='text-align: center; word-wrap: break-word;'>Probabilities</td><td style='text-align: center; word-wrap: break-word;'>SSA</td><td style='text-align: center; word-wrap: break-word;'>Marginal moments</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbb{P}_{t}(n_{sj}) $</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>$ \mu_{t}^{(m)}(s) = \sum_{n_{sj}} n_{sj}^{m} \mathbb{P}_{t}(n_{sj}) $ s fixed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \downarrow $</td><td style='text-align: center; word-wrap: break-word;'>$ \downarrow $</td><td style='text-align: center; word-wrap: break-word;'>$ \downarrow $</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hybrid model</td><td style='text-align: center; word-wrap: break-word;'>Chain length distribution and branching index probab.  $ \mathbb{P}_{t}(n_{sj} | c_{t}(P_{s})) $</td><td style='text-align: center; word-wrap: break-word;'>PREDICI coupled to SSA</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \uparrow $</td><td style='text-align: center; word-wrap: break-word;'>$ \uparrow $</td><td style='text-align: center; word-wrap: break-word;'>$ \uparrow $</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Deterministic reaction kinetics</td><td style='text-align: center; word-wrap: break-word;'>Concentrations, chain length distribution  $ c_{t}(P_{s}) = \mu_{t}^{(1)}(s)/V $</td><td style='text-align: center; word-wrap: break-word;'>PREDICI</td><td style='text-align: center; word-wrap: break-word;'>Chain length moments  $ \sum_{s} s^{m} c_{t}(P_{s}) = \lambda_{t}^{(m)} $</td></tr></table>

marginal probability distributions of copy numbers of chains with length s and distributed additional properties j (no moments here either). Thus, we still are able to compute all higher moments of chain length distribution and/or additional property indices if required.

## Concept of Hybrid Algorithm

However, in many realistic cases the distinction between large and low copy number particle will be difficult or even impossible. Nevertheless, the above derivation can help to reduce CME simulations drastically. In order to explain this let us return to our polymer system with types  $ P_{s,j} $ where s denote the chain length index and j another property index, e.g., some branching index. If we suppress the additional property index and consider just the polymer types  $ P_{s} $ in the y-part (that is, set y = N), then copy numbers will in general be large and the associated CME can be replaced by its large copy number rate equation limit. Returning to the desired level of resolution including the additional property index j, the associated CME contains low copy numbers. A partitioning of its state space into low and large copy number subspaces is impossible in general. However, we can do a SSA simulation of the full CME but with averaged reaction rates as in (13) (which is particularly simple wherever they contain the copy numbers  $ N_{s} $ that just depend on chain lengths). The general scheme of such a hybrid algorithm is illustrated in Scheme 1: after identification of the part of the systems for which (due to large copy numbers) a description in terms of concentrations is possible, one solves (12) with a deterministic solver like Predici, while in parallel a SSA according to Gillespie solves a CME of form (13) which includes the present concentrations of the deterministic solver in its reaction rate evaluations.

## Algorithm

The following algorithm is based on the assumption, that an approximation method is available that allows to represent all chain-length distributions of a kinetic model. Such single distributions are naturally induced by writing the kinetics in terms of active, inactive, dormant, branched species, etc., (e.g.,  $ R_s, D_s, Q_s $). The Galerkin h-p-method implemented in Predici allows a pointwise evaluation (i.e., for each single chain-length s) of all distributions within a controlled accuracy. Any other method leading to a full distribution might also serve as deterministic part of the hybrid algorithm. Here we follow the notation of ref. $ ^{[1]} $ and assume, that all distributions  $ P^i $ of a scheme can be approximated on grids  $ \Delta_i $ using  $ r_i $ degrees of freedom allowing evaluation of single concentrations  $ P_s^i $. In the following we will switch between the notations  $ c_s, c(P_s) $, or simply  $ P_s $ for the concentrations of the polymer type  $ P_s $ and likewise for  $ P_s,i $ if additional property indices have to be addressed; mostly we suppress the explicit dependence of all these objects on time.

<div style="text-align: center;"><img src="imgs/img_in_image_box_644_1193_1084_1353.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">Scheme 1. Structure of the hybrid-algorithm. Reactions can be described on different levels requiring different solution techniques. The hybrid algorithm combines the underlying equations as well as the numerical strategies.</div>


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

the concentrations and rates available at the begin of the time step t are used for the whole step. This aspect has only an effect on the local accuracy of the MC method. By using mean values or interpolation of the deterministic results along the time step, an improvement is possible. However, after trying different approaches, we decided to use the sufficiently good explicit scheme for all simulations presented in Section Numerical Experiments.

## Treatment of Reaction Steps

Apart from the computation of rates based on results of the deterministic method, up to this point the MC part of the algorithm looks quite similar to well-known approaches. This will change when we consider the treatment of the single reaction steps. For an illustration we choose a propagation step of a copolymerization scheme:

 $$ P_{s}^{1}+M_{2}\stackrel{k_{p12}}{\rightarrow}P_{s+1}^{2}, $$ 

selected at some time, where a monomer  $ M_2 $ adds to a chain with a different end-group such that this characteristic property of the molecule changes (typical terminal model). Related to  $ P^1 $ and  $ P^2 $ are overall concentrations  $ \lambda_0(P^1) = \sum_s P_s^1 $ and  $ \lambda_0(P^2) = \sum_s P_s^2 $ as well as MC ensembles  $ E_1 $ and  $ E_2 $ with numbers  $ m_1 $ and  $ m_2 $. At first, a single chain  $ e^1 $ has to be chosen randomly from the  $ P^1 $-ensemble  $ E_1 $. Now one could simply shift  $ e^1 $ to the other ensemble, however, this would disregard the different concentration levels and ensemble numbers. Instead, the reaction has different effects on the two ensembles. The number  $ m_a^2 $ of affected chains of type  $ P^2 $ is given by:

 $$ m_{a}^{2}=\frac{\lambda_{0}(P^{1})}{\lambda_{0}(P^{2})}\frac{m_{2}}{m_{1}}. $$ 

For  $ P^1 = P^2 $ we have  $ m_a^2 = 1 $ leading to the classical treatment. For the general case  $ m_a^2 \neq 1 $ the update of the ensembles involved requires some consideration. Firstly, the chain  $ e^1 $ has to be removed from the  $ P^1 $-ensemble. Since we want to keep  $ m^1 $ constant, then some other chain  $ e^2 $ has to be chosen and copied. The simplest way to do this is to select an entity  $ e^2 $ out of an ensemble  $ E_1 $ by using another random number  $ z_3 \in [1, m_1] $. Actually, if the ensemble is large and represents the chain-length distribution rather accurately, a random selection will automatically be proportional to the actual concentrations of the single polymer molecules. More complex copy strategies have been tested and will be discussed elsewhere. For  $ P^2 $ a certain number of chains has to be replaced by  $ e^2 $. If  $ m_a^2 < 1 $, we use another random number  $ z_4 $ to replace a chain if  $ z_4 < m_a^2 $. For that, one chain of ensemble  $ E_2 $ is randomly deleted and replaced by  $ e^2 $. If  $ m_a^2 \geq 1 $, a respective number of chains in  $ E_2 $ is replaced by copies of  $ e^1 $. Summarizing, for a single reaction  $ R_\mu $ the algorithm works as follows:



1. Select a chain  $ e^{1} $ from the ensemble  $ E_{1} $.

2. If  $ R_{\mu} $ is a bimolecular polymer reaction, select a partner chain  $ e^2 \in E_2 $.

3. If only one distribution is affected: change selected chains accordingly.

4. Otherwise: Compute the ensemble factor(s)  $ m_{a}^{i} $, replace the selected chain(s) in ensembles of distributions on the left-hand side and copy them. Apply weighting replacement to the ensembles on the right-hand side.

For some reaction step patterns a MC module has been implemented in a prototype version of Predici (compare Table 4 in ref. $ ^{[1]} $) The MC rates per deterministic step length  $ \tau $ use the molar concentrations of low molecular species like monomers, initiators and transfer agent and the statistical moments  $ \lambda_i(P) = \sum s'P_s $ of polymer species. The following Table 2 lists those rates when the first reactant on the left-hand side is selected first.

## Interpolation

If we want to use results from the MC part of the algorithm for output or even the computation of deterministic reaction rates, a technique to compute relatively smooth chain-length dependent information is required. Each chain  $ e \in E $ provides (not unique) relations between chain-length s and the property indices  $ i_1, i_2, \ldots $. However, in the numerical examples we require an average  $ i_2 $ (number of comonomers in a chain) for a given s. In Figure 7 an automatic regression of the graphic software has been used to compute the mean values, but such a regression requires some prescribed, parameterized function (linear, polynomial, exponential, etc.) and is only suited for a post-processing. During the time step evolution, we apply a more sophisticated algorithm:

<div style="text-align: center;">Table 2. Monte-Carlo reaction rates for selected elemental reaction steps.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Pattern</td><td style='text-align: center; word-wrap: break-word;'>Name</td><td style='text-align: center; word-wrap: break-word;'>MC-rate/ $ \tau $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ I + A \rightarrow P_{1} $</td><td style='text-align: center; word-wrap: break-word;'>Initiation</td><td style='text-align: center; word-wrap: break-word;'>$ k_{\lambda_{0}(Q)}^{\text{CICA}} m_{P} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + A \rightarrow Q_{s+1} $</td><td style='text-align: center; word-wrap: break-word;'>Propagation</td><td style='text-align: center; word-wrap: break-word;'>$ k_{C_{A}}m_{P} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + A \rightarrow Q_{s} + B $</td><td style='text-align: center; word-wrap: break-word;'>Transition</td><td style='text-align: center; word-wrap: break-word;'>$ k_{C_{A}}m_{P} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + Q_{r} \rightarrow D_{s+r} $</td><td style='text-align: center; word-wrap: break-word;'>Recombination</td><td style='text-align: center; word-wrap: break-word;'>$ k_{\lambda_{0}}(Q)m_{P} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + Q_{r} \rightarrow D_{s} + D_{r} $</td><td style='text-align: center; word-wrap: break-word;'>Disproportionation</td><td style='text-align: center; word-wrap: break-word;'>$ k_{\lambda_{0}}(Q)m_{P} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + A \rightarrow Q_{s} + T_{1} $</td><td style='text-align: center; word-wrap: break-word;'>Transfer</td><td style='text-align: center; word-wrap: break-word;'>$ k_{C_{A}}m_{P} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + D_{r} \rightarrow Q_{s} + T_{r} $</td><td style='text-align: center; word-wrap: break-word;'>Long-chain branching</td><td style='text-align: center; word-wrap: break-word;'>$ k_{\lambda_{1}}(D)m_{P} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ P_{s} + D_{r} \xrightarrow{r} Q_{s+r} $</td><td style='text-align: center; word-wrap: break-word;'>Cross-linking</td><td style='text-align: center; word-wrap: break-word;'>$ k_{\lambda_{1}}(D)m_{P} $</td></tr></table>

<div style="text-align: center;">Table 3. Rate constants for schemes (24) and (31).</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Name</td><td style='text-align: center; word-wrap: break-word;'>Value</td><td style='text-align: center; word-wrap: break-word;'>Unit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>k_{a}</td><td style='text-align: center; word-wrap: break-word;'>10^{-4}</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{s} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>k_{p_{1}}</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{mol s} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>k_{p_{2}}</td><td style='text-align: center; word-wrap: break-word;'>10^{4}</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{mol s} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>k_{d}</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{s} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>k_{tr}</td><td style='text-align: center; word-wrap: break-word;'>150</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{mol s} $</td></tr></table>

The rate constant  $ k_{tr} $ will only be needed in (31).

1. For a given chain-length $s$ the $h$-p-grid representation of the polymer species $P$ is taken to find an interval $I$, such that $s \in I$.

2. Then we compute

 $$ \overline{i}_{i}(s)=\frac{\sum_{e\in E,e_{s}\in I}e_{i}}{\sum_{e\in E,e_{s}\in I}1} $$ 

which simply is the average value of property i on interval I.

3. Since step 2 would lead to a piecewise constant function, the average is assigned to the mean of the interval and then interpolated linearly between neighbors of intervals.

Using this strategy, the results in Figure 6 and the backcoupling of averages into the reaction rate of the transfer step used below have been realized. Of course, the h-p-grid has been used as basis for the average, since the h-p-algorithm automatically detects where a distribution has important structures.

## Numerical Experiments

In this section we want to show how the hybrid algorithm, formally described by (12) and (13) works in typical situations. The used models are artificially designed to study the convergence behavior and some particular challenges of real-life models. Such applications — including a discussion of the chemical aspects of the results — will be considered in forthcoming papers and in cooperation with chemists and chemical engineers. Here we want to concentrate on the numerical issues. In Section Copolymerization with Drift and Section Additional Long-Chain Branching with Forward Coupling we realize the CME (13) by a stochastic method using overall concentrations obtained by the rate Equation (12), which in parallel is solved by the Galerkin method of Predici. In Section Long-Chain Branching with Backward Coupling we extend the model set-up and couple back results of the CME, here the average number of branches per chain-length, to the rate equations. In other words, in the first two examples, the averaged rate  $ \bar{a}_{\mu}(y) $ appears in its simple form (15), whereas in Section Long-Chain Branching with Backward Coupling we apply the general expression (11).



## Copolymerization with Drift

In order to get some confidence in the algorithm, we consider a simple copolymerization based on two monomers  $ M_{1}, M_{2} $. The reaction scheme consists of activation, propagation and deactivation only (one may think of a basic catalytic system):

 $$ \begin{aligned}C&\xrightarrow{k_{a}}P_{1,0}\\P_{s,i}+M_{1}&\xrightarrow{k_{p_{1}}}P_{s+1,i}+C_{1}\\P_{s,i}+M_{2}&\xrightarrow{k_{p_{2}}}P_{s+1,i+1}+C_{2}\\P_{s,i}&\xrightarrow{k_{d}}D_{s,i}\end{aligned} $$ 

 $ P_{s,i} $ denotes (the concentration of) a polymer of length s with  $ i $ units of comonomer  $ M_2 $. The initial values are:  $ C(0) = 10^{-1} \text{mol} l^{-1} $,  $ M_1(0) = 9.8 \text{mol} l^{-1} $,  $ M_2(0) = 0.1 \text{mol} l^{-1} $, where we assume the molecular weights of all species to be 0.1 kg mol $ ^{-1} $ (all simplifying assumptions and restrictions—here and below—are only made to focus on the main aspects of this examination and not induced by the method). The reaction rates are given as shown in Table 3:

It is easily seen that by choice of the propagation parameters  $ k_{p_1}, k_{p_2} $, and the low initial concentration of monomer  $ M_2 $ we will generate a broad chemical distribution. At the begin of the reaction, the instantaneous fraction  $ f_2(t) $ of incorporated monomer  $ M_2 $ will be:

 $$ f_{2}(0)=\frac{k_{p_{2}}M_{2}(0)}{k_{p_{1}}M_{1}(0)+k_{p_{2}}M_{2}(0)}\approx0.5, $$ 

where after consumption of  $ M_2 $ we will have  $ f_2(t) \approx 0 $. The “balance species”  $ C_1 $ and  $ C_2 $ are used to compute the time-dependent cumulated fractions of the monomers in the polymer  $ (C_i(t) > 0 $ for one  $ i $ and  $ t > 0) $:

 $$ F_{1}(t)=\frac{C_{1}(t)}{C_{1}(t)+C_{2}(t)},\quad F_{2}(t)=\frac{C_{2}(t)}{C_{1}(t)+C_{2}(t)}. $$ 

In order to check the results, a reference solution is required. For that, we apply the technique of balance distributions developed and applied in refs. $ ^{[4,5,12]} $ The general idea is to write down the full two-dimensional

rate equations of system (24) and then derive the differential equations for the boundary sums:

 $$ \begin{aligned}P_{s}&:=\sum_{i=0}^{\infty}P_{s,i},Q_{s}:=\sum_{i=0}^{\infty}iP_{s,i},D_{s}:=\sum_{i=0}^{\infty}D_{s,i},T_{s}:\\&=\sum_{i=0}^{\infty}iD_{s,i}.\end{aligned} $$ 

For example, the distribution  $ D_s $ denotes the concentration of all dead chains of length s (independent of their composition),  $ T_s $ describes the concentration of all  $ M_2 $-units in all such chains. Thus the pointwise ratio:

 $$ \overline{{F}}_{2}(s,t)=\frac{T_{s}(t)}{D_{s}(t)},D_{s}(t)>0, $$ 

describes the average number of  $ M_2 $-units in chains of length s. The derivation of the overall balance for  $ Q_s(t) $ and  $ T_s(t) $ is straightforward in this simple case (e.g., the additional balances for propagation steps are derived in ref., [4] Equation 8). In Predici, there are prepared modules for such balance equations and it is possible to compute  $ \overline{F}_2(s,t) $ within high accuracy as reference result.

Within the hybrid algorithm we solve the balances of only the overall chain-length distributions  $ P_{s} $ and  $ D_{s} $ by the deterministic algorithm (Predici). The underlying standard kinetic scheme is:

 $$ \begin{array}{c}C\xrightarrow{k_{a}}P_{1}\\P_{s}+M_{1}\xrightarrow{k_{p_{1}}}P_{s+1}+C_{1}\\P_{s}+M_{2}\xrightarrow{k_{p_{2}}}P_{s+1}+C_{2}\\P_{s}\xrightarrow{k_{d}}D_{s}\end{array} $$ 

In parallel the MC-algorithm is used to compute refined results regarding the composition of single chains — using MC reaction rates based on the solution of (29). For that, let us consider a single, randomly chosen hybrid MC simulation for the present model using ensembles of  $ m_{p} = 200 $ and  $ m_{D} = 2000 $ chains. All simulations are performed up to end time  $ t = 600 $ s. The choice of those numbers is mostly suggested by computing time issues. We do not want to spend too much additional computing time for the MC-part of the algorithm. At the same time, we want to show that even a small number of chains will provide reasonable results. Additionally, in systems with “living” and “dead” species, where it is obvious, that the living species will stay at concentration levels orders of magnitude smaller than the dead species, we use smaller sizes for the living MC population. Actually, all tests have shown, that in such systems the accuracy is mainly controlled by the number of dead chains.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length s</th><th style='text-align: center;'>h-p-Method</th><th style='text-align: center;'>MC-200-2000</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>5.0E-05</td><td style='text-align: center;'>4.4E-05</td></tr>
    <tr><td style='text-align: center;'>101</td><td style='text-align: center;'>2.2E-05</td><td style='text-align: center;'>2.4E-05</td></tr>
    <tr><td style='text-align: center;'>201</td><td style='text-align: center;'>1.0E-05</td><td style='text-align: center;'>1.1E-05</td></tr>
    <tr><td style='text-align: center;'>301</td><td style='text-align: center;'>0.3E-05</td><td style='text-align: center;'>0.4E-05</td></tr>
    <tr><td style='text-align: center;'>401</td><td style='text-align: center;'>0.1E-05</td><td style='text-align: center;'>0.1E-05</td></tr>
    <tr><td style='text-align: center;'>501</td><td style='text-align: center;'>0.05E+00</td><td style='text-align: center;'>0.05E+00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 1. Comparison between chain-length distributions  $ D(s) $ at t = 600 s obtained by our Galerkin method and one single Monte-Carlo realization.</div>


In Figure 1 we present the dead polymer chain-length distribution computed by the h-p-method and the MC method (range reduced to chain-length interval [1, 500] in order to amplify differences).

Significant concentrations range up to chain length  $ s = 10^3 $, such that we cannot expect to get a very accurate description of the CLD with  $ m_D = 2000 $ single chains, but using the interpolation technique of MC results (Section Ensemble of Chains) on the h-p-intervals, the results are in good agreement with the h-p-method. For comparison, the relative numbers of the MC method are normalized such that the maximal mean concentration of the h-p-method and the MC method on the intervals of the h-p-grid  $ \Delta $ are identical. Running different ensemble sizes or using an average of several MC simulations (each only one realization of the underlying master equation) leads to similar distributions, but since the differences are beyond visibility, we need a measure for the error. Since we have a pointwise solution from the h-p-method, we can compute the error induced by the MC method by:

 $$ \varepsilon_{\mathsf{M C}}=\left(\sum_{I\in\Delta}\left(\frac{(s_{2}^{I}-s_{1}^{I}+1)\left(D(s_{M}^{I})-A_{M C}^{I}\right)}{\lambda_{0}(D)}\right)^{2}\right)^{1/2}. $$ 

Here  $ s_{1}^{I} $ and  $ s_{2}^{I} $ are the bounds of interval I of the h-p-grid  $ \Delta $,  $ s_{M}^{I} $, and  $ A_{MC}^{I} $ denote the mean chain-length and the average normalized MC-based concentration on I.

Figure 2 shows the time evolution of the error for some realizations and for three different scenarios:  $ m_P = 100 $,  $ m_D = 1000 $;  $ m_P = 200 $,  $ m_D = 2000 $;  $ m_P = 500 $,  $ m_D = 5000 $ (in the following abbreviated by MC 100–1 000, MC 200–2 000, etc.).

Obviously the increase of the number of molecules leads to better results, whereas the improvement decreases for larger numbers. The linear regressions indicate relative errors of about 0.02, 0.03, 0.06 for the three simulations. It should be emphasized that the existence of an error

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time [s]</th><th style='text-align: center;'>Error-100-1000</th><th style='text-align: center;'>Error-200-2000</th><th style='text-align: center;'>Error-500-5000</th><th style='text-align: center;'>Linear (Error-100-1000)</th><th style='text-align: center;'>Linear (Error-200-2000)</th><th style='text-align: center;'>Linear (Error-500-5000)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.028</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.055</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2. Error estimates for the MC-method regarding full chain-length distributions (full time-dependent curves and linear average).</div>


estimate has valuable consequences when working with a numerical method.

Also the mean values  $ M_{n} $,  $ M_{w} $ of D are captured relatively well by the MC ensemble. Figure 3a and b present the results for the same three realizations as studied above.

However, we are not particularly interested in the CLD here, but rather want to compute information on the chemical distribution in an efficient way. As a first check we consider the overall fraction of the monomers and compare to the very exact results given in terms of (26). The MC results are so close to the deterministic curve (Figure 4), that one can hardly see a difference between the single simulations. Only at the end of the reaction there may be a slight underestimation of  $ F_{2}(t) $. The reason is, that the longest chains have the highest  $ M_{2} $-fraction and just these chains become less prominent in the MC ensemble. In the hP-method we use a special weighting to keep track of long chains and such a control can also be added to the MC method later.

Next we examine the inner structure of the chains. At first, we can use the single-chain information in the MC ensemble to compute the chemical composition, which is here defined as the molar fraction of monomer units in chains with a certain fraction of monomer  $ M_2 $. In Figure 5 the chemical distributions at  $ t = 10, 50, 100, 200, 400 $, and 600 s reaction time are plotted using a small smoothing index. As expected, the peaks move from the right to the left, whereas for  $ t = 600 $ s (dotted line) there is a significant amount of polymer without monomer  $ M_2 $ (a bit decreased in the graphic because of the smoothing).

A very important product index is provided by  $ \overline{F}(s,t) $, the time-dependent average number of comonomers in chains of a certain chain length s (we will make use of this distribution in the next example). In Figure 6 results for the h-p-method (straight line, based on balance distributions) and three MC scenarios are summarized, where we have

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time [s]</th><th style='text-align: center;'>h-p-method</th><th style='text-align: center;'>MC-100-1000</th><th style='text-align: center;'>MC-200-2000</th><th style='text-align: center;'>MC-500-5000</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>185</td><td style='text-align: center;'>195</td><td style='text-align: center;'>200</td><td style='text-align: center;'>205</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>175</td><td style='text-align: center;'>185</td><td style='text-align: center;'>190</td><td style='text-align: center;'>195</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>165</td><td style='text-align: center;'>175</td><td style='text-align: center;'>180</td><td style='text-align: center;'>185</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>158</td><td style='text-align: center;'>168</td><td style='text-align: center;'>170</td><td style='text-align: center;'>178</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>150</td><td style='text-align: center;'>160</td><td style='text-align: center;'>165</td><td style='text-align: center;'>172</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>145</td><td style='text-align: center;'>155</td><td style='text-align: center;'>160</td><td style='text-align: center;'>168</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>140</td><td style='text-align: center;'>150</td><td style='text-align: center;'>155</td><td style='text-align: center;'>165</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>135</td><td style='text-align: center;'>145</td><td style='text-align: center;'>150</td><td style='text-align: center;'>162</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>130</td><td style='text-align: center;'>140</td><td style='text-align: center;'>145</td><td style='text-align: center;'>158</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>125</td><td style='text-align: center;'>135</td><td style='text-align: center;'>140</td><td style='text-align: center;'>155</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>120</td><td style='text-align: center;'>130</td><td style='text-align: center;'>135</td><td style='text-align: center;'>152</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>118</td><td style='text-align: center;'>128</td><td style='text-align: center;'>132</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>115</td><td style='text-align: center;'>125</td><td style='text-align: center;'>128</td><td style='text-align: center;'>148</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>112</td><td style='text-align: center;'>122</td><td style='text-align: center;'>125</td><td style='text-align: center;'>145</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>110</td><td style='text-align: center;'>120</td><td style='text-align: center;'>122</td><td style='text-align: center;'>142</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>108</td><td style='text-align: center;'>118</td><td style='text-align: center;'>120</td><td style='text-align: center;'>140</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>105</td><td style='text-align: center;'>115</td><td style='text-align: center;'>118</td><td style='text-align: center;'>138</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>102</td><td style='text-align: center;'>112</td><td style='text-align: center;'>115</td><td style='text-align: center;'>135</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>100</td><td style='text-align: center;'>110</td><td style='text-align: center;'>112</td><td style='text-align: center;'>132</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>98</td><td style='text-align: center;'>108</td><td style='text-align: center;'>110</td><td style='text-align: center;'>130</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>95</td><td style='text-align: center;'>105</td><td style='text-align: center;'>108</td><td style='text-align: center;'>128</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>92</td><td style='text-align: center;'>102</td><td style='text-align: center;'>105</td><td style='text-align: center;'>125</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>90</td><td style='text-align: center;'>100</td><td style='text-align: center;'>102</td><td style='text-align: center;'>122</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>88</td><td style='text-align: center;'>98</td><td style='text-align: center;'>100</td><td style='text-align: center;'>120</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time [s]</th><th style='text-align: center;'>h-p-method [Mv #]</th><th style='text-align: center;'>MC-100-1000 [Mv #]</th><th style='text-align: center;'>MC-200-2000 [Mv #]</th><th style='text-align: center;'>MC-500-5000 [Mv #]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>380</td><td style='text-align: center;'>380</td><td style='text-align: center;'>380</td><td style='text-align: center;'>380</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>360</td><td style='text-align: center;'>360</td><td style='text-align: center;'>360</td><td style='text-align: center;'>360</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>340</td><td style='text-align: center;'>340</td><td style='text-align: center;'>340</td><td style='text-align: center;'>340</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>305</td><td style='text-align: center;'>305</td><td style='text-align: center;'>305</td><td style='text-align: center;'>305</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>295</td><td style='text-align: center;'>295</td><td style='text-align: center;'>295</td><td style='text-align: center;'>295</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>285</td><td style='text-align: center;'>285</td><td style='text-align: center;'>285</td><td style='text-align: center;'>285</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>275</td><td style='text-align: center;'>275</td><td style='text-align: center;'>275</td><td style='text-align: center;'>275</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>265</td><td style='text-align: center;'>265</td><td style='text-align: center;'>265</td><td style='text-align: center;'>265</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>255</td><td style='text-align: center;'>255</td><td style='text-align: center;'>255</td><td style='text-align: center;'>255</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>245</td><td style='text-align: center;'>245</td><td style='text-align: center;'>245</td><td style='text-align: center;'>245</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>240</td><td style='text-align: center;'>240</td><td style='text-align: center;'>240</td><td style='text-align: center;'>240</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>235</td><td style='text-align: center;'>235</td><td style='text-align: center;'>235</td><td style='text-align: center;'>235</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>230</td><td style='text-align: center;'>230</td><td style='text-align: center;'>230</td><td style='text-align: center;'>230</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>225</td><td style='text-align: center;'>225</td><td style='text-align: center;'>225</td><td style='text-align: center;'>225</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>220</td><td style='text-align: center;'>220</td><td style='text-align: center;'>220</td><td style='text-align: center;'>220</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>215</td><td style='text-align: center;'>215</td><td style='text-align: center;'>215</td><td style='text-align: center;'>215</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>210</td><td style='text-align: center;'>210</td><td style='text-align: center;'>210</td><td style='text-align: center;'>210</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>205</td><td style='text-align: center;'>205</td><td style='text-align: center;'>205</td><td style='text-align: center;'>205</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>195</td><td style='text-align: center;'>195</td><td style='text-align: center;'>195</td><td style='text-align: center;'>195</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>190</td><td style='text-align: center;'>190</td><td style='text-align: center;'>190</td><td style='text-align: center;'>190</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>185</td><td style='text-align: center;'>185</td><td style='text-align: center;'>185</td><td style='text-align: center;'>185</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 3. Comparison between deterministic and stochastic method for the (a) number mean value  $ M_{n} $ of the polymer and (b) weight mean value  $ M_{w} $ of the polymer.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time [s]</th><th style='text-align: center;'>h-p-method</th><th style='text-align: center;'>MC-100-1000</th><th style='text-align: center;'>MC-200-2000</th><th style='text-align: center;'>MC-500-5000</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.58</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.36</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.33</td><td style='text-align: center;'>0.33</td><td style='text-align: center;'>0.33</td><td style='text-align: center;'>0.33</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.27</td><td style='text-align: center;'>0.27</td><td style='text-align: center;'>0.27</td><td style='text-align: center;'>0.27</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.23</td><td style='text-align: center;'>0.23</td><td style='text-align: center;'>0.23</td><td style='text-align: center;'>0.23</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>0.21</td><td style='text-align: center;'>0.21</td><td style='text-align: center;'>0.21</td><td style='text-align: center;'>0.21</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>0.19</td><td style='text-align: center;'>0.19</td><td style='text-align: center;'>0.19</td><td style='text-align: center;'>0.19</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>0.17</td><td style='text-align: center;'>0.17</td><td style='text-align: center;'>0.17</td><td style='text-align: center;'>0.17</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.16</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.14</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>0.13</td><td style='text-align: center;'>0.13</td><td style='text-align: center;'>0.13</td><td style='text-align: center;'>0.13</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>0.11</td><td style='text-align: center;'>0.11</td><td style='text-align: center;'>0.11</td><td style='text-align: center;'>0.11</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>0.09</td><td style='text-align: center;'>0.09</td><td style='text-align: center;'>0.09</td><td style='text-align: center;'>0.09</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.08</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 4. Polymer composition as cumulative molar fraction of the comonomer  $ M_{2} $ in all chains. Good agreement between deterministic (reference) and MC-results.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>fraction M2</th><th style='text-align: center;'>Black</th><th style='text-align: center;'>Red</th><th style='text-align: center;'>Green</th><th style='text-align: center;'>Blue</th><th style='text-align: center;'>Cyan</th><th style='text-align: center;'>Yellow</th><th style='text-align: center;'>Red</th><th style='text-align: center;'>Green</th><th style='text-align: center;'>Blue</th><th style='text-align: center;'>Cyan</th><th style='text-align: center;'>Yellow</th><th style='text-align: center;'>Red</th><th style='text-align: center;'>Green</th><th style='text-align: center;'>Blue</th><th style='text-align: center;'>Cyan</th><th style='text-align: center;'>Yellow</th><th style='text-align: center;'>Red</th><th style='text-align: center;'>Green</th><th style='text-align: center;'>Blue</th><th style='text-align: center;'>Cyan</th><th style='text-align: center;'>Yellow</th><th style='text-align: center;'>Red</th><th style='text-align: center;'>Green</th><th style='text-align: center;'>Blue</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 5. Chemical distribution at  $ t=10, 50, 100, 200, 400 $, and 600s (peaks move from right to left) of polymer obtained by MC-method. A slight smoothing has been applied.</div>


set down the smallest ensembles to only 100 living and 500 dead chains.

Again, the simulation with the largest ensembles delivers slightly better results (and would even be more accurate if we had averaged several runs), but also for the smallest number of chains, the obtained profile will provide valuable information in many applications. The additional computing time induced by the MC method for this example (h-p-method, tolerance 0.003), is only 75% for the smallest scenario, but 200 and 800% (summing up to 500 s CPU on a 2.66 GHz processor) for the mean and the largest ensembles.

As expected, for the consideration of the copolymerization aspects, the longest simulation is not necessary, since the MC results for the fractions are much more accurate.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length</th><th style='text-align: center;'>h-p-method</th><th style='text-align: center;'>MC-100-500</th><th style='text-align: center;'>MC-200-2000</th><th style='text-align: center;'>MC-500-5000</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.125</td><td style='text-align: center;'>0.115</td><td style='text-align: center;'>0.105</td><td style='text-align: center;'>0.11</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.145</td><td style='text-align: center;'>0.135</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>0.125</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.165</td><td style='text-align: center;'>0.155</td><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.145</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.185</td><td style='text-align: center;'>0.175</td><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.165</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.205</td><td style='text-align: center;'>0.195</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.185</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.225</td><td style='text-align: center;'>0.215</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.205</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 6. Chain-length dependent molar fraction  $ F_{2}(s) $ of comonomer in polymer. Comparison between results of Galerkin h-p-method using balance calculus (can be considered as reference) and different realizations of the MC-method.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length</th><th style='text-align: center;'>fraction M2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-0.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-1.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-2.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-3.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-4.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-5.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-6.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-7.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-8.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-9.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-10.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-11.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-12.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-13.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-14.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-15.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-16.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-17.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-18.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-19.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-20.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-21.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-22.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-23.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-24.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-25.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-26.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-27.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-28.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-29.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-30.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-31.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-32.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-33.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-34.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-35.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-36.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-37.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-38.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-39.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.05</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.15</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.25</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.35</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.45</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.55</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.65</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.75</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.85</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-40.95</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>-41.0</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length</th><th style='text-align: center;'>fraction M2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.61</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.52</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.45</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.32</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.28</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.24</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.17</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.13</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.11</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.09</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.07</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>570</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>580</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>590</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>610</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>620</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>630</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>640</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>660</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>670</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>680</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>690</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>710</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>720</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>730</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>740</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>760</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>770</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>780</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>790</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>810</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>820</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>830</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>840</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>860</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>870</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>880</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>890</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>910</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>920</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>930</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>940</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>960</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>970</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>980</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>990</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>10</th><th style='text-align: center;'>0.00</th></tr></thead>
  <tbody>
  </tbody>
</table>

<div style="text-align: center;">Figure 7. Plot of comonomer fraction in all single chains of the MC-ensemble (a) at early reaction time  $ t = 60 \, s $, MC-500-5000. The straight line describes the average; (b) at final reaction time  $ t = 600 \, s $, MC-500-5000 and (c) at final reaction time  $ t = 600 \, s $ for a small MC-ensemble, setting MC-100-500. The thick straight line describes the average obtained by regression; the thin straight line is the average from the Galerkin method.</div>


than for the CLD itself and this is a main argument for this hybrid algorithm.

For the computation of the MC averages we again have applied a grid-based interpolation technique. Actually, one should not base the convergence analysis on single runs of the MC method, but use mean values of several realizations. In practice, however, a modeler will try to get important structure information from one or very few simulations. Therefore we try to mimic this behavior in our numerical experiments. In the next example we will see, that sometimes at least a few realizations have to be averaged.

At last we take a look at the full ensemble of chains. The three graphics of Figure 7 show, how nicely the hybrid MC algorithm behaves here. For  $ t = 60 \, s $, the distribution of fractions vs. chain-length is relatively narrow (scenario MC 500–5000), and the average (automatic polynomial regression) is very close to the average  $ \overline{F}_2(s, 60) $ of the h-p-method. For  $ t = 600 \, s $ the single chains are broadly distributed, but again the average is nicely captured. In Figure 7c one can see, that if only 100 and 500 chains are used, the structure of the full distribution is still visible with very accurate average. Besides, for this simple curve-structure a polynomial regression might be sufficient, but the h-p-interval-based approach (used in Figure 6) is more general and can be done automatically.

In retrospect, we have seen that with the hybrid approach we have combined the advantages of both worlds by computing the basic chain-length distributions deterministically and add further properties using a MC (SSA) based on relatively small ensembles of chains. In particular we could present the full chemical distribution with much less effort than in a full-scale SSA.

## Additional Long-Chain Branching with Forward Coupling

For our second examination we extend the previous example by a transfer-to-polymer reaction and assume, that each transfer step will lead to a long-chain branch (LCB). A more practical example including the formation of secondary radicals and subsequent  $ \beta $-scission might be considered in a forthcoming article. For now, we add another index j to the system counting the number of LCBs in chains of length s with i comonomer units, i.e., we consider polymer species  $ P_{s,ij} $ and  $ D_{s,ij} $. The basic reaction scheme then is:

 $$ \begin{array}{c}C\xrightarrow{k_{a}}P_{1,0,0}\\P_{s,i,j}+M_{1}\xrightarrow{k_{p_{1}}}P_{s+1,i,j}+C_{1}\\P_{s,i,j}+M_{2}\xrightarrow{k_{p_{2}}}P_{s+1,i+1,j}+C_{2}\\P_{s,i,j}\xrightarrow{k_{d}}D_{s,i,j}\\r,i,j+D_{r,k,l}\xrightarrow{g(r,k,l)k_{tr}}D_{s,i,j}+P_{r,k,l+1}\end{array} $$ 

with reaction rate coefficient  $ k_{tr} $ from Table 3. Its value has been set in order to generate a final polydispersity of about 7, which is fairly (but not too) broad. A reduction to an only chain-length-based description reads (introducing another counter species  $ C_{lcb} $):

The rate function  $ g(r, k, l) $ of the three-dimensional model is crucial for the reaction rate of the transfer-to-polymer step. For example, if the transfer can only occur (once) at comonomer units, we have  $ g(r, k, l) = k - l $. If the transfer is possible along the whole chain, one often sets  $ g(r, k, l) = r - l \approx r $. For the reduced system (32), the rate function has to be replaced by an average. Here typical settings are  $ \tilde{g}(r) = F_2(t) $,  $ F_2(t) $ the accumulated fraction of monomer  $ M_2 $ in the whole polymer, or more accurately:

 $$ \begin{array}{c}C\xrightarrow{k_{a}}P_{1}\\P_{s}+M_{1}\xrightarrow{k_{p_{1}}}P_{s+1}+C_{1}\\P_{s}+M_{2}\xrightarrow{k_{p_{2}}}P_{s+1}+C_{2}\\P_{s}\xrightarrow{k_{d}}D_{s}\\P_{s}+D_{r}\xrightarrow{\tilde{g}(r)}D_{s}+P_{r}+C_{lcb}\end{array} $$ 

This means, that we count the overall number of incorporated comonomer molecules and the number of branches and assume, that all chains have an average composition and branching structure. Despite this strong assumption, such models have turned out to be quite successful in applications. However, it is one major aspect of the hybrid method to study and validate (or falsify) such assumptions without too much mathematical and numerical effort. In Figure 7a–c we could observe, that with increasing reaction time the average number of comonomer units describes the full distribution of chains less and less. Thus the task of this example is to check the effect of distributed fractions. Since the number of transfer-reactions is small compared to the number of comonomers (i.e.,  $ C_2 \ll C_{lcb} $) in this example, for ease of presentation we will not consider the aspect of “consumed bonds” used described in numerator of (33). If one applies the balance distribution calculus to the full system (31), one can define a refined rate function by:

 $$ \tilde{g}(r,t)=\frac{C_{2}(t)-C_{lcb}(t)}{C_{1}(t)+C_{2}(t)}r. $$ 

with  $ \overline{F}_{2}(r,t) $ again the chain-length dependent fraction of the comonomer. Before we discuss the results, we have to explain, how the chain-length dependency has been realized within the MC method. Assume that at a certain stage for a given chain  $ P_{s} $ a partner chain for the

 $$ \overline{{g}}(r,t)=\overline{{F}}_{2}(r,t)r, $$ 

transfer-to-polymer step has to be selected. Instead of randomly choosing one chain out of the ensemble of dead polymers, we have to consider that—in the current averaged setting, where we assume, that the incorporated number of comonomers is proportional to the chain length—longer chains have a higher probability in view of the transfer. The following algorithm will support this:

1. Compute  $ s_{total} = \sum_{i=1}^{n_P} e_s^i $, i.e., we compute the total chain length of all chains  $ e^i $ in the ensemble  $ E $ with  $ n_P $ chains.

2. Take a new random number  $  z \in (0, 1]  $.

3. Choose  $ 1 \leq j \leq n_P $ such that  $ s_{\text{sub}}(j - 1)/s_{\text{total}} < z $ and  $ s_{\text{sub}}(j)/s_{\text{total}} \geq z $, where  $ s_{\text{sub}}(j) = \sum_{i=1}^j e_s^i $.

This is quite similar to the selection of the reaction steps in the modified Gillespie algorithm and leads to the required statistical behavior. For a validation of the extended system we perform simulations with ensembles sizes  $ m_{p}=200 $,  $ m_{D}=1000 $. In Figure 8a and b the mean values are compared. In this example, the perturbations are much bigger than before. The explanation is simple: due to the high dispersity, a few, very long chains affect the mean values drastically. In the deterministic approach, this induces not much problems (except that it requires a careful error control), but for the MC method there is some sensitivity. Nevertheless, if we perform three subsequent simulations, the obtained averages give a good estimate of the “real” mean values. This is improved, if we run ten consecutive simulations and compare  $ M_{n} $ to the MC-average and its standard deviation in Figure 8c. For the full distribution, a comparison of the concentration distribution looks similar to Figure 1 and the respective error estimates are also comparable, therefore we omit these pictures here.

Instead, we concentrate on the new aspect, the branching index. Figure 9a presents the fraction of branched monomer units per chain molecule (i.e., j/s) of all dead chains, the averages obtained from the MC method (thin line) and by the balance calculus of h-p-method (thick straight line) at the end of the reaction. Here we present the results of the  $ m_p = 500 $,  $ m_D = 5000 $ scenario.

The average of the hybrid MC method is very accurate, but we can observe, that there are many chains even without a branch (black box at the left bottom), actually in this single simulation we have 3325 out of 5000 chains without a branch. One can easily compute such a ratio with the purely deterministic method too by introducing additional polymer species describing branched polymer only  $ (1) $. However, we note again, that we want to keep the basic model as simple as possible and try to get as much as information as possible out of the hybrid approach. In Figure 9b the same kind of results are summarized for a simulation with  $ m_{p} = 200 $,  $ m_{D} = 1000 $.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time [s]</th><th style='text-align: center;'>h-p</th><th style='text-align: center;'>MC1</th><th style='text-align: center;'>MC3</th><th style='text-align: center;'>MC2</th><th style='text-align: center;'>Average</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>192</td><td style='text-align: center;'>192</td><td style='text-align: center;'>192</td><td style='text-align: center;'>192</td><td style='text-align: center;'>192</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td><td style='text-align: center;'>180</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td><td style='text-align: center;'>170</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td><td style='text-align: center;'>160</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>158</td><td style='text-align: center;'>158</td><td style='text-align: center;'>158</td><td style='text-align: center;'>158</td><td style='text-align: center;'>158</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>155</td><td style='text-align: center;'>155</td><td style='text-align: center;'>155</td><td style='text-align: center;'>155</td><td style='text-align: center;'>155</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td><td style='text-align: center;'>150</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>145</td><td style='text-align: center;'>145</td><td style='text-align: center;'>145</td><td style='text-align: center;'>145</td><td style='text-align: center;'>145</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td><td style='text-align: center;'>140</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>135</td><td style='text-align: center;'>135</td><td style='text-align: center;'>135</td><td style='text-align: center;'>135</td><td style='text-align: center;'>135</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td><td style='text-align: center;'>130</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>125</td><td style='text-align: center;'>125</td><td style='text-align: center;'>125</td><td style='text-align: center;'>125</td><td style='text-align: center;'>125</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>122</td><td style='text-align: center;'>122</td><td style='text-align: center;'>122</td><td style='text-align: center;'>122</td><td style='text-align: center;'>122</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td><td style='text-align: center;'>120</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>118</td><td style='text-align: center;'>118</td><td style='text-align: center;'>118</td><td style='text-align: center;'>118</td><td style='text-align: center;'>118</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>115</td><td style='text-align: center;'>115</td><td style='text-align: center;'>115</td><td style='text-align: center;'>115</td><td style='text-align: center;'>115</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>112</td><td style='text-align: center;'>112</td><td style='text-align: center;'>112</td><td style='text-align: center;'>112</td><td style='text-align: center;'>112</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td><td style='text-align: center;'>110</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>108</td><td style='text-align: center;'>108</td><td style='text-align: center;'>108</td><td style='text-align: center;'>108</td><td style='text-align: center;'>108</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>105</td><td style='text-align: center;'>105</td><td style='text-align: center;'>105</td><td style='text-align: center;'>105</td><td style='text-align: center;'>105</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>102</td><td style='text-align: center;'>102</td><td style='text-align: center;'>102</td><td style='text-align: center;'>102</td><td style='text-align: center;'>102</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>98</td><td style='text-align: center;'>98</td><td style='text-align: center;'>98</td><td style='text-align: center;'>98</td><td style='text-align: center;'>98</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>95</td><td style='text-align: center;'>95</td><td style='text-align: center;'>95</td><td style='text-align: center;'>95</td><td style='text-align: center;'>95</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>92</td><td style='text-align: center;'>92</td><td style='text-align: center;'>92</td><td style='text-align: center;'>92</td><td style='text-align: center;'>92</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time [s]</th><th style='text-align: center;'>h-p-method [Mw #]</th><th style='text-align: center;'>MC1 [Mw #]</th><th style='text-align: center;'>MC3 [Mw #]</th><th style='text-align: center;'>MC2 [Mw #]</th><th style='text-align: center;'>Average [Mw #]</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td><td style='text-align: center;'>320</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>480</td><td style='text-align: center;'>480</td><td style='text-align: center;'>480</td><td style='text-align: center;'>480</td><td style='text-align: center;'>480</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td><td style='text-align: center;'>550</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td><td style='text-align: center;'>600</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td><td style='text-align: center;'>650</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td><td style='text-align: center;'>700</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td><td style='text-align: center;'>750</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>780</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td><td style='text-align: center;'>800</td><td style='text-align: center;'>780</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>800</td><td style='text-align: center;'>850</td><td style='text-align: center;'>850</td><td style='text-align: center;'>850</td><td style='text-align: center;'>800</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>820</td><td style='text-align: center;'>880</td><td style='text-align: center;'>880</td><td style='text-align: center;'>880</td><td style='text-align: center;'>820</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>850</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td><td style='text-align: center;'>900</td><td style='text-align: center;'>850</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>880</td><td style='text-align: center;'>920</td><td style='text-align: center;'>920</td><td style='text-align: center;'>920</td><td style='text-align: center;'>880</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>900</td><td style='text-align: center;'>950</td><td style='text-align: center;'>950</td><td style='text-align: center;'>950</td><td style='text-align: center;'>900</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 8. Comparison between deterministic and stochastic method for the (a) number mean value of the polymer in LCB example and (b) the weight mean value of the polymer in LCB example. The average describes the mean of three MC-realizations. (c) Refined comparison between deterministic and stochastic method for the number mean value of the polymer in LCB example. The average describes the mean of ten MC-realizations. An estimate of the standard deviation s is added.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length</th><th style='text-align: center;'>fraction LCB</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>625</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>675</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>725</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>775</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>825</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>875</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>925</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>975</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>0.000</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length</th><th style='text-align: center;'>fraction LCB</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>65</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>70</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>80</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>85</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>90</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>95</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>105</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>110</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>115</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>120</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>130</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>135</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>140</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>145</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>155</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>160</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>165</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>170</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>180</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>185</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>190</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>195</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>205</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>210</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>215</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>220</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>230</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>235</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>240</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>245</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>255</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>260</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>265</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>270</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>280</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>285</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>290</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>295</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>305</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>310</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>315</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>320</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>330</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>335</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>340</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>345</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>355</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>360</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>365</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>370</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>380</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>385</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>390</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>395</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>405</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>410</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>415</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>420</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>430</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>435</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>440</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>445</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>455</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>460</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>465</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>470</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>480</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>485</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>490</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>495</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>505</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>510</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>515</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>520</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>530</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>535</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>540</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>545</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>555</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>560</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>565</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>570</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>580</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>585</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>590</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>595</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>605</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>610</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>615</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>620</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>625</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>630</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>635</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>640</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>645</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>655</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>660</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>665</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>670</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>675</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>680</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>685</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>690</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>695</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>705</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>710</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>715</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>720</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>725</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>730</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>735</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>740</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>745</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>755</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>760</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>765</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>770</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>775</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>780</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>785</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>790</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>795</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>805</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>810</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>815</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>820</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>825</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>830</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>835</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>840</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>845</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>855</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>860</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>865</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>870</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>875</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>880</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>885</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>890</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>895</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>905</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>910</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>915</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>920</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>925</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>930</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>935</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>940</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>945</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>955</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>960</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>965</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>970</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>975</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>980</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>985</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>990</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>995</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>998</td><td style='text-align: center;'>0.000</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length</th><th style='text-align: center;'>fraction M2</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.61</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.55</td></tr>
    <tr><td style='text-align: center;'>75</td><td style='text-align: center;'>0.48</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.42</td></tr>
    <tr><td style='text-align: center;'>125</td><td style='text-align: center;'>0.38</td></tr>
    <tr><td style='text-align: center;'>150</td><td style='text-align: center;'>0.35</td></tr>
    <tr><td style='text-align: center;'>175</td><td style='text-align: center;'>0.32</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.30</td></tr>
    <tr><td style='text-align: center;'>225</td><td style='text-align: center;'>0.28</td></tr>
    <tr><td style='text-align: center;'>250</td><td style='text-align: center;'>0.26</td></tr>
    <tr><td style='text-align: center;'>275</td><td style='text-align: center;'>0.24</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>0.22</td></tr>
    <tr><td style='text-align: center;'>325</td><td style='text-align: center;'>0.20</td></tr>
    <tr><td style='text-align: center;'>350</td><td style='text-align: center;'>0.18</td></tr>
    <tr><td style='text-align: center;'>375</td><td style='text-align: center;'>0.16</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>0.15</td></tr>
    <tr><td style='text-align: center;'>425</td><td style='text-align: center;'>0.14</td></tr>
    <tr><td style='text-align: center;'>450</td><td style='text-align: center;'>0.13</td></tr>
    <tr><td style='text-align: center;'>475</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>0.11</td></tr>
    <tr><td style='text-align: center;'>525</td><td style='text-align: center;'>0.10</td></tr>
    <tr><td style='text-align: center;'>550</td><td style='text-align: center;'>0.09</td></tr>
    <tr><td style='text-align: center;'>575</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>0.07</td></tr>
    <tr><td style='text-align: center;'>625</td><td style='text-align: center;'>0.06</td></tr>
    <tr><td style='text-align: center;'>650</td><td style='text-align: center;'>0.05</td></tr>
    <tr><td style='text-align: center;'>675</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>725</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>750</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>775</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>825</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>850</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>875</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>925</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>950</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>975</td><td style='text-align: center;'>0.00</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>0.00</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 9. Plot of branching fraction in all single chains of MC-ensemble (a) at final reaction time for the LCB case at t = 600 s, setting MC-500-5000. The thick straight line describes the average obtained by regression; the thin straight line is the average obtained by our Galerkin method; (b) at final reaction time for the LCB case and small MC-ensemble at t = 600 s, setting MC-200-1000. The thick straight line describes the average obtained by regression; the thin straight line is the average obtained by the Galerkin method. It can be seen, that many chains have no branching point at all. (c) Plot of comonomer fraction in all single chains of the MC-ensemble at final reaction time for the LCB case and large MC-ensemble at t = 600 s, setting MC-500-5000. The thick straight line describes the average obtained by regression; the thin straight line is the average obtained by our Galerkin method. Due to the transfer-to-polymer, the comonomer is more distributed in the ensemble than in Figure 7a.</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>No branches</th><th style='text-align: center;'>Fraction</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.09</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0.01</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>0.009</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0.008</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>0.006</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.003</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>0.004</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0.005</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>0.007</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0.004</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.003</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>0.0011</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>0.0012</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>0.0004</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>0.0001</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.0008</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>0.0011</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>0.0003</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>0.0004</td></tr>
  </tbody>
</table>

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>No. branches</th><th style='text-align: center;'>Fraction</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0.98</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0.12</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>0.09</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0.08</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>0.06</td></tr>
    <tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0.04</td></tr>
    <tr><td style='text-align: center;'>7</td><td style='text-align: center;'>0.03</td></tr>
    <tr><td style='text-align: center;'>8</td><td style='text-align: center;'>0.02</td></tr>
    <tr><td style='text-align: center;'>9</td><td style='text-align: center;'>0.015</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.012</td></tr>
    <tr><td style='text-align: center;'>11</td><td style='text-align: center;'>0.013</td></tr>
    <tr><td style='text-align: center;'>12</td><td style='text-align: center;'>0.014</td></tr>
    <tr><td style='text-align: center;'>13</td><td style='text-align: center;'>0.012</td></tr>
    <tr><td style='text-align: center;'>14</td><td style='text-align: center;'>0.009</td></tr>
    <tr><td style='text-align: center;'>15</td><td style='text-align: center;'>0.008</td></tr>
    <tr><td style='text-align: center;'>16</td><td style='text-align: center;'>0.004</td></tr>
    <tr><td style='text-align: center;'>17</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>18</td><td style='text-align: center;'>0.0001</td></tr>
    <tr><td style='text-align: center;'>19</td><td style='text-align: center;'>0.0003</td></tr>
    <tr><td style='text-align: center;'>20</td><td style='text-align: center;'>0.0007</td></tr>
    <tr><td style='text-align: center;'>21</td><td style='text-align: center;'>0.0003</td></tr>
    <tr><td style='text-align: center;'>22</td><td style='text-align: center;'>0.0002</td></tr>
    <tr><td style='text-align: center;'>23</td><td style='text-align: center;'>0.0001</td></tr>
    <tr><td style='text-align: center;'>24</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>25</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>26</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>27</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>28</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>29</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>30</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>31</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>32</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>33</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>34</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>35</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>36</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>37</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>38</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>39</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>40</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>41</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>42</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>43</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>44</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>45</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>46</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>47</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>48</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>49</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>50</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>51</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>52</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>53</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>54</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>55</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>56</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>57</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>58</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>59</td><td style='text-align: center;'>0.0000</td></tr>
    <tr><td style='text-align: center;'>60</td><td style='text-align: center;'>0.0000</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 10. (a) Fraction of chains for proportional chain transfer with a certain number of branches in a logarithmic scale indicating an exponential decay of branches. (b) Fraction of chains with a certain number of branches for the case with back coupling of MC-results to kinetic rate equations. Dotted line: proportional case.</div>


As for the comonomer fraction in the copolymerization example, averages and overall structure are nicely kept. A comparison of Figure 9c ( $ M_{2} $ fraction vs. chain-length for the LCB-case) with Figure 7a reveals, that due to the transfer-to-polymer process the comonomer fraction is more equilibrated.

In Figure 10a we plot the percentage of chains with a certain number of branches in a logarithmic scale. The roughly linear decrease indicates that we can expect an exponential decay of the branching number in such systems. This could already be shown in deterministic systems by introducing polymer populations for each branching number (numerical fractionation), but such a treatment tends to be complicated from a number of about ten branches per chain.

## Long-Chain Branching with Backward Coupling

In the previous part of this example, the MC part of the algorithm has only been used to produce additional results without a feedback to the deterministic system. This will be done now. For that we perform the MC transfer-to-polymer step with a slight variation of the algorithm described above: instead of the chain-length we use the comonomer index of each chain. By that we select chains for transfer according to the number of available comonomers — not as average, but individually for each single transfer step. On the deterministic side of the algorithm, where such a detailed treatment is not available in the basic formulation with only one property (chain-length), we have to use an averaged rate again, but now we can apply a chain-length dependent transfer rate (34) instead of the general average (33). In a purely deterministic system we could also apply the balance distribution approach again (and have for comparison), but here we restrict to minimal effort by evaluating the average  $ \overline{F}_2(r,t) $ directly from the MC population, oriented again on the current h-p-grid of the deterministic population. Instead of repeating all kind of results for this modified example, we only take a look at some differences.

• The polydispersity index is smaller (Figure 11).

- There seem to be more chains without branches (plausible) and more chains with many branches (range up to 60 instead 23 in the proportional example, Figure 10b).

- This is backed by Figure 12, where again (for MC 200-1 000) the branching fraction is shown. The straight line is the result from the proportional approach (Figure 9b).

The most important aspect in view of the development of the hybrid algorithm is, that both parts of the algorithm

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>time [s]</th><th style='text-align: center;'>Proportional</th><th style='text-align: center;'>MC-Transfer</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>2</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>3.2</td><td style='text-align: center;'>3.2</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>4.5</td><td style='text-align: center;'>4.5</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>5.5</td><td style='text-align: center;'>5.5</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>6.2</td><td style='text-align: center;'>6.2</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>6.8</td><td style='text-align: center;'>6.8</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>7.0</td><td style='text-align: center;'>7.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 11. Comparison of polydispersity between the two LCB models (averaged and MC-based).</div>


<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>chain length</th><th style='text-align: center;'>fraction LCB</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.001</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.002</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.003</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.004</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.005</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.006</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.007</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.008</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.009</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.011</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.012</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.013</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.014</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.015</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.016</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.017</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.018</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.019</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.021</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.022</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.023</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.024</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.025</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.026</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.027</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.028</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.029</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.030</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.031</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.032</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.033</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.034</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.035</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.036</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.037</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.038</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.039</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.040</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.041</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.042</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.043</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.044</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.045</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.046</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.047</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.048</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.049</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.050</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.051</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.052</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.053</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.054</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.056</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.057</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.058</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.059</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.060</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.061</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.062</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.063</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.064</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.065</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.066</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.067</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.068</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.069</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.070</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.071</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.072</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.073</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.074</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.075</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.076</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.077</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.078</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.079</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.080</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.081</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.082</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.083</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.084</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.085</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.086</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.087</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.088</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.089</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.090</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.091</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.092</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.093</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.094</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.095</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.096</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.097</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.098</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.099</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.100</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.101</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.102</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.103</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.104</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.105</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.106</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.107</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.108</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.109</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.110</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.111</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.112</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.113</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.114</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.115</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.116</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.117</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.118</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.119</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.120</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.121</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.122</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.123</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.124</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.125</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.126</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.127</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.128</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.129</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.130</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.131</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.132</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.133</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.134</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.135</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.136</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.137</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.138</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.139</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.140</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.141</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.142</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.143</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.144</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.145</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.146</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.147</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.148</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.149</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.150</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.151</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.152</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.153</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.154</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.155</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.156</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.157</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.158</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.159</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.160</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.161</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.162</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.163</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.164</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.165</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.166</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.167</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.168</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.169</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.170</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.171</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.172</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.173</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.174</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.175</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.176</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.177</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.178</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.179</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.180</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.181</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.182</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.183</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.184</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.185</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.186</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.187</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.188</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.189</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.190</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.191</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.192</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.193</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.194</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.195</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.196</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.197</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.198</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.199</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.200</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.201</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.202</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.203</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.204</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.205</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.206</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.207</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.208</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.209</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.210</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.211</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.212</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.213</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.214</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.215</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.216</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.217</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.218</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.219</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.220</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.221</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.222</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.223</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.224</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.225</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.226</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.227</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.228</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.229</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.230</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.231</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.232</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.233</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.234</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.235</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.236</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.237</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.238</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.239</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.240</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.241</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.242</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.243</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.244</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.245</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.246</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.247</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.248</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.249</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.250</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.251</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.252</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.253</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.254</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.255</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.256</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.257</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.258</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.259</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.260</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.261</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.262</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.263</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.264</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.265</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.266</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.267</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.268</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.269</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.270</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.271</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.272</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.273</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.274</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.275</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.276</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.277</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.278</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.279</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.280</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.281</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.282</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.283</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.284</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.285</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.286</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.287</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.288</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.289</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.290</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.291</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.292</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.293</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.294</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.295</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.296</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.297</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.298</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.299</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.300</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.301</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.302</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.303</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.304</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.305</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.306</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.307</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.308</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.309</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.310</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.311</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.312</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.313</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.314</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.315</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.316</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.317</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.318</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.319</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.320</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.321</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.322</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.323</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.324</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.325</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.326</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.327</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.328</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.329</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.330</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.331</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.332</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.333</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.334</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.335</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.336</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.337</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.338</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.339</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.340</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.341</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.342</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.343</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.344</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.345</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.346</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.347</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.348</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.349</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.350</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.351</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.352</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.353</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.354</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.355</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.356</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.357</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.358</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.359</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.360</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.361</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.362</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.363</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.364</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.365</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.366</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.367</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.368</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.369</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.370</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.371</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.372</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.373</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.374</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.375</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.376</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.377</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.378</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.379</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.380</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.381</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.382</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.383</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.384</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.385</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.386</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.387</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.388</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.389</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.390</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.391</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.392</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.393</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.394</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.395</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.396</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.397</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.398</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.399</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.400</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.401</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.402</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.403</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.404</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.405</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.406</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.407</td></tr>
    <tr><td style='text-align: center;'>10</td><td style='text-align: center;'>0.408</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 12. Plot of branching fraction in all single chains of the MC-ensemble at final reaction time  $ t = 600 \, s $, MC-200-1000, for the LCB case with back-coupling for small MC-ensemble. The thick straight line describes the average obtained by regression; the thin straight line is the average obtained by the Galerkin method.</div>


affect each other and all results go together. In particular, the overall branching rate obtained from the counter species  $ C_{lcb} $ has the same time evolution as the direct number of branches of the MC method. Also the full distributions and their mean values have been used to validate the accuracy of the feedback of MC results into the deterministic equations.

## Conclusion

Summarizing, we have seen again, that deterministic solvers like Predici can efficiently and accurately compute chain-length distributions and even averages of polymer properties with respect to additional property indices, if we apply the balance distribution approach. However, the resolution of details of distributions of additional property indices is necessarily limited and a lot of mathematical and numerical preparations have to be done.

On the other hand, a pure MC method like SSA would be inefficient in comparison to Predici for all results Predici can obtain, but allows much more complete insight into details (which cannot be gained by Predici).

With the hybrid approach we have combined the advantages of both worlds by computing the basic chain-length distributions deterministically and add further properties using a variant of SSA based on relatively small ensembles of chains. The ensembles are small, since the chain-length distribution is already approximated by the deterministic solver. Therefore, there is no need to increase the size of the ensemble in order to balance the

statistical weighting due to the chain-length distribution, which, in turn, reduces the task to the approximation of the low copy number statistics along the additional property indices. In particular, we could present the full chemical distribution with small additional effort and efficiently compute related expectation values.

We have shown that the hybrid approach is based on a derivation of the hybrid model in which a rate equation for some part of the system with large copy numbers is coupled to a CME for the remainder of the system (or even the entire system again). In the hybrid model considered herein the two equations are coupled via averaged rates in lowest order of the smallness parameter  $ 1/N_{0} $ where  $ N_{0} $ is a reference number for the large copy numbers. Considering higher orders will result in more elaborated couplings. However, such refined couplings and their application to polymerization processes will be covered in future investigations.

Received: November 2, 2009; Revised: April 6, 2010; Published online: July 15, 2010; DOI: 10.1002/mren.200900073

Keywords: Galerkin method; hybrid algorithm; modeling; Monte-Carlo simulation; polymerization kinetics



[1] M. Wulkow, Macromol. React. Eng. 2008, 2, 461–494.

[2] A. Krallis, P. Pladis, C. Kiparissides, Macromol. Theory Simul. 2007, 16, 593–609.

[3] A. D. Peklak, A. Butté, G. Storti, M. Morbidelli, Macromol. Symp. 2004, 206, 481–494.

[4] P. D. Iedema, M. Wulkow, H. C. J. Hoefsloot, Macromolecules 2000, 33, 7173–7184.

[5] R. A. Hutchinson, Macromol. Theory Simul. 2001, 10, 144–157.

[6] H. Tobita, Polym. React. Eng. 1993, 3, 379.

[7] J. B. P. Soares, A. E. Hamielec, Macromol. React. Eng. 2007, 1, 53–67.

[8] H. Chaffey-Millar, D. B. Stewart, M. T. Chakravarty, G. Keller, C. Barner-Kowollik, Macromol. Theory Simul. 2007, 16, 575–592.

[9] P. Idema, H. Hoefsloot, Macromolecules 2006, 39, 3081–3088.

[10] D. T. Gillespie, J. Comput. Phys. 1976, 22, 403–434.

[11] D. T. Gillespie, J. Phys. Chem. 1977, 81, 2340.

[12] M. Busch, K. Becker, Macromol. Symp. 2007, 259, 295.