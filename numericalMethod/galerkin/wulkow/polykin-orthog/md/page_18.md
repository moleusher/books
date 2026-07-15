### 3. Orthogonal Polynomials of a Discrete Variable

In this Section, the discrete Galerkin method derived in Section 2 above is exemplified in terms of special choices of the weight function  $ \Psi $. As it turns out, the first orthogonal polynomials of discrete variables have already been discussed by CHEBYSHEV [3] in 1855 and by STIELTJES [20] in 1894. Even though many of their properties can meanwhile be found in textbooks on special functions [17, 5], a summary of some properties seems to be justified — in view of the special application in mind. As a consequence of this application, most definitions in the literature must be rewritten for the grid  $ \{1, 2, \ldots\} $ instead of  $ \{0, 1, \ldots\} $. Moreover, some necessary properties had to be newly derived.

### 3.1 Discrete Laguerre Polynomials

As shown above, the exponential weight function in connection with the continuous inner product (2.26) defines the classical Laguerre polynomials  $ \{L_{k}\} $. For discrete variable s, the identification

 $$ \rho:=e^{-\beta}\quad,\quad\beta>0\quad, $$ 

transforms (2.27) to the discrete weight function

 $$ \Psi(s):=(1-\rho)\rho^{s-1}\;,\;0<\rho<1\;,\;s=1,2,\;\ldots\;. $$ 

Herein, the normalization (2.24) has been observed. In the chemical literature, (3.2) is also known as the Schulz-Flory distribution. With  $ \Psi $ from (3.2), the inner product (2.1) generates a set of orthogonal polynomials — to be naturally called discrete Laguerre polynomials, say  $ \{l_k\} $. These polynomials have been considered briefly by STIELTJES [20] in 1894 and in more detail by GOTTLIEB [16] in 1938.

The simplest representation of the discrete Laguerre polynomials  $ l_{k}(s) $ is via their three-term recurrence relation  $ (k=0,1,\ldots) $:

 $$ (k+1)l_{k+1}=[(k+1)\rho+k-(1-\rho)(s-1)]\;l_{k}-k\rho l_{k-1}\quad, $$ 

to be started with

 $$ l_{-1}:=0\quad,\quad l_{0}:=1\;. $$ 

The associated orthogonality relation is

 $$ (l_{i},\;l_{k})=\rho^{k}\cdot\delta_{i k}\quad i,\;k=0,\;1,\;\ldots. $$ 

Comparison with (2.4) shows that

 $$ \gamma_{k}=\rho^{k}\quad k=0,1,\dots. $$ 