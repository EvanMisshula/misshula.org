title: bugs-javascript 
date: 2015-03-07
author: emisshula
category: Tutorials
tags: Emacs, skewer-mode, javascript, d3.js, debugging
slug: skewer-tutorial

<p><img src="../../images/perlis.jpg" width="300px" alt="box" title="box"></p>

> When someone says: 'I want a programming language in which I need only
> say what I wish done', give him a lollipop. ~Alan J. Perlis

# The problem

Javascript can be notoriusly difficult to debug if you are coming from a language with tight 
degugger integration like C/C++ or Java.  Even if you are coming from other scripting languages
like R or Python. Peering into code running in the browser can be a real pain.  Now, I understand
that Firefox has firebug and Chrome has its own developer tools but I have never really felt 
comfortable in them.  I think it is becuase there graphical tools cover the entire screen and I
mostly develope on a laptop. (Think grad school, not Google.)

# Skewer Mode

Skewer mode is an amazing lightweight way to get debugging tools for Javascript into the editor
where you actually write the code.  Here is a link to the [youtube screencast](https://www.youtube.com/watch?v=4tyTgyzUJqM&feature=youtu.be).  The screencast has
no audio and while it shows the amazing things it can do, I had a very hard time reproducing it.

At the time of this writing it, (three years after its development) it has garnered 10 thousand 
views but few tutorials or stack overflow answers.  There are instructions in the [github repo](https://github.com/skeeto/skewer-mode). There
is also this [answer](http://emacs.stackexchange.com/questions/2376/how-to-use-skewer-mode) on emacs.stackexchange.com. 

# The setup

In order to set up skewer-mode, you technically only need httpd-simple server and js2 mode.  However,
when you are a beginner you really need auto-commplete and the snippets from YAS (yet another snippet 
library).  This marginally adds to the burden of set-up.  However, the major focus of this is set-up 
so I think it is worth it.  I am also including, R and ESS mode (Emacs-Speaks-Statistics).  I came to
javascript visualizations from static graphs in R.  I could have configured IPython as well and there is 
some benefit to showing the analogue but I have not done it for the time being.

The configuration file (known in the emacs world as .emacs, pronounced *dot emacs*) is available as a 
[gist](https://gist.github.com/EvanMisshula/e137e3dda382b8b1486d). To install packages, I am going to refer you to the excellent tutorial by Xah Lee available [here](http://ergoemacs.org/emacs/emacs_package_system.html).

# Modes

Skewer mode has two ways to operate.  Confusingly, these are also
called modes.  They are distinct from which functions are made
available in Emacs.  This is the primary definition of modes in
Emacs. The first of these is called automatic mode.  In the README
file of the [skewer mode repo](https://github.com/skeeto/skewer-mode) on github, automatic mode is outlined in
**Quick Start**.  If everything is properly configured you can find a
javascript file (using `C-x C-f`) and issue the command `M-x
run-skewer`.  Here the keystroke **Control-x** is abbreviated `C-x` and
the keystroke **Alt-x** si abbrevieated `M-x`. Let's review the
instructions in the README.

1.  Put this repository directory in your load-path
2.  Load skewer-mode.el
3.  `M-x run-skewer` to attach a browser to Emacs
4.  From a js2-mode buffer with skewer-mode minor mode enabled, send
    forms to the browser to evaluate

## Details on step 1

You want to have all of the requisite packages installed and
configured correctly.  If you get any error on start up, you have to
correct it before attempting to start skewer mode.  This is what an
error might look like.

<p><img src="../../images/startErr.png" width="550px" alt="err" title="startErr"></p>

## Details on step 2

Loading skewer-mode.el should occur in the .emacs file.

    (add-to-list 'load-path 
    "/Users/emisshula/.emacs.d/elpa/skewer-mode-20141215.1525")
    (require 'skewer-mode)
    (add-hook 'js2-mode-hook 'skewer-mode)
    (add-hook 'css-mode-hook 'skewer-css-mode)
    (add-hook 'html-mode-hook 'skewer-html-mode)

## Details on step 3

For this step you can just follow the instruction:

1.  `M-x run-skewer` to attach a browser to Emacs

This won't show anything in the browser but you can interact with the browser
through Emacs. What should happen is that your computer will switch focus to
the browser and it will open a blank tab with address 127.0.0.1:8080/skewer/demo
See the picture of my Safari browser below:

<p><img src="../../images/emptyTab.png" width="550px" alt="emptyTab" title="emptyTab"></p>

It is not very informative but at least when you see it, you won't be surprised.

## Details on step 4

1.  From a js2-mode buffer with skewer-mode minor mode enabled, send
    forms to the browser to evaluate

This is what is done in the first 2 minutes of the demo.  In order to
see if this is working you must pay attention to the bottom of the
screen. The second to last line is called the mode-line. It displays
information about the file.  At a minimum, the file name and what line
the cursor. To the right in parentheses are the modes of the file.
These modes dictate what functions are available for editing.  It will
be easier to edit a Python file in python-mode, a C file in c-mode, an
elisp file in lisp mode.  Well for skewer mode to work, you have to be
in js2 major mode and skewer minor mode.

<p><img src="../../images/checkModes.png" width="550px" alt="checkModes" title="checkModes"></p>

In the picture above in parentheses it says both Javascript-IDE and
skewer, this means that we are in the right modes.  Unfortunately, js2
is both not the only javascript mode and not the default mode for
javascript in Emacs.  Regular javascript mode was written before
Google made the V8 javascript API available so if your mode line does
not have IDE in it you are probably in Javascript mode and skewer mode
won't work.  When you try to execute a statement, you will get an
error that **no javascript AST is available**.  AST stands for Abstract
Syntax Tree and the communication to the V8 api is performed only by
js2-mode, not the javascript mode.

Well assuming now that you have checked your mode line you can execute the 
simple javascript statements.  Just put the cursor after the semi-colon and 
press `C-x C-e` (Control x Control e).

    Math.pow(3,14.1);
    
    var x = { foo: "Hello, World" };
    
    x.foo += '!';
    
    Math.floor( Math.random() * 6000);
    
    x.foo;

The first one will print the answer in the last line of Emacs. This is
called the mini-buffer. The definition of x as a key-value pair will
return undefined, but that is OK.  The third statement appends an
exclamation point to the value of `x.foo`.  The fourth statement uses
the javascript Math library. The final statement prints the value of the foo
property of x in the mini-buffer.

If you made this much work. Swagger over to the bar and:

**Buy yourself a drink!**

# More in quick mode

The second demo file in the shows that in skewer-mode you can define a function and apply it 

    function square(n) {
        return n * n;
    }
    
    square(14.4);
    
    [1,3,5,7,21].map(square);

In the above code snippet, I follow the video but add the function being applied to an array via
the map method.  The results are all printed in the mini-buffer. Now in demo3.js, skeeto shows 
the invocation of the skewer-repl. A repl is *Read-Evaluation-Print-Loop* also called a shell or 
console. In R, the repl is called the R console and it is an essential part of buiding programs and 
performing analusis. In Python, the repl of choice is the extremely popular IPython.  Here is an 
example of a complicated graph drawn using the repl.

    # data 
    set.seed(4566)
    data <- rnorm(100)
    
    # layout where the boxplot is at top  
    nf <- layout(mat = matrix(c(1,2),2,1, byrow=TRUE),  height = c(1,3))
    par(mar=c(3.1, 3.1, 1.1, 2.1))
    boxplot(data, horizontal=TRUE,  outline=TRUE,ylim=c(-4,4), frame=F, col = "green1")
    hist(data,xlim=c(-4,4), col = "pink")
    
    # layout boxplot is at the bottom 
    nf <- layout(mat = matrix(c(1,2),2,1, byrow=TRUE),  height = c(3,1))
    par(mar=c(3.1, 3.1, 1.1, 2.1))
    hist(data,xlim=c(-4,4), col = "pink")
    boxplot(data, horizontal=TRUE,  outline=TRUE,ylim=c(-4,4), frame=F, col = "green1", width = 10)

<p><img src="../../images/histBox.jpeg" width="450px" alt="histBox" title="histBox"></p>

If we want to examine the first 5 rows of data we can send it to the console as seen here:

<p><img src="../../images/RconsoleData.png" width="550px" alt="RconsoleData" title="RconsoleData"></p>

# Demo3

It is also possible to send data to the javascript repl.  Although we have to wrap
it in the `skewer.log()` function.  The first step is to open the skewer-repl with the command
`M-x skewer-repl`. (This is also bound to the keys `C-c C-z`.) From a file a
javascript file which we have named demo3.js to match the movie, we place the 
cursor immediately after the semi-colon in either statement:

    skewer.log(" 5 + 6 =" + (5+6));
    skewer.log("Hello, World");

Now instead of writing to the mini-buffer it is writing to the repl,
just like we can do in R or Python. Here is a picture.

<p><img src="../../images/demo3Res.png" width="550px" alt="demo3Res" title="demo3Res"></p>

# Manual

We can also insert live changes in the browser for a page we are developing.  However, the set
up changes as now use manual mode.  Again, here are the directions and we will add some detail.

1.  Load the dependencies
2.  Load skewer-mode.el
3.  Start the HTTP server (httpd-start)
4.  Include "<http://localhost:8080/skewer>" as a script (see example.html and check your httpd-port)
5.  Visit the document from your browser

We will break these down step by step.

## Details on step 1 and 2

1.  Load the dependencies
2.  Load skewer-mode.el

This should happen when start up Emacs if you made the first part work.

## Details on step 3

1.  Start the HTTP server (httpd-start)

It is important to note that you do not use `skewer-run`.  You start
the server in the directory that you want to serve.  Many books on
d3.js recommend this and have you use the python simple server. We are
going to have Emacs the page. The next code snippet is not something
you should use here, it is just an example of another simple web
server that serves a directory to localhost.

    python -m SimpleHTTPServer 8000

Although, if you have configured the direcory you want to run in your
.emacs file you can run `httpd-start`, I prefer not to rely on the
configuration.  An example of the configuration appears below:

    (setq httpd-root "/Users/emisshula/Documents/skewerDemo/boid-js")

Instead I prefer to use the command: `M-x httpd-serve-directory` so I am 
sure that I know what directory is being served and on what port. 

This bleeds a little into step 4 but I really like understanding what
my server is doing on my machine.  In fact, for debugging one other
command line tool that I find useful is `nmap` which can tell you what
ports are open.  If you are on unix variant machine (sometimes denote
\*nix), you can just take the version from your package manager.

For Mac, use [brew](http://brew.sh):

    brew install nmap

For Debian, Ubuntu:

    sudo apt-get install nmap

For Windows, download all of [CygWin](https://www.cygwin.com) (so you can forget you are even on a Windows box). To 
check the server has started:

    nmap -p 8080 localhost

The results of which will look like:

    Starting Nmap 6.47 ( http://nmap.org ) at 2015-03-08 09:30 EDT
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.00015s latency).
    PORT     STATE SERVICE
    8080/tcp open  http-proxy
    
    Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds

Now stop that server, using `httpd-stop`. Then you can clone Chris Wellon's [boids-js](https://github.com/skeeto/boids-js) repo. Try
restarting the server by pointing it at that directory. 

## Details on step 4

1.  Include "<http://localhost:8080/skewer>" as a script (see
    example.html and check your httpd-port)

Now examine the head of `example.html`.

    #+BEGIN_MARKDOWN 
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8"></meta>
            <title>Boids</title>
            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
            <script type="text/javascript" src="http://localhost:8080/skewer"></script>
               <script src="boids.js"></script>
          </head>
          <body style="background: darkgray; text-align: center;">
            <canvas id="canvas" width="640" height="640"
                    style="position: absolute; left: 0; top: 0;">
            </canvas>
          </body>
        </html>
    #+END_MARKDOWN

I have added a meta tag so that you won't get any inconsequential errors complaining that we have
not specified the charset.  The first script tag calls `jquerey`, a very popular cross browser
library.  Skewer-mode used to depend on jquerey but that dependency has been removed.  However,
code that we are running in this example does have the dependency so it can't be removed. The 
script's source is on a website `ajax.googleapis.com` so we have to be connected to the internet
to run this demo.  The prior ones would work on our subway commute.  They only relied on our local 
files and server.  Web pages can load javascript from a variety of different sources.  These include
different sites and local files. 

The second script is a local script.  It is running on our localhost at port 8080.  This is why
you can't start this with some other local webserver. Emacs knows about both files in the local 
directory and what to do with skewer. In fact, we are serving both example.html and skewer on the 
same port.  This is very different than if you have ever served a [leaflet.js](http://leafletjs.com/examples.html) map embeded in an
html page.  In that case, you serve the page on one port and the map tiles on another.

The third script, is the script that defines the \`\`boids'' and their motion.

## Details on the fifth step

1.  Visit the document from your browser

In the address bar put `http://localhost:8080/example.html`. Split
your screen between your browser and emacs so that you can see both
and little else. To change the size of the birds, go to line 9 of
`boids.js` and replace 6 with 2.  Now put the cursor after the
semi-colon and press `C M x` which is bound to the command
`skewer-html-eval-tag`.  The size of the \`\`boids'' should change
instantly.

# Evaluating a new file

In demo4.js Chris Wellon's adds a new javascript file which was not loaded when the browser visited
`example.html`.  He does this to experiment with assigning random colors to the boids. Here he
needs to change the boids.js script to load a random color.  He changes line 16 from 

    ctx.fillStyle = 'blue';

to:

    ctx.fillStyle = this.color;

After, you make the change put the cursor after the semi-colon next to `this.color;` and evaluate the 
tag (`C M x`). Don't worry if the page goes blank remember you have not yet defined `this.color`.
We define those random colors in demo4.js:

    for (var i = 0; i < swarm.boids.length; i++) {
        swarm.boids[i].color = '#' + Math.floor( Math.random() * 0xfff);
    }

Now demo4.js needs to be loaded into the example.html page.  This is
done with `C-c C-k` (control-c, control-k).

The boids change colors.  Everything else is a variation on this
theme.  I may add later more later but this should get you debugging
javascript.