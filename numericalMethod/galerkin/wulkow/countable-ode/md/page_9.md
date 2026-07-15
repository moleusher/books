The series on the right-hand side converges uniformly, since  $ u(t) \in C^{1}((0,T],l^{1}) $ by assumption and we can insert  $ u_{s}(t)=v_{s}(t)-v_{s+1}(t) $ into the s-th equation of the system (1.7). This yields the relation

 $$ v_{s}^{\prime}(t)+\left(s-1\right)v_{s}(t)=v_{s+1}^{\prime}(t)+s v_{s+1}(t), $$ 

which must be independent of s. If we denote the common value of both sides of (1.8) by  $ f(t) $, we can compute  $ v_s(t) $ by solving the linear ordinary differential equation

 $$ v_{s}^{\prime}(t)+\left(s-1\right)v_{s}(t)=f(t), $$ 

which easily leads to

 $$ .v_{s}(t)=v_{s}(0)e^{-(s-1)t}+\int_{0}^{t}e^{(s-1)(\tau-t)}f(\tau)\mathrm{d}\tau,s\in\mathbb{N}. $$ 

Finishing up with the re-substitution of the  $ u_{s} $ we get

 $$ u_{s}(t)=v_{s}(0)e^{-(s-1)t}-v_{s+1}(0)e^{-s t}-\int_{0}^{t}e^{s(\tau-t)}\left[1-e^{t-\tau}\right]f(\tau)\mathrm{d}\tau. $$ 

This shows, that the initial value problem (1.7) has solutions depending on an arbitrary function  $ f $, which only has to be integrable. From [30] we know, that (1.9) is in fact a solution in  $ l^{1} $. The task now is to find a sequence space, in which the solution is unique. For this, we define a family of Hilbert spaces

 $$ H_{t}:=\left\{u\in\mathbb{R}^{\mathbb{N}}\mid\|u\|_{t}^{2}:=\sum_{s=1}^{\infty}u_{s}^{2}e^{s t}<\infty\right\}, $$ 

and show, that the condition  $ u(t) \in H_t $ enforces uniqueness of the solution. A short calculation yields, that

 $$ \sum_{s=1}^{\infty}\left(v_{s}(0)e^{-(s-1)t}-v_{s+1}(0)e^{-st}\right)^{2}e^{st} $$ 

is bounded for  $ \varphi \in l^1 $,  $ t \in [0, T] $. Thus we can show that  $ u(t) \in H_t $, if

 $$ \sum_{s=1}^{\infty}\left(\int_{0}^{t}e^{s(\tau-t)}\left[1-e^{t-\tau}\right]f(\tau)\mathrm{d}\tau\right)^{2}e^{s t} $$ 

is bounded. This implies that

 $$ \int_{0}^{t}e^{s\tau-\frac{s t}{2}}\left[1-e^{t-\tau}\right]f(\tau)\mathrm{d}\tau\to0\quad\mathrm{f o r}\quad s\to\infty, $$ 