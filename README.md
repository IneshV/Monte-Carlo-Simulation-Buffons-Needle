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
P
=
\int_{0}^{\pi/2}
\int_{0}^{\frac{\ell}{2}\sin(\theta)}
\left(\frac{1}{\ell}\cdot \frac{2}{\pi}\right)
\,dy\,d\theta
$$

Since the integrand is constant with respect to \(y\), we can evaluate the inner integral first:

$$
P
=
\int_{0}^{\pi/2}
\left(\frac{1}{\ell}\cdot \frac{2}{\pi}\right)
\left[
y
\right]_{0}^{\frac{\ell}{2}\sin(\theta)}
\,d\theta
$$

Substitute the bounds:

$$
P
=
\int_{0}^{\pi/2}
\left(\frac{1}{\ell}\cdot \frac{2}{\pi}\right)
\left(\frac{\ell}{2}\sin(\theta)\right)
\,d\theta
$$

Now simplify the constants:

$$
\left(\frac{1}{\ell}\cdot \frac{2}{\pi}\right)
\left(\frac{\ell}{2}\right)
=
\frac{1}{\pi}
$$

So the probability becomes:

$$
P
=
\frac{1}{\pi}
\int_{0}^{\pi/2}
\sin(\theta)
\,d\theta
$$

Now evaluate the remaining integral:

$$
\int_{0}^{\pi/2}
\sin(\theta)
\,d\theta
=
\left[-\cos(\theta)\right]_{0}^{\pi/2}
=
-\cos\left(\frac{\pi}{2}\right) + \cos(0)
=
0 + 1
=
1
$$

Therefore,

$$
P
=
\frac{1}{\pi}
$$

Going back to the problem, if you drop $N_{\text{tot}}$ total needles, we expect approximately
$N_{\text{cross}} \=\ N_{\text{tot}} \times \frac{1}{\pi}$
needles to cross a line. Rearranging this, we get
$\frac{N_{\text{tot}}}{N_{\text{cross}}} \\approx\ \pi$
As $N_{\text{tot}}$ becomes very large, this ratio converges to $\pi$ (by the Law of Large Numbers), making it a neat way to estimate $\pi$ empirically.
