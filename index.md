# Welcome

Welcome to the wonderful world of ZineScript! If you're new here (or to zines at all), this is just the section for you!

To start, "What is a zine?"

> Zines, for those who don't know, are type of self-published short-form physical or digital media. The name "zine" is a shortening of the word "magazine".

"What is ZineScript and why did you make it?"

> ZineScript aims to bring zines to more programming-oriented minds. Originally conceived as a zine-like twist on [Sonic Pi](https://sonic-pi.net/), ZineScript is a lua-based scripting environment for programmatically creating/generating zines.

"How can I get started with ZineScript?"

## Installation

ZineScript can be installed on my itch page, [here](https://cmdrapollo.itch.io/). Purchasing or donating to ZineScript is strictly **not necessary**, but is greatly appreciated if you have the funds! Once you install the zipped folder, simply extract it to whatever folder you wish.

## Running ZineScript

To run a ZineScript source file (a file with the .zs extension), simply drag and drop the file onto ZineScript in your file explorer. Alteratively, if you are savvy with the terminal/windows command prompt/powershell, simply run ZineScript with the path to your file as the argument.

# Getting Started With ZineScript Scripting

Now that we've spoken in broad-strokes about how ZineScript, let's get into the nitty-gritty. To start, it is best practice to begin a .zs file with the following lines:

```lua
zine:title("Title Name Here")
zine:author("Author Name Here")
```

These lines are **not** necessary, but are useful for specifying metadata that can be used later on.