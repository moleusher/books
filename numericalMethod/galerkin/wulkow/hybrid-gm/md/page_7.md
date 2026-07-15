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