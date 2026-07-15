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