The number-average chain-length is the same as in the basic model, but there are much more long chains now — the weight mean increases (cf. Fig. 7). This effect is even much more pronounced at high temperatures or under high pressure.

We are also able now to compare a popular moment closing relation to the full distribution simulation. We use the formula of Hulburt and Katz $ ^{35)} $

 $$ \mu_{3}=\frac{\mu_{2}(2\mu_{2}\mu_{0}-\mu_{1}\mu_{1})}{\mu_{1}\mu_{0}} $$ 

and solve the moment equations of the system (12). As can be seen in Tab. 3, the deviations between both results are not large, so in this case the closing relation works. Generally, the h-p-algorithm can be used to check moment closures of any kind without additional assumptions.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Degree of polymerization</th><th style='text-align: center;'>W(log M) (Solid Line)</th><th style='text-align: center;'>W(log M) (Dashed Line)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
    <tr><td style='text-align: center;'>100</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.1</td></tr>
    <tr><td style='text-align: center;'>200</td><td style='text-align: center;'>0.5</td><td style='text-align: center;'>0.4</td></tr>
    <tr><td style='text-align: center;'>300</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>0.8</td></tr>
    <tr><td style='text-align: center;'>400</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.2</td></tr>
    <tr><td style='text-align: center;'>500</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.6</td></tr>
    <tr><td style='text-align: center;'>600</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.0</td></tr>
    <tr><td style='text-align: center;'>700</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>2.3</td></tr>
    <tr><td style='text-align: center;'>800</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>900</td><td style='text-align: center;'>2.2</td><td style='text-align: center;'>2.6</td></tr>
    <tr><td style='text-align: center;'>1000</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>2.5</td></tr>
    <tr><td style='text-align: center;'>1100</td><td style='text-align: center;'>1.9</td><td style='text-align: center;'>2.2</td></tr>
    <tr><td style='text-align: center;'>1200</td><td style='text-align: center;'>1.6</td><td style='text-align: center;'>1.8</td></tr>
    <tr><td style='text-align: center;'>1300</td><td style='text-align: center;'>1.2</td><td style='text-align: center;'>1.3</td></tr>
    <tr><td style='text-align: center;'>1400</td><td style='text-align: center;'>0.8</td><td style='text-align: center;'>0.9</td></tr>
    <tr><td style='text-align: center;'>1500</td><td style='text-align: center;'>0.4</td><td style='text-align: center;'>0.5</td></tr>
    <tr><td style='text-align: center;'>1600</td><td style='text-align: center;'>0.1</td><td style='text-align: center;'>0.2</td></tr>
    <tr><td style='text-align: center;'>1700</td><td style='text-align: center;'>0.0</td><td style='text-align: center;'>0.0</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Fig. 7. Molecular weight distributions for model (12) with transfer to polymer (—) compared to the model with  $ k_{1} = 0 $ ( $ \cdots $)</div>


All distributions are looking simple in the chosen graphical representation, but are quite broad and difficult to approximate. If the distributions were shown with respect to a linear chain length axis and as number or weight distribution  $ (D_s \text{ or } D_s \cdot s) $, only a sharp layer for small degrees of polymerization could be seen.

## Selection of further examples

The above example is only a test model to show how general the discrete h-p-algorithm can work. There are some publications using this algorithm for realistic problems, where also experimental data have been obtained.

## ● Pulsed-laser polymerization

In ref. $ ^{31)} $, Buback et al. describe the simulation of pulsed laser polymerization experiments with up to 2000 (!) laser flashes (time periods). There also the effect of chain-length dependent termination coefficient is studied with the h-p-method.

## • Precipitation polymerization

In a PhD-thesis $ ^{32} $, Fengler studied the precipitation polymerization of acrylic acid with PREDICI. He used a two-phase model describing molecular weight distributions, reaction velocity, number of particles and conversion and could fit the model to experimental data.