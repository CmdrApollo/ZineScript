---
title: ZineScript Documentation
layout: home
---

# ZineScript Documentation

Below is the documentation for all currently-available ZineScript functions, prefixed by `zine:`. Functions are listed in alphabetical order.

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

Set the background color for the active page. [zine:startpage](#startpage) must be called before calling `zine:background`. Note that colors are stored as strings such as "red", "yellow", or "forestgreen". You can also use hex values in the following format: "#rrggbb"

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

`zine:image` returns a surface object.