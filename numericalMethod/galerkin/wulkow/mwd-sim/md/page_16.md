1. Type of improvement: Decide, whether an interval  $ I_{i} $ has to be bisected or the present polynomial order p has to be increased. For that, the behavior of the error of the local expansion is compared to an error prediction model.

2. Cut-value: Compute a threshold value to decide which intervals have to be changed (bisection or increase of order).

3. Assemble and solve: Build up the Galerkin equations which describe the expansion coefficients on all intervals for all distributions and solve them.

4. Estimate: Estimate the error of the obtained solution. This works comparable to the weighted Galerkin method by considering the (local) expansion coefficients  $ a_{n+1}^{l} $.

5. Loop control: If the error is smaller than the required tolerance stop, otherwise go back to 1.

## Refinement strategy

The refinement strategy has to reduce not only the number of degrees of freedom but also the number of levels to obtain the final node-order-pattern. This can be done by a work-oriented device. For that, the following questions have to be answered:

● How does the error behave, if an interval is refined?

● How does the error behave, if the order is increased?

● How large is the effort to perform one of the above operations related to the obtained error and the required error?

● Which intervals will be improved?

We exemplify this part of the algorithm by the following situation: given an interval with width h, order p and error  $ \varepsilon(h, p) $. Let us assume that we also know the errors  $ \varepsilon(h, p - 1) $,  $ \varepsilon(2h, p - 1) $ and  $ \varepsilon(2h, p) $. Then the error predictions  $ \varepsilon(h/2, p - 1) $ and  $ \varepsilon(h, p + 1) $ can be obtained by extrapolation

 $$ \varepsilon(h/2,p-1)=\frac{\varepsilon(h,p-1)^{2}}{\varepsilon(2h,p-1)}\quad\varepsilon(h,p+1)=\frac{\varepsilon(h,p)^{2}}{\varepsilon(h,p-1)} $$ 

For the amount of work  $ w(p) $ to treat an interval with order  $ p $, we assume  $ w(p) \sim p $. However, not the absolute work  $ w(p) $ is important, but the effort to obtain the required accuracy. So for our possible decisions (increase  $ p $ by one or bisect the interval setting the order to  $ p - 1 $) we compare the normalized work  $ w(p + 1)\varepsilon(h, p + 1) $ and  $ 2w(p - 1)\varepsilon(h/2, p - 1) $. The alternative with a minimal normalized work will be chosen. In a more general setting, one may try to examine more alternatives, but this would lead too far here.

Finally we have to take care that the error on the complete grid is equilibrated. For that, a cutting value is computed by the maximum of all error predictions and only these intervals are improved whose error is beyond the cutting value. More details for such refinement strategies can be found in refs. $ ^{21,26,28} $