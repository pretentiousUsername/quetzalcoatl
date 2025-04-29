---
title: Custom macros
author: Ian Mitchell
date: \today
noIndentFirst: true
customType: \usepackage[knuth]{\packageDir/stylistic_sets}
---


# Bras and kets
Originally, I was using the `braket` package for this, but it was honestly
easy to just write some macros for this.

`\bra{\psi}` $\rightarrow \bra{\psi}$; `\ket{\phi}` $\rightarrow \ket{\phi}$

# Expectation value
`$\expval{a}$` $\rightarrow \expval{a}$

`$$\expval{\diff{f}{t}}$$` $$\rightarrow \expval{\diff{f}{t}}$$


# Commutation

## Commutator
`$\comm{\op{x}}{\op{p}} = i\hbar$` $\rightarrow \comm{\op{x}}{\op{p}} = i\hbar$

## Anticommutator
`$$\acomm{\op{c}{i}}{\hc{c}{j}} = \delta_{\alpha, \beta}$$`
$$\rightarrow \acomm{\op{c}{i}}{\hc{c}{j}} = \delta_{\alpha, \beta} $$


# Compact derivatives
`$$\dlp{f}{t}$$`
$$\rightarrow \dlp{f}{t}$$
