<div style="text-align: center;"><img src="imgs/img_in_image_box_256_228_970_324.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">TABLE 4.1: Coefficients  $ \alpha_{j}^{k} $ up to row k = 5 due to [8].</div>


The order control mechanism. As described by DEUFLHARD [15] we control the ‘order’, represented here by the row in the extrapolation table, simultaneous with the time-step. Relation (4.13) (replacing the semi discrete by the fully discrete error estimation) supplies us with step-size guesses  $ T_{j+1,j} $ for convergence of  $ U_{j+1,j} $, that means the algorithm expects  $ U_{j+1,j} $ to be near to the solution within the given tolerance. As in [15] we define

the normalized work per unit step, where  $ A_{j+1} $ measures the amount of work for achieving  $ U_{j+1,j+1} $, which is in turn depending on the work required by the CAE solver aiming at accuracy  $ \epsilon $ given in (4.21). But this  $ \epsilon $ does not only depend on j, the row of the table, but also on k, the final row, to which the table will be build up. Thus we should replace (4.22) by

 $$ \mathcal{W}_{j+1,j}:=\frac{T}{T_{j+1,j}}A_{j+1} $$ 

 $$ \mathcal{W}_{j+1,j}^{k}:=\frac{T}{T_{j+1,j}}A_{j+1}^{k}\;, $$ 

introducing  $ A_{j+1}^k $ as the amount of work for obtaining  $ U_{j+1,j+1} $ in a table up to  $ U_{kk} $. These  $ A_{j+1}^k $ will depend on the CAE solver or the projection mechanism. On this basis we can actually determine an optimal column index q by

 $$ \mathcal{W}_{q+1,q}^{q+1}=\operatorname*{m i n}_{j=1,\ldots,k-1}\mathcal{W}_{j+1,j}^{j+1}\;. $$ 

Knowing this q, we use the step-size guess  $ T_{q+1,q} $ for the next basic time–step and expect convergence in the vicinity of q. In order to get a reliable code, avoiding pseudo-convergence and related undesirable things which occur in practice three devices have to be implemented.

☑ convergence monitor

• order window

- a device for possible increase of order greater than q

– see for instance DEUFLHARD [16].