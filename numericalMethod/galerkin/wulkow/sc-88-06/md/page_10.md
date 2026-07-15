Lumping. A popular method to reduce the large number of (stiff) ordinary differential equations is the so-called lumping technique. In this approach, polymer species of chain lengths within certain prescribed intervals are “lumped” together to certain superspecies. It is clear that an appropriate interval definition requires a lot of a-priori insight into the chemical process (cf. [11]). Nevertheless, even in the best cases, this lumping technique introduces a modeling error of unknown size — which may be totally unacceptable especially in nonlinear models.

 $$ \sigma^{2} $$ 

Statistical moment treatment. The classical statistical moments are defined

 $$ \mu_{k}(t):=\sum_{s=1}^{\infty}s^{k}P_{s}(t),\quad k=0,1,\cdots. $$ 

Insertion of this definition into the kinetic models (cf. Section 1.1) leads to a system of ordinary differential equations for  $ \mu_{0}, \mu_{1}, \ldots $.

Mathematically speaking, the (bounded) infinite sequence  $ \mu_0 $,  $ \mu_1 $, ... essentially determines the distribution density  $ P_s $ — which is the well-known Stieltjes problem of mathematical statistics [20]. If, however, only a finite number of moments  $ \mu_0 $, ...,  $ \mu_N $ is known, then associated approximations  $ P_s^{(N)} $ of the exact distribution  $ P_s $ may vary within an extremely wide range! A detailed theoretical discussion of this fact and its consequences will be given in Section 2.2 below, a numerical illustration in Section 5.

For the sake of completeness, recall that mass conservation shows up in this treatment as

 $$ \mu_{0}(t)={~c o n s t.~}, $$ 

if (1.11) holds, or as

 $$ \mu_{1}(t)={~c o n s t.~}, $$ 

if (1.12) holds. (Herein,  $ P_{s}(t) $ in (1.13) must be replaced by  $ N_{s}(t) $, of course).

Continuous Models. In this kind of model, the polymer degree appears as a continuous real variable  $ s \geq 0 $. The polymer distribution  $ P_s(t) \equiv P(s, t) $ is then determined by a partial integro-differential equation. For example, the kinetic equations (1.4) are transformed to (see RAY [18]):

 $$ \begin{array}{r c l}{{a)}}&{{\displaystyle\frac{\partial}{\partial t}P(s,t)}}&{{=}}&{{\displaystyle-\frac{\partial}{\partial s}P(s,t)+\frac{1}{2}\left(\frac{\partial}{\partial s}\right)^{2}P(s,t)}}\\ {{}}&{{}}&{{}}&{{}}\\ {{b)}}&{{P(s,0)}}&{{=}}&{{P_{10}\cdot\delta(s-1)~,}}\\ \end{array} $$ 

where $\delta$ means the Dirac-distribution. However, RAY already indicates that the number of terms used in the Taylor expansion of the above right-hand side needs