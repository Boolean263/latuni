# LatUni: Format latin text with unicode

The Unicode specification allows a lot of glyphs that would normally require special fonts to now be available in "plain text" files. Chess pieces, mathematical symbols, etc.

Unicode even contains variants for the basic Latin alphabet in 𝐛𝐨𝐥𝐝, 𝑖𝑡𝑎𝑙𝑖𝑐, 𝒃𝒐𝒍𝒅 𝒊𝒕𝒂𝒍𝒊𝒄, 𝚖𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎, and 𝕞𝕠𝕣𝕖. LatUni flagrantly abuses this fact to allow you to add text formatting to "plain text" files.

Disclaimer: This is a novelty, and probably breaks some accessibility rules or something.

## Installation

As much as anything else, this was to help me learn python package/module distribution. If I've done it right, you should be able to do the standard `python3 setup.py install` (or `python3 setup.py develop` if you want to hack around with me on this mess).

## Future Plans

* Adding more formatting using combining characters (particularly overstrike and underline)
* The API could probably be improved

## Other Modules

I haven't published it yet, but I'm working on a plugin for the python [Markdown](https://pypi.org/project/Markdown/) library that uses LatUni to generate "plain text" from markdown text.

Yeah, I'm silly that way.
