---
title: ZineScript Tutorial
layout: home
---

# Welcome

Welcome to the wonderful world of ZineScript! If you're new here (or to zines at all), this is just the section for you!

To start, "What is a zine?"

> Zines, for those who don't know, are a type of self-published short-form physical or digital media. The name "zine" is a shortening of the word "magazine".

"What is ZineScript and why did you make it?"

> ZineScript aims to bring zines to those with more programming-oriented minds. Originally conceived as a zine-like twist on [Sonic Pi](https://sonic-pi.net/), ZineScript is a lua-based scripting environment for programmatically creating/generating zines.

"How can I get started with ZineScript?"

## Installation

ZineScript can be installed on my itch page, [here](https://cmdrapollo.itch.io/ZineScript/). Purchasing or donating to ZineScript is strictly **not necessary**, but is greatly appreciated if you have the funds! Once you install the zipped folder, simply extract it to whatever folder you wish. Important Note: this ZineScript tutorial is *not* intended for those new to programming. You are expected to have at least a basic knowledge of programming and the ability to write Lua scripts. That said, Lua *is* quite beginner-friendly, so it's not all doom and gloom if you don't know Lua. However, this tutorial will not be the place to learn it for the first time.

## Running ZineScript

To run a ZineScript source file (a file with the .zs extension), simply drag and drop the file onto ZineScript in your file explorer. Alteratively, if you are savvy with the terminal/windows command prompt/powershell, simply run ZineScript with the path to your file as the argument.

# Getting Started With ZineScript Scripting

Now that we've spoken in broad-strokes about how ZineScript operates, let's get into the nitty-gritty. To start, it is best practice to begin a .zs file with the following lines:

```lua
zine:title("Title Name Here")
zine:author("Author Name Here")
```

These lines are **not** necessary, but are useful for specifying metadata that can be used later on.

Next, let's add some content to our zine. We'll do this by looping over each page, and giving it a random background color with the following code:

```lua
...

for page = 1, 8 do
    zine:startpage(page)
    zine:background(zine:randomColor())
    -- this following line is not strictly
    -- necessary, but it is my personal
    -- preference to call it before going
    -- on to the next page
    zine:endpage()
end
```

Note: We only loop over the range 1-8. This is because, at the moment, ZineScript only supports 8-page folded zines. This is slated to change in the future. However, as it stands, ZineScript is in its infantile stages of development.

Now, let's add some unique text onto each page. For this example, I will use page numbers, but feel free to get creative!

```lua
...

-- this code slots in after we call
-- zine:background but before we call
-- zine:endpage
zine:add(
    zine:text({
        text = "Page " .. tostring(page),
        -- (x, y) coordinate pairs are measured
        -- in inches and are offset from the top-
        -- left. so (0.1, 0.1) means that the
        -- top-left corner of the text will be
        -- inset 0.1 inches from the left of the
        -- page and 0.1 inches from the top of
        -- the page.
        x = 0.1,
        y = 0.1,
    })
)

...
```

At this point, you may be tempted to run our script and see what beautiful artwork we have created. However, if you *do* try to run the script, you won't see anything! The reason for this is because at the very bottom of our file, outside of our pages loop, we need to put the following two function calls:

```lua
...

zine:render()
zine:save("output.png")
```

Now, if you run the script and find the image as specified by the path in zine:save, you should see some teeny-tiny page numbers on the top-left of each page along with our randomly-generated colors!

Since the text is so small, let's make it a bit bigger, and also give it a random color! To do that, we need to add a Lua table called `textOptions` in our larger table of all options for the text (including "text", "x", and "y"). So now, let's replace the previous `zine:text()` call with the following code:

```lua
zine:text({
    text = "Page " .. tostring(page),
    x = 0.1,
    y = 0.1,
    -- this part is new !!
    textOptions = {
        size = 30,
        color = zine:randomColor(),
    }
})
```

Note: There are more optional parameters to be changed via `textOptions` than just size and color! These include things like changing the font and centering the text. Check out the [docs](documentation/) for more details!

For the penultimate part of this tutorial, I will demonstrate how you can:
1. Transform surfaces in various ways
2. Stack zine calls in order to achieve multiple effects at once

So, let's rotate our text and then scale it up with the `zine:rotate` and `zine:scale` function calls. Let's replace our `zine:add()` call with the following code:

```lua
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
```

Notice the nesting of calls here. This is integral to the control flow of ZineScript and is what allows you, similarly to a guitar pedal board, to change the order of effects. For our simple example with rotation and scaling, this won't effect much, but it is something to consider!

Similarly important to note is the use of `zine:pageWidth()` and `zine:pageHeight()`. These are built in functions that can be used to return the size of a page in inches! So taking these values and dividing each by 2 means that we receive the center of the page in inches. This, when paired with the use of `centered = true`, means that our text will now be centered on the page!

Finally for this tutorial, I will just show off something fun: the `zine:spraypaint()` function! For the final time, replace the call to `zine:background()` with the following code:

```lua
zine:background(zine:randomColor())
zine:add(
    zine:spraypaint({
        surface = zine:newSurface({ x = 0, y = 0, width = zine:pageWidth(), height = zine:pageHeight() }),
        color = "white",
        region = { 0, 0, zine:pageWidth(), zine:pageHeight() }
    })
)
```

Run the script for the last time, and you should a white spraypaint-like effect over the randomly-colored-background. Thank you for sticking through to the end of the ZineScript tutorial, and happy coding!