COROLLARY 2.5. The forward difference operator applied to  $ l_{j}(s;\rho,\alpha) $ can be expanded into

 $$ \begin{array}{r c l}{\Delta l_{j}(s;\rho,\alpha)}&{=}&{l_{j}(s+1;\rho,\alpha)-l_{j}(s;\rho,\alpha)}\\ {}&{=}&{(\rho-1)\displaystyle\sum_{k=0}^{j-1}\rho^{j-1-k}l_{k}(s;\rho,\alpha)\;.}\\ \end{array} $$ 

Proof. Insertion of Lemma 2.4 into the fundamental difference relation (2.7) leads to transformation coefficients  $ d_{\rho}^{j,k}(\alpha,\alpha+1)=\rho^{j-1-k} $.

COROLLARY 2.6. The backward difference operator applied to  $ l_{j}(s;\rho,\alpha) $ can be expressed by

 $$ \nabla l_{j}(s;\rho,\alpha)=l_{j}(s;\rho,\alpha)-l_{j}(s-1;\rho,\alpha)=(\rho-1)\sum_{k=0}^{j-1}l_{k}(s;\rho,\alpha)\;. $$ 

Proof. Backward shift of the difference relation (2.12) in the argument yields

 $$ l_{j}(s-1;\rho,\alpha)+(\rho-1)\sum_{k=0}^{j-1}\rho^{j-1-k}l_{k}(s-1;\rho,\alpha)=l_{j}(s;\rho,\alpha)\;, $$ 

which can be regarded as an infinite triangular system of linear equations in the variables  $ l_{j}(s-1;\rho,\alpha) $ for given  $ l_{j}(s;\rho,\alpha) $. This system can be solved recursively by induction for each index j.

Further properties, which are related to degradation (Examples 1.2, 4.2) and combination processes (Example 1.3, 4.3) can be found in [39] and [38].

### 2.3 APPROXIMATION BY BASIS EXPANSIONS

Let  $ u \in H_{\rho,\alpha} $ be expanded in the orthogonal basis  $ \{\psi_k(\rho,\alpha)\} = \{\Psi_{\rho,\alpha} l_k(\rho,\alpha)\} $ of  $ H_{\rho,\alpha} $ by

 $$ u(s)=\Psi_{\rho,\alpha}(s)\sum_{k=0}^{\infty}a_{k}l_{k}(s;\rho,\alpha)\enspace. $$ 

The expansion coefficients  $ a_{k} $ are given formally by

 $$ a_{k}=\frac{1}{\gamma_{k}^{\rho,\alpha}}\sum_{s=1}^{\infty}u(s)l_{k}(s;\rho,\alpha)\;, $$ 