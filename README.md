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


$P =\frac{1}{\pi}(1)=\frac{1}{\pi}$


Going back to the problem, if you drop $N_{\text{tot}}$ total needles, we expect approximately
$N_{\text{cross}} \=\ N_{\text{tot}} \times \frac{1}{\pi}$
needles to cross a line. Rearranging this, we get
$\frac{N_{\text{tot}}}{N_{\text{cross}}} \\approx\ \pi$
As $N_{\text{tot}}$ becomes very large, this ratio converges to $\pi$ (by the Law of Large Numbers), making it a neat way to estimate $\pi$ empirically.

---

## How Fast Does It Approach $\pi$?

The estimate approaches $\pi$, but slowly. Each needle drop is a random trial with crossing probability

$$p = \frac{1}{\pi}$$

If we drop $N_{\text{tot}}$ needles, then the observed crossing probability is

$$\hat{p} = \frac{N_{\text{cross}}}{N_{\text{tot}}}$$

Since $p = 1/\pi$, we estimate $\pi$ by taking the reciprocal:

$$\hat{\pi} = \frac{1}{\hat{p}} = \frac{N_{\text{tot}}}{N_{\text{cross}}}$$

For a binomial experiment, the standard error of $\hat{p}$ is

$$\text{SE}(\hat{p}) = \sqrt{\frac{p(1-p)}{N_{\text{tot}}}}$$

So the error in $\hat{p}$ shrinks like

$$\frac{1}{\sqrt{N_{\text{tot}}}}$$

Now use the derivative idea. Since

$$f(p) = \frac{1}{p}$$

we have

$$f'(p) = -\frac{1}{p^2}$$

At $p = 1/\pi$,

$$f'(p) = -\pi^2$$

So small errors in $\hat{p}$ get multiplied by about $\pi^2$ when converted into errors in $\hat{\pi}$. But this only changes the constant, not the overall rate. Therefore,

$$\text{error} = O\left(\frac{1}{\sqrt{N_{\text{tot}}}}\right)$$

This means the estimate converges at the usual Monte Carlo rate: to make the error about 10 times smaller, we need about 100 times more needle drops.
