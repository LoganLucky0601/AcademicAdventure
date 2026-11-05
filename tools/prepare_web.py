"""Stage the desktop game for a Pygbag build."""
import ast
from pathlib import Path
import shutil
import symtable
import sys
from textwrap import indent


source = Path(__file__).resolve().parents[1] / "Academic Adventure"
destination = Path(sys.argv[1])
destination.mkdir(parents=True, exist_ok=True)
for directory in ("assets", "scripts"):
    shutil.copytree(source / directory, destination / directory, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__"))

code = (source / "main.py").read_text(encoding="utf-8")
loop = next(node for node in ast.parse(code).body if isinstance(node, ast.While))
lines = code.splitlines(keepends=True)
# The desktop loop runs at module scope. Preserve its shared state when wrapping it.
frame = "".join(lines[loop.lineno - 1:loop.end_lineno])
state = symtable.symtable(frame, "main.py", "exec")
globals_used = sorted(symbol.get_name() for symbol in state.get_symbols()
                      if symbol.is_assigned() or symbol.is_declared_global())
frame = "".join(line for line in frame.splitlines(keepends=True)
                if not line.lstrip().startswith("global "))
web_code = (
    "import asyncio\n"
    + "".join(lines[:loop.lineno - 1])
    + "\nasync def run_web_game():\n"
    + "".join(f"    global {name}\n" for name in globals_used)
    + indent(frame.rstrip(), "    ")
    + "\n        await asyncio.sleep(0)\n"
    + "    pygame.quit()\n\n"
    + "asyncio.run(run_web_game())\n"
)
compile(web_code, "main.py", "exec")
(destination / "main.py").write_text(web_code, encoding="utf-8")
