# Solid Shapes Catalogue

The Solid Shapes Catalogue is a collection of domain-specific SHACL validation shapes used across the Solid ecosystem.

**Application developers are invited to find, modify, and submit their own SHACL shapes to this repository for existing and new domains through a guided GitHub peer review (PR) process.**



## Background

Solid ([https://solidproject.org](https://solidproject.org)) is a project aiming to give individuals control over their own data.

Solid aims to decouple applications from user data. SHACL shapes act as contracts between applications, allowing apps to validate, discover, and reuse common data models when interacting with user data stored in Solid Pods.


## Purpose

The Solid Shapes Catalogue supports interoperability by:

* Allowing applications to validate user data before reading or writing to Pods
* Enabling discovery of common semantic models
* Supporting mapping between different data schemas
* Encouraging reuse of domain vocabularies across Solid applications

The catalogue acts as a coordination layer for decentralized data exchange without sacrificing semantic consistency.


## Repository Structure

Shapes are organised by semantic domain and validation purpose.

```
/shapes
   /core
   /vocab
```



### Core Shapes

Core shapes define the semantic model of data — they describe what the data represents.

Example domains include:

* address
* person
* organisation
* contact

Example path:

```
/shapes/core/address.ttl
```



### Vocabulary Mapping Shapes

Vocabulary shapes map external ontologies to SHACL validation shapes.

Example vocabularies include:

* vCard

Example path:

```
/shapes/vocab/vcard.ttl
```

Vocabulary mapping improves interoperability between semantic models.



## Guidelines for Contributing

Contributions are welcome through GitHub pull requests (PR).

When contributing:

1. Check whether a domain file already exists
2. Follow naming conventions
3. Include documentation using the GitHub PR template provided
4. Ensure shapes validate before submitting



## Adding Shapes

### Existing Domains

Each domain in the repository should have its own `{domain}.ttl` file.

If a domain file exists, add your shape to that file where appropriate.

If a domain file does not exist, create a new file using:

```
/shapes/core/{domain}.ttl
```

or

```
/shapes/vocab/{domain}.ttl
```

Rules:

* Domain names must be lowercase
* Domain names should be a minimal representation of the semantic concept

If using vocabularies, follow community ontology naming conventions. Check [https://prefix.cc](https://prefix.cc) if unsure.



## Naming Conventions

### Namespace Structure

Use the pattern:

```
https://solid.github.io/shapes/{layer}/{domain}#
```

Examples:

```
https://solid.github.io/shapes/core/address#
https://solid.github.io/shapes/vocab/vcard#
```



### Prefix Naming

Prefix labels may use lowercase letters, hyphens, or underscores, but must begin with a letter.

Example:

```turtle
@prefix core-address: <https://solid.github.io/shapes/core/address#> .
@prefix vocab-vcard: <https://solid.github.io/shapes/vocab/vcard#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
```



### Shape Naming

Use descriptive PascalCase names ending in `Shape`.

Examples:

```
AddressShape
AddressMinimalShape
AddressStrictShape
VCardAddressShape
```

Avoid ambiguous or numeric naming such as:

```
Address1
AddrFinal
VCard2
```



## Multiple Shapes per Domain

Multiple shapes may exist for a single domain.

This should be handled using semantic variation rather than new namespaces.

Example:

```
core-address:AddressShape
core-address:AddressMinimalShape
core-address:AddressStrictShape
```

## Validation Rules

Follow these guidelines:

* Prefer optional validation to maximise Pod interoperability
* Use `sh:minCount 0` when possible
* Keep constraints focused on structural validation
* Do not mix application business logic into core semantic shapes


## Design Principles

The catalogue is built on the following principles:

* Core shapes define semantic meaning
* Vocabulary shapes provide ontology compatibility
* Shapes should be reusable across applications
* Validation should favour interoperability over strict enforcement



## License

All content in this repository, including contributions, is subject to the repository's MIT license.

## Governance

Contributions are subject to peer review governance processes.

