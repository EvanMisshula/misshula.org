title: Emacs dies on popup
date: 2014-12-27
author: emisshula
category: Tutorials
tags: Emacs, homebrew, Mac, OS X, Mavericks, Darwin
slug: death-by-pop-up

# Switched to Mac

My switch to the Mac meant that I was making more typing mistakes and on one 
them I was always getting to Emacs to freeze.  I looked like this:

<p><img src="../images/Computer-Freezes.jpg" width="450px" alt="img" title="Computer-Freezes.jpg"></p>

I switched to the Mac last summer.  I was given one for work.  I would 
never buy one because they put corporate [malware](https://defectivebydesign.org/apple) on your machine.  However,
it is convenient to have one because I can test my tutorials on this machine.

Mac does not support a package manager to manage free software which
people install on the Mac.  So there is a community based one called
homebrew through which I installed Emacs.  I started switching between
my Linux laptop and my Mac.  Almost immediately, I ran across a bug.
When I typed Command-p on the Mac instead of M-p, a popup appeared and
asked if I wanted to print.  This happened often because of the different
layouts of the two keyboards.

I could not dismiss the popup.  The only way to continue working was to 
force-quit Emacs and lose my unsaved work.

I finally found the right answer [here](http://superuser.com/questions/125569/how-to-fix-emacs-popup-dialogs-on-mac-os-x).  Unfortunately, I don't have the 
points on SuperUser to vote it up.  The solution is:

    (defadvice yes-or-no-p (around prevent-dialog activate)
      "Prevent yes-or-no-p from activating a dialog"
      (let ((use-dialog-box nil))
        ad-do-it))
    (defadvice y-or-n-p (around prevent-dialog-yorn activate)
      "Prevent y-or-n-p from activating a dialog"
      (let ((use-dialog-box nil))
        ad-do-it))

The two functions are almost the same.  One takes care of \`\`yes or no'' and the other \`\`y or n''.