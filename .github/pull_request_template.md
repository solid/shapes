## Type of Contribution

What does this PR introduce?

### Domain File Change

* [ ] Adds a **new domain file**
* [ ] Updates an **existing domain file**
* [ ] No domain file changes

If this PR **updates an existing domain file**, what change does it introduce?

* [ ] Adds a **new SHACL shape**
* [ ] Adds **additional constraints to an existing shape** (non-breaking)
* [ ] Documentation or metadata only

If this PR **adds a new domain file**, what change does it introduce?

* [ ] Adds a **new SHACL shape**
* [ ] Documentation or metadata only



## Domain File Changes

If this PR **introduces or modifies a domain file**, describe it here.

**Domain file name:**

<!-- e.g., profile.ttl -->

### Domain Change Type

* [ ] New domain file
* [ ] Updates to existing domain file

### Purpose of the Domain

Explain what domain this file represents.

Examples:

* User profile data
* Contacts
* Messaging
* Application configuration

### How This Domain Is Intended To Be Used

Please describe:

* What **type of Solid data** this domain describes
* Which **applications or use cases** are expected to use it
* Whether this domain corresponds to an existing Solid ecosystem pattern



## Shape Immutability Policy

⚠️ **Existing published SHACL shapes are considered immutable.**

This means:

* Constraints in an existing shape **must not be modified or removed**.
* If behaviour needs to change, **a new shape (or versioned shape)** should be introduced.
* Existing shapes may only receive **non-breaking additions**, documentation improvements, or new shapes referencing them.

If this PR updates an existing shape, confirm the following:

* [ ] The change **does not alter existing constraints**
* [ ] The change **does not invalidate previously valid data**
* [ ] If behaviour needed to change, **a new shape has been introduced instead**

Explain how this PR complies with the immutability policy.



## Shape Changes

If this PR **adds or references SHACL shapes**, describe them here.

**Shape name(s):**

**Target class / node:**

**Files changed:**

### Change Type

* [ ] New shape definition
* [ ] New version of an existing shape
* [ ] Additional constraint(s) added (non-breaking)
* [ ] Documentation/comment updates only

### Description of the Shape Changes

Describe the change clearly and why it was needed.



## Motivation

Why is this change needed?

Questions to consider:

* What problem does this shape or domain solve?
* Is this required by a specific Solid app or ecosystem need?
* Is there an issue, proposal, or discussion related to it?

Related issue(s):



## Compatibility Impact

Does this change affect existing data or validation?

* [ ] Fully backwards compatible
* [ ] May cause new validation failures
* [ ] Breaking change

If breaking, explain the impact and possible migration steps.



## Example Data

### Valid Example

Example data that **should pass** validation.

```turtle
# example here
```

### Invalid Example

Example data that **should fail** validation.

```turtle
# example here
```

Explain briefly why the invalid example should fail.



## Validation

How were these shapes validated?

* [ ] Tested with a SHACL validator
* [ ] Tested against example data
* [ ] Tested with real Solid data
* [ ] Syntax checked

Tools used:



## Vocabulary Alignment

Does this shape rely on or align with existing vocabularies?

Examples:

* FOAF
* Schema.org
* ActivityStreams
* Other RDF vocabularies

Explain any deviations or extensions.



## Reviewer Checklist

* [ ] Immutability policy respected
* [ ] Domain usage is clearly described
* [ ] Shape definitions are clear
* [ ] Constraints are justified
* [ ] Examples demonstrate expected behaviour
* [ ] No unintended breaking changes



## Additional Notes

Anything else reviewers should know.
