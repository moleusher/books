and

 $$ P_{s}:=s\;\rho^{s-1}\;. $$ 

This is the problem setting from the simulation of smog reactions in Example 5.4. The parameters  $ \rho = 0.995 $ and  $ s_{\max} = 1000 $ have been chosen here, such that a direct summation could be performed in moderate computing times. Table 6.2 shows the number  $ n_f $ of evaluations of the term in the inner sum for technical accuracies. Note that this number is about 500000 if the sum is computed directly. Other successful attempts have been made for double sums arising in degradation processes.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>tol</td><td style='text-align: center; word-wrap: break-word;'>error</td><td style='text-align: center; word-wrap: break-word;'>$ n_{f} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ 10^{-1} $</td><td style='text-align: center; word-wrap: break-word;'>$ 1 \cdot 10^{-2} $</td><td style='text-align: center; word-wrap: break-word;'>93</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ 10^{-2} $</td><td style='text-align: center; word-wrap: break-word;'>$ 6 \cdot 10^{-3} $</td><td style='text-align: center; word-wrap: break-word;'>203</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ 10^{-3} $</td><td style='text-align: center; word-wrap: break-word;'>$ 2 \cdot 10^{-4} $</td><td style='text-align: center; word-wrap: break-word;'>1072</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ 10^{-4} $</td><td style='text-align: center; word-wrap: break-word;'>$ 4 \cdot 10^{-5} $</td><td style='text-align: center; word-wrap: break-word;'>1729</td></tr></table>

<div style="text-align: center;">TABLE 6.2: Performance of the SUMMATOR for a double series.</div>


The choice of the required tolerance TOL $ _{I} $ for the inner sum is a difficulty, which also arises for quadrature of functions (see [38]). We use the following argumentation:

Given a sub-interval on level $i$ of the outer sum, we need the $f$-value of the midpoint (used for computation of the Trapezoidal rule) with an error small enough to ensure the required global accuracy TOL, if level $i+1$ is the final one, but not smaller than the predicted error $\tilde{\varepsilon}_{j}^{i+1}$ of the associated interval on the next level. Finally it is reasonable to require at least the global tolerance. Thus we obtain a local inner tolerance by two steps:

 $$ T O L_{I}^{1}=\operatorname*{m a x}\left\{\frac{T O L}{n_{i}},\tilde{\varepsilon}_{j}^{i+1}\right\}, $$ 

 $$ T O L_{I}=\operatorname*{m i n}\left\{T O\dot{L},T O L_{I}^{1}\right\}. $$ 

We also want to mention, that the effect of loss of smoothness described in [38] for the approximation of double integrals by an adaptive algorithm is not so dramatic here, since the divided differences remain moderately bounded if the grid function f is perturbed.