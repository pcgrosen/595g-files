# IDA

IDA is a graphical disassembler with many useful features.

(You can get the free version here.)[https://www.hex-rays.com/products/ida/support/download_freeware.shtml]

To get started, launch IDA and open up a 64-bit ELF.

## Graph View

After IDA completes its auto-analysis (this can sometimes take several minutes), you'll be dropped into a graph view for the main function of the binary. This view contains a disassembly of the function separated into blocks that represent continuous control flow ("basic blocks"), i.e. there are no branches or if-statements inside of a single block.

In this view, you can click-and-drag to move the graph around.

## Text View

To switch to text view, click anywhere in the graph window and then press space. You will be switched to a simple linear disassembly of the program that represents the literal ordering of the instructions. In this view, you can see the address of each instruction on the left and scroll up and down to view lower and higher addresses, respectively.

## Navigating

To navigate around a program, you have a number of options:

* Switch to text view and scroll

* Click anywhere on the strip at the top (read the legend to understand the color scheme)

* Use the "Functions Window" on the left of your screen to move to another function

* Press "g" while focused in the main window and enter a symbol name or address

* Use any of the options under the "Jump" menu at the top

## Viewing function stack frames

To view a function's stack frame, navigate to the beginning of said function. If IDA has successfully identified a stack frame (and it should for all of the challenges we'll be doing), you should see a series of "var_" names in green. Double click on any of these to view the stack frame.

## Interacting with the disassembly

IDA is unparalleled in its features for interacting with disassembled code. For example, you can:

* Click on a variable and press "n" to change its name throughout the function (if local) or program (if global)

* Click on a variable in the stack frame view and press "d" to change its length (IDA will cycle through 1 byte -> 2 -> 4 -> 8 -> 1 etc.)

* Click on a variable or symbol and press "x" to view all of that identifier's "x-refs" (locations where it is referenced, accessed, or overwritten) throughout the function or program

* Press ";" to add a comment to a variable (e.g. in stack frame view) or line of assembly

And much more. To see more options, just right-click on something and look at the context menu.

## Hotkeys

* Space: switch between graph and text view

* g: goto a symbol

* n: rename a symbol

* d: change the data type of a variable

* x: view the x-refs of a symbol

* ; : add a comment

* Alt-T: search in any of IDA's views (useful in the function or symbol lists, for example)

* Ctrl-T: repeate the previous search

* Shift-F12: view all strings in the program

* Ctrl-W: save the database

* Alt-X: exit
