Even for distributions with high polydispersity this device works quite reliable as shown in the numerical section.

Remark: The dynamic of the integration process can additionally be captured by setting

 $$ s_{\mathrm{m a x}}^{\mathrm{n c w}}=s_{\mathrm{m a x}}^{\mathrm{n e w}}+c(s_{\mathrm{m a x}}^{\mathrm{n e w}}-s_{\mathrm{m a x}}^{\mathrm{o l d}})\quad c>0 $$ 

after evaluation of Eq. (11).

## Grid propagation

The most simple way to start the multilevel process would be a node-order-pattern of the form

 $$ \varDelta_{0}=\{([1,s_{\operatorname*{m a x}}],2)\} $$ 

But this would imply the loss of all information obtained in previous time steps resulting in too much refinement levels. The other extreme is to start with the final pattern from the last time step, but this leads to an increasing number of variables. Thus we need an heuristic, which keeps as much information as possible but is also able to delete nodes or to decrease orders. A simple device for that is:

## Heuristic 1

1. Take the final grid of the last step.

2. Eliminate each second interval.

3. Reduce all remaining orders by a certain number (e.g. by 1).

This strategy has turned out to be a very stable and reliable one, in particular for moving distributions, where old grid points have to be eliminated by time. However, when a distribution does not change its form in a time step, the reconstruction of the optimal grid can take a few levels longer than apparently necessary. An improvement of heuristic 1 is obtained by

## Heuristic 2

1. Take the final grid of the last step.

2. Eliminate all intervals with low order, i.e. intervals which are possibly not necessary.

3. Add an eliminated interval to the neighborhood interval with lower order.

The experiences with many attempts for such devices show that the grid propagation should not depend on error estimates, because in this case the algorithm has less chance to recover if an estimate fails.

Now we turn to the inner loop of the h-p-algorithm, where the multilevel process is performed.

## Algorithm III, building up the final node-order-pattern

Given: a starting grid and an error estimate of the local expansion on intervals  $ I_{i} $ of the grid.