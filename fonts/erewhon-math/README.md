Erewhon-Math package
====================

## Description

`Erewhon-Math.otf’ is an Utopia based OpenType mathematical font.
The mathematical symbols are borrowed or derived from Michel Bovani’s
Fourier-GUTenberg package, Latin letters and digits are borrowed from
Michael Shape’s Erewhon font.

## Contents

* Erewhon-Math.otf      OpenType Math font
* Erewhon-Math-Bold.otf Bold variant (limited coverage)
* fourier-otf.sty       LaTeX style file: replaces fourier.sty for LuaTeX/XeTeX
* Erewhon-Math.pdf      Documentation in PDF format
* Erewhon-Math.ltx      Source of Erewhon-Math.pdf
* unimath-erewhon.pdf   Modified version of unimath-symbols.pdf
                        showing available Erewhon-Math symbols compared to
                        LatinModern, STIXTwo, Erewhon, TeXGyrePagella,
                        Libertinus and EBGaramond.
* unimath-erewhon.ltx   Source of unimath-symbols.pdf
* README.md             (this file)

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.
Otherwise, Erewhon-Math can be installed under TEXMFHOME or TEXMFLOCAL, f.i.
Erewhon-Math.otf in directory  texmf-local/fonts/opentype/public/erewhon-math/
and fourier-otf.sty in directory  texmf-local/tex/latex/erewhon-math/.  
Documentation files and their sources can go to directory
texmf-local/doc/fonts/public/erewhon-math/

Don't forget to rebuild the file database (mktexlsr or so) if you install
under TEXMFLOCAL.

Finally, make the system font database aware of the Erewhon Math font
(fontconfig under Linux).

## License

* The font `Erewhon-Math.otf’ is licensed under the SIL Open Font License,
Version 1.1. This license is available with a FAQ at:
http://scripts.sil.org/OFL
* The other files are distributed under the terms of the LaTeX Project
Public License from CTAN archives in directory macros/latex/base/lppl.txt.
Either version 1.3c or, at your option, any later version.

## Changes

* First public version: 0.40
* v0.41:
    - Added chars U+2AB1 to U+2AB4 (\precneq, \succneq, \preceqq, \succeqq).
    - Fixed kerning between Italic/BoldItalic Latin and Greek letters
      and their subscript.
* v0.42:
    - Added thirty symbols U+00B0 (degree), U+01B5, U+214B, U+2232, U+2233,
    arrows U+2933 to U+2937 and some more.
    - Improved kerning between roots and degrees.
    - Improved kerning between arrows accents and parenthesis.
    - Accents position above italic dans bold italic latin
    and greek letters tuned.
* v0.43
    - Corrected "IsExtended" flags.
    - Improved kernings for differential elements.
    - Changed \hbar, which now behaves as intended by unicode-math package.
    - Glyph \Game (U+2141) corrected (it was upside down).
* v0.44
    - Improved sub- and superscripts: glyphs redesigned bolder,
    size reduced (70%, 55%) instead of (76%, 60%).
    - Fixed right kernings of "italic f".
    - Fixed right bearings and italic corrections of mathscr capitals.
* v0.45
    - Added stretchy accents \wideoverbar, \widebreve, \widecheck.
* v0.46
    - Stretchable \langle, \rangle, \lAngle and \rangle delimiters
    are now available in eight sizes (three bigger sizes added).
    - Sub- and superscripts reshaped: boldness slightly reduced.
* v0.47
    - Added \mdsmwhtsquare (U+25FD), \mdsmblksquare (U+25FE),
    \lgwhtsquare (U+02B1B), \lgblksquare U+02B1C).
    - Tuned all "squares", "circles" and "triangles": the smaller ones
    are centered on the math-axis, larger ones rest on the baseline.
    - Redesigned symbols \angle, \measuredangle, \sphericalangle
    (U+2220 to U+2222).
    - Redesigned lowercase script letters \mscre, \mscrg, \mscro
    (U+212F, U+210A, U+2134).
    - Added symbols \inttop, \intbottom, \sumtop, \sumbottom
    (U+2320, U+2321, U+23B2, U+23B3).
    - Added  symbols \hrectangleblack (U+025AC), \hrectangle (U+025AD),
    \mdlgwhtlozenge (U+25CA) \mdlgblklozenge (U+29EB).
    - Added symbols \enclosedcircle, \enclosedsquare, \encloseddiamond,
    \enclosedtriangle (U+20DD, U+20DE, U+20DF, U+20E4).
    - Added symbols \lozengeminus, \concavediamond, \concavediamondticketleft,
    \concavediamondticketright (U+27E0 to U+27E3).
    - Added symbols \mdblkdiamond, \mdwhtdiamond, \mdblklozenge,
    \mdwhtlozenge, \smblkdiamond, \smblklozenge, \smwhtlozenge
    (U+2B25 to U+2B2B).
     - Added two options (no-text, Scale=) to fourier-otf.sty.
* v0.50
    - Changes in Erewhon-Math:
      * Added upright versions of integrals (StylisticSet=3 feature).
      * All bold Math Script uppercase characters redesigned (their
        look was not consistent with their normal weight counterparts).
      * Added variants for mscrE, mscrQ and mscrT and their bold
        counterparts accessible through cv20, cv21 and cv22 respectively.
      * Added U+0338 for negation of "\mathrel" chars.
    - Changes in FourierOrns:
      * \texpertenthousand now defined in Erewhon (v.1.118).
      * \eurologo now borrowed from Erewhon (v.1.118).
      * Files FourierOrns-Bold.otf, FourierOrns-Italic.otf and
        FourierOrns-BoldItalic.otf (useless now) deleted.
      * Breaking change: ornaments \leafleft and \leafright
        swapped in order to match the orignal type1 version.
* v0.51
    - Feature +onum added (oldstyle numerals in maths).
    Option fulloldstyle added to fourier-otf.sty, this option was
    available with the original fourier-GUTenberg package.
    - Sub- and superscript placement corrected for bold calligraphic capitals.
    - Metrics changed for sans-serif and typewriter glyphs.
* v0.52
    - Over/underbrace: metrics of horizontal variants tuned.
    - Added glyphs \nleqqslant and \ngeqqslant (U+E09A, U+E09B).
    - Fixed "Style=" options in fourier-otf.sty (they didn't work for XeLaTeX).
* v0.53
    - fourier-otf.sty now loads realscripts for better superscripts.
    - Vertical variants of \mathslash, \backslash: slope corrected.
    - Added proportional digits and lnum, pnum features in math mode.
    - Added character variant (cv11) for \partial.
* v0.54
    - Delimiters’ sizes (), [] and {} now match those of the
      Erewhon text fonts.  Bacward compatibility option (+ss09) added.
    - Slight correction to degree position on radicals.
    - Experimental Bold variant added.
    - Glyph Bbbsum.v1 (displaystyle) added.
    - Metrics of some italic capitals (H,M,N,U) corrected.
* v0.55
    - Fixed vertical variants of \Vert and \Vvert.
    - Added stretchable integral for U+222B (usable with luametatex).
* v0.56
    - Package now compatible with mathtools’ stretchable arrows.
    - \diagup and \diagdown moved from private area to U+27CB, U+27CD.
* v0.60
    - Metrics of all "under" arrows and harpoons corrected.
    - Most horizontal arrows and harpoons are now stretchable.
* v0.61
    - fourier-otf.sty: options handled by `l3keys` instead of `xkeyval` 
    (requires a LaTeX kernel not older than 2022-06-01).
    - fourier-otf.sty: option "fulloldstyle" now applies to both text 
	and maths fonts.
	- Fixed widths of under/overbraces variants.
	- Blackboard bold capitals added to Erewhon-Math-Bold.otf.
* v0.62
    - Erewhon-Math-Bold: seven glyphs added (U+2107, U+2126, U+2127, 
      U+212B, U+2132, U+2141).
* v0.63
    - Bug corrections: large parentheses and integrals.
* v0.64
    - Fixed IsExtendedShape flags.
    - \mid (U+2223) and \parallel (U+2225) vertical variants changed.
    - Metrics and italic correction changed for italic uppercase letters
      (Latin and Greek).
    - OT features cvNN are now applied before ssty (applied last).
    - Inconsistencies between Bold Caligraphic glyphs and their Regular
      counter-parts fixed.
    - Superscripts redesigned.
    - Metrics of \widebreve, \widecheck, \widehat, \widetilde first
      horizontal variant (.h0) changed: f.i. $\hat{r} \ne \widehat{r}$.
    - Erewhon-Math-Bold: horizontal variants of the main accents added,
      plus another hundred glyphs.
* v0.65
    - Inconsistencies between vertical delimiter sizes fixed.
* v0.66
    - Fixed Game glyph (U+2141).
    - Erewhon-Math-Bold: missing italic correction added for int.up, 
      int.v1, int.v1.up.
* v0.67
    - \lgroup and \rgroup are extensible.
    - notaccent (U+0338) enlarged.
    - bar (U+0304), wideoverbar (U+0305), mathunderbar (U+0332) thicknesses' 
    unified to default rule thickness.
    - Glyphs U+2032 to U+2037 and U+2057 (prime and co.) resized so that f.i. 
    \(f'\), \(f\prime\) and \(f^{\prime}\) produce the same output.
    - `fourier-otf.sty` has a new option `fakedscripts` to stop `realscripts`
    package loading.
  
---
Copyright 2019-2025  Michel Bovani, Daniel Flipo  
E-mail: michel (dot) bovani (at) icloud (dot) com  
        daniel (dot) flipo (at) free (dot) fr
