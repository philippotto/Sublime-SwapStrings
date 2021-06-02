Sublime SwapBullets 

===================

A Sublime Text 2/3/4 Plugin which allows swapping of bullets from Microsoft OneNote to plain text bullets for common Markdown. A common usecase is prepping OneNote files to be stored as markdown so they can be exported and used elsewhere. 

![](http://philippotto.github.io/Sublime-SwapStrings/screens/swap-quotes.gif)


But it is also possible to choose other strings to swap, e.g.:

![](http://philippotto.github.io/Sublime-SwapStrings/screens/swap-strings.gif)


The command is called ```swap_bullets``` and can be parameterized with stringA and stringB.
The default keybinding is:
- ```ctrl/super+shift+alt+s``` for the generic ```swap_bullets``` command
- ```ctrl+shift+alt+c``` for ```swap_bullets``` parameterized with " and ' for stringA and stringB

The command will be executed on the current selection. If nothing is selected, the current line will be used for the command.


## Installation

Either use [Package Control](https://sublime.wbond.net/installation) and search for `SwapBullets` or clone this repository into Sublime Text's "Packages" directory.
