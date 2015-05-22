title: Intro to R with Emacs-Speaks-Statistics
date: 2014-06-29
author: emisshula
category: R-course
tags: Emacs, Rstats, ESS
slug: r-tutorial

# Intro

A number of my colleagues need to analyze data and are learning a
programming language for the first time.  It does not need to be said,
this is a very heavy lift and occurs in the presence of a wide diversity
of well intentioned opinion.  It also occurs in the presence of academic
bullshit.  This is not well intentioned.  It is designed to sell books and 
software licenses.  It is my opinion that the appropriate first scripting 
language to learn for the aspiring social scientist is [R](http://www.r-project.org/). Arguements could 
be made for perl, python or lisp.  I think these great languages can be learned
later.  For describing relationships with data and graphing results, [R](http://www.r-project.org/) has a great
set of libraries.

# R Front ends

There are a number of front-ends for [R](http://www.r-project.org/).  The most popular of which is
R-studio. I think it leaves much to be desired.  It is also produced
by a company that sells enhancements to [R](http://www.r-project.org/) that most users will never
need.  I find the better and more cost effective solution to be
[Emacs-Speaks-Statistics (ESS)](http://ess.r-project.org/). Much of the power of the language comes
from being able to read from files and streams.  Combining this with 
the uber editor [Emacs](http://www.gnu.org/software/emacs/) only makes sense.  For many data manipulation 
problems the student can solve it either with either tool.

The intellectual history of this tutorial is taken from Charles
DiMaggio's excellent [introduction to R](http://www.columbia.edu/~cjd11/charles_dimaggio/DIRE/styled-4/styled-6/) and two brilliant tutorials
from Stephen Elgen [An introduction to ESS from 2011](http://web.warwick.ac.uk/statsdept/user2011/tutorials/Eglen.html) and [Caimbridge R
bootcamp](http://sje30.github.io/2014-01-07-cam/).

Here is our introduction:

### Emacs

-   Why Emacs
-   History of Emacs
-   Moving around
-   Cut and paste
-   Loading/saving files
-   Windows
-   Search and replace
-   Macros
-   Modes
-   Completion
-   Getting help
-   libraries
-   Hooks
-   Philosophy

### ESS

-   Why ESS?
-   History of ESS
-   ESS Installation
-   Editing and viewing R code
-   Making comments
-   Indenting your code.
-   Viewing help files
-   Making help files (.Rd)
-   Inferior ESS Processes (`*R*`)
-   Which version of R will it find?
-   What can I do in `*R*`?
-   What is emacsclient?
-   Transcripts
-   How many versions of R can I run?
-   Sending code from an R buffer to `*R*`
-   Customizing ESS
-   When things go wrong with ESS

### Org Mode

-   intro
-   exporting to LaTeX or html
-   R examples

### R language

-   introduction
-   foundations
-   functions
-   packages
-   graphics
-   data
-   variables

### Advanced stats

-   power
-   web/online
-   bayes (multilevel, hierarchical)
-   spatial
-   meta-analysis

More to come&#x2026;