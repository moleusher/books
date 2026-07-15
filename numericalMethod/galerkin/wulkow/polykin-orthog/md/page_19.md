As in the continuous case, a Rodrigues-formula can be proved:

 $$ l_{k}(s)=\rho^{-s}\Delta^{k}\left[\left(\begin{array}{c}s-1\\ k\end{array}\right)\rho^{s}\right] $$ 

where  $ \Delta $ denotes the forward difference operator

 $$ \Delta\;f(s):=f(s+1)-f(s)\;. $$ 

In lieu of  $ (3.3.a, b) $, the following direct representation is sometimes useful:

 $$ l_{k}(s)=\rho^{k}\sum_{\nu=0}^{k}\left(\begin{array}{c}k\\ \nu\end{array}\right)\left(\frac{\rho-1}{\rho}\right)^{\nu}\left(\begin{array}{c}s-1\\ \nu\end{array}\right)\;. $$ 

From this, one readily verifies

 $$ \begin{array}{r c l}{{{\bf a})}}&{{l_{k}(0)}}&{{=}}\\ {{}}&{{}}&{{1}}\\ {{{\bf b})}}&{{l_{k}(1)}}&{{=}}\\ \end{array}\rho^{k} $$ 

For the treatment of the polyreaction model problems (Section 1.1 and Section 4), the following selection of properties are selected:

 $$ l_{k}(s+1)-l_{k}(s)=(\rho-1)\sum_{\nu=0}^{k-1}\rho^{k-1-\nu}l_{\nu}(s) $$ 

 $$ l_{k}(s-1)-l_{k}(s)=(1-\rho)\sum_{\nu=0}^{k-1}l_{\nu}(s) $$ 

 $$ \sum_{r=1}^{s}l_{k}(r)=\frac{1}{1-\rho}\left[l_{k}(s)-l_{k+1}(s)\right] $$ 

 $$ \sum_{r=1}^{s-1}l_{k}(r)l_{j}(s-r)=\frac{1}{1-\rho}\left(\rho l_{k+j}(s)\cdots r_{i+j+1}(s)\right) $$ 

In order to adapt the free parameter  $ \rho $ according to (2.25), one needs that

 $$ \nu_{1}=(1-\rho)^{-1} $$ 

which, in turn, leads to

 $$ 1-\rho=\frac{\mu_{0}}{\mu_{1}}. $$ 