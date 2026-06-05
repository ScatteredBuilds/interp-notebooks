# Interpretability Experiments

Status: Learning experiments.

These experiments are small, runnable artifacts for building intuition about transformer internals.

They are not experiments on real model activations unless a file explicitly says so.

## Current Experiments

- `attention_routing_toy.py` - a toy attention calculation that shows how attention weights mix value information.

Saved output:

- `../outputs/attention_routing_toy_run.md`

## What This Folder Is For

- Turn written notes into small checks.
- Make assumptions visible.
- Separate toy intuition from real-model evidence.
- Practice writing limitations next to the experiment.

## Limitations

- The current experiment uses hand-written toy vectors.
- It does not inspect a trained transformer.
- It does not prove how a real attention head behaves.
- It is useful for intuition, not for model-specific claims.
