# Font declaration
This is where you define font style sets. Essentially, all you need to do is
write some `fontspec` declarations in a `tex` file and then write your style set
using another `tex` file in this directory.

## FAQ
> Why do fonts like this?

I like the idea of the UNIX philosophy, in particular modular parts---I would
rather work on something with a lot of smaller, easily identifiable files than
a bunch of large files. Using TeX inputs means that I can do that quickly and
easily.

> Why is Garamond the header font in its font declaration?

Because I made it that way for the `pretentious` style---that might make
it a bit more difficult for you to work with. I don't plan on using Garamond
for anything other than a novelty---sorry, I just find it very spindly and
annoying to read---so it's the main header font there. I might make an alternate
font configuration in the future; you could make your own file until then
(I'm sorry).
