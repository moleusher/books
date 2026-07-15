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