---
title: "Typeset testing"
author: "Ian Mitchell"
date: \today
abstract:
 This is my abstract for this document. It is a summary of
 everything in the document---though it does not *really* tell you much
 about what the whole paper is about. Good luck trying to get anything out
 of this, nerd!
numberSections: true
bibliography: ref.bib
csl: /home/ian/.pandoc/csl/natureBox.csl
reportNo: WTF-420-\LaTeX
institution: Ducky Fooniversity
titlepage: true
tableOfContents: true
raggedLines: false
logo: ./img/theDude.pdf
logoWidth: 10em
---

# A manifesto (of sorts)
Typesetting is art, both in the sense that is beautiful, and that it is 
useful. Beauty is of course in the eye of the beholder---it is derived
from many things; while *The Fountain* is a urinal, and not a Baroque
painting, its use in demonstrating the hypocrisy in the wider avant-garde
art world was beautiful in and of itself. In essence, the beauty derived
from the function of the object---that is much of art in and of itself.
What is aesthetically beautiful---what we find easy on the eyes---is
culturally defined.

For most people, that works perfectly, but typesetters are not so lucky. 
Typography's beauty doesn't derive from process, message, or raw 
aesthetics---it is instead from how easy a document can be read, and 
whether or not the style matches the medium and purpose. If I were to 
print a document, with *massive* comic sans, on printer paper that says 
"***DO YOU'RE BEST :))))***," and handed it out to everyone in my 
neighborhood, people would find it ridiculous; if I were to print that in 
Garamond, and place it in a book a thousand times *a-la The Shining*, 
people would think I'm a serial killer. If I put it on a poster, in bright 
Frutiger or Helveitca, give it some contrasting colors, and hang it up in 
some bar in a gentrified part of New York or Philadelphia---and maybe throw
in a picture of an possum---people would call it graphic design---if I'm 
lucky, they'd call it art.

![Behold: the dude.](img/theDude.pdf)

To make good typesetting, you need to know your purpose. This template is
designed to do two things: make your information look decent, and make it 
readable. If you're not writing "***DO YOU'rE BESt***" a thousand times, 
you're on route to making something good. Not only is this designed to
make whatever you're writing look good, it's also trying to make it as
timeless as possible. I avoided design trends---I avoided those puffy
serif fonts, such as [New Spirit][ns]. This is a pandoc template for
typesetting documents that matter, not advertising that will wind up
in the dustbin of history, relegated to simply being a marker of the times.

This template was created for a simple reason: I'm sick and tired of
Computer Modern and Times (New Roman). I see a lot of good scientists
typesetting their documents in Computer Modern---and if they're using Word,
Times New Roman---and I have to just ask *why*? The backbone of modern
science---the [arXiv](https://arxiv.org)---puts all of its documents in
plain `{\LaTeX}`{=latex}. (Either that, or they're horribly typeset in MS
Word.) That's fine, but I think it can be done better. If you're going to be 
making non-choices, then you might as well make them look nice and print well.

[ns]: https://fonts.adobe.com/fonts/new-spirit


# Modern typesetting for the modern type
Much like in writing, the golden rule everyone teaches you is
*readability*---many times it is a typographer's job to break that down, 
and make something eyecatching and unique. This is not one of those times. 
I need the reader to actually read this.

I tried to gaslight myself into using StixTwo as the main font, but I realized
that it just wasn't working for me---despite its more modern features, like
basic ligatures, I just prefer XCharter. Charter in general is just a wonderful
typeface, and I loathe to fully replace it. So, StixTwo is still an
alternative---I know I'll be using it for [my hugo theme][delay] if I ever
manage to implement an automatic PDF generation script in there---but Charter is
still my main.

In a supporting role are two other nice typefaces, \textsf{Inter} and
\texttt{Julia Mono}.

Let's go over some facts:

#. I am the coolest person to *ever* live---my body temperature is just barely
   \qty{1}{\kelvin}.
#. I am very cold. Please get me a blanket.
    #. If I don't get a blanket I will continue to be cold.
    #. If you're already grabbing me a blanket, would you get me some hot
       cocoa too?
       #. Yes, with marshmallows.

+ I like a few subjects:
    + Math
    + Science
    + Other assorted nerd stuff
        + See *The Physics of Your Mom and Ancient Aliens*, by Michio Kaku.
+ I sometimes type things on a computer.
+ Sometimes the things I type aren't very good, and other times they're great.


[delay]: https://github.com/pretentiousUsername/delay

## Math typesetting
Now we can have some fun with typesetting equations. Obviously, since this
is a `{\LaTeX}`{=latex} template, it's for people that---at least likely---do 
*something* with math. There are a few areas that I can test this out in,
so, without further ado, I'll get to making some stuff.


### Physics.
Let's start with the Linblad master equation, a fine
choice for starters,[@manzano_short_2020]
$$ \begin{aligned}
\diffp{\rho(r, t)}{t} = 
& \sum_j \gamma_j \left( \op{L}{j} \rho(r, t) \hc{L}{j}
- \frac{1}{2} \left\{ \op{L}{j} \hc{L}{j}, \rho(r, t) \right\} \right) \\
& - i \left[ H, \rho(r, t) \right] \,. \end{aligned} $$ {#eq:linblad}

There's also the Laughlin wavefunction,[@laughlin_anomalous_1983] which 
got Robert Laughlin a Nobel,
$$ \psi( z_i ) = \prod_{i < j} \left( z_i - z_j \right)^m
\exp \left[ -\sum_{i = 1}^{N} \frac{| z_i |^2}{4 \ell_B^2}
\right] \,. $$ {#eq:laughlin}
It shows up just about everywhere in many-body physics. I can't remember
what paper it was, but if memory serves me right---it often
doesn't---it appears as the wavefunction for a Tomanaga-Luttinger Liquid
as well, which is pretty neat.

The time evolution for some operator is
$$ \diff{\op{a}}{t} = \comm{\op{H}}{\op{a}} $$

The general solution to the Poisson equation is
$$ \phi(r) = \frac{1}{4\pi\epsilon_0} \int \frac{n(r')}
{| r - r' |} \dl[3] r \,. $$
Which, all things considered, is rather useful.




### Synthesizer stuff.
The transfer function for a realistic, $N$-pole Moog transistor ladder 
filter was derived by D'Angelo and Valimaki[@dangelo_generalized_2014] as
$$ H(s) = - \prod_{u = 0}^{N - 1} \frac{
\left( \frac{I_\text{ctl}}{4 C V_T} \right)^N}{s + \frac{I_\text{ctl}}{
4 C V_T} \left(1 - \sqrt[N]{k} e^{i\pi (2 u + 1) / N} \right) } \,,$$
which is different from, Stinchcombe's result[@stinchcombe_analysis_2008]
$$ H(s) = \frac{1}{(s + 1)^4 + k} \,. $$
Both of these are technically correct---as they're both derived from a
linearized analysis of the Moog ladder filter---the key difference is
in that D'Angelo and Valimaki's transfer function is about the *poles* of 
the transfer function, rather than the (normalized) cutoff frequency.


### Some thoughts.
I really like that there's an otf math typeface for XCharter, but I can
say for certain that I'm *not* a fan of the sum or product signs---they
feel just a *bit* too thin and piddly. I think it would be better if they
were stretched out form of the sigma ($\Sigma$) and pi ($\Pi$) characters,
they would look much better. Conversely, the integral, partial derivative 
symbol, and the rest all look great.



#### Some other thoughts.
I really like having the ability to just press a few buttons and immediately
get the document typeset. Pandoc really is an excellent package. I also really
appreciate the work put in for all the typefaces I'm using now, and the amount
of work people have done to make `{\TeX}`{=latex} not only useable, but *good*.

Of course, Knuth and Lamport should get a lot of the credit for that, but there 
are so many other people. Javier Bezos, I think, is one of many unsung 
`{\TeX}`{=latex} heroes---just for writing the `titlesec` package alone he 
deserves more clout. Though, how much clout can you *really* get for doing
something good with a nerd's typesetting language?


#### Anor Londo adventure
I keep writing things---dumb things---into this markdown file, and eventually
my fingers will grow tired---but still, for now, I persevere. My fingers
will grow tired, my mind weary, but never will the indomitable flame of
good typography be snuffed out within me---as long as I live, I will
rekindle the flame.

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
that---perhaps it is one of `{\TeX}`{=latex}'s great mysteries.^[Look at me, 
Ma! I'm in an footnote!]


# Wrapping this up a bit
\lipsum[1]

I would like to thank all the people that have suffered through 
`{\TeX}`{=latex}'s bullshit---from the overfull hboxes to the arcane
syntax---you have all made this accursed template possible.



# References
