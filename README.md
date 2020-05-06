# LatUni: Format latin text with unicode

The Unicode specification allows a lot of glyphs that would normally require special fonts to now be available in "plain text" files. Chess pieces, mathematical symbols, etc.

Unicode even contains variants for the basic Latin alphabet in 𝐛𝐨𝐥𝐝, 𝑖𝑡𝑎𝑙𝑖𝑐, 𝒃𝒐𝒍𝒅 𝒊𝒕𝒂𝒍𝒊𝒄, 𝚖𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎, and 𝕞𝕠𝕣𝕖. LatUni flagrantly abuses this fact to allow you to add text formatting to "plain text" files.

Disclaimer: This is a novelty, and probably breaks some accessibility rules or something. There is also probably some software which won't be able to handle text formatted in this way. (A lot of unicode-aware software still has trouble handling actually meaningful use cases like R-to-L text.)

## Installation

As much as anything else, this was to help me learn python package/module distribution. If I've done it right, you should be able to do the standard `python3 setup.py install` (or `python3 setup.py develop` if you want to hack around with me on this mess).

## Example Script

Once you install LatUni, you'll have a script in your path called `latuni`. You can use it to apply formatting to standard input, a text file, or a string on the command line. Run `latuni --help` for usage.

## API

(I should probably use this project to learn about making a self-documenting API too.)

`format(format_flags, string)` returns a version of `string` formatted according to the given flags. Available flags are `FACE_PLAIN`, `FACE_BOLD`, `FACE_ITAL`, `STYLE_SANS`, `STYLE_SERIF`, `STYLE_MONO`, `STYLE_SCRIPT`, `STYLE_DOUBLE`, and `STYLE_FRAKTUR`. Many (but not all) of these can be combined. If you specify an unsupported combination, you may just get plain text.

`fullwidth(string)` returns a version of `string` with all ASCII characters replaced with fullwidth versions. This could be handy for replicating formatting-sensitive text when you can't otherwise count on a monospace font.

In both cases, I recommend that you normalize the text in NFD form before passing it in. You can do this with the built-in `unicodedata` module:

    import unicodedata
    text = unicodedata.normalize('NFD', text);

Doing this makes it a bit more likely that accents and whatnot will survive the transformation.

## Future Plans

* Adding more formatting using combining characters (particularly overstrike and underline)
* The API could probably be improved

## Other Modules

I haven't published it yet, but I'm working on a plugin for the python [Markdown](https://pypi.org/project/Markdown/) library that uses LatUni to generate "plain text" from markdown text.

Yeah, I'm silly that way.
