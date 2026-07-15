In literature problems with invariant operators are sometimes called self-closing, problems with m-invariant or general operators are called open. In order to explain Definition 3.1, we consider

 $$ u\in H_{\rho,\alpha},u=x+y,x=\mathcal{P}_{n}^{\rho,\alpha}u,y=(I-\mathcal{P}_{n}^{\rho,\alpha})u. $$ 

From (3.5) it follows for an invariant operator A that

 $$ \mathcal{P}_{n}^{\rho,\alpha}\;A y=0\;, $$ 

that means the complement of  $ H_{\rho,\alpha}^n $ is invariant under  $ A $. Similar considerations turn out that with (3.6) an  $ m $-invariant operator  $ A $ maps the complement of  $ H_{\rho,\alpha}^m $ onto the complement of  $ H_{\rho,\alpha}^n $. By this notions the backward shift operator  $ S_- $ is invariant, since

 $$ \mathcal{P}_{n}^{\rho,\alpha}S_{-}u=\sum_{j=0}^{n}\frac{1}{\gamma_{j}^{\rho,\alpha}}\left(S_{-}u,\psi_{j}\right)_{\rho,\alpha}\psi_{j}=\sum_{j=0}^{n}\frac{1}{\gamma_{j}^{\rho,\alpha}}\left(u,\left.S_{+}\psi_{j}\right)_{\rho,\alpha}\psi_{j}\right.. $$ 

With relation (2.31) the last scalar product can be expressed in terms of the coefficients  $ a_k $,  $ k \leq j $, if we assume an  $ H_{\rho,\alpha} $ - expansion of  $ u $. For the forward shift operator  $ S_+ $ things are different:

 $$ \mathcal{P}_{n}^{\rho,\alpha}S_{+}u=\sum_{j=0}^{n}\frac{1}{\gamma_{j}^{\rho,\alpha}}\left[\left(u\;,S_{-}\psi_{j}\right)_{\rho,\alpha}-u_{1}\psi_{j}(0)\right]\;\psi_{j}\;, $$ 

where the component  $ u_1 $ depends on all expansion coefficients  $ a_k $ of  $ u $. Thus  $ S_+ $ is a general operator and this makes the classification from the beginning of Section 1.3 consistent with the above definition in  $ H_{\rho,\alpha} $: if  $ (Au)_s $ depends on the component  $ u_{s+r} $,  $ r \in \mathbb{N} $, it can be expressed in terms of  $ S_+ $.

As a last example we mention that the degradation operator is 1-invariant (see Example 5.3).

For the treatment of m-invariant or general operators we have to replace

 $$ \mathcal{P}_{n}^{\rho,\alpha}\;A\to\mathcal{P}_{n}^{\rho,\alpha}A\mathcal{P}_{n+\tilde{n}}^{\rho,\alpha} $$ 

for some  $ \tilde{n} > 0 $. That means we use the coefficients  $ a_0, \ldots, a_{n+\tilde{n}} $ of  $ u $ to obtain approximations of the first  $ n+1 $ expansion coefficients of  $ Au $. Obviously we expect, that these approximations will become better for increasing  $ \tilde{n} $.

As in the situation of projections of elements above, the scalar products

 $$ \begin{array}{r l}{(A u\;,\;\psi_{j})_{\rho,\alpha}}&{{}\mathrm{r e s p e c t i v e l y}\;(A\psi_{k}\;,\;\psi_{j})_{\rho,\alpha}\;,\;j,\;k=0,\;1,\ldots,\;n,}\end{array} $$ 

can only be evaluated by numerical approximation in general, leading to a perturbed expansion (3.1).