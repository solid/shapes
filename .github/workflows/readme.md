# GitHub Action Workflows

This directory contains the GitHub Actions workflows used to validate SHACL shapes and enforce repository governance rules.


## *Push* Validation on *Main*

> **File:** [main-push-validation.yml](./main-push-validation.yml)

This workflow runs whenever changes are **pushed to the *main* branch** of the shapes repository. It performs full validation to ensure that all SHACL shapes and repository standards remain correct.

### Checks Performed

* [Validate all SHACL shapes in the repository](../../scripts/validate-shacl-shapes-dir.sh) for syntax and constraints
* [Check metadata and immutability](../../scripts/check-metadata-and-immutability.py) to ensure published shapes are not modified improperly
* [Verify namespaces and naming conventions](../../scripts/check-namespaces-and-names.py) across all shapes

### Outcome

* **Fails the workflow** if any validation or policy check fails, preventing broken shapes from being merged
* Ensures the **entire repository remains valid** after changes are merged



## *Pull Request* Validation on *Main*

> **File:** [shacl-pr-validation.yml](./shacl-pr-validation.yml)

This workflow runs whenever a **pull request targets the *main* branch** and modifies SHACL files (*.ttl*) in the *shapes/* directory. It ensures that any new or changed shapes comply with repository rules before merging.

### Checks Performed

* **Detect changed SHACL files** in the pull request (*.ttl* files)
* [Validate the modified SHACL shapes](../../shapes/scripts/validate-shacl-shapes-file.py) for syntax and constraints
* [Check metadata and immutability](../../scripts/check-metadata-and-immutability.py) to ensure required metadata exists and published shapes are not modified improperly
* [Verify namespaces and naming conventions](../../scripts/check-namespaces-and-names.py) across all modified shapes

### Outcome

* **Fails the workflow** if any validation or policy check fails, preventing the PR from being merged
* Ensures that **all new or changed shapes follow repository standards** before integration into `main`

