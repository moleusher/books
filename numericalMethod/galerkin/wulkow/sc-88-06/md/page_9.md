Coagulation [12] and irreversible polycondensation [18]. These processes can be modelled by the following system of nonlinear ordinary differential equations:

 $$ N_{s}^{\prime}=\frac{1}{2}\sum_{r=1}^{s-1}k_{r,s-r}N_{r}N_{s-r}-N_{s}\sum_{r=1}^{\infty}k_{s r}N_{r}\quad,\quad s=1,2, $$ 

Let an initial distribution  $ N_{s}(0) $ be given. With the additional specification

 $$ k_{s r}=k_{p} $$ 

this model is also referred to as Smoluchowski coagulation model. At the same time, RAY [18] uses (1.9) with (1.10) to model the polycondensation of A-B type monomer. As an example of this mechanism, [18] mentions the production of pólysters from hydroxy acids in a well-stirred batch reactor. Note that under the specification (1.10) the nonlinear system (1.9) can be solved in closed analytic form.

In the case of heterogeneous reactions, fractional powers like in (1.8.b,c) may also arise in model (1.9) — e.g. in soot formation [13].

Mass conservation. For the first two models, (1.4) and (1.6), one easily verifies that

 $$ \sum_{s=1}^{\infty}P_{s}^{\prime}(t)=0\quad,\quad t>0\;, $$ 

which means mass conservation:

 $$ \sum_{s=1}^{\infty}P_{s}(t)=\sum_{s=1}^{\infty}P_{s}(0)\quad,\quad t>0\;. $$ 

For the other two models, (1.7) and (1.9), mass conservation shows up in the form

 $$ \sum_{s=1}^{\infty}s N_{s}^{\prime}(t)=0\quad,\quad t>0\quad, $$ 

which is equivalent to

\[\begin{array}{r l}{\frac{\partial\left(S_{1}\right.}{\partial t}\frac{\partial\left(S_{2}\right.}{\partial t}\right)\left(\frac{\partial\left(S_{1}\right.}{\partial t}\frac{\partial\left(S_{2}\right.}{\partial t}\right)}&{{}\displaystyle\sum_{s=1}^{\infty}s N_{s}(t)=\displaystyle\sum_{s=1}^{\infty}s N_{s}(0)\quad,\quad t>0~.}\\ {\frac{\partial\left(S_{1}\right.}{\partial t}\frac{\partial\left(S_{2}\right.}{\partial t}\right)\left(\frac{\partial\left(S_{1}\right.}{\partial t}\frac{\partial\left(S_{2}\right.}{\partial t}\right)}&{{}\displaystyle\sum_{s=1}^{\infty}s N_{s}(t)=\frac{\partial\left(S_{1}\right.}{\partial t}\frac{\partial\left(S_{2}\right.}{\partial t}\right)\left(\frac{\partial\left(S_{1}\right.}{\partial t}\frac{\partial\left(S_{2}\right.}{\partial t}\right)\left(\frac{\partial\left(S_{1}\right.}{\partial t}\frac{\partial\left(S_{2}\right.}{\

### 1.2 Standard Computational Approaches

Large scale stiff integration. On the basis of chemical insight into a specific polyreaction process, the infinite system of differential equations may be truncated. The arising finite systems are usually still large and stiff — with a rather full Jacobian matrix. As a consequence, this kind of simulation leads to prohibitive array storage and computing time.