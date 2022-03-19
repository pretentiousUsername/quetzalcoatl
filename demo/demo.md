---
title: "Typeset testing"
author: "Ian Mitchell"
date: \today
abstract:
 This is my abstract for this document. It is a summary of
 everything in the document---though it does not *really* tell you much
 about what the whole paper is about. Good luck trying to get anything out
 of this, nerd! `\textsf{Sans!}`{=latex}
numberSections: true
sansSections: true
customTitle: true
bibliography: ref.bib
csl: /home/ian/.pandoc/csl/chicago_note.csl
---

# Modern typesetting for the modern type
Much like in writing, the golden rule everyone teaches you is
*readability*---many times it is a typographer's job to break that down, 
and make something eyecatching and unique. This is not one of those times. 
I need the reader to actually read this.

Luckily for me, there are plenty of readable typefaces. The main type for
this document is XCharter---an extended version of Matthew Carter's
original Bitstream Charter. Overall, it is *very* readable, and prints out
well at just about any resolution, making it perfect for just about any
occasion; the typeface also benefits from not being anywhere near as
overused as, say, Times---and, unlike Computer Modern, can be read for an
extended period of time.

In a supporting role are two other nice typefaces, \textsf{Noto Sans} and
\texttt{Julia Mono}.

`{\sffamily`{=latex}
 Noto Sans, developed by the folks over at Google, is a rather nice
sans-serif typeface. I especially love the fact they gave the *I* two
serifs on the top and bottom---it's amazing how few typefaces actually
do that, and how much it hurts their overall readability.

Despite being made for a whole other family of typefaces---Noto in
general was made to achieve a visual hegemony at Google---Noto Sans works
very well with Charter. That said, Noto Sans is no substitute for
Frutiger, which I would have loved to include in this template, but 
intellectual property laws---as they always do---get in the way of good 
design.
`}`{=latex}

`{\ttfamily`{=latex}
Juilia Mono, on the other hand, is a simple---though feature rather
complete---monospaced typeface. It has, unlike many other monospaced
typefaces, *italic*, **bold**, and ***bold-italic*** built in, along with
a *ton* of unicode characters. Though, as you can probably tell, the
dashes leave something left to be desired---I'll make some modifications
to them at some point.

With all of that put together, Julia Mono could be used to typeset entire
documents---though I'm not sure if doing all that with a monospaced 
typeface, for anything other than aesthetics, is the best idea. I don't
know---I'll try it out some time.
`}`{=latex}

## Math typesetting
Now we can have some fun with typesetting equations. Obviously, since this
is a LaTeX template, it's for people that---at least likely---do 
*something* with math. There are a few areas that I can test this out in,
so, without further ado, I'll get to making some stuff.


### Physics
Let's start with the Linblad master equation, a fine
choice for starters,[@manzano_short_2020]
$$ \sum_j \gamma_j \left( L_j \rho(r, t) L_j^\dagger
- \frac{1}{2} \left\{ L_j L_j^\dagger, \rho(r, t) \right\} \right)
- i \left[ H, \rho(r, t) \right]
- \frac{\partial \rho(r, t)}{\partial t} = 0 \,. $$ {#eq:linblad}
As it stands now (\today), I'm not a huge fan of the sum sign, but oh
well---that can change in the future.

There's also the Laughlin wavefunction,[@laughlin_anomalous_1983] which 
got Robert Laughlin a Nobel,
$$ \psi( z_i ) = \prod_{i < j} \left( z_i - z_j \right)^m
\exp \left[ -\sum_{i = 1}^{N} \frac{| z_i |^2}{4 \ell_B^2}
\right] \,. $$ {#eq:laughlin}
It shows up just about everywhere in many-body physics. I can't remember
what paper it was, but if memory serves me right---it often
doesn't---it appears as the wavefunction for a Tomanaga-Luttinger Liquid
as well, which is pretty neat.

The general solution to the Poisson equation is
$$ \phi(r) = \frac{1}{4\pi\epsilon_0} \int \frac{n(r')}
{| r - r' |} \,d^3 r \,. $$
Which, all things considered, is rather useful.


### Synthesizer stuff
The transfer function for a realistic, $N$-pole Moog transistor ladder 
filter was derived by @dangelo_generalized_2014 as
$$ H(s) = - \prod_{u = 0}^{N - 1} \frac{
\left( \frac{I_\text{ctl}}{4 C V_T} \right)^N}{s + \frac{I_\text{ctl}}{
4 C V_T} \left(1 - \sqrt[N]{k} e^{i\pi (2 u + 1) / N} \right) } \,,$$
which is different from @stinchcombe_analysis_2008,
$$ H(s) = \frac{1}{(s + 1)^4 + k} \,. $$
Both of these are technically correct---as they're both derived from a
linearized analysis of the Moog ladder filter---the key difference is
in that D'Angelo and Valimaki's transfer function is about the *poles* of 
the transfer function, rather than the (normalized) cutoff frequency.


## Code!
This has some pretty decent, albeit incomplete, code typesetting. For
example, here's a hello world in Julia.
```julia
println("Hello world")
```

## Some other nifty things
In this template I have some pretty nice looking block quotes.

> He's right. These are some pretty nice looking block quotes.
>
> ---Jeebus

However, for some reason, whenever I put in block quotes, it makes the
rules near the abstract act a bit funny. I have no idea why it does
that---perhaps it is one of TeX's great mysteries.


# Wrapping this up a bit
\lipsum[1]

I would like to thank all the people that have suffered through LaTeX's
bullshit---from the overfull hboxes to the arcane syntax---you have all
made this accursed template possible.

