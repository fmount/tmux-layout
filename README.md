Tmux layout plugin
---

This is a tmux plugin that allow users to load a pre-written layout on the current window / pane
attached to the current session.


Configurable parameters
---

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
|MENU_KEY       | / | [leader]+[key] to run the menu on the left side of the window |
|LAYOUT_MENU_PREFIX  | @layout-menu | The default prefix of the metadata registered on the global tmux session |
|LOG_TARGET  | layoutplugin.log  | File name used by the logger (It logs by default in the /tmp/) |
|SESSION| 0  | Default session passed to the plugin|
|SIZE | 40 | % of menu size when window is splitted |


Manual install
---

Clone the repo:

    $ git clone https://github.com/fmount/tmux-layout ~/clone/path

Then simply go to the ~/clone/path/ and install all required python dependencies running:

    $ pip install -r requirements.txt

Add this line to the bottom of `.tmux.conf`:

    run-shell ~/clone/path/layout.tmux

Reload TMUX environment:

    # type this in terminal
    $ tmux source-file ~/.tmux.conf

You should now be able to use the plugin.


Install using tpm
----

Simply add to the tpm section of .tmux.conf:

    set -g @plugins 'fmount/tmux-layout'

Press `prefix` + <kbd>I</kbd> (capital I, as in **I**nstall) to fetch the plugin.

The plugin was cloned to `~/.tmux/plugins/` dir and sourced.

Go to the ~/.tmux/plugins/tmux-layout/ directory and install all required python dependencies
launching:

    $ pip install -r requirements.txt


[![asciicast](https://asciinema.org/a/dr3t2gb6h5f00vu2xo6bi0l0j.png)](https://asciinema.org/a/dr3t2gb6h5f00vu2xo6bi0l0j)


Where I can put my layouts?
---
Before start using this plugin there are just few things to consider:

In the layouts/ provided directory inside this package there are a couple of pre-defined templates to help user to understand how it works.
This path is called **layout\_home** and is defined in the **config/parameters.json** file.
Thus, looking at the directory tree of the plugin:

.
├── config
    └── parameters.json
├── docs
├── layouts
├── scripts
│   ├── dist
│   └── menu
│       ├── config -> ../../config
│       └── utils
└── test

Users can customize the layout_home and the others parameters just modifying the parameters.json file that come like this:


    {
        "globals": {
                "layout_home": "~/.tmux/plugins/tmux-layout/layouts/",
        "endpoint": "https://localhost:5444",
        "default_layout": "none",
        "default_session": "$0",
        "sleep": 5
      }
    }

Right now, the only parameter that is used is the layout_home, the others are intended for future
feature releases for this plugin (so please ignore those options).

License
---
[MIT](License)
