# Buffon's Needle README

If you randomly drop needles onto a plane with parallel lines spaced a distance of 2 needles apart, the total number of needles over those that intersect a line approaches $\pi$???
Mysterious, huh? Let's see what's going on!

![Buffon’s Needle Demo](buffons-needle-visual.png)

This is a small project to learn and practice fascinating (geometric) probability theory, specifically Monte Carlo simulations.

---

## Here is the Math Explained

Let’s say the needle has length $\ell$.

- For intersection, we care about the position $y$ (for horiziontal lines) of the needle’s center and the angle $\theta$.
- The probability density of the center of the needle is  
  $P_y = \frac{1}{\ell}$
- The probability density of the angle is  
  $P_\theta = \frac{2}{\pi}$
- The probability for the needle to cross a line is given by the double integral  
  $P = \iint \bigl(P_y \,P_\theta\bigr)\,dy\,d\theta$
- The condition for the needle to cross the line is  
  $y < \frac{\ell}{2}\sin(\theta)$
- Therefore, the $y$ integration bounds are from $0$ to $\frac{\ell}{2}\sin(\theta)$, and the $\theta$ integration goes from $0$ to $\frac{\pi}{2}$.

Following through with these integrals, we get:

$$
P =
\int_{0}^{\pi/2}
\int_{0}^{(\ell/2)\sin(\theta)}
\left(\frac{1}{\ell} \cdot \frac{2}{\pi}\right)
\,dy\,d\theta
$$

First, combine the constants:

$$
P =
\int_{0}^{\pi/2}
\int_{0}^{(\ell/2)\sin(\theta)}
\frac{2}{\pi \ell}
\,dy\,d\theta
$$

Now evaluate the inside integral with respect to $y$:

$$
P =
\int_{0}^{\pi/2}
\frac{2}{\pi \ell}
\left[
y
\right]_{0}^{(\ell/2)\sin(\theta)}
d\theta
$$

Plug in the bounds for $y$:

$$
P =
\int_{0}^{\pi/2}
\frac{2}{\pi \ell}
\left(
\frac{\ell}{2}\sin(\theta) - 0
\right)
d\theta
$$

Simplify:

$$
P =
\frac{1}{\pi}
\int_{0}^{\pi/2}
\sin(\theta)
\,d\theta
$$

Now integrate:

$$
P =
\frac{1}{\pi}
\left[
-\cos(\theta)
\right]_{0}^{\pi/2}
$$

Evaluate the bounds:

$$
P =
\frac{1}{\pi}
\left(
-\cos(\pi/2) + \cos(0)
\right)
$$

Since $\cos(\pi/2)=0$ and $\cos(0)=1$,


$P =\frac{1}{\pi}$


Going back to the problem, if you drop $N_{\text{tot}}$ total needles, we expect approximately
$N_{\text{cross}} \=\ N_{\text{tot}} \times \frac{1}{\pi}$
needles to cross a line. Rearranging this, we get
$\frac{N_{\text{tot}}}{N_{\text{cross}}} \\approx\ \pi$
As $N_{\text{tot}}$ becomes very large, this ratio converges to $\pi$ (by the Law of Large Numbers), making it a neat way to estimate $\pi$ empirically.

---

## How Fast Does It Approach $\pi$?

The estimate approaches $\pi$, but slowly. Each needle drop is a Bernoulli trial: it either crosses a line or it does not. Since the crossing probability is

$$p = \frac{1}{\pi}$$

the number of crossings after $N_{\text{tot}}$ drops follows a binomial distribution:

$$N_{\text{cross}} \sim \text{Binomial}\left(N_{\text{tot}}, p\right)$$

The observed crossing probability is

$$\hat{p} = \frac{N_{\text{cross}}}{N_{\text{tot}}}$$

and since $p = 1/\pi$, our estimate of $\pi$ is

$$\hat{\pi} = \frac{1}{\hat{p}} = \frac{N_{\text{tot}}}{N_{\text{cross}}}$$

For a binomial experiment, the standard error of the observed proportion is

$$\text{SE}(\hat{p}) = \sqrt{\frac{p(1-p)}{N_{\text{tot}}}}$$

So the error in the crossing probability shrinks like

$$\frac{1}{\sqrt{N_{\text{tot}}}}$$

To understand how this affects the estimate of $\pi$, think of $\hat{\pi}$ as a function of $\hat{p}$:

$$f(\hat{p}) = \frac{1}{\hat{p}}$$

The derivative is

$$f'(\hat{p}) = -\frac{1}{\hat{p}^2}$$

This tells us how sensitive the $\pi$ estimate is to small errors in the crossing probability. Near the true value $p = 1/\pi$, this derivative is approximately

$$f'(p) = -\pi^2$$

So a small error in $\hat{p}$ becomes about $\pi^2$ times larger when converted into an error in $\hat{\pi}$. However, multiplying by a constant does not change the overall convergence rate.

Therefore, Buffon's Needle has the usual Monte Carlo convergence rate:

$$\text{error} = O\left(\frac{1}{\sqrt{N_{\text{tot}}}}\right)$$

This means that to make the estimate about 10 times more accurate, we need about 100 times more needle drops.
