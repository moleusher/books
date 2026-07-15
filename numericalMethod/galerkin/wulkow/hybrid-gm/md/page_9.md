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
