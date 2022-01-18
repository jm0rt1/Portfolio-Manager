

import rich.console


console = rich.console.Console()

with console.status("working...", spinner="grenade"):
    while True:
        pass
