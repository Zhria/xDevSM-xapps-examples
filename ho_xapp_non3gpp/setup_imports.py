import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parent
candidate_paths = [
    base_dir / "xDevSM",
    base_dir.parent / "xDevSM",
]

added = []

for path in candidate_paths:
    if path.is_dir():
        resolved = str(path)
        if resolved not in sys.path:
            sys.path.insert(0, resolved)
            added.append(resolved)

        sm_path = path / "sm_framework"
        if sm_path.is_dir():
            resolved_sm = str(sm_path)
            if resolved_sm not in sys.path:
                sys.path.insert(0, resolved_sm)
                added.append(resolved_sm)

if added:
    print(f"[setup_imports] Added paths: {added}")
else:
    print(f"[setup_imports] No xDevSM paths found from {candidate_paths}")
