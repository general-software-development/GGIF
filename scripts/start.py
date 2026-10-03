import subprocess
from pathlib import Path
from rich.console import Console
import sys

console = Console()
console.rule("GGIF Server")

console.print(f"[bold]\[/]\tPreparing for startup")

this = Path(__file__)

console.print(f"\t\t[green]\[:heavy_check_mark:]\tDone")

console.print(f"[bold]\[/]\tPreparing static file manifest")

p = subprocess.run(["uv", "run", this.parent / "generate_static_manifest.py"], stdout=sys.stdout, stderr=sys.stderr)

console.print(f"\t\t[green]\[:heavy_check_mark:]\tManifest written")

console.print(f"[bold]\[/]\tStarting GGIF server")

p2 = subprocess.run(["uv", "run", "zensical", "serve", "--dev-addr", "0.0.0.0:8080"], stderr=sys.stderr, stdout=subprocess.PIPE, text=True, bufsize=1)

for line in p2.stdout:
    console.print(f"\t\t#\t{line}")

p2.wait()
return_code = p2.returncode
console.print(f"\n\n[bold]Exited with code {return_code}.")
