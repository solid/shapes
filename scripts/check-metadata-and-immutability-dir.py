#!/usr/bin/env python3
"""
check_metadata_and_immutability.py

Validates SHACL shapes for:
- Required metadata (sh:name, dct:created, vs:term_status)
- Correct metadata formats
- Status validity
- Immutability rules (placeholder for future logic)
"""

import sys
import glob
from rdflib import Graph, Namespace
from rdflib.namespace import RDF

# Namespaces
SH = Namespace("http://www.w3.org/ns/shacl#")
DCT = Namespace("http://purl.org/dc/terms/")
VS = Namespace("http://www.w3.org/2003/06/sw-vocab-status/ns#")

# Allowed status values
VALID_STATUS = {"unstable", "testing", "stable", "archaic"}

# Paths
SHAPES_DIR = "shapes/"

exit_code = 0


def report_error(file, shape, property_name, message, value=None, expected=None):
    """Print a structured validation error."""
    global exit_code
    exit_code = 1

    print("\n[SHACL METADATA ERROR]")
    print(f"File:        {file}")
    print(f"Shape:       {shape}")
    print(f"Property:    {property_name}")

    if value is not None:
        print(f"Found:       {value}")

    if expected is not None:
        print(f"Expected:    {expected}")

    print(f"Problem:     {message}")


def check_shape_metadata(g, file, shape_uri):

    label = g.value(shape_uri, SH.name)
    created = g.value(shape_uri, DCT.created)
    status = g.value(shape_uri, VS.term_status)

    # sh:name
    if not label:
        report_error(
            file,
            shape_uri,
            "sh:name",
            "Missing required name for SHACL NodeShape.",
            expected="Human readable name e.g. sh:name  \"Person Shape\""
        )

    # dct:created
    if not created:
        report_error(
            file,
            shape_uri,
            "dct:created",
            "Creation date missing.",
            expected="ISO 8601 date literal e.g. \"2025-02-10\"^^xsd:date"
        )
    else:
        try:
            created.toPython()
        except Exception:
            report_error(
                file,
                shape_uri,
                "dct:created",
                "Invalid date literal.",
                value=created,
                expected="ISO 8601 xsd:date (YYYY-MM-DD)"
            )

    # vs:term_status
    if not status:
        report_error(
            file,
            shape_uri,
            "vs:term_status",
            "Status missing.",
            expected=f"One of {sorted(VALID_STATUS)}"
        )
    else:
        status_str = str(status)

        if status_str not in VALID_STATUS:
            report_error(
                file,
                shape_uri,
                "vs:term_status",
                "Invalid status value.",
                value=status_str,
                expected=f"One of {sorted(VALID_STATUS)}"
            )


def check_immutability(g, file, shape_uri):
    """
    Placeholder for immutability validation.

    In production you would:
    - Compare against previous committed version
    - Detect structural changes
    - Ensure version increment
    """

    status = g.value(shape_uri, VS.term_status)

    if status and str(status) in {"stable", "archaic"}:
        # Future logic example:
        # compare shape hash with previous commit
        pass


def main():
    global exit_code

    ttl_files = glob.glob(f"{SHAPES_DIR}/*.ttl")

    if not ttl_files:
        print(f"[ERROR] No Turtle files found in '{SHAPES_DIR}'")
        sys.exit(1)

    for file in ttl_files:

        g = Graph()

        try:
            g.parse(file, format="turtle")
        except Exception as e:
            print("\n[PARSE ERROR]")
            print(f"File: {file}")
            print(f"Problem: Failed to parse Turtle file")
            print(f"Details: {e}")
            exit_code = 1
            continue

        shapes_found = False

        for shape_uri in g.subjects(RDF.type, SH.NodeShape):
            shapes_found = True
            check_shape_metadata(g, file, shape_uri)
            check_immutability(g, file, shape_uri)

        if not shapes_found:
            print(f"\n[WARNING] No sh:NodeShape found in {file}")

    if exit_code:
        print("\n Validation FAILED")
        print("Fix the above issues before committing shapes.")
    else:
        print("\n Metadata and immutability validation passed.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()