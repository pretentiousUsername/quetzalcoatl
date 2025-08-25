---
title: Abscence of diffusion in certain random lattices
subtitle: testing out titles and stuff
authorAffiliations:
 - \author{P.W. Anderson}
 - \affil{Bell Telephone Laboratories}
date: 1957-10-10
abstract:
 This paper presents a simple model for such processes as spin diffusion or
 conduction in the "impurity band." These processes involve transport in a
 lattice which is in some sense random, and in them diffusion is expected to
 take place via quantum jumps between localized sites. In this simple model the
 essential randomness is introduced by requiring the energy to vary randomly
 from site to site. It is shown that at low enough densities no diffusion at
 all can take place, and the criteria for transport to occur are given.
style: regular
titlepage: true
titlepageAbstract: true
tableOfContents: false
bibliography: ref.bib
csl: /home/pines/.pandoc/csl/chicago-author-date.csl
eqnPrefix: equation
includeAtPreamble:
 - \definecolor{titlepageTextColor}{HTML}{4f6cad}
institution: Bell Telephone Laboratories
reportNo: 1234-FOO-AAAA
---

<!--
reportNo: 1234-FOO-AAAA
logo: ./img/bell_edit.pdf
logoWidth: 0.25in
-->

<!--
csl: /home/pines/.pandoc/csl/chicago-author-date.csl
-->
<!--
numberSections: false
-->

<!--
subtitle: testing out titles and stuff
-->

<!--
abstract:
 This paper presents a simple model for such processes as spin diffusion or
 conduction in the "impurity band." These processes involve transport in a
 lattice which is in some sense random, and in them diffusion is expected to
 take place via quantum jumps between localized sites. In this simple model the
 essential randomness is introduced by requiring the energy to vary randomly
 from site to site. It is shown that at low enough densities no diffusion at
 all can take place, and the criteria for transport to occur are given.
-->

<!--
authorAffiliations:
 - \author{P.W. Anderson}
 - \affil{Bell Telephone Laboratories, Murray Hill, New Jersey}

<!--
authorAffiliations:
 - \author[1]{Ian Mitchell}
 - \author[2]{Other Author}
 - \affil[1]{Workplace Laboratories Inc.™}
 - \affil[2]{Another Fun Place}
-->

# Introduction
A number of physical phenomena seem to involve
quantum-mechanical motion, without any particular thermal activation, among
sites at which the
mobile entities (spins or electrons, for example) may be
localized. The clearest case is that of spin diffusion" [@bloembergen_1949; @portis_1956];
another might be the so-called impurity band conduction
at low concentrations of impurities. In such
situations we suspect that transport occurs not by
motion of free carriers (or spin waves), scattered as
they move through a medium, but in some sense by
quantum-mechanical jumps of the mobile entities from
site to site. A second common feature of these phenomena is
randomness: random spacings of impurities,
random interactions with the "atmosphere" of other
impurities, random arrangements of electronic or
nuclear spins, etc.

Our eventual purpose in this work will be to lay the
foundation for a quantum-mechanical theory of transport
problems of this type. Therefore, we must start
with simple theoretical models rather than with the
complicated experimental situations on spin diffusion
or impurity conduction. In this paper, in fact, we
attempt only to construct, for such a system, the
simplest model we can think of which still has some
expectation of representing a real physical situation
reasonably well, and to prove a theorem about the
model. The theorem is that at sufficiently low densities,
transport does not take place; the exact wave functions
are localized in a small region of space. We also obtain
a fairly good estimate of the critical density at which the
theorem fails. An additional criterion is that the forces
be of sufficiently short range---actually, falling off as
$r \rightarrow \infty$ faster than $1/r^3$---and we derive a rough estimate
of the rate of transport in the $V \propto 1/r^3$ case.

...


# Summary of the reasoning
Since the mathematical development is fairly complicated and involves lengthy
consideration of each of a number of points, we should like to summarize the
reasoning rather fully in this section, leaving the proofs and details to later
sections. First, then, let us set up the simple model which we study. The
equation for the time-dependence of the probability amplitude $a$, that a
particle is on the site $j$ is:
$$i \, \dot{a}_j = E_j \, a_j + \sum_{k \neq j} V_{j k} \, a_k \,.$$ {#eq:1}
Here we measure energies in frequency units, so we can
set $\hbar = 1$. Equation [-@eq:1] simply restates the assumptions
about the model made in the Introduction.
We study the Laplace transform of the equation
([-@eq:1]): let
$$ f_j(s) = \int_{0}^{\infty} e^{-s \, t} a_j(t) \dl{t} \,, $$ {#eq:2}
and then
$$ i \left[ s \, f_j(s) - a_j(0) \right] = E_j \, f_j + \sum_{k \neq j} V_{j k} \, f_k \,.$$ {#eq:3}
The variables $s$ must be as an arbitrary complex frequency with positive or
zero real part.

`Now this is being written on a typewriter.`

# References {-}
