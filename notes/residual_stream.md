# Residual Stream Study Notes

Status: Learning Note

Goal: Build an accurate mental model of the residual stream.

Reviewed: TODO

Open Questions: TODO

## Key Terms

- **Token representation:** The vector the model carries for one token position at a given point in the transformer.
- **Residual stream:** The running token representation that moves through the transformer as layers read from it and write updates back to it.
- **Layer:** A repeated processing step in a transformer. A layer usually includes attention and an MLP, plus normalization steps.
- **Read:** A component uses the current residual stream as input.
- **Write:** A component adds its output back into the residual stream.

TODO: VERIFY the exact layer order for a specific model before describing its residual stream in detail. Some models place normalization steps in different positions.

TODO: VERIFY whether components read directly from the residual stream or from a normalized version of it in the specific model being described.

## What The Residual Stream Is

The residual stream is the main path that carries each token's internal representation through the transformer.

A beginner mental model:

```text
token embedding
      |
      v
residual stream at layer 0
      |
      v
attention reads from it and writes an update
      |
      v
MLP reads from it and writes an update
      |
      v
residual stream at the next layer
```

Each token position has its own stream. In the sentence below, the model keeps a separate representation for each token position.

```text
The   cat   sat   because   it   was   tired   .
 |     |     |       |       |    |      |     |
 v     v     v       v       v    v      v     v
stream stream stream stream stream stream stream stream
```

The streams are not isolated forever. Attention can move information between token positions. After attention writes an update, the destination token's residual stream contains its previous representation plus the new routed information.

## Why Information Accumulates There

The residual stream accumulates information because transformer components usually add updates instead of replacing the whole token representation.

A simplified example:

```text
The cat sat because it was tired.
```

At the token `it`, the early representation may include information about the token itself and its position. Later attention may route information from `cat` into the `it` position. Later layers may add updates that could relate to local syntax, nearby context, or prediction-relevant information.

The result is not a clean checklist in plain English. It is a vector that has received many updates.

```text
representation for "it"
      |
      + token identity
      + position information
      + routed context from earlier tokens
      + later layer updates
```

This accumulation matters because later layers do not only see the latest component output. They receive the current residual stream, which includes previous updates that may later be cancelled, suppressed, transformed, or made harder to read.

TODO: VERIFY how much any specific feature remains available in a real model. The residual stream can carry information forward, but that does not prove a feature is cleanly represented or used later.

## How Layers Read From It

Attention heads and MLPs read from the residual stream.

For attention, reading can mean using the residual stream, or a normalized version of it, to form queries, keys, and values. In beginner terms:

```text
destination token stream -> what am I looking for?
source token streams ----> what can each source offer?
source token streams ----> what information might be moved?
```

For an MLP, reading means processing the current token representation at one position. The MLP does not decide which other token positions to inspect in the same direct way attention does. It works on the representation already present at that position.

Concrete example:

```text
Token: "tired"

Attention may read from earlier token streams and route information into "tired".
The MLP then reads the updated "tired" stream and writes another update.
```

The read step is important because a component can only use information that is present in, or reachable from, its input representation. For attention, information from other token positions is also subject to masking and architecture constraints.

## How Layers Write To It

Transformer components write by adding their outputs back into the residual stream.

Simplified:

```text
current residual stream
        +
component output
        =
updated residual stream
```

For attention, the written update may contain information routed from other token positions. For an MLP, the written update may transform information already present at the same token position.

Example:

```text
Before attention at "it":
"it" stream mostly reflects the token, position, and earlier updates.

Attention update:
information routed from "cat" may be added.

After attention:
"it" stream contains the previous stream plus the attention update.
```

This does not mean the model writes a readable fact like `it = cat`. A safer claim is that an attention update may add information from the `cat` position into the `it` position. Whether that information is used later requires more evidence.

## Why Interpretability Researchers Care

Interpretability researchers care about the residual stream because it is where many transformer components interact.

If an attention head routes information into a token position, later components usually receive that information through the residual stream. If an MLP changes a representation, later attention heads may read from the changed stream.

The residual stream helps frame careful questions:

- What information is present at this token position?
- Which earlier component may have added it?
- Which later component may read it?
- Does the model behavior depend on this information, or is it only present?

These questions keep claims narrower. An attention pattern may show a possible route. The residual stream asks the next question: what was written into the representation, and what happened to it later?

## Common Misconceptions

- **Misconception:** The residual stream is a memory bank with neat facts.
  **Correction:** It is a vector representation. Some information may be readable from it, but not always in a simple or human-labeled form.

- **Misconception:** If information is added once, it must stay important.
  **Correction:** Later components may ignore it, transform it, or add competing updates.

- **Misconception:** Attention explains the whole model because it writes to the residual stream.
  **Correction:** Attention is one kind of update. MLPs and later layers also read from and write to the stream.

- **Misconception:** The residual stream has one meaning for the whole sentence.
  **Correction:** Each token position has its own residual stream representation, and attention can move information between positions.

## Practical Rule

Use the residual stream as the place to track information flow through the transformer.

Attention helps ask where information may move from. The residual stream helps ask where that information is added, carried forward, and later read.

Attention patterns alone do not prove what information is being moved. They are a clue about possible routes.

## Questions For Future Investigation

- How do attention outputs become part of the residual stream in a specific model?
- Which later layers read information written by earlier attention heads?
- When does information remain available across many layers?
- How can a beginner inspect residual stream representations without overclaiming?
- What examples show the difference between information being present and information being used?

## References

- Neel Nanda: A Comprehensive Mechanistic Interpretability Explainer: https://www.neelnanda.io/mechanistic-interpretability/glossary
- Transformer Circuits: https://transformer-circuits.pub/
- Anthropic Interpretability Team: https://www.anthropic.com/research
- Attention Heads Study Notes in this repository
