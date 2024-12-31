# VF-1

VF-1 is a command line client for the Gopher protocol, written in Python and
released under the BSD 2-Clause License.  It features a unique and minimalistic
user interface designed to facilitate rapid keyboard-driven navigation of
Gopherspace.  It boasts world-beating support for non-ASCII charactersets and
ANSI colour codes, as well as experimental support for Gopher over TLS.

By design, VF-1 consists of a single file, vf1.py, and has no mandatory
dependencies beyond the Python standard library (although the `chardet` library
will be used opportunistically if installed).

VF-1 naturally has
[its own Gopherhole](gopher://zaibatsu.circumlunar.space:70/1/~solderpunk/vf-1).
You can use VF-1 (or any other Gopher client!) to access ASCII-formatted
versions of the VF-1 man pages there.

The source code lives in a
[git repo hosted at Sourcehut](https://git.sr.ht/~solderpunk/VF-1).

The repository contains the following files (plus some development / packaging
related noise):

* LICENSE - text of BSD 2-Clause License
* README.md - the README file you are currently reading
* vf1-tutorial.7 - troff source for the vf1-tutorial(7) man page
* vf1.1 - troff source for the vf1(1) man page
* vf1.py - Python source for VF-1 itself

VF-1 was developed by Solderpunk with substantial contributions from Alex
Schroeder (aka Kensanata) and little bits of help from a few other helpful
Gopherspace folk.  See the top of the vf1.py source file for all contributors.
