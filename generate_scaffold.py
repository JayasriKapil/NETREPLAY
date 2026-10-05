import os
import sys

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '')

files = {
    'netreplay/__init__.py': '',
    
    'netreplay/__main__.py': '''
import sys
from netreplay.cli import main
if __name__ == "__main__":
    sys.exit(main())
''',

    'netreplay/ui.py': '''
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.layout import Layout

console = Console()
plain_mode = False

def init_ui(plain=False):
    global plain_mode, console
    plain_mode = plain
    if plain:
        console = Console(color_system=None, force_terminal=False)

def print_header(title, device="PHONE"):
    """Stage header."""
    text = f" {title} "
    device_label = f"[{device}]"
    
    if plain_mode:
        print(f"\{'='*50}")
        print(f"{device_label} {title}")
        print(f"CONCEPT PROTOTYPE - all network data simulated")
        print(f"{'='*50}\")
    else:
        console.print()
        console.print(Panel(
            Text("CONCEPT PROTOTYPE - all network data simulated", style="dim italic"),
            title=f"[bold cyan]{text}[/bold cyan] [bold yellow]{device_label}[/bold yellow]",
            title_align="left",
            border_style="blue"
        ))
        console.print()
''',

    'netreplay/cli.py': '''
import argparse
import sys
import time
from netreplay.ui import init_ui, print_header, console

def demo_command(args):
    stages = [
        (0, "Title card", "LAPTOP"),
        (1, "The problem", "LAPTOP"),
        (2, "Architecture", "LAPTOP"),
        (3, "Capture", "PHONE"),
        (4, "Voice stamp", "PHONE"),
        (5, "Office Kit hand-off", "OFFICE KIT"),
        (6, "Autopsy", "LAPTOP"),
        (7, "Explanation + fix", "LAPTOP"),
        (8, "Replay", "PHONE"),
        (9, "Verify", "LAPTOP"),
        (10, "India profiles + resilience matrix", "LAPTOP"),
        (11, "Scenario gallery", "LAPTOP"),
        (12, "Regression test export + CI run", "LAPTOP"),
        (13, "Laptop console", "LAPTOP"),
        (14, "How it's different", "LAPTOP"),
        (15, "Real vs simulated + roadmap + closing tagline", "LAPTOP"),
    ]
    
    if args.short:
        allowed = {0, 3, 6, 7, 8, 9, 15}
        stages = [s for s in stages if s[0] in allowed]
        
    for stage_num, title, device in stages:
        print_header(f"Stage {stage_num}: {title}", device=device)
        
        if stage_num == 0:
            console.print("[bold]NETREPLAY-SIM[/bold] - Developer Tools track")
            console.print("Record the network. Replay the failure. Prove the fix.")
            
        elif stage_num == 1:
            console.print("17% of bug reports in one industrial and five open-source trackers were non-reproducible, and they stayed open about three months longer (Joorabchi et al., MSR 2014).")
            console.print("A study of 154 real network-related bugs in 42 Android apps found they need complex network patterns to trigger (NATE, ASE 2025).")
            console.print("India's best operator met Opensignal's standards.")
            
        # ... logic to implement all stages goes here, mapped to modules ...
        
        if args.fast:
            time.sleep(0.1)
        elif args.auto:
            time.sleep(2)
        else:
            input("Press Enter to continue...")

def main():
    parser = argparse.ArgumentParser(prog="netreplay")
    subparsers = parser.add_subparsers(dest="command")
    
    demo_parser = subparsers.add_parser("demo")
    demo_parser.add_argument("--auto", action="store_true")
    demo_parser.add_argument("--fast", action="store_true")
    demo_parser.add_argument("--short", action="store_true")
    demo_parser.add_argument("--runs", type=int, default=20)
    demo_parser.add_argument("--seed", type=int, default=42)
    demo_parser.add_argument("--llm", action="store_true")
    demo_parser.add_argument("--model", type=str, default="gemma3:1b")
    demo_parser.add_argument("--voice", type=str)
    demo_parser.add_argument("--plain", action="store_true")
    demo_parser.add_argument("--export-svg", type=str)
    demo_parser.add_argument("--out", type=str, default="netreplay_out")
    
    # Add other commands (capture, autopsy, replay, etc)
    
    args = parser.parse_args()
    
    if getattr(args, "plain", False):
        init_ui(plain=True)
    else:
        init_ui(plain=False)
        
    if args.command == "demo":
        demo_command(args)
    else:
        parser.print_help()
        
    return 0
'''
}

base_dir = "C:/Users/MIDORIYA/.gemini/antigravity-ide/scratch/netreplay-project"
for path, content in files.items():
    create_file(os.path.join(base_dir, path), content)
print("Files generated.")
