title: Intro to Emacs Speaks Statistics
date: 2014-07-01
author: emisshula
category: R-course
tags: Emacs, Rstats, ESS
slug: r-tutorial-intro-ess

# Emacs Speaks Statistics (ESS)

ESS is a library (package) for Emacs which allows it to interact with
a number of statistical packages including S+, R, SaS, SPSS and Stata.
For the purpose of these notes.  We will only deal with R.  It allows
the command history to be searchable and modifiable.  It allows for the 
command line completion of both filenames and objects.  It creates Hot-
keys for commonly used commands in R.  It records a complete transcript 
of our R session.  It provides a interface to the help system.  It allows
us to edit R objects/data structures.  When we edit code in ESS, it provides
indentation and highlighting which makes code easier to read and understand.
Ess allows us to evaluate arbitrary regions of a file.  Finally it allows
us to load files into R for evaluation.

# History outline

-   3 branches: S-mode, SAS-mode, Stata-mode
-   S-mode: 1989, 2 groups managing the project before (Bates/F
    Ritter/E Kademan, M Meyer, DM Smith).
    R added in 1995 (Rossini/Maechler)
-   SAS: '94, Tom Cook ('92, John Sall, SAS).  Integrated '95-6, Rossini
-   Stata-mode: 1997, Thomas Lumley. Added 1997 (Rossini).
-   1997: last major restructuring (\`\`grand unification'')
-   2004: switch leaders: Maechler takes over