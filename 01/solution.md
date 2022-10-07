# Exercise 1

We will assume that the table has unit length, and the first throw lands at point $y=\lambda$, such that
$$
P(A \ scores \ | \ \lambda) = 1 - \lambda \\ \\
P(B \ scores \ | \ \lambda) = \lambda
$$
Ideally, $\lambda \sim U(0,1)$, (uniform distribution over the [0,1] interval). However, we already have the 5-3 score in favour of Alice (which we will label as the event $S$). Hence, we must consider the posterior distribution
$$
p(\lambda \ | S) = \frac{p(S | \lambda) \cdot p(\lambda)}{\int_0^1 p(S | \lambda) \cdot p(\lambda) \ d\lambda}
$$
with 
$$
p(\lambda) = 1
$$
$$
p(S | \lambda) = {8 \choose 3} \cdot (1 - \lambda)^5 \cdot \lambda^3 = 56 \cdot (1 - \lambda)^5 \cdot \lambda^3 
$$
$$
\int_0^1 p(S | \lambda) p(\lambda) d\lambda = \frac{1}{9}
$$
$$
\implies p(\lambda \ | S) = 504 \cdot (1 - \lambda)^5 \cdot \lambda^3 
$$
 
In this case, our posterior distribution $\lambda \ | S \sim Beta(4, 6)$, i.e. a beta distribution with parameters 4 and 6. 

Bob needs to win four times in a row to win the game:
$$
p(B \ wins) = \int_{0}^{1} \lambda^4 \cdot p(\lambda | S) \ d\lambda = \frac{7}{143} \approx 0.049
$$

In conclusion, the probability that Bob wins is $\approx 0.049$. 