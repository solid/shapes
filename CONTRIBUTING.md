# Contributing to the Solid SHACL Shapes Catalogue

This repository accepts contributions of SHACL shapes, improvements to existing shapes, and documentation updates. All contributions are reviewed through a GitHub pull request (PR) process. 

If you have feedback on this process, please raise it in the **[GitHub discussion](https://github.com/solid/shapes/discussions/20)**.


## Guidelines

When contributing:

- Create a new branch
- Check whether a domain file already exists
- Follow the naming conventions defined in this document
- Include documentation using the GitHub PR template
- Ensure shapes validate before submitting



## Pull Request Process

* Create branch 
* Ensure the shape validates before opening a PR
    * [validation scripts](./scripts) are available 
* Open a PR and complete the questions in the PR template provided
* Respond to review feedback and iterate as needed

All contributions are subject to peer review before merging.

## Branch Requirements

All contributions must be made from a separate branch. 

## Domain Files

Each domain has a {domain}.ttl file. If a domain file exists, add your shape to that file otherwise create a new file in the shapes directory /shapes/{domain}.ttl. Domain file names are lowercase and should be a minimal representation of the semantic concept.

### Namespace and Prefix Conventions

Use the following pattern for namespace:
```
https://solidproject.org/shapes/{domain}#
```

Prefix labels must begin with a letter and use lowercase letters, hyphens, or underscores, e.g.:

```turtle
@prefix address-shape: <https://solidproject.org/shapes/address#> .
```


### Multiple Shapes per Domain

A goal of the solid/shapes repository is to work towards consensus on a single shape for a given domain where possible. Where this is not possible, multiple shapes may exist for a given domain. If a new shape needs to be added for an existing domain, naming conventions recommend the use of a semantic variation for the shape name, e.g.:

```
address-shape:AddressShape
address-shape:AddressMinimalShape
```

## Shape Name



Shape names should use PascalCase abd end with `Shape`, e.g.:

```
address-shape:AddressShape
```




## Validation Rules
A goal of solid/shapes is to support interoperability in the Solid ecosystem, and with this in mind, it is recommended that shapes should have constraints that maximise their potential reuse. 


## Shape Immutability Policy

Shapes published to this catalogue are **immutable** to ensure predictable behaviour for applications/agents that might use them. Once a shape is merged and published:

* Shapes MUST NOT be modified in place
* Validation rules MUST NOT be changed retrospectively
* Structural or semantic changes MUST be introduced via new shapes


## Evolving Shapes

The Solid/shapes repository supports the evolution of shapes, where a change to the shape is not a breaking change.

A non-breaking change for a domain file would be:
* Addition of a new optional property
* Addition of metadata/documentation
* Addition of a new shapes

A breaking change for an existing shape would be:
* Addition of a new mandatory field 
* Change of cardinality rules of existing properties
* Change of target class mappings

If validation rules need to change for a published shape that would constitute a breaking change, a new shape should be created.

## Contributor Checklist

Before submitting your PR, ensure:

* [ ] The correct domain file is used or created
* [ ] No existing shapes are modified in a breaking way
* [ ] Naming conventions are followed
* [ ] The shape validates successfully
* [ ] Descriptive metadata is included


## Human Consensus Process

In addition to the contribution process described above, there is an important **human consensus** step that we are still refining. 

If a PR introduces a shape that overlaps conceptually with an existing one, we will ask contributors to collaborate with the current maintainer(s) of that shape, aiming to align on a shared model where possible.

If alignment is reached, contributors should work together to evolve the existing shape. If not, both shapes can continue to be maintained independently.

If you have feedback on this process, please raise it in the **[GitHub discussion](https://github.com/solid/shapes/discussions/20)**.




