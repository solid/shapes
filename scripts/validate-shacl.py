#!/usr/bin/env python3

import sys
from pyshacl import validate
from rdflib import Graph
from rich.console import Console

console = Console()


def validate_file(path):
    console.print(f"\n[bold]Checking[/bold] {path}")

    try:
        data_graph = Graph()
        data_graph.parse(path, format="turtle")

        # Meta validate SHACL shapes
        conforms, _, report = validate(
            data_graph,
            shacl_graph=data_graph,
            inference="none",
            meta_shacl=True
        )

        if conforms:
            console.print("[green]✓ SHACL is valid[/green]")
            return True

        console.print("[red]✗ SHACL validation failed[/red]")
        console.print(report)

        return False

    except Exception as e:
        console.print("[red]Parsing error[/red]")
        console.print(str(e))
        return False


if __name__ == "__main__":
    ok = True

    for file in sys.argv[1:]:
        if not validate_file(file):
            ok = False

    sys.exit(0 if ok else 1)