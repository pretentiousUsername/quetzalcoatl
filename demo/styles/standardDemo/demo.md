The following text is a collection of *fragments* taken from Lieb, Schultz,
Mattis (2004/1961).[^citation] Please, go read the actual paper, it's great.


## Formulation
The first model consists of $N$ spin $1/2$'s ($N$ even) arranged in a row and
having only the nearest neighbor interactions. It is
$$H_{\gamma} = \sum_{i} \left[ \left( 1 + \gamma\right) S_i^x \, S_{i + 1}^x + \left(1 - \gamma\right) S_i^y \, S_{i + 1}^y \right] \,,$$
where $\gamma$ is a parameter characterizing the usual degree of anisotropy in
the $xy$-plane. Because the Hamiltonian only involves the $x$- and $y$-
components of the spin operators, we call this model the $XY$ model.

To solve the $XY$ model, we first introduce the raising and lowering operators
$$a_i^\dagger = S_i^x + \ii \, S_i^y \ \text{and} \ a_i = S_i^x - \ii \, S_i^y$$
in terms of which the Pauli spin operators are
$$S_i^x = \left(a_i^\dagger + a_i\right) / 2; \ S_i^y = \left(a_i^\dagger - a_i\right) / 2 \ii; \ S_i^z = a_i^\dagger \, a_i - \frac{1}{2}$$
and the Hamiltonian is
$$H_\gamma = \frac{1}{2} \sum_i \left[ \left(a_i^\dagger \, a_{i + 1} + \gamma \, a_i^\dagger \, a_{i + 1}^\dagger\right) + \mathrm{h.c.}\right] \,.$$

The ground state $\Psi_0$ is the state with no elementary excitations:
$$\eta_k \, \Psi_0 = 0\,, \ \text{all} \ k \,.$$
The ground-state energy, according to (A-12) is
$$E_0 = -\frac{1}{2} \sum_k \Lambda_k \,.$$
In the limit $N \rightarrow \infty$, the sum can be replaced by an integral
giving
$$\begin{aligned}
    \frac{E_0}{N} &= -\frac{1}{4 \pi} \int_{-\pi}^{+\pi} \left[1 - \left(1 - \gamma^2\right) \sin^2{k}\right]^{1/2} \dl{k} \\
    &= -\frac{1}{\pi} \, \mathcal{E}\left(1 - \gamma^2\right) \,,
\end{aligned}$$
where $\mathcal{E}\left(k^2\right)$ is one of the complete elliptic integrals
(13).


[^citation]: Two Soluble Models of an Antiferromagnetic Chain. In: Nachtergaele, B., Solovej, J.P., Yngvason, J. (eds) Condensed Matter Physics and Exactly Soluble Models. Springer, Berlin, Heidelberg. <https://doi.org/10.1007/978-3-662-06390-3_35>

<!--Lieb, E., Schultz, T., Mattis, D. (2004).-->
