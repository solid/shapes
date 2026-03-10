#!/usr/bin/env python3
# -----------------------------------------------
# Script: validate-shacl-shapes-file.py
# Purpose: Validate Turtle (TTL) files against SHACL shapes using pySHACL.
# Features:
#   - Parses TTL files using rdflib
#   - Runs SHACL validation (meta-SHACL included)
#   - Prints nice colored output using Rich
#   - Returns exit code 0 if all files valid, 1 if any file fails
# -----------------------------------------------
# HOW TO USE:
# 1. Install dependencies:
#      pip install pyshacl rdflib rich
#
# 2. Run the script on one or more TTL files:
#      ./validate-shacl-shapes-file.py shapes/shape1.ttl shapes/shape2.ttl
#
# 3. Exit codes:
#      0 → all files valid
#      1 → at least one file failed
# -----------------------------------------------

import sys
from pyshacl import validate
from rdflib import Graph
from rich.console import Console

# Create a Rich console for colorful output
console = Console()


def validate_file(path):
    """
    Validate a single TTL file against SHACL shapes.

    Args:
        path (str): Path to the TTL file to validate.

    Returns:
        bool: True if the file passes SHACL validation, False otherwise.
    """
    console.print(f"\n[bold]Checking[/bold] {path}")

    try:
        # Parse the TTL file into an RDF graph
        data_graph = Graph()
        data_graph.parse(path, format="turtle")

        # Run SHACL validation
        # - shacl_graph=data_graph: using the same graph for data and shapes
        # - inference="none": no RDFS or OWL inference
        # - meta_shacl=True: enable meta-SHACL validation
        conforms, _, report = validate(
            data_graph,
            shacl_graph=data_graph,
            inference="none",
            meta_shacl=True
        )

        if conforms:
            console.print("[green]✓ SHACL is valid[/green]")
            return True

        # If validation fails, print the report
        console.print("[red]✗ SHACL validation failed[/red]")
        console.print(report)
        return False

    except Exception as e:
        # Catch parsing errors or unexpected exceptions
        console.print("[red]Parsing error[/red]")
        console.print(str(e))
        return False


if __name__ == "__main__":
    # Track overall validation result
    ok = True

    # Loop over each TTL file provided as command-line arguments
    for file in sys.argv[1:]:
        if not validate_file(file):
            ok = False

    # Exit code 0 if all files passed, 1 if any failed
    sys.exit(0 if ok else 1)