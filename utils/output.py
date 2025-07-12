from rich import print
import csv

def print_result(results):
    if not results:
        print("[red] No hashes were cracked.[/red]")
    else:
        print("[bold green] Cracked Passwords:[/bold green]")
        for h, pw in results.items():
            print(f"[blue]{h}[/blue] → [yellow]{pw}[/yellow]")

def save_result(results, path="results.csv"):
    with open(path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Hash", "Password"])
        for h, pw in results.items():
            writer.writerow([h, pw])
