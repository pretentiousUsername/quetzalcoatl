---
title: "Annoucning v1.0!"
subtitle: "among other things"
author: "Ian Mitchell"
date: \today
abstract: This is the demo for the other set of fonts I'm using in
 *Quetzalcoatl*, StixTwo and Noto Sans---they can be mixed and matched to your
 heart's content, but I thought I would show them both off in one document.
 I think they're both nice, useful fonts.
raggedLines: true
stixFonts: true
notoSans: true
---

[gregg]: https://youtu.be/PRFubyO4Bp0


# Introduction
As you can tell, there's something different about this demo---there are new
fonts. Yep, I added in a few new fonts to use, and you can read about them
in the next section.

As you might be able to tell, *Quetzalcoatl* is largely influenced by my
workflow. The main way I produce documents is just by writing a markdown file,
then using a few macros to produce a PDF output using this template, and it's
been that way for about three years now, roughly. When I was younger---from
about eighth through eleventh grade---I used to write LaTeX files *from scratch*
every single time I wanted to write a document. Naturally, this wasn't really
conducive to getting anything done---pandoc, in that regard, basically saved
me from wasting so much needless time writing whole TeX files.

I've been working on *this* particular template since 2022-01-13, but in
reality I've been working on a pandoc template for about two years now---before
then I was just using the [Eisvogel][eisvogel] template---but *Quetzalcoatl*
represents a much better, much more thought out pandoc template. Originally, I
used a copy of the default pandoc + XeTeX template with a few things
swapped---*Quetzalcoatl*, though, was done pretty much from scratch. I'm quite
proud of that.

Today (2023-03-04) I'm *finally* releasing this as version 1.0 of
*Quetzalcoatl*. That might not seem like a big achievement---it's not like it's
a potentially important piece of software---but it is to me. I've never actually
felt comfortable doing an actual *version* of anything I've worked on.


[eisvogel]: https://github.com/Wandmalfarbe/pandoc-latex-template


# New fonts[^font]
Look at me---I decided to switch it up a bit for this. Yeah, I included a new
stylistic set into the template. Now, instead of just XCharter and Inter,
there's StixTwo and Noto Sans---the latter pair quite well with each other.


[^font]: Yes, I'm saying "font" instead of "typeface" now. For a while I had
a weird superiority complex over calling fonts "typefaces", because "fonts are
just variations in a typeface", but time---and Microsoft Office---have changed
the meaning of the word. Rather than attempt to cling on to the old, I will
simply embrace the change. Saying "font" instead of "typeface" also has some
practical benefit---it certainly cuts down on character length.


## Beaten with Stix
I know what you're probably thinking: Why would I put *Stix* into my beautiful,
precious pandoc template?---how could I *ever* put something even remotely
resembling *Times* into the *greatest* piece of typesetting ever made? Well,
here's the thing---I actually really like Stix. Aesthetically, I prefer Charter,
just because it's *different*---and readable on many displays---but it's not
the only typeface I really like.

Stix is a wonderful workhorse typeface, and has many modern features sorely
missing from XCharter, like ligatures, case alternatives, and, what should be
standard in basically every serious, non-decorative typeface, kerning. Stix
also has a very nice *italic* and **bold**, and to boot has a wonderful math
font to go with it. In general, Stix really has the whole package.


## Noto Sans
`{\sffamily`{=latex}
Noto Sans is a pretty nifty sans serif with *loads* of symbols, and some nice
features, such as a proper *italic*. I can type "fuck" in italics and it'll
have a long f. Watch---*fuck*!
`}`{=latex}


# Math typesetting

## Physics stuff

### Header 3.
Here's some math typesetting stuff. For starters I'll just write down the
Linblad equation, a nice bit of physics for open quantum systems,
$$ \begin{aligned}
\pdv{\rho(r, t)}{t} = 
& \sum_j \gamma_j \left( L_j \rho(r, t) L_j^\dagger
- \frac{1}{2} \acomm{L_j L_j^\dagger}{\rho(r, t)} \right) \\
& - i \comm{H}{\rho(r, t)} \,. \end{aligned} $$ {#eq:linblad}
Does $v = \nu$? How do $g$, $u$, $v$ and *v*, $w$, and $z$ look? This is
slightly unrelated to the Linblad equation, since it's classical, but I'm the
God of this document, so I'll also write down the Boltzmann equation,
$$\pdv{f}{t} + \pdv{H}{\mathbf{p}} \cdot \nabla f + \pdv{H}{\mathbf{r}} \cdot 
\pdv{f}{\mathbf{p}} = \left( \pdv{f}{t}
\right)_{\text{coll}} \,. $$ {#eq:boltzmann}


### Another header 3.
What about some *even more* fun stuff with Green's functions?---possibly from
*Quantum Kinetics in Transport and Optics of Semiconductors* by Haug and
Jauho?
$$ G(x, t; x', t') = \theta(t - t') G^>(x, t; x', t') + \theta(t' - t)
G^<(x, t; x', t') \,.$$
$$ A(k, \omega) = \ii \left[ G^>(k, \omega) - G^<(k, \omega) \right]$$
Maybe there's an equation we can use from Freerick's *Transport in Multilayer
Nanostructures*?
$$ G_{ii} (z) = \int \frac{A_{ii}(\omega')}{z - \omega'} d\omega' \,. $$
$$\begin{aligned}
\pdv{G_{i j}(\tau)}{\tau} &=  \theta(\tau) \expval{c_j^\dagger(0) \comm{\hat{\mathcal{H}} - \mu N}{c_i(\tau)} } \\
& -\theta(\tau)\expval{
\comm{\hat{\mathcal{H}} - \mu N}{c_i(\tau)} c_j^\dagger(0) }\,.
\end{aligned}$$ {#eq:hubbardG}


## The *LaTeX Companion* gauntlet
A problematic example:
$$ t[u_1, \dots, u_n] = \sum_{k=1}^{n} \binom{n-1}{k-1} (1 - t)^{n - k}
t^{k - 1} u_k $$

An example showing a trigonometric function:
$$ \sin \frac{\alpha}{2} = \pm \sqrt{ \frac{1 - \cos \alpha}{2} } $$

Let $f$ be analytic in the region $G$ except for the isolated
singularities $a_1,a_2,\dots,a_m$. If $\gamma$ is a closed
rectifiable curve in $G$ which does not pass through any of the
points $a_k$ and if $\gamma\approx 0$ in $G$, then
$$
    \frac{1}{2\pi i} \int_\gamma f\Bigl(x^{\mathbf{N}\in\mathbb{C}^{N\times 10}}\Bigr)
    = \sum_{k=1}^m n(\gamma;a_k)\oint(f;a_k)\,.
$$
First some large operators both in text: $\iiint_{Q}f(x,y,z)
\dd{x} \dd{y} \dd{z}$ and 
$\prod_{\gamma\in\Gamma_{\bar{C}}}\partial(\tilde{X}_\gamma)$; and also on 
display
$$
    \iiiint_{Q}f(w,x,y,z) \dd{w} \dd{x} \dd{y} \dd{z}
    \leq
    \oint_{\partial Q} f'\Biggl(\max\Biggl\{
    \frac{\Vert w\Vert}{\vert w^2+x^2\vert};
    \frac{\Vert z\Vert}{\vert y^2+z^2\vert};
    \frac{\Vert w\oplus z\Vert}{\vert x\oplus y\vert}
    \Biggr\}\Biggr)\,.
$$
