COROLLARY 2.7. The application of the forward difference operator to  $ l_{j}(s;\rho,\alpha) $ can be expanded into

 $$ \begin{array}{r c l}{\Delta l_{j}(s;\rho,\alpha)}&{=}&{l_{j}(s+1;\rho,\alpha)-l_{j}(s;\rho,\alpha)}\\ {}&{=}&{(\rho-1)\displaystyle\sum_{k=0}^{j-1}\rho^{j-1-k}l_{k}(s;\rho,\alpha)\;.}\\ \end{array} $$ 

Proof. Insertion of Lemma 2.2 into the fundamental difference relation (2.23):

 $$ l_{j}(s+1;\rho,\alpha)-l_{j}(s;\rho,\alpha)=\left(\rho-1\right)l_{j-1}(s;\rho,\alpha+1) $$ 

leads to transformation coefficients  $ d_{\rho}^{j,k}(\alpha,\alpha+1)=\rho^{j-1-k} $.

COROLLARY 2.8. The application of the backward difference operator to  $ l_{j}(s;\rho,\alpha) $ can be expressed by

 $$ \nabla l_{j}(s;\rho,\alpha)=l_{j}(s-1;\rho,\alpha)-l_{j}(s;\rho,\alpha)=(1-\rho)\sum_{k=0}^{j-1}l_{k}(s;\rho,\alpha)\;. $$ 

Proof. Backward shift of the difference relation (2.31) in the argument yields

 $$ l_{j}(s-1;\rho,\alpha)+(\rho-1)\sum_{k=0}^{j-1}\rho^{j-1-k}l_{k}(s-1;\rho,\alpha)=l_{j}(s;\rho,\alpha)\;, $$ 

which can be regarded as an infinite triangular system of linear equations in the variables  $ l_{j}(s-1;\rho,\alpha) $ for given  $ l_{j}(s;\rho,\alpha) $. This system can be solved recursively by induction for each index j.

Finally we derive relations, which will be used in Chapter 5 for the treatment of the degradation operator respectively the convolution operator.

LEMMA 2.9. For  $ s \geq 2 $ the following relation holds

 $$ 2.33)\sum_{r=1}^{s}l_{j}(s;\rho,\alpha)=\frac{1}{1-\rho}\left(l_{j}(s;\rho,\alpha)-l_{j+1}(s;\rho,\alpha)+\rho^{j+1}\binom{j+\alpha}{j+1}\right). $$ 

Proof. Induction over s using

 $$ l_{j}(1;\rho,\alpha)=\rho^{j}\begin{pmatrix}j+\alpha\\ j\end{pmatrix} $$ 

and the well-known property

 $$ \begin{pmatrix}x+1\\j\end{pmatrix}=\begin{pmatrix}x\\j\end{pmatrix}+\begin{pmatrix}x\\j-1\end{pmatrix},x\in\mathbb{R},j\in\mathbb{N}. $$ 