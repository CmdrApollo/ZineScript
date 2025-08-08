---
title: ZineScript Examples
layout: home
---

# Welcome

Before I get into the examples, I just want to say: feel free to take any of these examples and modify them to make them your own! They can very well be used as templates and guides for your own works! For the most part, these examples won't be super heavily commented, so check out the [documentation](../documentation/) if you want to know what anything does in more detail!

## Tutorial Example

```lua
zine:title("Title Name Here")
zine:author("Author Name Here")

for page = 1, 8 do
    zine:startpage(page)
    zine:background(zine:randomColor())
    zine:add(
        zine:spraypaint({
            surface = zine:newSurface({ x = 0, y = 0, width = zine:pageWidth(), height = zine:pageHeight() }),
            color = "white",
            region = { 0, 0, zine:pageWidth(), zine:pageHeight() }
        })
    )

    zine:add(
        zine:scale({
            surface = zine:rotate({
                surface = zine:text({
                    text = "Page " .. tostring(page),
                    x = zine:pageWidth() / 2,
                    y = zine:pageHeight() / 2,
                    textOptions = {
                        size = 30,
                        color = zine:randomColor(),
                        centered = true
                    }
                }),
                angle = 90
            }),
            scale = 2.0
        })
    )
    
    zine:endpage()
end

zine:render()
zine:save("output.png")
```

## Randomly Rotated Random Images Example

```lua
zine:title("Title Name Here")
zine:author("Author Name Here")

local allImages = { "image1.png", "image2.png", "image3.png" }

for page = 1, 8 do
    zine:startpage(page)
    -- this line isn't necessary. backgrounds are automatically white
    zine:background("white")

    local image = 1 + math.floor(zine:random() * #allImages)

    zine:add(
        zine:rotate({
            surface = zine:image({
                path = allImages[image],
                x = zine:pageWidth() / 2,
                y = zine:pageHeight() / 2,
                centered = true
            }),
            angle = zine:random() * 360
        })
    )
    
    zine:endpage()
end

zine:render()
zine:save("output.png")
```

## Spraypaint Rings Example

```lua
zine:title("Title Name Here")
zine:author("Author Name Here")

for page = 1, 8 do
    zine:startpage(page)
    -- this line isn't necessary. backgrounds are automatically white
    zine:background("white")

    for i = 1, 8 do
        zine:add(
            zine:spraypaint({
                surface = zine:newSurface({
                    x = zine:pageWidth() / 2 - zine:pageWidth() / i,
                    y = zine:pageHeight() / 2 - zine:pageHeight() / i,
                    width = zine:pageWidth() / (i / 2),
                    height = zine:pageHeight() / (i / 2)
                }),
                color = zine:randomColor(),
                region = {0, 0, zine:pageWidth() / (i / 2), zine:pageHeight() / (i / 2)},
                pixelSize = 5 - math.floor(i / 2),
                coverage = 0.5
            })
        )
    end
    
    zine:endpage()
end

zine:render()
zine:save("output.png")
```