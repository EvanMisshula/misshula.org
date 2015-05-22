title: docview-setup 
date: 2015-04-01
author: emisshula
category: Tutorials
tags: Emacs, pdf, meta-cognition
slug: doc-setup

<p><img src="../../images/carolDweck.jpg" width="600px" alt="carol<sub>dweck</sub>" title="box"></p>

# The problem

We all have to complete tutorials to learn new languages.  One
constant pain is that the tutorials are usually trapped in pdf's when
we need to type code.  Emacs makes this problem go away through its 
*doc-view* mode which allows you to render pdf's in Emacs. The problem is 
that it only works out of the box in Linux.

<p><img src="../../images/mindset.jpg" width="600px" alt="mindset" title="box"></p>

# The Mac OS X solution

For mac, you need to install emacs via [homebrew](http://brew.sh).  Open a terminal by going to Finder, see the picture
below.

<p><img src="../../images/utilities.png" width="550px" alt="utl" title="utlities"></p>

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Copy the installation command from homebrew into the terminal.  Type brew doctor.  The complication
is that you may have to modify your path.  If so, see this [answer](http://stackoverflow.com/questions/10343834/homebrew-wants-me-to-amend-my-path-no-clue-how) from stack overflow.

    brew install ghostscript
    brew install emacs --with-cocoa
    brew linkapps emacs

# Windows

For windows, the situation is considerablely more complicated.  You must install the incredibly
useful [cygwin](https://cygwin.com) which provides the libraries for *ghostscript* and *xpdf*.  Watch this [video](https://www.youtube.com/watch?v=TjxEH_tr7e0) by Paul
Royer on installing cygwin and downloading the libraries.  You then need to modify the windows
path environmental variable using these [instructions](https://www.java.com/en/download/help/path.xml) to include thos libraries which are found in 
your new home directory.  I will add to this later as these instructions are vague.