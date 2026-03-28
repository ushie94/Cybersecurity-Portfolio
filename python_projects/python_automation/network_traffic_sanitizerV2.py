import time
from rich.console import Console
from rich.table import Table
from rich.progress import track

# Initialize Rich Console
console = Console()

def validate_and_categorize(ip_list):
    # Create the Rich Table
    table = Table(title="🛡️ SOC Laboratory: Network Traffic Sanitizer V2.0", 
                  caption="Rule of 255 Enforcement Active",
                  show_header=True, 
                  header_style="bold magenta")

    table.add_column("Index", justify="right", style="dim", width=6)
    table.add_column("IP Address", style="cyan", width=20)
    table.add_column("Classification", justify="center")
    table.add_column("Status", justify="left")

    # Simulate a "Scan" process with a progress bar
    for i, ip in enumerate(track(ip_list, description="[bold green]Analyzing Traffic...")):
        time.sleep(0.2)  # Just for visual effect in the terminal
        
        try:
            parts = ip.split(".")
            
            # The "Rule of 255" Logic
            is_valid = (
                len(parts) == 4 and 
                all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
            )

            if not is_valid:
                status = "[bold red]❌ INVALID DATA[/]"
                category = "N/A"
            elif ip.startswith("192.168") or ip.startswith("10."):
                status = "[green]✅ ALLOWED[/]"
                category = "INTERNAL"
            else:
                status = "[yellow]🔍 MONITOR[/]"
                category = "EXTERNAL"

            table.add_row(str(i+1), ip, category, status)

        except Exception as e:
            table.add_row(str(i+1), ip, "ERROR", f"[red]System Failure: {e}[/]")

    # Print the finished table to the console
    console.print("\n", table)

# Data from your GitHub commit
ip_addresses = [
    "192.168.1.1", "10.0.0.1", "8.8.8.8", 
    "192.168.1.256", "256.0.0.1", "172.16.0.1", 
    "192.168.1", "192.168.1.1.1", "not_an_ip"
]

if __name__ == "__main__":
    validate_and_categorize(ip_addresses)