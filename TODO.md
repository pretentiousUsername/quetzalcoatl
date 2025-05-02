+ [ ] Refactor code into multiple different TeX files.
  - The code at present is in one big TeX file, which makes changes very
    precarious—I should refactor the many different aspects of this code into
    different TeX files to make the template more understandable, and also
    easier to work with.
  - [ ] It might be worth considering a full rewrite of this template.
  - [ ] Should I just make a document class?
    * Consider having an option to just use either the `article` or the `memoir`
      class.
+ [ ] Include better font management.
  - Right now, fonts are managed in a really ad-hoc, willy-nilly sort of manner,
    using what amounts to glue and duct tape. I should write `fontspec` files for
    the different fonts and use that.
  - For some fonts, this would necessitate changing the `titlesec` stuff.
  - [ ] Include fine tuning for the different fonts (e.g. using the `Features`
        to give fonts more spacing with caps and small caps).
+ [ ] Make better titles
  - [ ] Make a better title page.
    * Make it more modular, or at least make different title pages.
  - [ ] Make the title *not* a tabular.
  - [ ] Make it easier to include affiliations with the `authblk` package.
+ [ ] Page layout types
  - [ ] Make single *and* double sided layouts
  - [ ] Ripoff Tufte–styled layout
+ [ ] Stylistic sets `(More work is needed, but the fonts have been chosen.)`
  - [X] *regular* – [STIX2][stix2] + [Inter][inter]
  - [X] *knuth* – [New Computer Modern][newcm], plus my own twists
  - [X] *classical* – [Cochineal][cochineal][^crimson] and [Ysabeau][ysabeau]


[^crimson]: Or [Crimson Pro](https://github.com/Fonthausen/CrimsonPro) if that
ever gets a math font—Crimson Pro is *so* good.

[stix2]: https://github.com/stipub/stixfonts

[inter]: https://github.com/rsms/inter

[cochineal]: https://ctan.org/pkg/cochineal

[ysabeau]: https://ctan.org/pkg/ysabeau

[newcm]: https://www.ctan.org/pkg/newcomputermodern
