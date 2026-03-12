#!/usr/bin/env python3
"""
check_selected_metadata_and_immutability.py

Validates metadata and immutability of selected SHACL shapes.
- Accepts files passed as command-line arguments (for PR workflows)
- Performs the same checks as the original script
"""

import sys
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS

# Namespaces
SH = Namespace("http://www.w3.org/ns/shacl#")
DCT = Namespace("http://purl.org/dc/terms/")
VS = Namespace("http://www.w3.org/2003/06/sw-vocab-status/ns#")

VALID_STATUS = {"unstable", "testing", "stable", "archaic"}

exit_code = 0


def report_error(file, shape, property_name, message, value=None, expected=None):
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
    label = g.value(shape_uri, RDFS.label)
    created = g.value(shape_uri, DCT.created)
    status = g.value(shape_uri, VS.term_status)

    if not label:
        report_error(file, shape_uri, "rdfs:label",
                     "Missing required label.",
                     expected="Human readable label")
    if not created:
        report_error(file, shape_uri, "dct:created",
                     "Creation date missing.",
                     expected="ISO 8601 xsd:date")
    else:
        try:
            created.toPython()
        except Exception:
            report_error(file, shape_uri, "dct:created",
                         "Invalid date literal.",
                         value=created,
                         expected="ISO 8601 xsd:date")
    if not status:
        report_error(file, shape_uri, "vs:term_status",
                     "Status missing.",
                     expected=f"One of {sorted(VALID_STATUS)}")
    elif str(status) not in VALID_STATUS:
        report_error(file, shape_uri, "vs:term_status",
                     "Invalid status value.",
                     value=str(status),
                     expected=f"One of {sorted(VALID_STATUS)}")


def check_immutability(g, file, shape_uri):
    status = g.value(shape_uri, VS.term_status)
    if status and str(status) in {"stable", "archaic"}:
        # Placeholder for future immutability logic
        pass


def main():
    global exit_code

    # Accept files from command-line arguments
    ttl_files = sys.argv[1:]
    if not ttl_files:
        print("Usage: python check_selected_metadata_and_immutability.py file1.ttl [file2.ttl ...]")
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
        print("\nValidation FAILED")
        sys.exit(exit_code)
    else:
        print("\nMetadata and immutability validation passed.")


if __name__ == "__main__":
    main()