import time
import psutil

from rich.bar import Bar
from rich.console import Console
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel

def get_usage(interval=1):
    """Get CPU and memory usage."""
    cpu_usage = psutil.cpu_percent(interval=interval)
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage, memory_usage

def get_top_processes(n=8):
    """Get the top n processes by MEMORY usage."""
    all_processes = list(psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']))
    for p in all_processes:
        try:
            p.cpu_percent(interval=None)
        except psutil.NoSuchProcess:
            continue

    time.sleep(0.1)
    

    processes = [(p.info['pid'], p.info['name'], p.info['memory_percent'], p.info['cpu_percent']) 
                 for p in all_processes]
    processes.sort(key=lambda x: x[2], reverse=True)
    return processes[:n]

def display_usage_panel():
    """Create a panel displaying CPU and memory usage."""
    cpu, memory = get_usage()
    panel_content = f"\nCPU Usage: {cpu:5>.2f}%\n{"".join(['|' if i < cpu%100 else '.' for i in range(100)])}\n\nMemory Usage: {memory:.2f}%\n{''.join(['|' if i < memory%100 else '.' for i in range(100)])}\n"
    return Panel(panel_content, title="System Resource Usage", border_style="blue", height=10)

def display_processes_table():
    processes = get_top_processes()
    panel_content = ""
    panel_content += f"{'PID':<8}\t{'Process Name':<20}\t{'Memory %':>10}\t{'CPU %':>10}\n"
    for p in processes:
        panel_content += f"{p[0]:<8}\t{p[1][:17]:<17}{'...' if len(p[1]) > 17 else '':<3}\t{p[2]:>6.2f} %\t{p[3]:>9.2f}%\n"
    return Panel(panel_content, title="Top Processes", border_style="blue", height=10)

def display_usage_and_processes():
    layout =Layout()
    layout.split_column(
        Layout(display_usage_panel()),
        Layout(display_processes_table())
    )
    return Panel(layout, title="Resource Monitor", border_style="green", height=25)

if __name__ == "__main__":
    console = Console()
    try:
        console.clear()
        psutil.cpu_percent(interval=None)
        with Live(display_usage_and_processes(), console=console, refresh_per_second=1) as live:
            while True:
                live.update(display_usage_and_processes())  
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)