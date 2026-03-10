#!/bin/bash
# -----------------------------------------------
# Script: validate-shacl-shapes-dir.sh
# Purpose: Validate all Turtle (TTL) files in a directory against SHACL shapes using pySHACL.
# -----------------------------------------------
# HOW TO USE THIS SCRIPT:
# 1. Prerequisites:
#    - Python 3 installed
#    - pySHACL installed (run: pip install pyshacl)
#    - TTL files to validate placed in ./shapes (or change SHAPES_DIR below)
#
# 2. Make the script executable:
#    chmod +x validate_shapes.sh
#
# 3. Run the script:
#    ./validate-shacl-shapes-dir.sh
#
# 4. Script behavior:
#    - Searches for all .ttl files in the SHAPES_DIR
#    - Validates each file against SHACL shapes using pySHACL
#    - Reports for each file:
#        ✅ Conforms to SHACL
#        ❌ Does NOT conform or has syntax errors
#    - Prints a summary at the end with total, valid, and failed files
#    - Exit codes:
#        0 → all files valid
#        1 → at least one file failed validation
# -----------------------------------------------

set -e  # Exit immediately if any command returns a non-zero status

SHAPES_DIR="./shapes"  # Directory containing TTL files to validate

# Initialize counters for reporting
total=0       # Total TTL files found
valid=0       # Number of files that pass validation
invalid=0     # Number of files that fail validation

echo "Searching for TTL files in $SHAPES_DIR..."
files=($SHAPES_DIR/*.ttl)  # Get a list of all .ttl files in the directory

# Check if there are any TTL files
if [ ${#files[@]} -eq 0 ]; then
    echo "❌ No TTL files found in $SHAPES_DIR"
    exit 1
fi

# Loop over each TTL file
for file in "${files[@]}"; do
    ((total++))  # Increment total counter
    echo "───────────────────────────────"
    echo "Validating $file..."

    # Run pySHACL validation inside an embedded Python script
    # Capture output (including errors) to show in the terminal
    if output=$(python3 - <<EOF 2>&1
import sys
from pyshacl import validate
from rdflib.plugins.parsers.notation3 import BadSyntax

ttl_file = "$file"  # File to validate
try:
    # Run validation
    conforms, v_graph, v_text = validate(
        ttl_file,
        shacl_graph=None,  # No separate SHACL graph, uses SHACL included in TTL
        inference='rdfs',  # Use RDFS inference
        abort_on_error=True,  # Stop at first error
        advanced=True,       # Enable advanced SHACL features
        meta_shacl=True,     # Enable Meta-SHACL checks
        debug=False
    )
    if conforms:
        # TTL file conforms to SHACL
        print("✅ $ttl_file conforms to SHACL")
        sys.exit(0)
    else:
        # TTL file fails validation, print first 15 lines of errors
        print("❌ $ttl_file does NOT conform:")
        print(v_text.splitlines()[0:15])
        sys.exit(1)
except BadSyntax as e:
    # Handle syntax errors in TTL files
    msg = str(e)
    if "Prefix" in msg:
        prefix = msg.split('"')[1]
        print(f"❌ {ttl_file} has syntax errors:")
        print(f"  Missing prefix declaration: {prefix}")
        print(f"  Suggestion: Add '@prefix {prefix}: <URI> .' at the top of the TTL file")
    else:
        print(f"❌ {ttl_file} has syntax errors:")
        print(f"  {msg}")
    sys.exit(1)
except Exception as e:
    # Catch-all for unexpected errors
    print(f"❌ {ttl_file} validation failed due to unexpected error:")
    print(f"  {str(e)}")
    sys.exit(1)
EOF
); then
        ((valid++))  # If Python exits 0, increment valid counter
    else
        # If validation failed, print captured output
        echo "$output"
        ((invalid++))  # Increment invalid counter
    fi
done

# Print summary of results
echo "───────────────────────────────"
echo "Validation Summary:"
echo "Total files: $total"
echo "✅ Conforms: $valid"
echo "❌ Failed: $invalid"

# Exit with non-zero if any files failed validation
if [ $invalid -gt 0 ]; then
    exit 1
else
    exit 0
fi