import psutil

def get_usage(interval=1):
    """Get CPU and memory usage."""
    cpu_usage = psutil.cpu_percent(interval=interval)
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage, memory_usage

def get_top_processes(n=5):
    """Get the top n processes by MEMORY usage."""
    processes = [(p.info['pid'], p.info['name'], p.info['memory_percent'], p.info['cpu_percent']) 
                 for p in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent'])]
    processes.sort(key=lambda x: x[2], reverse=True)
    return processes[:n]

if __name__ == "__main__":
    while True:
        cpu, memory = get_usage()
        print(f"CPU usage: {cpu}%, Memory usage: {memory:.2f}%")

        top_processes = get_top_processes()
        print("Top processes by CPU usage:")
        for process in top_processes:
            print(f"PID: {process[0]}, Name: {process[1]}, RAM usage: {process[2]:.2f}%, CPU usage: {process[3]:.2f}%")
        print("\n=======================================================\n")