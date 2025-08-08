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