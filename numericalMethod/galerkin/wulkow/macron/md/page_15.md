
<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>n</td><td style='text-align: center; word-wrap: break-word;'>estimated error  $ \epsilon_{n} $</td><td style='text-align: center; word-wrap: break-word;'>true error  $ \bar{\epsilon}_{n} $</td><td style='text-align: center; word-wrap: break-word;'>prediction of  $ \epsilon_{n} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0.50</td><td style='text-align: center; word-wrap: break-word;'>0.87</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>0.16</td><td style='text-align: center; word-wrap: break-word;'>0.76</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0.26</td><td style='text-align: center; word-wrap: break-word;'>0.72</td><td style='text-align: center; word-wrap: break-word;'>0.02</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>0.11</td><td style='text-align: center; word-wrap: break-word;'>0.62</td><td style='text-align: center; word-wrap: break-word;'>no monotony</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>0.11</td><td style='text-align: center; word-wrap: break-word;'>0.61</td><td style='text-align: center; word-wrap: break-word;'>0.04</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>0.08</td><td style='text-align: center; word-wrap: break-word;'>0.49</td><td style='text-align: center; word-wrap: break-word;'>no monotony</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>40</td><td style='text-align: center; word-wrap: break-word;'>0.10</td><td style='text-align: center; word-wrap: break-word;'>0.46</td><td style='text-align: center; word-wrap: break-word;'>0.05</td></tr></table>

<div style="text-align: center;">Table 3: Behavior of error, Test 2</div>


the reason for such an error behavior we could use the  $ \alpha $-check of MACRON. In this case we would obtain

 $$ \bar{\rho}=0.01\ ,\ \bar{\alpha}=5000\ . $$ 

According to Section 2.3 in [13], this result indicates that $u_s$ is a Poisson distribution indeed. Note, that a Poisson distribution reaches its maximum at the index $s = \bar{\rho} \cdot \bar{\alpha}$.

The attempt to approximate  $ u_{s} $ with 10 and 20 discrete Laguerre polynomials is shown in Figure 2. Even the approximation with 20 discrete Laguerre polynomials is not very good.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>s ( * E+02 )</th><th style='text-align: center;'>P(s) ( * E-01 ) (Solid)</th><th style='text-align: center;'>P(s) ( * E-01 ) (Dashed)</th><th style='text-align: center;'>P(s) ( * E-01 ) (Dotted)</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>0.01</td><td style='text-align: center;'>-0.110</td><td style='text-align: center;'>-0.120</td><td style='text-align: center;'>-0.100</td></tr>
    <tr><td style='text-align: center;'>0.02</td><td style='text-align: center;'>-0.100</td><td style='text-align: center;'>-0.110</td><td style='text-align: center;'>-0.090</td></tr>
    <tr><td style='text-align: center;'>0.03</td><td style='text-align: center;'>-0.090</td><td style='text-align: center;'>-0.100</td><td style='text-align: center;'>-0.080</td></tr>
    <tr><td style='text-align: center;'>0.04</td><td style='text-align: center;'>-0.080</td><td style='text-align: center;'>-0.090</td><td style='text-align: center;'>-0.070</td></tr>
    <tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>-0.070</td><td style='text-align: center;'>-0.080</td><td style='text-align: center;'>-0.060</td></tr>
    <tr><td style='text-align: center;'>0.06</td><td style='text-align: center;'>-0.060</td><td style='text-align: center;'>-0.070</td><td style='text-align: center;'>-0.050</td></tr>
    <tr><td style='text-align: center;'>0.07</td><td style='text-align: center;'>-0.055</td><td style='text-align: center;'>-0.065</td><td style='text-align: center;'>-0.045</td></tr>
    <tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>-0.050</td><td style='text-align: center;'>-0.060</td><td style='text-align: center;'>-0.040</td></tr>
    <tr><td style='text-align: center;'>0.09</td><td style='text-align: center;'>-0.045</td><td style='text-align: center;'>-0.055</td><td style='text-align: center;'>-0.035</td></tr>
    <tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>-0.040</td><td style='text-align: center;'>-0.050</td><td style='text-align: center;'>-0.030</td></tr>
    <tr><td style='text-align: center;'>0.11</td><td style='text-align: center;'>-0.035</td><td style='text-align: center;'>-0.045</td><td style='text-align: center;'>-0.025</td></tr>
    <tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>-0.030</td><td style='text-align: center;'>-0.040</td><td style='text-align: center;'>-0.020</td></tr>
    <tr><td style='text-align: center;'>0.13</td><td style='text-align: center;'>-0.025</td><td style='text-align: center;'>-0.035</td><td style='text-align: center;'>-0.015</td></tr>
    <tr><td style='text-align: center;'>0.14</td><td style='text-align: center;'>-0.020</td><td style='text-align: center;'>-0.030</td><td style='text-align: center;'>-0.010</td></tr>
    <tr><td style='text-align: center;'>0.15</td><td style='text-align: center;'>-0.015</td><td style='text-align: center;'>-0.025</td><td style='text-align: center;'>-0.005</td></tr>
    <tr><td style='text-align: center;'>0.16</td><td style='text-align: center;'>-0.010</td><td style='text-align: center;'>-0.020</td><td style='text-align: center;'>-0.002</td></tr>
    <tr><td style='text-align: center;'>0.17</td><td style='text-align: center;'>-0.005</td><td style='text-align: center;'>-0.015</td><td style='text-align: center;'>0.000</td></tr>
    <tr><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>-0.010</td><td style='text-align: center;'>0.005</td></tr>
    <tr><td style='text-align: center;'>0.19</td><td style='text-align: center;'>0.005</td><td style='text-align: center;'>-0.005</td><td style='text-align: center;'>0.010</td></tr>
    <tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.010</td><td style='text-align: center;'>0.000</td><td style='text-align: center;'>0.015</td></tr>
    <tr><td style='text-align: center;'>0.21</td><td style='text-align: center;'>0.015</td><td style='text-align: center;'>0.005</td><td style='text-align: center;'>0.020</td></tr>
    <tr><td style='text-align: center;'>0.22</td><td style='text-align: center;'>0.020</td><td style='text-align: center;'>0.010</td><td style='text-align: center;'>0.025</td></tr>
    <tr><td style='text-align: center;'>0.23</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.015</td><td style='text-align: center;'>0.030</td></tr>
    <tr><td style='text-align: center;'>0.24</td><td style='text-align: center;'>0.030</td><td style='text-align: center;'>0.020</td><td style='text-align: center;'>0.035</td></tr>
    <tr><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.025</td><td style='text-align: center;'>0.040</td></tr>
    <tr><td style='text-align: center;'>0.26</td><td style='text-align: center;'>0.040</td><td style='text-align: center;'>0.030</td><td style='text-align: center;'>0.045</td></tr>
    <tr><td style='text-align: center;'>0.27</td><td style='text-align: center;'>0.045</td><td style='text-align: center;'>0.035</td><td style='text-align: center;'>0.050</td></tr>
    <tr><td style='text-align: center;'>0.28</td><td style='text-align: center;'>0.050</td><td style='text-align: center;'>0.040</td><td style='text-align: center;'>0.055</td></tr>
    <tr><td style='text-align: center;'>0.29</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.045</td><td style='text-align: center;'>0.060</td></tr>
    <tr><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.060</td><td style='text-align: center;'>0.050</td><td style='text-align: center;'>0.065</td></tr>
    <tr><td style='text-align: center;'>0.31</td><td style='text-align: center;'>0.065</td><td style='text-align: center;'>0.055</td><td style='text-align: center;'>0.070</td></tr>
    <tr><td style='text-align: center;'>0.32</td><td style='text-align: center;'>0.070</td><td style='text-align: center;'>0.060</td><td style='text-align: center;'>0.075</td></tr>
    <tr><td style='text-align: center;'>0.33</td><td style='text-align: center;'>0.075</td><td style='text-align: center;'>0.065</td><td style='text-align: center;'>0.080</td></tr>
    <tr><td style='text-align: center;'>0.34</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>0.070</td><td style='text-align: center;'>0.085</td></tr>
    <tr><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.085</td><td style='text-align: center;'>0.075</td><td style='text-align: center;'>0.090</td></tr>
    <tr><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.090</td><td style='text-align: center;'>0.080</td><td style='text-align: center;'>0.095</td></tr>
    <tr><td style='text-align: center;'>0.37</td><td style='text-align: center;'>0.095</td><td style='text-align: center;'>0.085</td><td style='text-align: center;'>0.100</td></tr>
    <tr><td style='text-align: center;'>0.38</td><td style='text-align: center;'>0.100</td><td style='text-align: center;'>0.090</td><td style='text-align: center;'>0.105</td></tr>
    <tr><td style='text-align: center;'>0.39</td><td style='text-align: center;'>0.105</td><td style='text-align: center;'>0.095</td><td style='text-align: center;'>0.110</td></tr>
    <tr><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.110</td><td style='text-align: center;'>0.100</td><td style='text-align: center;'>0.115</td></tr>
    <tr><td style='text-align: center;'>0.41</td><td style='text-align: center;'>0.115</td><td style='text-align: center;'>0.105</td><td style='text-align: center;'>0.120</td></tr>
    <tr><td style='text-align: center;'>0.42</td><td style='text-align: center;'>0.120</td><td style='text-align: center;'>0.110</td><td style='text-align: center;'>0.125</td></tr>
    <tr><td style='text-align: center;'>0.43</td><td style='text-align: center;'>0.125</td><td style='text-align: center;'>0.115</td><td style='text-align: center;'>0.130</td></tr>
    <tr><td style='text-align: center;'>0.44</td><td style='text-align: center;'>0.130</td><td style='text-align: center;'>0.120</td><td style='text-align: center;'>0.135</td></tr>
    <tr><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.135</td><td style='text-align: center;'>0.125</td><td style='text-align: center;'>0.140</td></tr>
    <tr><td style='text-align: center;'>0.46</td><td style='text-align: center;'>0.140</td><td style='text-align: center;'>0.130</td><td style='text-align: center;'>0.145</td></tr>
    <tr><td style='text-align: center;'>0.47</td><td style='text-align: center;'>0.145</td><td style='text-align: center;'>0.135</td><td style='text-align: center;'>0.150</td></tr>
    <tr><td style='text-align: center;'>0.48</td><td style='text-align: center;'>0.150</td><td style='text-align: center;'>0.140</td><td style='text-align: center;'>0.155</td></tr>
    <tr><td style='text-align: center;'>0.49</td><td style='text-align: center;'>0.155</td><td style='text-align: center;'>0.145</td><td style='text-align: center;'>0.160</td></tr>
    <tr><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.160</td><td style='text-align: center;'>0.150</td><td style='text-align: center;'>0.165</td></tr>
    <tr><td style='text-align: center;'>0.51</td><td style='text-align: center;'>0.165</td><td style='text-align: center;'>0.155</td><td style='text-align: center;'>0.170</td></tr>
    <tr><td style='text-align: center;'>0.52</td><td style='text-align: center;'>0.170</td><td style='text-align: center;'>0.160</td><td style='text-align: center;'>0.175</td></tr>
    <tr><td style='text-align: center;'>0.53</td><td style='text-align: center;'>0.175</td><td style='text-align: center;'>0.165</td><td style='text-align: center;'>0.180</td></tr>
    <tr><td style='text-align: center;'>0.54</td><td style='text-align: center;'>0.180</td><td style='text-align: center;'>0.170</td><td style='text-align: center;'>0.185</td></tr>
    <tr><td style='text-align: center;'>0.55</td><td style='text-align: center;'>0.185</td><td style='text-align: center;'>0.175</td><td style='text-align: center;'>0.190</td></tr>
    <tr><td style='text-align: center;'>0.56</td><td style='text-align: center;'>0.190</td><td style='text-align: center;'>0.180</td><td style='text-align: center;'>0.195</td></tr>
    <tr><td style='text-align: center;'>0.57</td><td style='text-align: center;'>0.195</td><td style='text-align: center;'>0.185</td><td style='text-align: center;'>0.200</td></tr>
    <tr><td style='text-align: center;'>0.58</td><td style='text-align: center;'>0.200</td><td style='text-align: center;'>0.190</td><td style='text-align: center;'>0.205</td></tr>
    <tr><td style='text-align: center;'>0.59</td><td style='text-align: center;'>0.205</td><td style='text-align: center;'>0.195</td><td style='text-align: center;'>0.210</td></tr>
    <tr><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.210</td><td style='text-align: center;'>0.200</td><td style='text-align: center;'>0.215</td></tr>
    <tr><td style='text-align: center;'>0.61</td><td style='text-align: center;'>0.215</td><td style='text-align: center;'>0.205</td><td style='text-align: center;'>0.220</td></tr>
    <tr><td style='text-align: center;'>0.62</td><td style='text-align: center;'>0.220</td><td style='text-align: center;'>0.210</td><td style='text-align: center;'>0.225</td></tr>
    <tr><td style='text-align: center;'>0.63</td><td style='text-align: center;'>0.225</td><td style='text-align: center;'>0.215</td><td style='text-align: center;'>0.230</td></tr>
    <tr><td style='text-align: center;'>0.64</td><td style='text-align: center;'>0.230</td><td style='text-align: center;'>0.220</td><td style='text-align: center;'>0.235</td></tr>
    <tr><td style='text-align: center;'>0.65</td><td style='text-align: center;'>0.235</td><td style='text-align: center;'>0.225</td><td style='text-align: center;'>0.240</td></tr>
    <tr><td style='text-align: center;'>0.66</td><td style='text-align: center;'>0.240</td><td style='text-align: center;'>0.230</td><td style='text-align: center;'>0.245</td></tr>
    <tr><td style='text-align: center;'>0.67</td><td style='text-align: center;'>0.245</td><td style='text-align: center;'>0.235</td><td style='text-align: center;'>0.250</td></tr>
    <tr><td style='text-align: center;'>0.68</td><td style='text-align: center;'>0.250</td><td style='text-align: center;'>0.240</td><td style='text-align: center;'>0.255</td></tr>
    <tr><td style='text-align: center;'>0.69</td><td style='text-align: center;'>0.255</td><td style='text-align: center;'>0.245</td><td style='text-align: center;'>0.260</td></tr>
    <tr><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.260</td><td style='text-align: center;'>0.250</td><td style='text-align: center;'>0.265</td></tr>
    <tr><td style='text-align: center;'>0.71</td><td style='text-align: center;'>0.265</td><td style='text-align: center;'>0.255</td><td style='text-align: center;'>0.270</td></tr>
    <tr><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.270</td><td style='text-align: center;'>0.260</td><td style='text-align: center;'>0.275</td></tr>
    <tr><td style='text-align: center;'>0.73</td><td style='text-align: center;'>0.275</td><td style='text-align: center;'>0.265</td><td style='text-align: center;'>0.280</td></tr>
    <tr><td style='text-align: center;'>0.74</td><td style='text-align: center;'>0.280</td><td style='text-align: center;'>0.270</td><td style='text-align: center;'>0.285</td></tr>
    <tr><td style='text-align: center;'>0.75</td><td style='text-align: center;'>0.285</td><td style='text-align: center;'>0.275</td><td style='text-align: center;'>0.290</td></tr>
    <tr><td style='text-align: center;'>0.76</td><td style='text-align: center;'>0.290</td><td style='text-align: center;'>0.280</td><td style='text-align: center;'>0.295</td></tr>
    <tr><td style='text-align: center;'>0.77</td><td style='text-align: center;'>0.295</td><td style='text-align: center;'>0.285</td><td style='text-align: center;'>0.300</td></tr>
    <tr><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.300</td><td style='text-align: center;'>0.290</td><td style='text-align: center;'>0.305</td></tr>
    <tr><td style='text-align: center;'>0.79</td><td style='text-align: center;'>0.305</td><td style='text-align: center;'>0.295</td><td style='text-align: center;'>0.310</td></tr>
    <tr><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.310</td><td style='text-align: center;'>0.300</td><td style='text-align: center;'>0.315</td></tr>
    <tr><td style='text-align: center;'>0.81</td><td style='text-align: center;'>0.315</td><td style='text-align: center;'>0.305</td><td style='text-align: center;'>0.320</td></tr>
    <tr><td style='text-align: center;'>0.82</td><td style='text-align: center;'>0.320</td><td style='text-align: center;'>0.310</td><td style='text-align: center;'>0.325</td></tr>
    <tr><td style='text-align: center;'>0.83</td><td style='text-align: center;'>0.325</td><td style='text-align: center;'>0.315</td><td style='text-align: center;'>0.330</td></tr>
    <tr><td style='text-align: center;'>0.84</td><td style='text-align: center;'>0.330</td><td style='text-align: center;'>0.320</td><td style='text-align: center;'>0.335</td></tr>
    <tr><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.335</td><td style='text-align: center;'>0.325</td><td style='text-align: center;'>0.340</td></tr>
    <tr><td style='text-align: center;'>0.86</td><td style='text-align: center;'>0.340</td><td style='text-align: center;'>0.330</td><td style='text-align: center;'>0.345</td></tr>
    <tr><td style='text-align: center;'>0.87</td><td style='text-align: center;'>0.345</td><td style='text-align: center;'>0.335</td><td style='text-align: center;'>0.350</td></tr>
    <tr><td style='text-align: center;'>0.88</td><td style='text-align: center;'>0.350</td><td style='text-align: center;'>0.340</td><td style='text-align: center;'>0.355</td></tr>
    <tr><td style='text-align: center;'>0.89</td><td style='text-align: center;'>0.355</td><td style='text-align: center;'>0.345</td><td style='text-align: center;'>0.360</td></tr>
    <tr><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.360</td><td style='text-align: center;'>0.350</td><td style='text-align: center;'>0.365</td></tr>
    <tr><td style='text-align: center;'>0.91</td><td style='text-align: center;'>0.365</td><td style='text-align: center;'>0.355</td><td style='text-align: center;'>0.370</td></tr>
    <tr><td style='text-align: center;'>0.92</td><td style='text-align: center;'>0.370</td><td style='text-align: center;'>0.360</td><td style='text-align: center;'>0.375</td></tr>
    <tr><td style='text-align: center;'>0.93</td><td style='text-align: center;'>0.375</td><td style='text-align: center;'>0.365</td><td style='text-align: center;'>0.380</td></tr>
    <tr><td style='text-align: center;'>0.94</td><td style='text-align: center;'>0.380</td><td style='text-align: center;'>0.370</td><td style='text-align: center;'>0.385</td></tr>
    <tr><td style='text-align: center;'>0.95</td><td style='text-align: center;'>0.385</td><td style='text-align: center;'>0.375</td><td style='text-align: center;'>0.390</td></tr>
    <tr><td style='text-align: center;'>0.96</td><td style='text-align: center;'>0.390</td><td style='text-align: center;'>0.380</td><td style='text-align: center;'>0.395</td></tr>
    <tr><td style='text-align: center;'>0.97</td><td style='text-align: center;'>0.395</td><td style='text-align: center;'>0.385</td><td style='text-align: center;'>0.400</td></tr>
    <tr><td style='text-align: center;'>0.98</td><td style='text-align: center;'>0.400</td><td style='text-align: center;'>0.390</td><td style='text-align: center;'>0.405</td></tr>
    <tr><td style='text-align: center;'>0.99</td><td style='text-align: center;'>0.405</td><td style='text-align: center;'>0.395</td><td style='text-align: center;'>0.410</td></tr>
    <tr><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.410</td><td style='text-align: center;'>0.400</td><td style='text-align: center;'>0.415</td></tr>
    <tr><td style='text-align: center;'>1.01</td><td style='text-align: center;'>0.415</td><td style='text-align: center;'>0.405</td><td style='text-align: center;'>0.420</td></tr>
    <tr><td style='text-align: center;'>1.02</td><td style='text-align: center;'>0.420</td><td style='text-align: center;'>0.410</td><td style='text-align: center;'>0.425</td></tr>
    <tr><td style='text-align: center;'>1.03</td><td style='text-align: center;'>0.425</td><td style='text-align: center;'>0.415</td><td style='text-align: center;'>0.430</td></tr>
    <tr><td style='text-align: center;'>1.04</td><td style='text-align: center;'>0.430</td><td style='text-align: center;'>0.420</td><td style='text-align: center;'>0.435</td></tr>
    <tr><td style='text-align: center;'>1.05</td><td style='text-align: center;'>0.435</td><td style='text-align: center;'>0.425</td><td style='text-align: center;'>0.440</td></tr>
    <tr><td style='text-align: center;'>1.06</td><td style='text-align: center;'>0.440</td><td style='text-align: center;'>0.430</td><td style='text-align: center;'>0.445</td></tr>
    <tr><td style='text-align: center;'>1.07</td><td style='text-align: center;'>0.445</td><td style='text-align: center;'>0.435</td><td style='text-align: center;'>0.450</td></tr>
    <tr><td style='text-align: center;'>1.08</td><td style='text-align: center;'>0.450</td><td style='text-align: center;'>0.440</td><td style='text-align: center;'>0.455</td></tr>
    <tr><td style='text-align: center;'>1.09</td><td style='text-align: center;'>0.455</td><td style='text-align: center;'>0.445</td><td style='text-align: center;'>0.460</td></tr>
    <tr><td style='text-align: center;'>1.10</td><td style='text-align: center;'>0.460</td><td style='text-align: center;'>0.450</td><td style='text-align: center;'>0.465</td></tr>
    <tr><td style='text-align: center;'>1.11</td><td style='text-align: center;'>0.465</td><td style='text-align: center;'>0.455</td><td style='text-align: center;'>0.470</td></tr>
    <tr><td style='text-align: center;'>1.12</td><td style='text-align: center;'>0.470</td><td style='text-align: center;'>0.460</td><td style='text-align: center;'>0.475</td></tr>
    <tr><td style='text-align: center;'>1.13</td><td style='text-align: center;'>0.475</td><td style='text-align: center;'>0.465</td><td style='text-align: center;'>0.480</td></tr>
    <tr><td style='text-align: center;'>1.14</td><td style='text-align: center;'>0.480</td><td style='text-align: center;'>0.470</td><td style='text-align: center;'>0.485</td></tr>
    <tr><td style='text-align: center;'>1.15</td><td style='text-align: center;'>0.485</td><td style='text-align: center;'>0.475</td><td style='text-align: center;'>0.490</td></tr>
    <tr><td style='text-align: center;'>1.16</td><td style='text-align: center;'>0.490</td><td style='text-align: center;'>0.480</td><td style='text-align: center;'>0.495</td></tr>
    <tr><td style='text-align: center;'>1.17</td><td style='text-align: center;'>0.495</td><td style='text-align: center;'>0.485</td><td style='text-align: center;'>0.500</td></tr>
    <tr><td style='text-align: center;'>1.18</td><td style='text-align: center;'>0.500</td><td style='text-align: center;'>0.490</td><td style='text-align: center;'>0.505</td></tr>
    <tr><td style='text-align: center;'>1.19</td><td style='text-align: center;'>0.505</td><td style='text-align: center;'>0.495</td><td style='text-align: center;'>0.510</td></tr>
    <tr><td style='text-align: center;'>1.20</td><td style='text-align: center;'>0.510</td><td style='text-align: center;'>0.500</td><td style='text-align: center;'>0.515</td></tr>
    <tr><td style='text-align: center;'>1.21</td><td style='text-align: center;'>0.515</td><td style='text-align: center;'>0.505</td><td style='text-align: center;'>0.520</td></tr>
    <tr><td style='text-align: center;'>1.22</td><td style='text-align: center;'>0.520</td><td style='text-align: center;'>0.510</td><td style='text-align: center;'>0.525</td></tr>
    <tr><td style='text-align: center;'>1.23</td><td style='text-align: center;'>0.525</td><td style='text-align: center;'>0.515</td><td style='text-align: center;'>0.530</td></tr>
    <tr><td style='text-align: center;'>1.24</td><td style='text-align: center;'>0.530</td><td style='text-align: center;'>0.520</td><td style='text-align: center;'>0.535</td></tr>
    <tr><td style='text-align: center;'>1.25</td><td style='text-align: center;'>0.535</td><td style='text-align: center;'>0.525</td><td style='text-align: center;'>0.540</td></tr>
    <tr><td style='text-align: center;'>1.26</td><td style='text-align: center;'>0.540</td><td style='text-align: center;'>0.530</td><td style='text-align: center;'>0.545</td></tr>
    <tr><td style='text-align: center;'>1.27</td><td style='text-align: center;'>0.545</td><td style='text-align: center;'>0.535</td><td style='text-align: center;'>0.550</td></tr>
    <tr><td style='text-align: center;'>1.28</td><td style='text-align: center;'>0.550</td><td style='text-align: center;'>0.540</td><td style='text-align: center;'>0.555</td></tr>
    <tr><td style='text-align: center;'>1.29</td><td style='text-align: center;'>0.555</td><td style='text-align: center;'>0.545</td><td style='text-align: center;'>0.560</td></tr>
    <tr><td style='text-align: center;'>1.30</td><td style='text-align: center;'>0.560</td><td style='text-align: center;'>0.550</td><td style='text-align: center;'>0.565</td></tr>
    <tr><td style='text-align: center;'>1.31</td><td style='text-align: center;'>0.565</td><td style='text-align: center;'>0.555</td><td style='text-align: center;'>0.570</td></tr>
    <tr><td style='text-align: center;'>1.32</td><td style='text-align: center;'>0.570</td><td style='text-align: center;'>0.560</td><td style='text-align: center;'>0.575</td></tr>
    <tr><td style='text-align: center;'>1.33</td><td style='text-align: center;'>0.575</td><td style='text-align: center;'>0.565</td><td style='text-align: center;'>0.580</td></tr>
    <tr><td style='text-align: center;'>1.34</td><td style='text-align: center;'>0.580</td><td style='text-align: center;'>0.570</td><td style='text-align: center;'>0.585</td></tr>
    <tr><td style='text-align: center;'>1.35</td><td style='text-align: center;'>0.585</td><td style='text-align: center;'>0.575</td><td style='text-align: center;'>0.590</td></tr>
    <tr><td style='text-align: center;'>1.36</td><td style='text-align: center;'>0.590</td><td style='text-align: center;'>0.580</td><td style='text-align: center;'>0.595</td></tr>
    <tr><td style='text-align: center;'>1.37</td><td style='text-align: center;'>0.595</td><td style='text-align: center;'>0.585</td><td style='text-align: center;'>0.600</td></tr>
    <tr><td style='text-align: center;'>1.38</td><td style='text-align: center;'>0.600</td><td style='text-align: center;'>0.590</td><td style='text-align: center;'>0.605</td></tr>
    <tr><td style='text-align: center;'>1.39</td><td style='text-align: center;'>0.605</td><td style='text-align: center;'>0.595</td><td style='text-align: center;'>0.610</td></tr>
    <tr><td style='text-align: center;'>1.40</td><td style='text-align: center;'>0.610</td><td style='text-align: center;'>0.600</td><td style='text-align: center;'>0.615</td></tr>
    <tr><td style='text-align: center;'>1.41</td><td style='text-align: center;'>0.615</td><td style='text-align: center;'>0.605</td><td style='text-align: center;'>0.620</td></tr>
    <tr><td style='text-align: center;'>1.42</td><td style='text-align: center;'>0.620</td><td style='text-align: center;'>0.610</td><td style='text-align: center;'>0.625</td></tr>
    <tr><td style='text-align: center;'>1.43</td><td style='text-align: center;'>0.625</td><td style='text-align: center;'>0.615</td><td style='text-align: center;'>0.630</td></tr>
    <tr><td style='text-align: center;'>1.44</td><td style='text-align: center;'>0.630</td><td style='text-align: center;'>0.620</td><td style='text-align: center;'>0.635</td></tr>
    <tr><td style='text-align: center;'>1.45</td><td style='text-align: center;'>0.635</td><td style='text-align: center;'>0.625</td><td style='text-align: center;'>0.640</td></tr>
    <tr><td style='text-align: center;'>1.46</td><td style='text-align: center;'>0.640</td><td style='text-align: center;'>0.630</td><td style='text-align: center;'>0.645</td></tr>
    <tr><td style='text-align: center;'>1.47</td><td style='text-align: center;'>0.645</td><td style='text-align: center;'>0.635</td><td style='text-align: center;'>0.650</td></tr>
    <tr><td style='text-align: center;'>1.48</td><td style='text-align: center;'>0.650</td><td style='text-align: center;'>0.640</td><td style='text-align: center;'>0.655</td></tr>
    <tr><td style='text-align: center;'>1.49</td><td style='text-align: center;'>0.655</td><td style='text-align: center;'>0.645</td><td style='text-align: center;'>0.660</td></tr>
    <tr><td style='text-align: center;'>1.50</td><td style='text-align: center;'>0.660</td><td style='text-align: center;'>0.650</td><td style='text-align: center;'>0.665</td></tr>
    <tr><td style='text-align: center;'>1.51</td><td style='text-align: center;'>0.665</td><td style='text-align: center;'>0.655</td><td style='text-align: center;'>0.670</td></tr>
    <tr><td style='text-align: center;'>1.52</td><td style='text-align: center;'>0.670</td><td style='text-align: center;'>0.660</td><td style='text-align: center;'>0.675</td></tr>
    <tr><td style='text-align: center;'>1.53</td><td style='text-align: center;'>0.675</td><td style='text-align: center;'>0.665</td><td style='text-align: center;'>0.680</td></tr>
    <tr><td style='text-align: center;'>1.54</td><td style='text-align: center;'>0.680</td><td style='text-align: center;'>0.670</td><td style='text-align: center;'>0.685</td></tr>
    <tr><td style='text-align: center;'>1.55</td><td style='text-align: center;'>0.685</td><td style='text-align: center;'>0.675</td><td style='text-align: center;'>0.690</td></tr>
    <tr><td style='text-align: center;'>1.56</td><td style='text-align: center;'>0.69</td></tr>
  </tbody>
</table>

<div style="text-align: center;">Figure 2: Approximations of a Poisson distribution (—) with with 10 (…) and 20 (−−) discrete Laguerre polynomials.</div>


Anyhow, it is possible to compute the statistical moments of  $ u_{s} $ exactly. A post-transformation of an approximation  $ u_{s}^{n} $ to an expansion in terms of the