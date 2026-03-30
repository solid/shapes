# Solid SHACL Shapes Catalogue

The *Solid SHACL Shapes Catalogue* is a collection of domain-specific **SHACL** validation shapes used across the Solid ecosystem.

**Application developers are invited to find, modify, and submit their own SHACL shapes to this repository for existing and new domains through a guided GitHub peer review (PR) process.**

## Background

Solid ([https://solidproject.org](https://solidproject.org)) is a project aiming to give individuals control over their own data. Solid aims to decouple applications from user data. SHACL shapes act as contracts between applications, allowing apps to validate, discover, and reuse common data models when interacting with user data stored in Solid Pods.

## Purpose

The *Solid SHACL Shapes Catalogue* supports interoperability by:

* Allowing applications to validate user data before reading or writing to Pods
* Enabling discovery of common semantic models
* Supporting mapping between different data schemas
* Encouraging reuse of domain vocabularies across Solid applications

The catalogue acts as a coordination layer for decentralized data exchange without sacrificing semantic consistency.

## Repository Structure

SHACL shapes are organised in a single flat directory structure, in the [/shapes](/shapes/) folder. Each file corresponds to a semantic domain or vocabulary. There are no sub-folders.

### Domain Shapes

Domain shapes define the semantic model of data — they describe what the data represents. Example domains include: address, person, organisation, contact, e.g. [/shapes/address.ttl](/shapes/address.ttl)

### Vocabulary Mapping Shapes

Vocabulary shapes map external ontologies to SHACL validation shapes, e.g. [/shapes/vcard.ttl](/shapes/vcard.ttl)

## Design Principles

The Solid Shapes Catalogue follows a set of design principles to support interoperability, reuse, and long-term stability across the Solid ecosystem.

### Interoperability First

Shapes prioritise interoperability between Solid applications rather than strict validation. Overly strict validation can prevent applications from reading or writing compatible data across Pods. Shapes therefore favour flexible structures that allow different clients to operate safely on shared data.

### Domain-Oriented Organisation

Shapes are organised by semantic domain rather than by application or implementation. Each domain file represents a conceptual data entity, e,g. address. This keeps shapes discoverable and avoids fragmentation across the catalogue.

### Vocabulary Reuse

Shapes reuse well-known vocabularies wherever possible rather than inventing new terms, e.g. vCard, FOAF, Schema.org. Reusing established vocabularies improves compatibility with the broader Linked Data ecosystem.

### Self-Contained Shapes

Shapes are be understandable without requiring extensive external context. A shape definition clearly describes the target class, the properties being validated and the intended structure of the data. This makes shapes easier to reuse across applications.

### Application Neutrality

Shapes describe **data structure**, not **application behaviour**. Application-specific business rules should be implemented by individual clients rather than embedded in shared validation shapes. This ensures that shapes remain reusable across the Solid ecosystem.

### Stable Contracts

Shapes function act as contracts between applications and user data. Once published they remain stable so that applications can rely on consistent validation behaviour. See the **[Shape Immutability Policy](./CONTRIBUTING.md)** section for details on how shapes evolve over time.

## License

All content in this repository, including contributions, is subject to the repository's MIT license.

## Governance

Contributions are subject to peer review governance processes.

