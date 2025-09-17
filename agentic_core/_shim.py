from __future__ import annotations
import importlib
import importlib.util
import sys
from types import ModuleType
from typing import Dict

def alias_modules(alias_map: Dict[str, str]) -> None:
    """
    Create 1:1 module aliases in sys.modules for a small set of targets.

    alias_map: { "agentic_core.path": "semantic_kernel.path", ... }

    - If a *real* local module exists for the destination (agentic_core.*), we DO NOT alias.
    - Otherwise we import the source (semantic_kernel.*) once and alias the same module object
      under the destination name—so class identity and isinstance checks remain consistent.
    """
    for dst_name, src_name in alias_map.items():
        # If there's an existing local implementation, do nothing.
        if importlib.util.find_spec(dst_name) is not None:
            continue

        # If already imported/aliased, skip.
        if dst_name in sys.modules:
            continue

        # Import source and alias
        try:
            src_mod = importlib.import_module(src_name)
            sys.modules[dst_name] = src_mod
        except Exception as e:
            # Be forgiving—consumer might not need this path at runtime.
            # You could log a debug message here if you like.
            continue
