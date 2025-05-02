# Quetzalcoatl
> A pandoc template for everyday typesetting.

The original pandoc template is, by most respects, *passable*, but not
exactly great; it's mediocre at best. So, I went ahead and made a template
for myself. It's nothing fancy---there isn't any beamer functionality or
anything built into it, and I'm yet to define a color palette for it---but
overall it's useable.

See the [documentation](doc/README.md) for more information on this template.

More work is needed, but, for now, it works. See the [`TODO`](TODO.md) for
more information.


## List of parameters
| Parameter | Function | Value |
|:----------|:---------|:------|
| `stixFonts` | uses StixTwo for the serif font | `true` or `false` |
| `notoSans` | uses Noto Sans for the sans-serif font | `true` or `false` |
| `erewhonFonts` | use the Erewhon font | `true` or `false` |
| `kpFonts`[^like] | use the KpSerif font | |`true` or `false` |
| `paperSize` | changes paper size | Standard paper sizes |
| `twoSided` | makes the page double-sided | `true` or `false` |
| `titlepage` | adds a titlepage | `true` or `false` |
| `defaultTitle` | uses default LaTeX title for documents without a titlepage | `true` or `false` |
| `customType` | uses custom typefaces input by the user | see `quetzacoatl.tex` |
| `useEndnotes` | use endnotes instead of footnotes | `true` or `false` |
| `language` | sets the documents language | name of a language (defaults to English) |
| `fullpage` | uses the *whole* page of a document | `true or false` |
| `lineno` | adds line numbers to the text | `true` or `false` |
| `lineStretch` | sets line spacing | Float |
| `draft` | gives the document a draft watermark | `true` or `false` |
| `geometry` | sets up page geometry | see the LaTeX `geometry.sty` documentation |
| `listings` | uses the `listings` package | `true` or `false` |
| `linkAsNotes` | uses footnotes instead of hotlinks for URLs | `true` or `false` |
| `numberSections` | number sections in the document | `true` or `false` |
| `verbatimInNote` | allows verbatim text in footnotes | `true` or `false` |
| `title` | document title | text |
| `author` | document author | text/your name |
| `date` | date | yyyy-mm-dd preferably |
| `headerIncludes` | put stuff in the header | text |
| `sansTitle` | makes the title sans serif | `true` or `false` |
| `parIndent` | sets the paragraph indentation | float |
| `raggedLines` | uses ragged instead of justified paragraphs | `true` or `false` |
| `parSpacing` | sets the length between paragraphs | float |
| `includeAtPreamble` | put whatever you want in the preamble | TeX code |
| `abstract` | your document abstract | text |
| `tableOfContents` | include table of contents in your document | `true` or `false` |
| `ruleColor` | color of the horizontal rule on the titlepage | HTML color code |
| `reportNo` | text on top of the horizontal rule---generally thought to be a report number for cataloging purposes | text |
| `institution` | text on the side of the horizontal rule---generally thought to be the institution | text |
| `sansDefault` | set the body text to a sans font | `true` or `false` |
| `urlMarkColor` | set the color for the url mark | HTML color |
| `urlMarkSymbol` | set the mark for urls | unicode character |
