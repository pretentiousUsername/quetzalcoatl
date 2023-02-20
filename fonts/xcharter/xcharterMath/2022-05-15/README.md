XCharter-Math package
====================

## Description

`XCharter-Math.otf’ is an OpenType mathematical font to be used
with the XCharter text fonts.

## Contents

* XCharter-Math.otf     OpenType Math font
* xcharter-otf.sty      LaTeX style file
* XCharter-Math.pdf     Documentation in PDF format
* XCharter-Math.ltx     Source of XCharter-Math.pdf
* unimath-xcharter.pdf  Modified version of unimath-symbols.pdf
                        showing available XCharter-Math symbols compared to
		                LatinModern, STIXTwo, Erewhon, TeXGyrePagella,
						Libertinus and EBGaramond.
* unimath-xcharter.ltx  Source of unimath-xcharter.pdf
* README.md            (this file)

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.
Otherwise, XCharter-Math can be installed under TEXMFHOME or TEXMFLOCAL, f.i.
XCharter-Math.otf in directory  texmf-local/fonts/opentype/public/xcharter-math/
and fourier-otf.sty in directory  texmf-local/tex/latex/xcharter-math/.  
Documentation files and their sources can go to directory
texmf-local/doc/fonts/public/xcharter-math/

Don't forget to rebuild the file database (mktexlsr or so) if you install
under TEXMFLOCAL.

Finally, make the system font database aware of the XCharter Math font
(fontconfig under Linux).

## License

* The font `XCharter-Math.otf’ is licensed under the SIL Open Font License,
Version 1.1. This license is available with a FAQ at:
http://scripts.sil.org/OFL
* The other files are distributed under the terms of the LaTeX Project
Public License from CTAN archives in directory macros/latex/base/lppl.txt.
Either version 1.3 or, at your option, any later version.

## Changes

* First public version: 0.30
* v0.31:
     - Fixed "Style=" options in xcharter-otf.sty (they didn't work for XeLaTeX).
	 - Added glyphs \nleqqslant and \ngeqqslant (U+E09A, U+E09B).
	 - Corrected glyphs \varsubsetneqq \varsusetneqq (U+E09C, U+E09D).
* v0.32:
	 - all vertical delimiters resized.
     - \mathslash, \backslash and their vertical variants: slope corrected.
     - xcharter-otf.sty now loads realscripts for better superscripts.
	 
---
Copyright 2022-  Daniel Flipo  
E-mail: daniel (dot) flipo (at) free (dot) fr
