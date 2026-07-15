The truncation index  $ s_{max} $ is not known a priori, but practical considerations lead to the order of magnitude  $ s_{max} = 50.000 $, which means that the above system consists of 100.000 differential equations!

Standard computational approaches to solve such systems would include

- Large scale stiff integration by the sparse mode of any of the more efficient stiff integrators such as the BDF method (Gear, Hindmarsh) or a semi-implicit extrapolation integrator (Deuflhard et al.). However, a prohibitive feature of these systems often is that the Jacobian, which is used in all of these integrators, is not really sparse — which drives the storage and computation time beyond reasonable bounds.

● Lumping techniques. In this approach knowledge about details of the chemical process (in isolated form!) is applied to derive a rule for arranging appropriate compartments of polymers to obtain smaller differential systems. This method works nicely in linear models only. Its extension to nonlinear models, however, is more than dubious.

● Statistical moment treatment. This rather popular method suffers from the serious drawback that it is not really clear when to truncate the number of moments to be computed — at least in the most frequent case of so-called open loops.

- Continuous modelling by partial integro-differential equations of neutron transport type. However, this type of modelling makes the discrete variable s artificially a continuous variable – a mathematical crime which is punished by the occurrence of ill-posed problems in realistic models.

In this situation, Deuflhard and Wulkow had suggested a new approach, which they called discrete Galerkin method. This approach combines the advantages of all of the other approaches and avoids the disadvantages — as described in the initializing paper [13]. Two variants of this method are now given in the subsequent survey.