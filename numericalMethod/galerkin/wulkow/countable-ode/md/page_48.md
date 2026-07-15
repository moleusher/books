(i)  $ \tau A $ is contractive. Then the estimation

 $$ \left|\left|u-u^{n}\right|\right|\leq\left(1-\tau\left|\left|A\right|\right|_{\rho,\alpha}\right)^{-1}\left|\left|u-\mathcal{P}_{n}^{\rho,\alpha}u\right|\right| $$ 

holds.

(ii) A is generator of a $C_{0}$-semigroup of contractions and additionally invariant. Then we have convergence for $\tau > 0$ and for the Galerkin solution $u^{n}$ holds

 $$ u^{n}=\mathcal{P}_{n}^{\rho,\alpha}u. $$ 

Proof. (i) As  $ \|\mathcal{P}_n^\rho, \alpha A\|_{\rho, \alpha} \leq \|A\|_{\rho, \alpha} $ the equations (3.8) and (3.9) have unique solutions by the Banach fixed-point theorem. Further

 $$ \|(I-\tau\mathcal{P}_{n}^{\rho,\alpha}A)^{-1}\|_{\rho,\alpha}\leq(1-\tau\|A\|_{\rho,\alpha})^{-1} $$ 

by use of the Neumann series. Summarizing (3.8) and (3.9) we obtain

 $$ (I-\tau\mathcal{P}_{n}^{\rho,\alpha}A)(u-u^{n})=u-\mathcal{P}_{n}^{\rho,\alpha}u $$ 

and therefore (3.12) and the convergence for  $ n \to \infty $.

(ii) We know that  $ (I - \tau A) $ is invertible for all  $ \tau > 0 $. The question is, what can be said about  $ (I - \tau \mathcal{P}_n^{\rho,\alpha} A)^{-1} $? From perturbation theory it is known, that the uniform boundedness of

 $$ \|A-\mathcal{P}_{n}^{\rho,\alpha}A\|_{\rho,\alpha}\mathrm{~f o r~}n\to\infty $$ 

is crucial (see e.g. [34], IV.3, IV.4). This condition is met for compact operators A and the convergence of the Galerkin method can be proven ([53], Theorem 21.G,(b)). For A invariant a result by means of semigroup theory can be derived. The infinitesimal generator A of a  $ C_0 $-semigroup of contractions is characterized by the Lumer-Phillips theorem:

A is dissipative, i.e.  $ (Au, u) \leq 0 $ and for a  $ \lambda_0 > 0 $ the range of  $ \lambda_0 I - A $ is  $ H_{\rho, \alpha} $. For  $ u^n \in H_{\rho, \alpha}^n $ it follows from

 $$ \left(\mathcal{P}_{n}^{\rho,\alpha}A u^{n},u^{n}\right)_{\rho,\alpha}=\left(A u^{n},u^{n}\right)_{\rho,\alpha} $$ 

that  $ \mathcal{P}_n^{\rho,\alpha}A $ is also dissipative and the range condition is fulfilled in  $ H_{\rho,\alpha}^n $ since  $ \mathcal{P}_n^{\rho,\alpha}A = \mathcal{P}_n^{\rho,\alpha}A\mathcal{P}_n^{\rho,\alpha} $. Hence  $ \mathcal{P}_n^{\rho,\alpha}A $ generates a contractive  $ C_0 $ - semigroup too. Note that if the original and the Galerkin equation are uniquely solvable and  $ A $ is invariant, we always have  $ u^n = \mathcal{P}_n^{\rho,\alpha}u $.

The derivation of the Galerkin equations uses (if possible) properties of the discrete Laguerre polynomials. As an illustration we consider again the