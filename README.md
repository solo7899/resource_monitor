# Resource Monitoring Terminal App

A simple terminal-based resource monitor built with Python, [psutil](https://pypi.org/project/psutil/), and [Rich](https://rich.readthedocs.io/). It displays real-time CPU and memory usage with percentage bars, and lists the top memory-consuming processes.

## Features

- **Live CPU and Memory Usage:**
  Visual percentage bars for CPU and memory usage, updated every second.
- **Top Processes Table:**
  Shows the most memory-intensive processes, including PID, name, memory %, and CPU %.
- **Responsive Layout:**
  Adapts to your terminal size using Rich's layout system.

## Requirements

- Python 3.7+
- [psutil](https://pypi.org/project/psutil/)
- [rich](https://pypi.org/project/rich/)

## Installation

```sh
pip install psutil rich
```

## Usage

```sh
python resource_mon.py
```

Press `Ctrl+C` to exit.

## Screenshots

```
+------------------------ Resource Monitor ------------------------+
| +----------- System Resource Usage -----------+                 |
| | CPU Usage:    12.34%  ████████............ |                 |
| | Memory Usage: 45.67%  ███████████......... |                 |
| +--------------------------------------------+                 |
| +-------------- Top Processes ---------------+                 |
| | PID   Process Name   Memory %   CPU %      |                 |
| | ...   ...            ...        ...        |                 |
| +--------------------------------------------+                 |
+---------------------------------------------------------------+
```

---

_Made with [Rich](https://github.com/Textualize/rich) and [psutil](https://github.com/giampaolo/psutil)_
