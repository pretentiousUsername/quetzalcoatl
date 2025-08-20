---
title: Testing the titles
subtitle: subtitles galore
authorAffiliations:
 - \author[1]{Ian Mitchell\thanks{\texttt{my email address!}}}
 - \author[1,2]{Other Author}
 - \author[3]{Yet Another}
 - \affil[1]{My University}
 - \affil[2]{Another University}
 - \affil[3]{US Army DEVCOM Blowing Stuff Up and ACRONYM Research Center, Springfield Division}
titlepage: true
---

Unfortunately, I can't change the font on the `authblk` superscripts because
of how `{\TeX}`{=latex} works---it uses a hack by doing the superscript in
math mode, which means that it's non-trivial to turn it into a sans serif font.
