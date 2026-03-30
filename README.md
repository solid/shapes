# Solid SHACL Shapes Catalogue

The *Solid SHACL Shapes Catalogue* is a collection of domain-specific **SHACL** validation shapes used across the Solid ecosystem.

**Application developers are invited to find, modify, and submit their own SHACL shapes to this repository for existing and new domains through a guided GitHub peer review (PR) process.**

If you have feedback on this process, please raise it in the **[GitHub discussion](https://github.com/solid/shapes/discussions/20)**.

## Background

Solid ([https://solidproject.org](https://solidproject.org)) is a project aiming to give individuals control over their own data. Solid aims to decouple applications from user data. SHACL shapes act as contracts between applications, allowing apps to validate, discover, and reuse common data models when interacting with user data stored in Solid Pods.

## Purpose

The *Solid SHACL Shapes Catalogue* supports interoperability and is designed to:

* Provide a space for the community to converge on the data models used across applications – declared using SHACL shapes
* Build up a collection of well-understood, reusable shape patterns
* Enable a collaborative review process where shapes can be compared and discussed transparently
* Support artefact generation from shapes, including object abstractions in Javascript, data validators (using SHACL engines), and forms.
* Offer visibility into existing shapes to encourage reuse, reduce duplication, contributor recognition, and help new participants get started more easily


## Repository Structure

SHACL shapes are organised in a single flat directory structure, in the [/shapes](/shapes/) folder. Each file corresponds to a semantic domain or vocabulary. There are no sub-folders.

The repository contains shapes that we know are already used within the Solid ecosystem – including shapes based on the data models used by SolidOS, organised by semantic domain e.g. [/shapes/address.ttl](/shapes/address.ttl) and vocabulary e.g. [/shapes/vcard.ttl](/shapes/vcard.ttl). [Contributions from the community](./CONTRIBUTING.md) of shapes in use in the Solid ecosystem, as well as feedback are very much welcomed.

## Contributing Shapes 

See the **[guidelines for contributing](./CONTRIBUTING.md)**. 

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

