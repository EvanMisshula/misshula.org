title: Python Dev Env
modifies: 2014-01-20
category: Tutorials
tags: Python, environments, virtualization, ubuntu
slug: python-dev-env
date: 2014-01-20 20:10:47
author: Evan Misshula
summary: Set up

# Ubuntu: Set up a virtual environment with IPython, numpy and pandas

So this is a much needed update for an earlier post on setting up a
virtual environment. The original post was based on one I found
[technomilk-setup](http://technomilk.wordpress.com/2011/07/27/setting-up-our-django-site-environment-with-pythonbrew-and-virtualenv/). My prior post is [mofj-setup](http://mofj.commons.gc.cuny.edu/2013/06/25/setting-up-a-virtual-environment-with-ipython-numpy-and-pandas/). Most of the time you
read about setting up virtual environments, it is in the context of
web development. But the same benefits hold for analysis and research
software. You want to be able to reproduce results. It also increases
security not to be adding all the unverified libraries with root level
privileges. This post is a minor modification of the outstanding
tutorial I have been using for the last few months. There are three
reasons why this needs to be updated:

1.  there is another version of python

2.  it does not cover IPython

3.  pythonbrew which managed the versions of python is longer maintained

    I will repeat the steps here. First install the c libraries that
    python needs to function.
    
    I use apt-get in ubuntu so type
    
        $ cd ~
        
        $ sudo apt-get install libsqlite3-dev libbz2-dev libxml2-dev libxslt-dev curl

## Get a non-system version of python.

Then install the pyenv scripts from source. Here is the link for
[pyenv](https://github.com/yyuu/pyenv#basic-github-checkout). Pyenv is in many ways more sophsticated than pythonbrew. It is
written in [bash](http://en.wikipedia.org/wiki/Bash_shell) not any particular version of python. The advantage is
that it is not dependent on anything in the language itself. The
disadvantage is that it is much harder to read the code and understand
the nature of a bug. One important trick is to turn on the `debug`
flag. As my advisor always used to tell me there was nothing more
brain-dead than a shell, I have spent most of my time avoiding them. I
use the Bourne Again Shell that comes with Ubuntu. The syntax is
tricky because everything is a string. Variable definitions can’t have
any spaces. There are some good tutorials which I will include
later. For now, here are three links that can tell you the differences
between bash and an interpreted language like Python.

1.  [python-bash](http://askubuntu.com/questions/110907/python****compared-to-bash)

2.  [when-to-use](http://superuser.com/questions/414965/when-to-use-bash-and-when-to-use-perl-python-ruby)

3.  [can-i-replace](http://stackoverflow.com/questions/209470/can-i-use-python-as-a-bash-replacement)

    I am assuming you have git installed. If not, [git-tutorial](https://www.digitalocean.com/community/articles/how-to-install-git-on-ubuntu-12-04) is a good
    tutorial for installing git.
    
        $ cd ~
        $ git clone git://github.com/yyuu/pyenv.git .pyenv
    
    Define environment variable `PYENV_ROOT` to point to the path where
    pyenv repo is cloned and add `$PYENV_ROOT/bin` to your `$PATH` for access
    to the pyenv command-line utility.
    
        $ echo ‘export PYENV_ROOT=”$HOME/.pyenv”‘ >> ~/.bashrc
        $ echo ‘export PATH=”$PYENV_ROOT/bin:$PATH”‘ >> ~/.bashrc
    
    Add pyenv init to your shell to enable shims and autocompletion. Shims
    and binstubs are worth knowing about.  You can read up on them
    [understand-shims](https://github.com/yyuu/pyenv#understanding-shims).
    
        $ echo ‘eval “$(pyenv init -)”‘ >> ~/.bashrc
    
    Restart your shell so the path changes take effect. You can now begin using pyenv.
    
        $ exec $SHELL
    
    Install Python versions into `$PYENV_ROOT/versions`. For example, to
    install Python 2.7.5, download and unpack the source, then run:
    
        $ pyenv install 2.7.5
        $ pyenv rehash
    
    And now we have to tell the system to use this new version of python
    
        $ pyenv local 2.7.5

## Install virtualenv

We are going to do two tricky things we are going to install
virtualenv in the version of python AND install the pyenv plugin virtualenv.

    $ pip install virtualenv

and to install the pyenv plugin.

    $ git clone git://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

You are now ready to create a virtual environment in a non-system version of python. I don’t understand why this will not work if you are anywhere else.

    $ pyenv virtualenv
    $ pyenv virtualenv 2.7.5 no-more-drug-war

We can list all of the virtual environments. Change directory to the
one you want to work in and in my case the virtual environment is
no-more-drug-war:

    $ pyenv activate no-more-drug-war:

We can list the virtualenvs:

\#+BEGIN<sub>SRC</sub> 
$ pyenv virtualenvs
dssg (created from /usr)
lc (created from /usr

# no-more-drug-war (created from /usr)

scrp (created from /usr)
seek (created from /usr)
\\#+END<sub>SRC</sub>

To review, we can activate the virtual environment with the following command.

    $ pyenv activate no-more-drug-war

You can deactivate the activate’d virtualenv by pyenv deactivate.

    $ pyenv deactivate

So, in order to know what packages we have installed at any time, we install yolk.

    $ pip install yolk

Do not type sudo! To see what it installed at any time:

    $ yolk -l

A list of further packages for IPython are available here. Type these individually and they each may take a few minutes to install.

    $ pip install jinja2
    
    $ pip install pyzmq
    
    $ pip install pygments
    
    $ pip install tornado
    
    $ pip install nose
    
    $ pip install numpy
    
    $ pip install scipy
    
    $ pip install matplotlib
    
    $ pip install pandas
    
    $ pip install ipython

Turning it on and off

Now to get out of your virtual environment, just type

    $ pyenv deactivate

To get back in, type:

    $ pyenv activate no-more-drug-war

Good luck!

I will try to send a pull request to add some of this to pyenv and
correct my question on stack overlfow.