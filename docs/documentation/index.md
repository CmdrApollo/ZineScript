---
title: ZineScript Documentation
layout: home
---

# ZineScript Documentation

Below is the documentation for all currently-available ZineScript functions, prefixed by `zine:`. Functions are listed in alphabetical order. To see the documentation in action, check out the [example programs](../examples/)!

## add

```lua
zine:add(element) -> nil
```

Add an element to the active page. [zine:startpage](#startpage) must be called before calling `zine:add`.

## author

```lua
zine:author(authorName) -> nil
```

Specify the author's name. Stored in the `zine.author_name` variable.

## background

```lua
zine:background(color) -> nil
```

Set the background color for the active page. [zine:startpage](#startpage) must be called before calling `zine:background`. Note that colors are stored as strings such as "red", "yellow", or "forestgreen". You can also use hex values in the following format: `#rrggbb`.

## blur

```lua
zine:blur(surface) -> Surface
```

Apply a gaussian blur to a given surface.

`zine:blur` returns the surface object that was passed into it.

## contour

```lua
zine:contour(surface) -> Surface
```

Apply a contour effect to a given surface.

`zine:contour` returns the surface object that was passed into it.

## endpage

```lua
zine:endpage() -> nil
```

Make it so that there is no active page.

## fill

```lua
zine:fill(optionsTable) -> Surface
```

Fill a surface with a given color.

Options for `zine:fill` are as follows:

1. surface - surface to be filled
2. color - color to be filled with

`zine:fill` returns the surface object that was passed into it.

## image

```lua
zine:image(optionsTable) -> Surface
```

Create a new image surface from a given path.

Options for `zine:image` are as follows:

1. path - **relative** path to the image to be loaded
2. x - the image's `x` position relative to the left of the page, measured in inches
3. y - the image's `y` position relative to the top of the page, measured in inches
4. centered - whether or not the image is centered on its (x, y) coordinate

`zine:image` returns a surface object.

## invert

```lua
zine:invert(surface) -> Surface
```

Invert the color of every pixel in the surface.

`zine:invert` returns the surface object that was passed into it.

## newSurface

```lua
zine:newSurface(optionsTable) -> Surface
```

Create a new surface at the given position with the given dimensions.

Options for `zine:newSurface` are as follows:

1. x - the surface's `x` position relative to the left of the page, measured in inches
2. y - the surface's `y` position relative to the top of the page, measured in inches
3. width - the surface's width, measured in inches
4. height - the surface's height, measured in inches

`zine:newSurface` returns a surface object.

## noise

```lua
zine:noise(optionsTable) -> Surface
```

Add colored noise to the surface provided.

Options for `zine:noise` are as follows:

1. surface - the surface to apply noise to
2. color - the color of the noise
3. region - the region of the surface that the noise should cover, stored as a table in the format `{ x, y, width, height }`, all measured in inches
4. pixelSize - size in pixels of each noise tile
5. coverage - likelihood for each pixel in the surface to get chosen to be filled by the noise

`zine:noise` returns the surface object that was passed into it.

## pageHeight

```lua
zine:pageHeight() -> number
```

Return the height per page, measured in inches.

## pageWidth

```lua
zine:pageWidth() -> number
```

Return the width per page, measured in inches.

## random

```lua
zine:random() -> number
```

Return a random floating point number in the range 0-1.

## randomColor

```lua
zine:randomColor() -> string
```

Return a random color represented as a hexadecimal string in the format `#rrggbb`.

## render

```lua
zine:render() -> nil
```

Render the zine to an internal image. Required to be called before [zine:save](#save).

## rotate

```lua
zine:rotate(optionsTable) -> Surface
```

Rotate a surface with a given angle, measured in degrees.

Options for `zine:rotate` are as follows:

1. surface - surface to be rotated
2. angle - angle by which to rotate the surface

Note that positive angles are counterclockwise.

`zine:rotate` returns the surface object that was passed into it.

## save

```lua
zine:save(path) -> nil
```

Save the internally rendered zine to the given path. Cannot be called before [zine:render](#render).

## scale

```lua
zine:scale(optionsTable) -> Surface
```

Scale a surface by a given factor.

Options for `zine:scale` are as follows:

1. surface - surface to be scaled
2. scale - factor by which to scale a surface

`zine:scale` returns the surface object that was passed into it.

## spraypaint

```lua
zine:spraypaint(optionsTable) -> Surface
```

Add weighted, colored noise to the surface provided.

Options for `zine:spraypaint` are as follows:

1. surface - the surface to apply spraypaint to
2. color - the color of the spraypaint
3. region - the region of the surface that the spraypaint should cover, stored as a table in the format `{ x, y, width, height }`, all measured in inches
4. pixelSize - size in pixels of each paint drop
5. inverted - whether or not to invert the distance
6. coverage - likelihood for each pixel in the surface to get chosen to be filled by the spraypaint

`zine:spraypaint` returns the surface object that was passed into it.

## startpage

```lua
zine:startpage(pageNumber) -> nil
```

Sets the active page. Note that while you *can* set pages outside of the range 1-8, they will not be rendered.

## tableToColor

```lua
zine:tableToColor(colorTable) -> string
```

From a color that is represented as a table in the format `{ red, green, blue }`, return a color represented as a hexadecimal string in the format `#rrggbb`.

## text

```lua
zine:text(optionsTable) -> Surface
```

Create a new text surface.

Options for `zine:text` are as follows:

1. text - literal text to be displayed
2. x - the text's `x` position relative to the left of the page, measured in inches
3. y - the text's `y` position relative to the top of the page, measured in inches
4. textOptions - a table of **many** optional parameters to modify text with
    1. font - the font with which to render the text, default is arial
    2. size - the size of the text, default is 12
    3. color - the color of the text, default is black
    4. backgroundColor - the background color of the text, default is no background color
    5. antialias - whether or not to antialias the text, default is true
    6. centered - whether or not to center the text surface
    7. wrapWidth - at what width, measured in inches, to automatically wrap text
    8. bold - whether or not text is bold
    9. italic - whether or not text is italic

`zine:text` returns a surface object.

## title

```lua
zine:title(zineTitle) -> nil
```

Specify the zine's title. Stored in the `zine.title_text` variable.

## wavy

```lua
zine:wavy(optionsTable) -> Surface
```

Make a surface nice and wavy.

Options for `zine:wavy` are as follows:

1. surface - surface to be made wavy
2. frequency - frequency of the waviness, measured in inches
3. amplitude - amplitude of the waviness, measured in inches

`zine:wavy` returns the surface object that was passed into it.