from pathlib import Path
import json

static_dir = Path("docs/static")
output = static_dir / "manifest.json"

extensions = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp",
    ".mp4", ".webm", ".ogg", ".mov", ".m4v"
}

files = [
    str(path.relative_to(static_dir)).replace("\\", "/")
    for path in static_dir.rglob("*")
    if path.is_file() and path.suffix.lower() in extensions
]

files.sort()

output.write_text(
    json.dumps(files, indent=2),
    encoding="utf-8"
)

print(f"Generated {output} with {len(files)} files.")
