title: Intro to basic Emacs for statistics
date: 2014-07-01
author: emisshula
category: R-course
tags: Emacs, Rstats, ESS
slug: r-tutorial-emacs-basics

# Emacs

> What I cannot build, I do not understand. — Richard Feynman

## Why Emacs?

-   This section is borrows heavily from [Stephen Elgen](http://www.damtp.cam.ac.uk/user/sje30/ess11/) and [Phil Sung](http://web.psung.name/emacs/2009/part1.html)

### The long answer (though still far from complete)

Emacs provides the same editing commands available for each language
you are using.  This is a big advantage if you are using a variety of
tools to solve a given problem. Right now you care about using R.
Soon you will realize that you may need a database.  Databases don't
naturally speak R.  They speak Structured Querey Language (SQL).
Emacs can speak SQL.  You may need to create a web program.  You will
need to speak Python or Ruby.  Emacs can speak python or ruby.

Instead of a graph, you may want to create an interactive
vizualization using d3.js.  Again Emacs can edit javascript.  You may
need to turn your report into a LaTex report, again Emacs speaks Latex
or HTML.  

Otherwise you might use R-studio for R, Eclipse for python,
Gedit or Notepad++ for LaTex, Webstorm for Javascript, Netbeans for
Java, phpMyAdmin for SQL.  You don't want to learn a new editor every
time you use a new tool.

Also, as we will see, there are a large set of tools available at all
times. Emacs lets us move text between tasks easily.  Because Emacs
exposes its source code, it easy to extend.  There is also a facillity
for creating macros to accomplish one off tasks.  The language Emacs
is written in, Elisp, allows us to add new features. These new
features don't require you to restart Emacs, it is a fully dynamic
environment.

### The short answer

Emacs is an editor for code. Emacs is an Integrated Development
Environment (IDE) for any language you will ever need (including R).
Emacs is a terminal emulator. Emacs is a file manager.  And Emacs can
show the differences between files and integrate with all version control
systems.  If you want to build something, then Emacs is the right environment

## History of Emacs

### Brief outline

The chief architect of Emacs is Richard Stallman ([RMS](https://www.fsf.org/about/staff-and-board)).  He is the
founder of the Free Software foundation. Richard developed a number of
widely used software components of GNU, including the original Emacs,
the GNU Compiler Collection, the GNU symbolic debugger (gdb), GNU
Emacs, and various other programs for the GNU operating system. He
invented the idea of copyleft and licenses that allow for copying.
When he invented it, he and the other principal inventor [Guy Steele](https://labs.oracle.com/pls/apex/f?p%3Dlabs:bio:0:120)
were in researchers at the artificial intelligence lab at MIT, [CSAIL](http://www.csail.mit.edu/).
They were both graduate students of Gerald J Sussman ([GJS](http://groups.csail.mit.edu/mac/users/gjs/biography.html)) who was
working with lisp variant languages to solve decision problems.

Emacs has evolved from a terminal only editor to one with a rich
graphical support.  Emacs is capable through (tramp mode) of editing
files on remote machines.  This means that you can edit files that
need to run on a machine that you share such as an Amazon cluster
(AWS) or a super computer. Don't worry we will start much smaller!

Emacs development has been undergoing a renissaince since the
development of org-mode.  Prior development cycles had been slow.  As
of this writing, the latest Emacs version is 24.3 and org-mode is
8.2.5.  Prior development cycles had been slow.  Also in the 1990's
Emacs split with more graphic support being available [XEmacs](http://www.xemacs.org/).  At
least two other variants are still maintained [Aquamacs](http://aquamacs.org/) for Mac OS X and
[Ergo-Emacs](http://ergoemacs.org/) which claims to be easier on your fingers.  The inventor of
Ergo-Emacs, [Xah Lee](http://xahlee.org/), is a prolific contributor of tutorials and other
resources to the Emacs community.

## Where do your documents live?

Your documents live on Disk.  However if you use a modern graphical 
user interface it is not always easy to find out where the document 
you care about is.  Your docuents folder is a subdirectory.  My 
user name is 'evan'. In linux, my documents are in:

    /home/evan/Documents

In Mac OS X and Windows 8, my documents are in:

    /Users/evan/Documents

You create a document by asking Emacs to find a document that does not
exist yet.  Before we can do this you have to understand the instructions
this tutorial is going to give.  So we need to define certain keystrokes:

-   `TAB` is the TAB (indent) key.
-   `RET` is the Return (carriage return, enter) key.
-   `C-h` means press control key AND \`\`h'' together
-   `ESC-h` means press ESC key THEN \`\`h''
-   `M-h` means press ALT or Meta key AND \`\`h'' together.
-   `M-C-h` means press Meta or Alt while pressing  h and control key.  OR
    (if no meta/alt): ESC THEN (control and h keys together).
-   Older keyboards (and sometimes older Macs) without ALT or Meta
    lead to confusion between ESC and Meta, but ideally they should
    be different.

To do this start Emacs and find the file \`\`practice.org''.  So if you are 
on Linux:

    C-x C-f /home/evan/Documents/practice.org

If you are on Windows or Mac:

    C-x C-f /Users/evan/Documents/practice.org

If you see a blank screen, you have done it right.

## Every time you press a key&#x2026;you call a function

This is going to seem pedantic but I am betting you will refer back to
this.  It is easy to get lost with keypresses, keystrokes and
keybindings. When you type the letter "a", that is called a *keystroke*.
A *keybinding* is the function that is bound to a combiantion of
*keystrokes*.

One of the most important keybindings is:

-   `M-x` is bound to execute-extended-command, which allows you to run a
    command by name (there are many commands that are not bound to
    keys).

(Rember that the `M-x` is probably `Alt-x` on your machine.) Another
important keystroke combination is `C-g` is bound to Quit which will
end the command.  If you have typed `M-x` now, then type `C-g` to
Quit.  Mapping between keybindings and commands is flexible; can
change on fly.

## Moving around

I find this picture from Phil Sung helps me remember how to move:

<p><img src="../images/EvAtWork.png" width="300px" alt="img" title="arrows.png"></p>

    C-v    Move forward one screenful
    M-v    Move backward one screenful
    C-l    Clear and redraw screen
    M- ->  Meta-<right> - moves forward a word
    M- <-  Meta-<left> - moves back a word
    M- {   Meta-<up> - move up a paragraph
    M- }   Meta-<down> - move down a paragraph
    M- <   Meta-<less than> - move to file start
    M- >   Meta-<greater than> - move to file end

Instead of the squiggly brace `{` or `}` the up or down arrow will work
as well.

## Cut and paste

Instead of `C-c` to copy and `C-v` to paste, Emacs has older
keybindings. This seems strange

    C-d    Delete
    C-k    Kill from the cursor position to
           end of line
    C-y    Recover/Paste (Yank) killed text
           (repeat to copy)
    M-y    recover former killed text (after C-y).
           Repeat to go back through stack).
    C-x u  _U_ndo  (multiple undo/redo)

Here is the payoff:

-   *point* is current location of cursor

-   *mark* `C-SPC` to define another point

-   *region* is text between mark and point

-   `C-w` kills from point to mark.

-   `C-y` yanks that text back.

## Loading/saving files

Now we can look at the commands to find files and see the buffers
we have loaded into Emacs.  Emacs actually does not save all of your
changes to the file.  Emacs makes a copy of your file on disk to a
copy, called a *buffer*. You make all of your changes to the buffer and 
when you write the file to disk, it replaces the file.

    C-x C-f  _F_ind a file
    C-x C-s  _S_ave the file
    C-s C-w  _W_rite the file to a new name
    If you find a second file with C-x C-f,
    the first file remains inside Emacs.
    You can switch back to it by finding it
    again with C-x C-b.  This way you can get
    quite a number of files inside Emacs.

## Windows

Here is how you work with the buffers that you have loaded into Emacs:

    C-x 0      Move between windows
               (Oh, not Zero!)
    C-x 1      One window
               (i.e., kill all other windows).
    C-x 2      Split horizontally
    C-x 3      Split vertically
    C-x b      Switch to new _b_uffer
    C-x C-b    List _b_uffers

## Search and replace

Here are the commands for searching and replacing:

    M-x (then) replace-string
               Replace string
    M-x (then) query-replace-string
               Will ask you, for each match,
               if you really want to replace
               the old string with the new one.
    C-s        _S_earch forward (repeat to
               reuse past search strings)
    C-r        Search _R_everse (repeat to
               reuse past search strings)

## Quitting and getting help

Here are the commands for quitting and getting help:

    C-h or C-h ?    _H_elp
    C-h c (command) _H_elp on this _c_ommand
    
    C-u 8 (character or command)
                 Repeat character/command 8 times
    
    C-g          Stop, unhang.
    C-x C-c      Stop and exit (_c_lose) Emacs

## Macros

### Repeating yourself

Repeat C-n ten times:

C-u 10 C-n

C-u 70 #

### Keyboard macros

`C-x (` lots of stuff  `C-x )`

Can include counters.  e.g.

    C-x ( TAB step C-x C-k C-i RET C-x )

will make:

    step 0
    step 1
    step 2

&#x2026;

(info "(emacs)Keyboard Macros")

I use this all the time to automate boring editing functions all
the time!!

## Modes

Modes contain specialisations (commands/variables) for different
languages.

-   Major modes are defined for different languages (C, latex, R,
    python, &#x2026;).

-   Consistency across modes where possible (e.g. commands for
    commenting, indentation).  Keybindings consistent.  *Font lock*
    also consistent, e.g. comments in red.

-   Major mode decided typically based on buffer name.

-   `C-h m` describes features available in current buffer.

## Completion

-   TAB completion where possible, e.g `M-x describe- TAB`

## Getting help

Here is how to get help:

    C-h m       describe mode 
    C-h k       describe key  
    C-h i       info          
    C-h t       tutorial

Check out <http://emacswiki.org>

It also lists cool packages (or libraries) you can add to Emacs 
to make it do more.

## libraries

Emacs' `load-path` controls which directories are searched.

    (defun init_ess ()
    "initialize ess"
    (locate-library "ess")
    (add-to-list 'load-path "~/langs/emacs/org-mode/lisp"))

Or to look up the definition of a function, try:

    M-x find-function ess-dirs

## Hooks

Hooks are usually the way you set up Emacs to act on a file you
want to behave in a certain way.

Hooks are run e.g. after major-mode has been created.

    (defun init_eldoc()
    (add-hook 'emacs-lisp-mode-hook 'turn-on-eldoc-mode))

Compare the following two versions:

    ;; version 1
    (defun my-ess-hook ()
      "Add my keybindings to ESS mode."
      (local-set-key (kbd "C-j") 'ess-eval-line-and-step))
    
    (add-hook 'R-mode-hook 'my-ess-hook)
    
    ;; version 2
    (add-hook 'R-mode-hook
              '(lambda ()  (local-set-key (kbd "M-RET")
                                          'ess-R-use-this-dir)))