# ipython and jupyter startup file

Tired of importing the same thing over and over when starting a new notebook or ipython session?

taken from [this](https://towardsdatascience.com/how-to-automatically-import-your-favorite-libraries-into-ipython-or-a-jupyter-notebook-9c69d89aa343) article

# to use:

All `*.py` files in `~/.ipython/profile_default/startup/` are executed when new ipython kernel is started.  Symlink `start.py` into that folder ('Nix)

(from this directory)
`ln -s start.py ~/.ipython/profile_default/startup/start.py`
