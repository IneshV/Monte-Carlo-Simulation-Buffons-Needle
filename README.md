# Buffon's Needle README

If you were to randomly drop needles onto a plane with parallel lines spaced a distance of 2 **needls** apart, the ratio of needles that intersect a line to total needles approaches \(\pi\).  
Mysterious? I think not.  
*(Insert image here)*

This is a small project to learn and practice fascinating **(geometric) probability theory**, specifically Monte Carlo simulations.

---

## Here is the Math Explained

Let’s say the needle has length \(\displaystyle \ell\).

- For intersection, we care about the position \(x\) of the needle’s center and the angle \(\displaystyle \theta\).
- The probability density of the center of the match is  
  \[
  P_x \;=\; \frac{1}{\ell}.
  \]
- The probability density of the angle is  
  \[
  P_\theta \;=\; \frac{2}{\pi}.
  \]
- The probability for the match to cross the line is given by the double integral  
  \[
  P \;=\; \iint \bigl(P_x \,P_\theta\bigr)\,dx\,d\theta.
  \]
- The condition for the match to cross the line is  
  \[
  x \;<\; \frac{\ell}{2}\,\sin(\theta).
  \]
- Therefore, the \(x\) integration bounds are from \(0\) to \(\displaystyle \frac{\ell}{2}\,\sin(\theta)\), and the \(\theta\) integration goes from \(0\) to \(\frac{\pi}{2}\).

