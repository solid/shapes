#!/bin/bash
# -----------------------------------------------
# Script: validate-shacl-shapes-dir.sh
# Purpose: Validate all Turtle (TTL) files in a directory against SHACL shapes using pySHACL.
# -----------------------------------------------

set -o pipefail
set +e

SHAPES_DIR="./shapes"

# Initialize counters
total=0
valid=0
invalid=0

echo "Searching for TTL files in $SHAPES_DIR..."

# Ensure directory exists
if [ ! -d "$SHAPES_DIR" ]; then
    echo "ERROR: Directory '$SHAPES_DIR' does not exist."
    echo "Current repository structure:"
    ls -R
    exit 1
fi

# Prevent *.ttl from expanding to literal string if no files exist
shopt -s nullglob

files=($SHAPES_DIR/*.ttl)

# Check if there are any TTL files
if [ ${#files[@]} -eq 0 ]; then
    echo "ERROR: No TTL files found in '$SHAPES_DIR'."
    echo "Directory contents:"
    ls -l "$SHAPES_DIR"
    exit 1
fi

echo "Found ${#files[@]} TTL files."

# Loop over each TTL file
for file in "${files[@]}"; do
    ((total++))
    echo "--------------------------------"
    echo "Validating file: $file"

    if output=$(python3 - <<EOF 2>&1
import sys
from pyshacl import validate
from rdflib.plugins.parsers.notation3 import BadSyntax

ttl_file = "$file"

try:
    conforms, v_graph, v_text = validate(
        ttl_file,
        shacl_graph=None,
        inference='rdfs',
        abort_on_first=True,
        advanced=True,
        meta_shacl=True,
        debug=False
    )

    if conforms:
        print("RESULT: CONFORMS")
        print("File:", ttl_file)
        sys.exit(0)

    else:
        print("RESULT: VALIDATION FAILED")
        print("File:", ttl_file)
        print("Validation report (first 15 lines):")
        print("\\n".join(v_text.splitlines()[:15]))
        sys.exit(1)

except BadSyntax as e:
    msg = str(e)

    print("RESULT: SYNTAX ERROR")
    print("File:", ttl_file)

    if "Prefix" in msg:
        try:
            prefix = msg.split('"')[1]
            print("Missing prefix declaration:", prefix)
            print("Suggested fix: add '@prefix {}: <URI> .' near the top of the file.".format(prefix))
        except:
            pass

    print("Parser message:", msg)
    sys.exit(1)

except Exception as e:
    print("RESULT: UNEXPECTED ERROR")
    print("File:", ttl_file)
    print("Error message:", str(e))
    sys.exit(1)

EOF
); then
        echo "$output"
        ((valid++))
    else
        echo "$output"
        ((invalid++))
    fi
done

echo "--------------------------------"
echo "Validation Summary"
echo "Total files processed: $total"
echo "Files conforming: $valid"
echo "Files failed: $invalid"

if [ $invalid -gt 0 ]; then
    exit 1
else
    exit 0
fi