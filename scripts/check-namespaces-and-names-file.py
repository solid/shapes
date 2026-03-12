#!/usr/bin/env python3
"""
check_namespaces_and_names_selected.py

Validates SHACL shapes for:
- Namespace correctness
- Shape naming conventions
- Prefix labels

Usage:
    python check_namespaces_and_names_selected.py file1.ttl [file2.ttl ...]
"""

import sys
from rdflib import Graph, Namespace
from rdflib.namespace import RDF

# Namespaces
SH = Namespace("http://www.w3.org/ns/shacl#")
EXPECTED_NS_PREFIX = "https://solidproject.org/shapes/"

# Exit code
exit_code = 0


def check_shape_names(g, shape_uri):
    """Check namespace and local name conventions of a single shape."""
    global exit_code
    uri = str(shape_uri)
    
    # Namespace check
    if not uri.startswith(EXPECTED_NS_PREFIX):
        print(f"[NAMESPACE ERROR] Shape {uri} does not start with {EXPECTED_NS_PREFIX}")
        exit_code = 1
    
    # Local name check
    local_name = uri.split("#")[-1]
    if not local_name.endswith("Shape"):
        print(f"[NAME ERROR] Shape {uri} local name '{local_name}' should end with 'Shape'")
        exit_code = 1
    if not local_name[0].isupper():
        print(f"[NAME ERROR] Shape {uri} local name '{local_name}' should start with uppercase letter (PascalCase)")
        exit_code = 1


def check_prefix_labels(g):
    """Check that all prefixes are lowercase and contain only allowed characters."""
    global exit_code
    for prefix, ns in g.namespaces():
        if prefix:  # skip default namespace
            if not prefix[0].islower():
                print(f"[PREFIX ERROR] Prefix '{prefix}' should start with lowercase")
                exit_code = 1
            if any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-_" for c in prefix):
                print(f"[PREFIX ERROR] Prefix '{prefix}' contains invalid characters")
                exit_code = 1


def main():
    global exit_code

    # Get files from command-line arguments
    ttl_files = sys.argv[1:]
    if not ttl_files:
        print("Usage: python check_namespaces_and_names_selected.py file1.ttl [file2.ttl ...]")
        sys.exit(1)

    for f in ttl_files:
        g = Graph()
        try:
            g.parse(f, format="turtle")
        except Exception as e:
            print(f"\n[PARSE ERROR] Failed to parse {f}")
            print(f"Details: {e}")
            exit_code = 1
            continue

        check_prefix_labels(g)
        for shape_uri in g.subjects(RDF.type, SH.NodeShape):
            check_shape_names(g, shape_uri)

    if exit_code:
        print("\nValidation failed. Please fix the above errors.")
    else:
        print("Namespace and naming validation passed.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()