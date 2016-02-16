title: Learning environments for data analysis software
date: 2013-02-02 23:32
author: emisshula
category: Tutorials 
tags: configuration, docview, emacs, internet pedagogy, linux, statistics, windows
slug: learning-environments-for-data-analysis-software

# Welcome to my blog

This is my first blog post using the IPython notebook. I am very excited
about the things it can do. 

## Here is what I want to cover

1.  Who I am
2.  What the blog will cover
3.  Why I named it Measure of Justice

# Evan Misshula

I am a PhD student in Criminal Justice. I try to use social networks and
data mining to help people make rational decisions about public safety.
I care passionately about people that the world writes off. It is no
shock. There have been many times when I have been written off.

# Math, Computing, Causality, Networks, Security and Ethics

Early in my graduate career, I was struck that we spend a great deal of
effort policing minority communities for drug use which has little
effect on the non-involved but spend way less effort protecting the
banking system from hackers. I also thought that there was a lot to
learn about managing threats from inside by looking at both intrusion
detection and counter- intelligence. Not suprisingly, I believe in
second chances. Who gets those chances and when they come are an area of
great interest.

# What's in a name?

When I studied Stochastic Control, Girsanov's Theorem governed which
measures were deformable into each other. Two measures needed to have
the same sets of measure zero, to equivilent. In other words it is
what we think that is impossible, not unlikely that is important.

# My favorite new toy

I am excited about blogging again because I can now put code and math in
the blog. I have spent a lot of time in graduate school learning new
tools. This blog will hopefully document some of the challenges and help
others find their way. Others blogs have certainly helped me.

We can assign variables in the ipython notebook.

    a=5
    print a

    5

    a=5
    b=9 a+b

But you can also reach into the operating system and execute bash
commands.

    pwd

    u'/home/evan/Documents/ipython/blog/blog'

    ls

    cp 120907-Blogging with the IPython Notebook.ipynb EvanNB1.html old/
    cp 121120-Back from PyCon Canada 2012.ipynb EvanNB1.ipynb EvanNB1_header.html fig/

# This is a markdown cell

You can *italicize* and use **boldface**. It allows us to comment code
and create interactive presentations. You can build lists of your
favorite tools. Here are mine.

-   linux
-   emacs
-   r statistical language
-   Emacs Speaks Statistics
-   Org-mode
-   LaTeX
-   Sweave
-   Ggplot

What is most important is to LaTeX support. My favorite math equation
is \[ e^{i\\pi}+1=0 \]. It can also render math numbered equations:

# The browser displays

The program can display the numeric or character output of programs.

    print "hi Doug"
    x=3

    hi Doug

    x

    3

It can also display graphs:

    %pylab inline
    plot(rand(100))

    Welcome to pylab, a matplotlib-based Python environment [backend: module://IPython.zmq.pylab.backend_inline].
    For more information, type 'help(pylab)'.

    x = linspace(0, 3*pi)
    plot(x, 0.5*sin(x), label=r'$\sin(x)$') plot(x, cos(x), 'ro', label=r'$\cos(x)$') title(r'Two familiar functions')
    legend()

# Symbolic Manipulation

The IPython notebook can also make symbolic calculations and solve
complex algebraic equations:

    %load_ext sympyprinting import sympy as sym
    from sympy import *
    x, y, z = sym.symbols("x y z")

    The sympyprinting extension is already loaded. To reload it, use:
    %reload_ext sympyprinting

    eq = ((x+y)**3 * (x+3)) eq

    \\left(x + 3\\right) \\left(x + y\\right)^{3}

    expand(eq)

Ipython can even calculate the derivative!!

    diff(cos(x**2)**2 / (1+x)**2, x)

It can also display pictures and videos&#x2026;

    from IPython.display import Image
    Image(filename='/home/evan/Pictures/Evan.jpg')

<p><img src="../images/Evan.jpg" width="300px" alt="img" title="Evan"></p>

    from IPython.display import YouTubeVideo
    YouTubeVideo('ystkKXzt9Wk')

<iframe width="560" height="315" src="//www.youtube.com/embed/ystkKXzt9Wk" frameborder="0" allowfullscreen></iframe>

# We can even use other languages (including R)!!

This is because ipython communicates between the kernel and the
browser so it knows how to send data to another interpreter.

So we can process code from Ruby:

    %%ruby puts "Hello from Ruby #{RUBY_VERSION}"

    Hello from Ruby 1.9.3

We can run bash scripts:

    %%bash echo "hello from $BASH"

    hello from /bin/bash

We can interact with an R environment:    

    import rpy2;
    from rpy2 import robjects; robjects.r("version")

    platform x86_64-unknown-linux-gnu
    arch x86_64
    os linux-gnu
    system x86_64, linux-gnu
    status
    major 2
    minor 15.2
    year 2012
    month 10
    day 26
    svn rev 61015
    language R
    version.string R version 2.15.2 (2012-10-26)
    nickname Trick or Treat

    %load_ext rmagic

    The rmagic extension is already loaded. To reload it, use: %reload_ext rmagic

We can return R objects to python

    X = np.array([0,1,2,3,4]) Y = np.array([3,5,4,6,7])
    %%R -i X,Y -o XYcoef
    XYlm = lm(Y~X)
    XYcoef = coef(XYlm)
    print(summary(XYlm))
    par(mfrow=c(2,2))
    plot(XYlm)

    Call:
    lm(formula = Y ~ X)
    
    Residuals:
    1 2 3 4 5
    -0.2 0.9 -1.0 0.1 0.2
    
    Coefficients:
    Estimate Std. Error t value Pr(>|t|)
    (Intercept) 3.2000 0.6164 5.191 0.0139 *
    X 0.9000 0.2517 3.576 0.0374 *
    ---
    Signif. codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
    
    Residual standard error: 0.7958 on 3 degrees of freedom
    Multiple R-squared: 0.81,   Adjusted R-squared: 0.7467
    F-statistic: 12.79 on 1 and 3 DF, p-value: 0.03739

There is more to come. Ipython does d3 interactive graphs but I have
not been able to get them to work. It also handles cython (python
wrapped c-code) and mpi parallel code. More later. It is time for bed.