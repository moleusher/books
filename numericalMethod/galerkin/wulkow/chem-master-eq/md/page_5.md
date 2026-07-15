### 1.1 Chemical Master Equation as Discrete PDE

Consider a well-mixed system of volume V with d chemical species  $ S_1, \ldots, S_d $ involved in M reactions  $ R_1, \ldots, R_M $. The state of the system is characterized by the numbers  $ X_i(t) $ of molecules of  $ S_i $. In the stochastic modelling approach treated here, the discrete variable

 $$ X(t)=(X_{1}(t),\cdots,X_{d}(t)) $$ 

is understood to be random. The reaction probability for each reaction  $ R_j $ is specified by the propensity function  $ \alpha_j = \alpha_j(X(t), t) $, which is equal to the product of a rate constant  $ c_j $ and the number of possible combinations of reactant molecules involved in reaction  $ R_j $. The most frequently arising reaction types are listed in Table 1.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>chemical reaction</td><td style='text-align: center; word-wrap: break-word;'>$ \alpha_{j} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ S_{a} \rightarrow * $</td><td style='text-align: center; word-wrap: break-word;'>$ c_{j}X_{a}(t) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ S_{a} + S_{b} \rightarrow * $</td><td style='text-align: center; word-wrap: break-word;'>$ c_{j}X_{a}(t)X_{b}(t) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ S_{a} + S_{a} \rightarrow * $</td><td style='text-align: center; word-wrap: break-word;'>$ c_{j}X_{a}(t)(X_{a}(t)-1)/2 $</td></tr></table>

<div style="text-align: center;">Table 1: Stochastic propensity functions</div>


Once a reaction  $ R_j $ takes place, the number of molecules for each species changes according to the stoichiometric vector  $ \nu_j \in \mathbf{N}^d $, i.e.,  $ X(t) \to X(t) + \nu_j $. Note that the first two propensity terms above have the same form as in the continuous case, while the third one clearly reveals the discrete nature of the process.

Following [20, 18, 14], the time evolution of the probability distribution function (PDF)

 $$ \begin{array}{r l r}{p(t,x)}&{=}&{\mathrm{P}\big[X_{1}(t)=x_{1},\dots,X_{d}(t)=x_{n}\big],\quad x\in\mathbf{N}^{d}}\end{array} $$ 

of the random variable  $ X(t) $ is described by the chemical master equation (CME)

 $$ \begin{array}{r c l}{\partial_{t}p(t,x)}&{=}&{\displaystyle\sum_{m=1}^{M}\alpha_{m}(x-\nu_{m})p(t,x-\nu_{m})-\alpha_{m}(x)p(t,x)\;.}\\ \end{array} $$ 