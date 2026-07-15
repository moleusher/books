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