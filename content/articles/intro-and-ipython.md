title: Intro and iPython
date: 2013-01-02 21:05
author: emisshula
category: Tutorials
tags: Emacs, org-mode, reproducible research
slug: intro-and-ipython

So I was able to get this to post to my [blog](http://EvanMisshula.github.io). However I was not
able to get it to work here. Since then, to my surprise I have found
myself working less with the visually amazing, but temperamental iPython
and more with [Emacs org-mode](http://orgmode.org/).

The ability to toggle between thirty different languages and output to
html or LaTeX is pretty overwhelming. This is not to say that I have
had no trouble at all. Python sessions were broken for a
while. Overall it has been a pleasant experience. If you are
interested start with the article in [the Journal of Statistical
Software](http://www.jstatsoft.org/v46/i03/paper). But that is just the advertisement for what it can do. To
master the usage you should go to the [supplementary materials](http://www.jstatsoft.org/v46/i03). You can
download both the source code for the paper and the babel
library. None of this is behind a pay-wall.

Here are the tricks:

1.  The paper uses an initialization file, but you don't need to do
    that. I generally just put an elisp block in the paper and execute
    that.
2.  They defined a Journal of statistical software class to comply
    with formating requirement. You will generally just output to
    LaTeX.
3.  Any questions, just reach out to me on Twitter @emisshula