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