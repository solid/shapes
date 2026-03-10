# Solid SHACL Shapes Catalogue – Validation Strategy

## Overview

The Solid SHACL Shapes Catalogue enforces a rigorous validation strategy to ensure that all contributed SHACL shapes are:

- **Syntactically correct**  
- **Metadata-complete**  
- **Immutable (once stable/archaic)**  
- **Versioned correctly**  
- **Named and namespaced consistently**

This ensures **interoperability, FAIR principles, and stable contracts** for all applications consuming shapes.

All validations are automated through **GitHub Actions** and provide **immediate, actionable feedback** to contributors.

---

## Validation Steps for Pull Requests

Every pull request (PR) undergoes the following validations:

### 1. SHACL Syntax Validation

- Uses PySHACL to check all `.ttl` files in `/shapes/`.  
- Detects syntax errors or constraint violations.  
- **Feedback:** Exact line numbers and constraint violations shown in PR checks.

### 2. Metadata Completeness

Required metadata for each shape:

- `rdfs:label` – human-readable label  
- `dct:created` – creation date  
- `vs:term_status` – lifecycle status: `unstable`, `testing`, `stable`, `archaic`

**Feedback:** Missing or invalid metadata triggers specific error messages.

### 3. Immutability Enforcement

- Stable and archaic shapes cannot be modified.  
- Only permitted changes: `dct:isReplacedBy`, `vs:term_status` update to `"archaic"`.  
- **Feedback:** PR fails if any immutable shape is altered incorrectly.

### 4. Versioning Consistency

- Successor shapes must use `-v2`, `-v3`, etc.  
- Predecessors must include `dct:isReplacedBy` links.  
- New versions must include `dct:replaces` links.  
- **Feedback:** Missing or inconsistent links are reported in the PR.

### 5. Namespace and Naming Checks

- Namespace: `https://solidproject.org/shapes/{domain}#`  
- Shape names: PascalCase ending with `Shape`  
- Prefix labels: lowercase letters, hyphens, or underscores  

**Feedback:** Invalid namespaces, prefixes, or names are reported with line references.

### 6. Optional: Sorted Turtle Serialisation

- Ensures deterministic `.ttl` file ordering for meaningful diffs.  
- Contributors receive warnings if Turtle files are not sorted.

---

## Implementation in GitHub Actions

Validation workflow is defined in `.github/workflows/validate-shapes.yml`.  
- Runs automatically on PRs affecting `/shapes/**/*.ttl`.  
- Executes scripts in `/scripts/`:

```text
/scripts/check-metadata-and-immutability.py
/scripts/check-namespaces-and-names.py