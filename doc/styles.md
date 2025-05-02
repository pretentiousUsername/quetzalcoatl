# Styles
In this template, there are a number of pre-defined styles for you to choose
from—these are essentially just font sets, but do include different formats for
section headings and other various things. The 



## Table of styles
| **Name** | **Serif font** | **Sans font** | **Monospaced font** | **mood** | **Demo** |
|:---------|:---------------|:--------------|:--------------------|:---------|:----------------|
| `regular` | STIX 2 | Inter | Julia Mono | standard | [—](../demos/styles/regular.pdf) |
| `knuth` | New Computer Modern Serif | New  Computer Modern Sans  | New Computer Modern Monospace | learneded | [—](../demos/styles/knuth.pdf) |
| `utopia` | Utopia | Merriweather Sans | ??? | alright | [—](../demos/styles/utopia.pdf) |
| `pretentious` | EBGaramond/Garamond-Math | Ysabeau | ??? | something like old books | [—](../demos/styles/pretentious.pdf) |
| `dvdnormal` | mesagess | **dracaula** | ??? | my name is dvd normal | 10m ago |


## Writing your own styles
Owing to my desperation to get a working version of the `stylistic_sets` package
to just *work*, I decided to make it so that you define a font file and a header
file as raw TeX files which then get inserted with the `\input` command.[^input]

1. Think of a name for your own style.
2. Put the fonts into `packages/fonts/<your_style>.tex`. This file should be
   written as just a collection of fonts in fontspec.
3. Write your `titlesec` style in `packages/headers/<your_style>.tex`. You
   *should*, tecnically, limit this to just being a file for `fontsec`
   commands, but you could probably do a little more without doing too much
   damage.




[^input]: Let me note here first that the `\input` command is a TeX primitive,
and therefore is far less safe than opening a package. I do not intend on
continuing with the `\input` primitive outside of this edge case, wherein I was
being attacked by LaTeX's sometimes annoying restrictions (e.g. I couldn't
declare a package in the options section).
