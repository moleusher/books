Discrete Simpson rule. Now take three nodes,  $ s_0 $,  $ s_1 $,  $ s_2 $, where  $ s_1 := s_0 + \delta_1 $ and  $ s_2 := s_1 + \delta_2 $. As the local error estimation will compare Trapezoidal sums on an interval with Simpson sums we are interested in approximations  $ S^L(\delta_1, \delta_2) $ and  $ S^R(\delta_1, \delta_2) $ of  $ \sum_{s=s_0}^{s_1} f(s) $ and  $ \sum_{s=s_1}^{s_2} f(s) $. Some tedious calculations (which fortunately could have been performed with the algebraic package REDUCE) lead to the following expressions:

 $$ \begin{array}{rcl}S^{L}(\delta_{1},\delta_{2})&=&f_{0}\frac{(2\delta_{1}+3\delta_{2}+1)(\delta_{1}+1)}{6(\delta_{1}+\delta_{2})}+f_{1}\frac{(\delta_{1}+3\delta_{2}-1)(\delta_{1}+1)}{6\delta_{2}}\\&&-f_{2}\frac{\delta_{1}(\delta_{1}^{2}-1)}{6\delta_{2}(\delta_{1}+\delta_{2})}\end{array} $$ 

for the left interval  $ \{s_{0},\ldots,s_{0}+\delta_{1}\} $ and

 $$ \begin{array}{rcl}\boldsymbol{S}^{R}(\delta_{1},\delta_{2})&=&-f_{0}\frac{\delta_{2}(\delta_{2}^{2}-1)}{6\delta_{1}(\delta_{1}+\delta_{2})}+f_{1}\frac{(3\delta_{1}+\delta_{2}-1)(\delta_{2}+1)}{6\delta_{1}}\\&+&f_{2}\frac{(3\delta_{1}+2\delta_{2}+1)(\delta_{2}+1)}{6(\delta_{1}+\delta_{2})}\end{array} $$ 

for the right interval  $ \{s_{1},\ldots,s_{1}+\delta_{2}\} $.

The above formulas are the basis of the SUMMATOR.

Error estimation. Let  $ I_j^i $ and  $ I_{j+1}^i $ be sub-intervals of  $ I $ which have been generated on refinement level  $ i $ by subdividing an interval  $ I_k^{i-1} $. We denote by  $ T_{I_j^i} $ the Trapezoidal sum on  $ I_j^i $ and by  $ S_{I_j^i} $ the Simpson sum using the three different  $ f $-values the end points of  $ I_j^i $ and  $ I_{j+1}^i $ and the formula (6.8) (analogue for the right sub-interval).

<div style="text-align: center;"><img src="imgs/img_in_image_box_349_942_929_1105.jpg" alt="Image" width="48%" /></div>


Then the error

 $$ |T_{I_{j}^{i}}-\sum_{I_{j}^{i}}f(s)| $$ 

will be estimated by

 $$ \varepsilon_{j}^{i}:=|T_{I_{j}^{i}}-S_{I_{j}^{i}}|\;, $$ 

assuming that the Simpson formula will be significantly more accurate on  $ I_{j}^{i} $ than the Trapezoidal rule.