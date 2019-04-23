### Emojitwo Emoticon Theme for Pidgin <img src="svg/1f44d-1f3fd.svg" width="32" height="32" />

<!--
![thumbs up](svg/1f44d-1f3fd.svg =24x24)
-->

The [Emojitwo](https://emojitwo.github.io/) emoticon theme made usable with
[Pidgin](http://pidgin.im/) instant messanger.

Emoji artwork is provided by Emojitwo, originally released as
[Emojione 2.2](https://www.emojione.com/) by [Ranks.com](http://www.ranks.com/)
with contributions from the Emojitwo community and is licensed under CC-BY 4.0.

This version/release is not endorsed by Ranks.com or the Emojitwo community.

### Licensing

#### EmojiOne Artwork

*  Applies to all PNG and SVG files as well as any adaptations made.
*  License: Creative Commons Attribution 4.0 International
*  Human Readable License: http://creativecommons.org/licenses/by/4.0/
*  Complete Legal Terms: http://creativecommons.org/licenses/by/4.0/legalcode

### Creating/Exporting Theme

#### Commands

If [Python](https://www.python.org/) is installed (requires version 3+), the
included ***release.py*** script can be run to export the theme for use with
Pidgin.

```
Usage:
	release.py [options]

Description
	Helper script for creating release.

Options:
	-h | --help             Show this usage information.
	-O | --overwrite        Existing PNG images will be overitten with new ones.
	-n | --dry-run          No action is taken.
	-c | --clean            Cleans the directory tree.
	-s | --size             Size(s) for exported PNG images in pixels (e.g.
							--size 24,32,64).
	--no-update-template    Theme template will not be regenerated (only works
							if template exists).
	--force-update-template Forces the template to be updated (only useful with
							--dry-run).
	--all-images			Don't ignore images marked for exclusion in template
							file.
							Also removes images found in release that have been
							marked for exclusion.
	-t | --tag              Create Git tag from INFO file (requires "git"
							command).
```

The exported files will be created in the ***release*** directory. By default,
PNG images will be exported in 16x16 & 24x24 pixels. To specify which pixel
sizes to export use the ***--size*** option. It accepts a comma-separated list
(e.g. *--size 16,24,32*).

Example:

```
./release.py --size 16,24,32
```

Existing PNG images will not be overwritten when the theme is exported. To force
overwriting existing images use the ***--overwrite*** option:

```
./release.py --overwrite
```

If you only want to overwrite/update specific images, the ***--overwrite***
accepts a comma-separated list value:

```
./release.py --overwrite 263a.png,2639.png
```

#### Template File

A template file named ***[template.txt](template.txt)*** controls how the theme
will be exported. This file is automatically generated by the ***release.py***
script using information found in the ***[INFO](INFO)*** file & will add any new
images found in the ***svg*** directory to the ***default*** group. Lines
beginning with "#!" denote that the image will *not* be included in the exported
theme.

```
[default]
# included images
263a.png
2639.png
# excluded images
#!1f600.png
#!1f601.png
```

To override this behavior, use the ***--all-images*** option:

```
./release.py --all-images
```
