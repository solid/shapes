# Solid SHACL Shapes Catalogue

The *Solid SHACL Shapes Catalogue* is a collection of domain-specific **SHACL** validation shapes used across the Solid ecosystem.

**Application developers are invited to find, modify, and submit their own SHACL shapes to this repository for existing and new domains through a guided GitHub peer review (PR) process.**



## Background

Solid ([https://solidproject.org](https://solidproject.org)) is a project aiming to give individuals control over their own data.

Solid aims to decouple applications from user data. SHACL shapes act as contracts between applications, allowing apps to validate, discover, and reuse common data models when interacting with user data stored in Solid Pods.


## Purpose

The *Solid SHACL Shapes Catalogue* supports interoperability by:

* Allowing applications to validate user data before reading or writing to Pods
* Enabling discovery of common semantic models
* Supporting mapping between different data schemas
* Encouraging reuse of domain vocabularies across Solid applications

The catalogue acts as a coordination layer for decentralized data exchange without sacrificing semantic consistency.


## Repository Structure

SHACL Shapes are all contained in a single flat organisational structure in .ttl files under the /shapes directory.

- SHACL shape files are contain in the [/shapes](/shapes/) folder 
- Shapes are separated by domain or vocabulary identifier into separate .ttl files
- There should be no sub-folders

### Domain Shapes

Domain shapes define the semantic model of data — they describe what the data represents.

Example domains include:

* address
* person
* organisation
* contact

Example path for the address domain in this catalogue:

[/shapes/address.ttl](/shapes/address.ttl)

### Vocabulary Mapping Shapes

Vocabulary shapes map external ontologies to SHACL validation shapes.

Example vocabularies include:

* vCard

Example path:

[/shapes/vcard.ttl](/shapes/vcard.ttl)

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

If a domain file does not exist, create a new file e.g.:

```
/shapes/{domain}.ttl
```

Rules:

* Domain names must be lowercase
* Domain names should be a minimal representation of the semantic concept

If using vocabularies, follow community ontology naming conventions. Check [https://prefix.cc](https://prefix.cc) if unsure.


## Naming Conventions

### Namespace Structure

Use the pattern:

```
https://solidproject.org/shapes/{domain}#
```

Examples:

```
https://solidproject.org/shapes/address#
https://solidproject.org/shapes/vcard#
```



### Prefix Naming

Prefix labels may use lowercase letters, hyphens, or underscores, but must begin with a letter.

Example:

```turtle
@prefix address-shape: <https://solidproject.org/shapes/address#> .
@prefix vcard-shape: <https://solidproject.org/shapes/vcard#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
```

### Shape Naming

Use descriptive PascalCase names ending in `Shape`.

Examples:

```
address-shape:AddressShape
vcard-shape:VCardAddressShape
```

## Multiple Shapes per Domain

Multiple shapes may exist for a single domain.

This should be handled using semantic variation rather than new namespaces.

Example:

```
address-shape:AddressShape
address-shape:AddressMinimalShape
```

## Validation Rules

Follow these guidelines:

- Prefer optional validation to maximise Pod interoperability
- Use `sh:minCount 0` when possible
- Keep constraints focused on structural validation
- Do not mix application business logic into core semantic shapes

## Shape Immutability Policy

Shapes published to this catalogue are treated as immutable.

Once a shape is merged into the repository and published:

- Shapes must not be modified in place
- Validation rules must not be changed retrospectively
- Structural or semantic changes must be introduced via new shapes

This ensures predictable behaviour for applications using Solid Pods.

### Why Shapes Are Immutable

Shapes function as contracts between applications and user data. Modifying a published shape could cause:

- Validation inconsistencies across applications
- Silent breaking changes in decentralized clients
- Data interoperability failures

Immutability ensures that applications can safely cache and reuse shapes.

### How to Evolve Shapes

If validation rules must change, create a new shape rather than modifying an existing one.

Recommended approaches:

#### Option 1 — Create a New Shape Variant

Example:

```
address-shape:AddressShape
address-shape:AddressStrictShape
```

### When Adding New Constraints

Do not:

- Add new mandatory fields to existing shapes
- Change cardinality rules of existing properties
- Change target class mappings

Instead:

- Introduce a new shape version or variant

Allowed changes:

- Adding new optional properties
- Adding documentation
- Adding new shapes


Below is a **Design Principles** section that fits naturally in your document (typically placed after **Purpose** or before **Repository Structure**). It stays consistent with the philosophy you already described (immutability, interoperability, domain organisation).

You can paste it directly.


## Design Principles

The Solid Shapes Catalogue follows a set of design principles to support interoperability, reuse, and long-term stability across the Solid ecosystem.

### Interoperability First

Shapes should prioritise interoperability between applications rather than strict validation.

Where possible:

- Prefer optional properties over mandatory ones
- Avoid over-constraining data structures
- Allow applications flexibility in how data is produced and consumed

The goal is to enable different Solid applications to safely read and write shared user data.

### Domain-Oriented Organisation

Shapes are organised by semantic domain rather than by application or implementation.

Each domain file represents a conceptual data entity such as:

- address
- person
- organisation
- meeting

This approach keeps shapes discoverable and avoids fragmentation across the catalogue.

### Vocabulary Reuse

Shapes should reuse existing well-known vocabularies wherever possible rather than inventing new terms.

Examples include:

- [vCard](https://www.w3.org/TR/vcard-rdf/)
- [FOAF](http://xmlns.com/foaf/spec/)
- [Schema.org](https://schema.org/)

Reusing existing vocabularies improves compatibility with the broader Linked Data ecosystem.

### Self-Contained Shapes

Shapes should be self-contained and understandable without requiring external dependencies whenever possible.

A shape definition should clearly describe:

- the target class
- the properties being validated
- the intended structure of the data

This makes shapes easier to reuse across applications.

### Shape Immutability

Published shapes are treated as immutable contracts. Once a shape has been merged into the catalogue:

- Its validation rules should not be modified
- Breaking changes must be introduced through new shapes
- Existing shapes remain available for backward compatibility

This ensures predictable behaviour for applications that depend on specific shapes.

### Evolution Through New Shapes

When validation requirements change, new shapes should be introduced rather than modifying existing ones. 

### Decentralised Application Compatibility

- Shapes should avoid embedding application-specific logic.
- A shape should describe **data structure**, not **application behaviour**.
- Business rules specific to an application should be implemented outside the shared catalogue.
- This ensures that shapes remain reusable across the broader Solid ecosystem.


## License

All content in this repository, including contributions, is subject to the repository's MIT license.

## Governance

Contributions are subject to peer review governance processes.

