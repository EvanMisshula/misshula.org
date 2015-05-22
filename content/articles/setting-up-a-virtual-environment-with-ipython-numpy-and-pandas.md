title: Setting up a virtual environment with Ipython, numpy and pandas
date: 2013-06-25 00:56
author: emisshula
category: Tutorials
tags: Emacs, IPython, virtual env, linux
slug: setting-up-a-virtual-environment-with-ipython-numpy-and-pandas

Most of the time you read about setting up virtual environments, it is
for web development. But the same benefits hold for analysis and
research software. You want to be able to reproduce results. It also
increases security not to be adding all the unverified libraries with
machine level privileges. This post is a minor modification of the
[outstanding-tutorial](http://technomilk.wordpress.com/2011/07/27/setting-up-our-django-site-environment-with-pythonbrew-and-virtualenv/) I have been using for the last few months. Since
it is two years old, there is another version of python and it does
not cover [IPython](http://ipython.org/), I will repeat the steps here.

# First install Pythonbrew and another version of python

I use apt-get in ubuntu so type

    $ cd ~
    
    $ sudo apt-get install libsqlite3-dev libbz2-dev libxml2-dev libxslt-dev curl

Then get pythonbrew:

    $ ``curl -kL http://github.com/utahta/pythonbrew/raw/master/pythonbrew-install | bash``

This line gets the repository and executes through bash. We will need
to modify the configuration file for bash.

    $ echo "source $HOME/.pythonbrew/etc/bashrc" >> ~/.bashrc

Don't forget the dot in `.bashrc`. Now nothing changes until this file is
executed by the operating system:

    $ source .bashrc

This should complete with no errors. The next step is to install python
2.7.3. It is going to take a few minutes to complete.

    $ pythonbrew install --verbose 2.7.3

And now we have to tell the system to use this new version of python

    $ pythonbrew use 2.7.3

# Install virtualenv and virtualenvwrapper

We have to install virtualenv in the system's python and
virtualenvwrapper in the new python.

    $ sudo apt-get install python-virtualenv
    
    $ pip install virtualenvwrapper

The first line only needs to be executed once. It works for the whole
system. The second one needs to be done for each new python environment
you create. Make a hidden directory to hold the virtual environments.

    $ mkdir ~/.virtualenvs

Add the following three lines at the end of your .bashrc.

    export WORKON_HOME=$HOME/.virtualenvs``
    export VIRTUALENVWRAPPER_PYTHON=$HOME/.pythonbrew/pythons/Python-2.7.3/bin/python``
    source $HOME/.pythonbrew/pythons/Python-2.7.3/bin/virtualenvwrapper.sh``

You will need to use an editor. Then you have to reload them:

    $ source .bashrc

# Create the virtual environment

To create a virtual environment called 'no-more-drug-war', type:

    $ mkvirtualenv --no-site-packages no-more-drug-war

# Important libraries

---

So, in order to know what packages we have installed at any time, we
install yolk.

    $ pip install yolk

Do not type sudo! To see what it installed at any time:

    $ yolk -l

A list of further packages for IPython are available [here](http://ipython.org/ipython-doc/stable/install/install.html).
Type these individually and they each may take a few minutes to install.

    $ pip install pyzmq
    
    $ pip install pygments
    
    $ pip install tornado
    
    $ pip install nose
    
    $ pip install numpy
    
    $ pip install scipy
    
    $ pip install matplotlib
    
    $ pip install pandas

# Turning it on and off

Now to get out of your virtual environment, just type

    $ exit

To get back in, type:

    $ workon no-more-drug-war

Good luck!