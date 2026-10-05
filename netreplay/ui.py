import sys
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
import random

console = Console()
plain_mode = False
export_dir = None
stage_idx = 0

def init_ui(plain=False, export_svg_dir=None):
    global plain_mode, console, export_dir
    plain_mode = plain
    export_dir = export_svg_dir
    if plain:
        console = Console(color_system=None, force_terminal=False)
    else:
        # We allow exporting SVG by overriding console
        if export_dir:
            os.makedirs(export_dir, exist_ok=True)
            console = Console(record=True)

def export_svg_if_needed(filename):
    global console, export_dir
    if export_dir and not plain_mode:
        path = os.path.join(export_dir, filename)
        console.save_svg(path, title=filename)
        # Clear record buffer after save so next stage starts fresh
        console._record_buffer.clear()

def print_header(title, device="PHONE"):
    """Stage header."""
    text = f" {title} "
    device_label = f"[{device}]"
    
    if plain_mode:
        print(f"{'='*50}")
        print(f"{device_label} {title}")
        print(f"CONCEPT PROTOTYPE - all network data simulated")
        print(f"{'='*50}")
    else:
        console.print()
        console.print(Panel(
            Text("CONCEPT PROTOTYPE - all network data simulated", style="dim italic"),
            title=f"[bold cyan]{text}[/bold cyan] [bold yellow]{device_label}[/bold yellow]",
            title_align="left",
            border_style="blue"
        ))
        console.print()

def print_panel(text, title=None):
    if plain_mode:
        if title:
            print(f"--- {title} ---")
        print(text)
    else:
        console.print(Panel(text, title=title, expand=False))