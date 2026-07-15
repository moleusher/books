<div style="text-align: center;"><img src="imgs/img_in_image_box_428_253_789_537.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">Figure 2: Sketch of the flow of information for one single domain.</div>


$$D^{(n)} = I^{(n,1)} \otimes I^{(n,2)},\ \text{and to be tested with all such pairs from test elements } D^{(m)} = I^{(m,1)} \otimes I^{(m,2)}.\ \text{Thus we have to compute double sums } S = S(i,j,k,l;n,m)\ \text{of the form}$$

 $$ S=\sum_{x\in I^{(n,1)}}\sum_{y\in I^{(n,2)}}T_{i}^{(m,1)}(x)T_{j}^{(m,2)}(y)\alpha(x-1,y+1)T_{k}^{(n,1)}(x-1)T_{l}^{(n,2)}(y+1) $$ 

for all $i,j,k,l$ and $1 \leq m,n \leq M$. Here, the complexity is reduced by the fact that only neighboring elements can lead to non-zero $S$. The intersection of the edges of neighboring elements will be denoted by

 $$ \begin{array}{r c l}{I_{S}^{1}}&{=}&{[\operatorname*{m a x}(L^{(m,1)},L^{(n,1)}-1),\operatorname*{m i n}(U^{(m,1)},U^{(n,1)}-1)]}\\ {I_{S}^{2}}&{=}&{[\operatorname*{m a x}(L^{(m,2)},L^{(n,2)}+1),\operatorname*{m i n}(U^{(m,2)},U^{(n,2)}+1)].}\\ \end{array} $$ 

Note that the  $ I_{S}^{i} $ may consist of a single point, which will contribute to the summation. Depending on the structure of the propensity function  $ \alpha = \alpha(x, y) $ two different scenarios are discussed below.

For the first scenario we assume that the propensity factorizes according to  $ \alpha(x,y)=\alpha_{1}(x)a_{2}(y) $. Then we obtain

 $$ \begin{array}{r c l}{S}&{=}&{\displaystyle\sum_{x\in I_{S}^{1}}\alpha_{1}(x)T_{i}^{(m,1)}(x)T_{k}^{(n,1)}(x-1)\cdot}\\ {}&{}&{\displaystyle\sum_{y\in I_{S}^{2}}\alpha_{2}(y)T_{j}^{(m,2)}(y)T_{l}^{(n,2)}(y+1)}\\ \end{array} $$ 