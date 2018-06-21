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
yarl-plot file [--component COMPONENT] [--mode MODE] [--host HOST] [--port PORT]
```

For example:

```bash
yarl-plot dqn_agent.py --component exploration --mode web
```

This will run a local webserver and open a browser window at http://localhost:8080 (default host and port) and
display the YARL metagraph.