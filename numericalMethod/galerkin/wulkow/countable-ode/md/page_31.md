would fail in our context, because the application of Euler steps destroys the strong decaying behavior for  $ s \rightarrow \infty $ of elements of the associated sequence space, implying that Euler steps cannot be performed.

Now we turn to broad distributions  $ (d \gg 1) $ which can be approximated well by choosing  $ \alpha < 0 $ and  $ \rho $ close to one. Then  $ \Psi_{\rho,\alpha} $ approaches to a hyperbola of the form  $ 1/s^\alpha $. This has been used in [52] to model fractional powers appearing in certain chemical processes. The connection between both extreme properties  $ (d \to 1 $ and  $ d \gg 1) $ with only one family of weight functions is the key to the efficiency of the method to be developed herein.

In this chapter, an orthogonal basis of the spaces  $ H_{\rho,\alpha} $ introduced in Section 1.2 will be constructed. This basis is given by means of the modified discrete Laguerre polynomials which will be derived in Section 2.1. Important properties and transformation formulas of these polynomials are added in Section 2.2. The approximation of an element  $ u \in H_{\rho,\alpha} $ by the orthogonal basis is backed by a theorem proven in Section 2.3. As not stated otherwise, we always assume  $ 0 < \rho < 1 $ and  $ \alpha > -1 $.

### 2.1 Construction of the Polynomials

In this section we will construct first a set of orthogonal polynomials  $ \{l_{k}\} $ with respect to the scalar product

 $$ (u\;,\;v)^{\rho,\alpha}:=\sum_{s=1}^{\infty}u(s)\;v(s)\;\Psi_{\rho,\alpha}(s)\quad, $$ 

where  $ u, v : \mathbb{N} \to \mathbb{R} $ can be interpreted as sequences or as grid functions on  $ \mathbb{N} $. The isometric isomorphism

 $$ T_{\rho,\alpha}:H^{\rho,\alpha}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid(u,u)^{\rho,\alpha}<\infty\right\}\longrightarrow H_{\rho,\alpha} $$ 

defined by

 $$ (T_{\rho,\alpha}u)(s)=u(s)\Psi_{\rho,\alpha}(s) $$ 

will transform the polynomial basis $\{l_k(\rho, \alpha)\}$ of $H^{\rho,\alpha}$ to the basis $\{\psi_k(\rho, \alpha)\} := \{\Psi_{\rho,\alpha} l_k(\rho, \alpha)\}$ of $H_{\rho,\alpha}$. This has to be kept in mind in the following, because it will be switched between both bases very often.

We know from [10], Theorem 3.1, that there exists an orthogonal set of polynomials with respect to the scalar product (2.5), if all statistical moments  $ \mu_k[\Psi_{\rho,\alpha}] $ are bounded and the determinant condition

 $$ \Delta_{n}:=\det\left(\mu_{i+j}[\Psi_{\rho,\alpha}]\right)_{i,j=0}^{n}=\left|\begin{array}{c c c c}\mu_{0}&\mu_{1}&\cdots&\mu_{n}\\ \mu_{1}&\mu_{2}&\cdots&\mu_{n+1}\\ \vdots&\vdots&\vdots&\vdots\\ \mu_{n}&\mu_{n+1}&\cdots&\mu_{2n}\end{array}\right|\neq0 $$ 