title: Resources on Django and D3
date: 2013-04-02 11:27
author: emisshula
category: Tutorials
tags: D3, Django, linux
slug: resources-on-django-and-d3

It is no secret that I have been working on delivering d3 over django.
I am a novice to both of these technologies, I have been scouring the
internet for FREE resources. Of what I have found. Here are my
impressions. On Django, there seem to be few full tutorials analogous
to [Michael Hartle's book](http://ruby.railstutorial.org/ruby-on-rails-tutorial-book). However what there is works. The early
version's of Michael's book were hell if you did not have the latest
$2,500 Mac. The Django \`official tutorial [official tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) was
manageable. It should really spend time telling you to set up a
virtual environment but you can find that material in [Technomilk](http://technomilk.wordpress.com/2011/07/27/setting-up-our-django-site-environment-with-pythonbrew-and-virtualenv/).
There is also a very good [book](http://www.amazon.com/Practical-Django-Projects-Pratical/dp/1590599969) by John Bennett of Django's main
authors but is behind a pay-wall. The reason that I am switching to
django is that there is a growing number of resources for [scientific
computation](http://www.amazon.com/Scientific-Programming-Computational-Science-Engineering/dp/3642302920) (apologies, this is behind a pay-wall) in python. I
believe that it will emerge as a successor to the R statistical
language. If you are still using R, you should check out [IPython](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html),
[Pandas](http://pandas.pydata.org/), [NumPy](http://www.numpy.org/) and [SciPy](http://www.scipy.org/). Also I have not finished them, but there is
another FREE (video) tutorial, [Getting Started with Django](http://gettingstartedwithdjango.com/en/lessons/introduction-and-launch/#toc0), for after
you have finished the official one.

The other great strength of R is its graphics, both the base graphics
and [ggplot](http://ggplot2.org/). (Truth be told, I found that indecipherable without the
companion [book](http://www.amazon.com/ggplot2-Elegant-Graphics-Data-Analysis/dp/0387981403), which is of course behind a pay-wall.) However as data
presentation evolves from static graphs to user interfaces, we need to
move to tools like [D3.js](http://d3js.org/) which allow us to create graphs from html
styling elements. These are also called svg or css graphics. Right now
there are only two books on the subject. Mike Dewar's [Getting Started
with D3](http://shop.oreilly.com/product/0636920025429.do) and Scott Murray's [Interactive Visualization for the
Web](http://shop.oreilly.com/product/0636920025429.do). Mike's book is strictly limited to D3 and was hard for me to get
a clear idea of what is going on because of my own limitations in HTML
and CSS. Both books say that they are only going to explain D3 but
Murray's book and free [tutorials](http://ofps.oreilly.com/titles/9781449339739/_introduction.html) explains more of the
background. making it easier to understand what is happening. There
are more small examples so you can draw circle or rectangle before you
draw a scatter plot. Both [Mike's](https://github.com/mikedewar/getting_started_with_d3) and [Scott's](https://github.com/alignedleft/d3-book) book make a github
repository available so you can see full examples of what is in the
text. With Mike's book some of what is in the repository is different
than what is printed in the text. This is particularly frustrating on
the Subway wait user interface. This is not to trash Michael's book. I
at least understood something after reading it. Looking at the
documentation from M Bostock made me feel like a complete idiot.