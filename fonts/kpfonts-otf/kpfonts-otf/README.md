>The kpfonts-otf package
========================

## Description

`kpfonts-otf` is meant as a replacement, for LuaLaTeX and XeLaTeX users,
of Christophe Caignaert’s `kpfonts` package. Christophe’s Type1 fonts have
been converted to OpenType using fontforge and Adobe's AFDKO bundle.
The package is still experimental, bug reports and suggestions are welcome.

## Contents

* the `font/` directory holds 21 OpenType fonts (16 for text and 5 for maths);
* the `tex/`  directory holds the style file kpfonts-otf.sty and
  fontspec configuration files;
* the `doc/`  directory holds documentation in English and French and
  a table of available maths symbols comparing kpfonts-otf to LatinModern,
  STIXTwo, Erewhon, TeXGyreTermes, Garamond and Libertinus.

## Installation

This package is meant to be installed automatically by TeXLive, MikTeX, etc.
Otherwise, `kpfonts-otf` can be installed under TEXMFHOME or TEXMFLOCAL, f.i.

+ alls fonts (`fonts/*.otf` files) in directory
  `texmf-local/fonts/opentype/public/kpfonts-otf/`
+ style and fontspec files (`tex/kpfonts-otf.sty` and `tex/*.fontspec`) in
  directory `texmf-local/tex/latex/kpfonts-otf/`
+ documentation (from doc/ directory) in
  `texmf-local/doc/fonts/public/kpfonts-otf/`

Don't forget to rebuild the file database (mktexlsr or so) if you install
under TEXMFLOCAL.

Finally, you may want to make the system font database aware of the
`kpfonts-otf` fonts (fontconfig under Linux).

## License

* The fonts included in `kpfonts-otf` are licensed under the
SIL Open Font License, Version 1.1.
This license is available with a FAQ at: http://scripts.sil.org/OFL
* The other files are distributed under the terms of the LaTeX Project
Public License from CTAN archives in directory macros/latex/base/lppl.txt.
Either version 1.3 or, at your option, any later version.

## Changes
* First release version: 0.30 (experimental, expect changes!).

* v. 0.31:
  Fixed inconsistent widths/sidebearings for six glyphs:
  =  ≠  <  ≤  >  ≥ (all five maths fonts affected, original Type1 too).

* v. 0.32:
  1. Text fonts:
     - `kpfonts-otf.sty` corrected: the "light" option didn't work properly.
     - kpfonts-otf should now cover all glyphs in TS1 encoding (`textcomp.sty`).
     - The height of all diacritics has been reviewed and corrected.
     - New combining diacritics added : U+0310, U+0323, U+0325, U+0327, U+0328.
     - New glyphs added: U+0110 (Dcroat), U+0111 (dcroat), U+0123 (gcircumflex),
       U+0126 (Hbar),  U+0127 (hbar), U+0129 (itilde), U+012B (imacron),
       U+012D (ibreve), U+0135 (jcircumflex), U+0166 (Tbar),  U+0167 (tbar)
       and their counterparts in Petite Caps and Small Caps.
     - Corrected Petite Caps and Small Caps variant for U+00F0 (eth),
       U+00FE (thorn), U+0111 (dcroat)  and U+014B (eng).
     - Optional ft and tt ligatures added, see feature "Ligatures=Required".
     - Variants for ligatures fi ffi fl ffl added, see "Alternate=1".
     - (faked) slanted fonts added to match kpfonts T1 version.
  2. Maths fonts:
     - Corrected mismatch between mitl (U+1d459) and ell (U+2113).
     - Slanted versions for \shortparallel and \nshortparallel
       and for \gtreqless, \lesseqgtr, \gtreqqless, \lesseqqgtr added.
     - Stretchy accents \wideoverbar, \widebreve, \widecheck added.
     - Reduced boldness for superscripts and supersuperscripts.
     - New option "tight" to reduce horizontal spaces in maths mode
       (same settings as \pkg{fourier} and \pkg{fourier-otf}).

* v. 0.33:
    - Roman Text fonts:
      Added 54 glyphs in Latin-ExtendedA range (mostly complete now).
    - Maths fonts:
      Fixed inconsistencies in superscripts and supersuperscripts metrics.

* v. 0.34:
  Massive glyph cleaning: many spurious control points deleted in glyphs
  for both Maths and Text fonts.

  1. Text fonts:
     - kernings before and after quoteright improved.
     - German capital Eszet (U+1E9E) added, in Petite and Small caps too,
       feature "StylisticSet=2" added to get SS instead of capital Eszet.
     - diacritics corrected in `KpRoman-LightItalic` (some were upright).
     - breaking change: feature "Alternate=1" changed to "StylisticSet=1"
       as it didn't work with XeTeX.
  2. Maths fonts:
     -  metrics (width, italic correction) reviewed.
     -  accents ovhook (U+0309), candra (U+0310), vertoverlay (U+202D) added.

* v. 0.35:
  1. Text fonts:
     - Added 54 glyphs in Latin-ExtendedA range for `KpSans` fonts.
     - Euro symbol added in Roman, Sans and Mono, option StyleSet=3 to
	   trigger it.
     - Added missing anchors for "dot below" on P, p, p.pc, p.sc, a.sc.
     - HarfBuzz renderer no longer loaded for HBLuaTeX engine, new option
       "harfbuzz" to force loading it (`kpfonts-otf.sty`).
  2. Maths fonts:
     - Stretchable delimiters corrected in KpMath-Sans.
     - Options `frenchstyle`, `partialup` and `fancyReIm` now work as intended.

* v. 0.36:
    Maths fonts:
    - `kpfonts-otf.sty`: Option mathcal deleted, \mathcal{} and \mathscr{}
      now print different glyphs.
    - mathcal substitutions corrected for `KpMath-Regular` and `KpMath-Sans`.
    - Stretchable \langle, \rangle, \lAngle and \rangle delimiters are now
      available in eight sizes (three bigger sizes added).
    - All vertical arrows are now stretchable.
    - Bug fix: stretchable right paren was broken in `KpMath-Sans`, thanks
      to Tom Stotko for pointed it out!

* v. 0.37:
  1. Text fonts:
     - Added glyphs U+2010 and U+2011 (hyphens).
     - Corrected `kpfonts-otf.sty`: option "largesmallcaps" fixed, new weights
       added (\sbseries, \ltseries, \ebseries), see documentation.
     - Breaking change: files `*.fontspec` changed so that the default smallcaps
       are now "Petite" instead of "Small" to match the orignal kpfonts default.
  2. Maths fonts:
     - Completed the collection of "squares", "triangles", "diamonds" and
       "lozenges".
     - Tuned all "squares", "circles" and "triangles": the smaller ones are
       centered on the math-axis, larger ones rest on the baseline.
     - \perp, \bot, \rightangle, \angle, \measuredangle, \sphericalangle
       shifted up, their bottom rests on the baseline now.

* v. 0.38:
  1. Text fonts:
     - Glyphs U+200B (zero width space) and U+2060 (word joiner) added.
     - Improved option "veryoldstyle" (luatex only): a final "s" is no longer
	   turned into the long variant.
     - Fixed kerning after "f" in KpSans-BoldItalic.
  2. Maths fonts:
     - Added bold versions to \dotlessi, \dotlessj, named \mbfdotlessi,
	   \mbfdotlessj (\mbfimath and \mbfjmath were already available).

* v. 0.39:
  New option "longs". Documentation corrected, thanks to Frank Mittelbach for
  pointing out the glitch in v0.38.

* v. 0.40:
  - OS2 FSType corrected (0 now): the fonts are now declared "installable".
  - kpfonts-otf.sty corrected (missing \fi), thanks to Denis Bitouzé
    for pointing it out.

* v. 0.41:
  1. Text fonts:
     - eurosym reshaped, width slightly reduced.
  2. Math fonts:
     - \vert and \Vert corrected: left and right bearings enlarged.
     - \Vvert (U+2980) added.
     - \coloneqq, \Coloneqq, \colonsim etc. corrected to be compatible
	   with mathtools’ definitions.

* v. 0.42:
     Maths fonts:
	 - Added missing U+0338 for negation of \mathrel chars.
	 - Added \smallin (U+220A), \smallni (U+220D).
     - Added \awint (U+2A11).

* v. 0.43:
     Text fonts: kpfonts-otf.sty now loads realscripts for better superscripts.
	 Maths fonts: Vertical variants of slash and backslash are now accessible.

* v. 0.44:
     Maths fonts: fixed bug for \vert variants in script and scriptscriptstyle.

* v. 0.45:
     Maths fonts: delimiters, integrals, sum, prod etc. are now vertically
     centred by design on the maths axis (required by luametatex).
	 Fixed inconsistencies about bold and semibold integrals.

* v. 0.46:
  1. Text fonts: option longs deleted, option veryoldstyle improved, the
	 substitution from `s' to `ſ' is now handled by "StylisticSet=12".
  2. Maths fonts:
     - Added a smaller variant for \widehat, \widetilde, \widecheck.
	 - Vertical variants added for \vert, \Vert, \Vvert.
     - Added stretchable integral for U+222B (usable with luametatex).

* v. 0.47:
	 Text fonts: moved the s= ligature from liga to hlig as it only makes
	 sense with the "veryoldstyle" option.

* v. 0.48:
  1. Text fonts: oldstyle digits added to lookups "sups" and "subs" for
     \textsuperscript{} and \textsubscript{} (`realscripts` package).
  2. Maths fonts: package now compatible with mathtools’ stretchable arrows.
     New Bold Sans variant: KpMath-SansBold.otf.
     \diagup and \diagdown moved from private area to U+27CB, U+27CD.
  
* v. 0.51:
   - Math fonts: \overleftrightarrow is now stretchable. 
     Metrics of all "over" arrows and harpoons corrected. 
     Metrics of all "under" arrows and harpoons corrected. 
     Most horizontal arrows and harpoons are now stretchable. 
  
---
Copyright 2020-2023  Daniel Flipo  
E-mail: daniel (dot) flipo (at) free (dot) fr
