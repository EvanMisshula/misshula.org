title: Emacs Speaks Statistics (ESS) Tutorial
date: 2014-07-02 15:03
author: emisshula
category: R-course
tags: Emacs, Rstats, ESS
slug: r-tutorial-ess

# Making your editor do statistics

<p><img src="../../images/gbox.jpeg" width="300px" alt="box" title="box"></p>

> All models are wrong, but some are useful.~George E. P. Box

## Why is ESS useful?

ESS makes your command history searchable and modifiable. When you
start doing statistics you think you will always remember what you did
and instantly recall why you did it with that particular data. As you
work on more projects you realize that is a hopeless task. But you
will get questions on what you have done, especially if it was novel
or well thought out.  These questions may not start until months after
your work is done.  Having a command history is the bare minimum of
what you will need to support your work.  We will talk about creating
*replicable research* later in these tutorials. Unbelievably, this is
a topic almost never addressed in introductory courses.

ESS does other tasks for you as well that make interacting with your
data easier.  ESS gives you command line completion of both object
(data) and file names which saves on both typing and mistakes. It
creates so-called *Hot Keys* for quick performance of wrote tasks.  It
records a complete transcript of your R session.  It provides an
interface to the R help system. It allows you to edit your data.  It
provides highlighting and proper indentation which makes your code
easier to read for you and others.  It allows you to run either parts 
of files (called regions) or entire files.

## ESS history

The project has been going since before the invention of R.  It was
around in 1989, when it was used to interact with R's proprietary
antecedent Bell Lab's S-language built by Richard Chambers. I am a a
geek about the history of scientific and mathematical ideas. If you
are interested in the history, the [wikipedia](http://en.wikipedia.org/wiki/S_%2528programming_language%2529) article is a good start.
You can also check out the [S-page](http://stat.bell-labs.com/S/) at Bell Labs.  For any academic work
I strongly suggest citing the published paper on ESS which is available
at this [link](http://biostats.bepress.com/uwbiostat/paper173/).

## Installing ESS

There are a number of ways to install ESS.  I will create a separate 
series of posts on this.  For many, this will be your first foray
into FREE software and installing for the first time is not easy,
particularly on a Mac.  Here is a much to brief set of instructions:

### Linux

#### Beginner

Install from the ELPA package manager.  You should search for ESS
(C-s, where C-s means press the Control and "s" keys at the same
time).  Refer to Xah Lee's [tutorial](http://ergoemacs.org/emacs/emacs_package_system.html) on loading from the packackage 
manager.

#### Advanced

Download the [package](http://ess.r-project.org/index.php?Section%3Ddownload). If you do not have a hidden file called
*home/username*.emacs create one and add the line:

    (load "~/langs/emacs/elisp-ds/ess/lisp/ess-site")

#### Trap

Do not install Emacs and ESS from the Ubuntu or Debian repositories.  They
are usually hoplelessly out of date.

### Windows

Download the emacs distribution for [Windows](http://vgoulet.act.ulaval.ca/en/emacs/windows/) from Vincent Goulet.
Remember this is an executable file and you will have to allow it to
work.

### Mac OS X

Download the emacs distribution for [Mac OS X](http://vgoulet.act.ulaval.ca/en/emacs/mac/)  Vincent Goulet.
Remember this is an executable file and you will have to allow it to
work. Also you have to drag the downloaded file to your apps file. I
have never understood the point of this and I forget to how to do it 
every time.  Here is a [reference and explanation](http://apple.stackexchange.com/questions/15306/why-do-i-have-to-drag-my-new-apps-into-the-application-folder).  It always makes me 
think of how Richard Stallman who founded the Free Software movement
hated Steve Jobs:

> Steve Jobs, the pioneer of the computer as a jail made cool, designed
> to sever fools from their freedom, has died.
> 
> As Chicago Mayor Harold Washington said of the corrupt former Mayor
> Daley, "I'm not glad he's dead, but I'm glad he's gone." Nobody
> deserves to have to die &#x2013; not Jobs, not Mr. Bill, not even people
> guilty of bigger evils than theirs. But we all deserve the end of
> Jobs' malign influence on people's computing.
> 
> Unfortunately, that influence continues despite his absence. We can
> only hope his successors, as they attempt to carry on his legacy, will
> be less effective. ~Richard M Stallman

<p><img src="../../images/rms.jpeg" width="300px" alt="box" title="box"></p>

## Testing your installation

You have to have installed R.  The instructions are [here](http://cran.r-project.org/doc/manuals/r-release/R-admin.html). You have to
have installed Emacs and ESS.  For Windows and Mac Users, you get both
Emacs and ESS when you download from Vincent Goulet. Now type `M-x R`.
This will start an R process within a new buffer.  These buffers are
called *inferior* as they run a process under Emacs.  The ESS manual
calls them *iESS* buffers.

If something went wrong, note the error and search.  If nothing happened
try searching "Emacs can't find my R installation."

## Editing R code

Indentation is automatic.  If you want to do something special use the
command `M-x indent region`. If you don't understand what that means
please refer to my earlier tutorial on [basic emacs](http://EvanMisshula.github.io/r-tutorial-emacs-basics.html). It also resets the
underscore "\_" to the assignment arrow "<-" which saves a keystroke
many times. If not you can use the underscore by typing `M-q _` or just
"\_" twice.  You can tab complete objects (data) with `C-c TAB` in buffers
that end with .R extension.  It is by the file extension that Emacs 
knows what mode to use.

Here are the key-bindings for moving around functions:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybinding</th>
<th scope="col" class="left">Function</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">C-M-a</td>
<td class="left">ess-beginning-of-function</td>
</tr>


<tr>
<td class="left">C-M-e</td>
<td class="left">ess-end-of-function</td>
</tr>


<tr>
<td class="left">C-M-h</td>
<td class="left">ess-mark-function</td>
</tr>
</tbody>
</table>

## Viewing help files

You can view a help file two ways.  If you are in the R console:

>?pbinorm

If you are not:

`C-c C-v RET pbinom RET`

# The R session

In the `*R*` buffer you can run any R command.  R and statistics will be 
the next tutorial.  You can recall your command history.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">keybinding</th>
<th scope="col" class="left">function</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">M-p</td>
<td class="left">comint-previous-input</td>
</tr>


<tr>
<td class="left">M-n</td>
<td class="left">comint-next-input</td>
</tr>


<tr>
<td class="left">M-r</td>
<td class="left">comint-previous-matching-input</td>
</tr>
</tbody>
</table>

# Transcripts

You can save an R buffer to create a transcript. You can clean up the
transcript with `M-x ess-transcript-clean-buffer`.  You can run
multiple sessions of R.=M-x R= multiple times will generate multiple
processes, e.g. `*R*`, `*R:2*`, &#x2026;

# Sending code from an R buffer to an R session

If you only have one R session (typical), it will automatically be
associated with the R buffer.  Otherwise you can associate the buffer
with `C-c C-s`.  Here are the bindings for sending code:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybinding</th>
<th scope="col" class="left">Function</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">`C-c C-j`</td>
<td class="left">`ess-eval-line`</td>
</tr>


<tr>
<td class="left">`C-c M-j`</td>
<td class="left">`ess-eval-line-and-go`</td>
</tr>


<tr>
<td class="left">`C-c C-f`</td>
<td class="left">`ess-eval-function`</td>
</tr>


<tr>
<td class="left">`C-c M-f`</td>
<td class="left">`ess-eval-function-and-go`</td>
</tr>


<tr>
<td class="left">`C-c C-r`</td>
<td class="left">`ess-eval-region`</td>
</tr>


<tr>
<td class="left">`C-c M-r`</td>
<td class="left">`ess-eval-region-and-go`</td>
</tr>


<tr>
<td class="left">`C-c C-b`</td>
<td class="left">`ess-eval-buffer`</td>
</tr>


<tr>
<td class="left">`C-c M-b`</td>
<td class="left">`ess-eval-buffer-and-go`</td>
</tr>


<tr>
<td class="left">`C-c C-n`</td>
<td class="left">`ess-eval-line-and-step`</td>
</tr>
</tbody>
</table>

About 90% of the time I only use:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">Keybinding</th>
<th scope="col" class="left">Function</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">`C-c C-r`</td>
<td class="left">`ess-eval-region`</td>
</tr>
</tbody>
</table>

<h2>Next we are on to statistics!!</h2>

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> Box & Draper (1987), Empirical model-building and response surfaces, Wiley, p. 424.</div>

<div class="footdef"><sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> Windows 8 hides the file extension by default. You can change
this evil behavior by seting the environment variable.</div>


</div>
</div>