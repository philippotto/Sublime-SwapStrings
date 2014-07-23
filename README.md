Sublime SwapStrings [![Build Status](https://travis-ci.org/philippotto/Sublime-SwapStrings.svg?branch=master)](https://travis-ci.org/philippotto/Sublime-SwapStrings)
===================

A Sublime Text 2/3 Plugin which allows swapping of arbitrary strings within a selection. A common usecase is swapping of single and double quotation marks:

![](http://philippotto.github.io/Sublime-SwapStrings/screens/swap-quotes.gif)


But it is also possible to choose other strings to swap, e.g.:

![](http://philippotto.github.io/Sublime-SwapStrings/screens/swap-strings.gif)


The command is called ```swap_strings``` and can be parameterized with stringA and stringB.
The default keybinding is:
- ```ctrl/super+shift+alt+s``` for the generic ```swap_strings``` command
- ```ctrl+shift+alt+c``` for ```swap_strings``` parameterized with " and ' for stringA and stringB

The command will be executed on the current selection. If nothing is selected, the current line will be used for the command.


## Installation

Either use [Package Control](https://sublime.wbond.net/installation) and search for `SwapStrings` or clone this repository into Sublime Text's "Packages" directory.
