YARL metagraph plotting utility
===============================

This utility can be used to plot yarl metagraphs.

*Work In Progress.*

## Installation

Install from PyPI (yet to come):

```bash
sudo python3 -m pip install yarl-plot
```

Install from git:

```bash
git clone https://github.com/YARL-project/yarl-plot
cd yarl-plot
sudo python3 -m pip install -e .
```

## Usage

```bash
yarl-plot [--listen] [--token TOKEN] [--file FILE] [--component COMPONENT] [--mode MODE] [--host HOST] [--port PORT]
```

For example:

```bash
yarl-plot --file dqn_agent.py --component exploration --mode web
```

This will run a local webserver and open a browser window at http://localhost:8080 (default host and port) and
display the YARL metagraph.

Other examples:

```bash
yarl-plot --listen
```

This allows you to use `yarl.utils.visualization_util.send_graph_markup()` to send the graph markup to the local
webserver and display the current component. Use this for pseudo-interactive development.
