# Contributing to the Solid SHACL Shapes Catalogue

Thank you for your interest in contributing. 

This repository accepts contributions of SHACL shapes, improvements to existing shapes, and documentation updates. All contributions are reviewed through a GitHub pull request (PR) process. 

If you have feedback on this process, please raise it in the **[GitHub discussion](https://github.com/solid/shapes/discussions/20)**.


## Guidelines for Contributing

When contributing, you MUST:

- Check whether a domain file already exists
- Follow the naming conventions defined in this document
- Include documentation using the GitHub PR template
- Ensure shapes validate before submitting

### Branching Requirements

All contributions MUST be made from a separate branch.

- Do NOT commit directly to the `main` branch
- Create a new branch for each contribution or feature
- Use a clear and descriptive branch name

## Adding Shapes

### Existing Domains

Each domain MUST have a single `{domain}.ttl` file.

- If a domain file exists, add your shape to that file where appropriate
- Do NOT create duplicate domain files

### New Domains

If a domain file does not exist, create a new file:

```
/shapes/{domain}.ttl
```

### Rules

- Domain names MUST be lowercase
- Domain names SHOULD be a minimal representation of the semantic concept

If using vocabularies, follow community ontology naming conventions.  
If unsure, check: https://prefix.cc



## Naming Conventions

### Namespace Structure

Use the following pattern:

```
[https://solidproject.org/shapes/{domain}#](https://solidproject.org/shapes/{domain}#)
```

Examples:
```
[https://solidproject.org/shapes/address#](https://solidproject.org/shapes/address#)
[https://solidproject.org/shapes/vcard#](https://solidproject.org/shapes/vcard#)
````



### Prefix Naming

- Prefix labels MUST begin with a letter
- Prefix labels MAY use lowercase letters, hyphens, or underscores

Example:

```turtle
@prefix address-shape: <https://solidproject.org/shapes/address#> .
@prefix vcard-shape: <https://solidproject.org/shapes/vcard#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
````



### Shape Naming

* Shape names MUST use PascalCase
* Shape names MUST end with `Shape`

Examples:
```
address-shape:AddressShape
vcard-shape:VCardAddressShape
```


## Multiple Shapes per Domain

Multiple shapes MAY exist within a single domain.

* Use semantic variation rather than creating new namespaces

Example:
```
address-shape:AddressShape
address-shape:AddressMinimalShape
```


## Validation Rules

Shapes SHOULD follow these guidelines:

* Prefer optional validation to maximise Pod interoperability
* Keep constraints focused on structural validation

## Shape Immutability Policy

Shapes published to this catalogue are **immutable**.

Once a shape is merged and published:

* Shapes MUST NOT be modified in place
* Validation rules MUST NOT be changed retrospectively
* Structural or semantic changes MUST be introduced via new shapes

This ensures predictable behaviour for applications using Solid Pods.



### Why Shapes Are Immutable

Shapes function as contracts between applications and user data. Modifying a published shape can cause:

* Validation inconsistencies across applications
* Silent breaking changes in decentralized clients
* Data interoperability failures

Immutability ensures that applications can safely cache and reuse shapes.



## Evolving Shapes

If validation rules need to change, you MUST create a new shape.

### Recommended Approach

#### Create a New Shape Variant

Example:

```
address-shape:AddressShape
address-shape:AddressStrictShape
```



### When Adding New Constraints

You MUST NOT:

* Add new mandatory fields to existing shapes
* Change cardinality rules of existing properties
* Change target class mappings

Instead:

* Introduce a new shape variant or version

You MAY:

* Add new optional properties
* Add documentation
* Add new shapes





## Pull Request Process

* Submit a PR with a clear description of the shape and its purpose
* Indicate whether you are modifying an existing domain or creating a new one
* Ensure the shape validates before submission
* Include documentation using the PR template
* Respond to review feedback and iterate as needed

All contributions are subject to peer review before merging.

## Contributor Checklist

Before submitting your PR, ensure:

* [ ] The shape validates successfully
* [ ] Naming conventions are followed
* [ ] The correct domain file is used or created
* [ ] Documentation is included
* [ ] No existing shapes are modified in a breaking way


## Human Consensus Process

In addition to the contribution process described above, there is an important **human consensus** step that we are still refining. For example:

```
If a PR introduces a shape that overlaps conceptually with an existing one, we will ask contributors to collaborate with the current maintainer(s) of that shape, aiming to align on a shared model where possible.

If alignment is reached, contributors should work together to evolve the existing shape. If not, both shapes can continue to be maintained independently.
```


If you have feedback on this process, please raise it in the **[GitHub discussion](https://github.com/solid/shapes/discussions/20)**.




