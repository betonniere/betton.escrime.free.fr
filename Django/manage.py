#!/usr/bin/env python
import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

if __name__ == "__main__":
    if os.environ.get('RUN_MAIN') == 'true':
        console = Console()

        texte = Text("Lancement de http://127.0.0.1:8080/fencing-tournament-software", style="bold")
        console.print(Panel(texte,
                            border_style="green",
                            expand=False,
                            padding=(1, 2)))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bellepoule.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
