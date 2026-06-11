# Transformer Interpretability Learning Notes

This repository is a beginner-friendly workspace for learning transformer interpretability concepts by building small, readable artifacts.

The focus is practical intuition for software engineers: understand what transformer components are doing, learn what evidence can and cannot show, and develop careful habits before moving into more advanced interpretability workflows.

This repository contains learning notes and small notebook artifacts focused on understanding transformer internals. It does not claim interpretability expertise.

## Project Status

Status: Active learning project.

Current focus:

- Attention heads as information-routing components.
- Residual stream as the running representation that layers read from and write to.
- Careful wording around what attention patterns and residual stream explanations can and cannot prove.

## Learning Goals

- Build a clear mental model of core transformer components.
- Learn how to inspect model behavior without overclaiming.
- Connect diagrams, toy examples, and written notes into reusable study artifacts.
- Practice separating useful interpretability evidence from incomplete explanations.

## Current Artifacts

- `notebooks/01_attention_heads.ipynb` - beginner intuition for attention heads and attention patterns using toy examples and careful caveats.
- `notes/attention_heads.md` - study notes on attention-head terms, common misconceptions, and why attention patterns are useful but incomplete evidence.
- `notes/residual_stream.md` - study notes on the residual stream, including how layers read from it, write to it, and why model-specific details need verification.
- `experiments/attention_routing_toy.py` - a runnable toy calculation showing how attention weights can mix value information.
- `outputs/attention_routing_toy_run.md` - saved output from the toy attention-routing experiment.

## Limitations

- The repository currently contains learning notes and one markdown-focused notebook, not a full interpretability research project.
- The notebook and current experiment use toy examples rather than experiments on model activations.
- The notes mark some model-specific claims with `TODO: VERIFY`.
- The repository does not yet include reproducible code for inspecting a real model.
- The current artifacts are beginner-oriented and should not be presented as expert-level interpretability work.
