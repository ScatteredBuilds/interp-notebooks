# Attention Routing Toy Run

Command:

```bash
python3 experiments/attention_routing_toy.py
```

Output:

```text
Toy sentence: The cat sat because it was tired.
Destination token: it

Note: value-vector labels are hand-written for this toy example.
They are not evidence about a trained model.

Case 1: focused attention toward cat
====================================
Top attention weights:
- cat: 0.634
- tired: 0.064
- sat: 0.057
- The: 0.052

Weighted value update:
- animal: 0.643
- action: 0.051
- state: 0.068
- syntax: 0.184

Case 2: mixed attention toward cat and tired
============================================
Top attention weights:
- cat: 0.395
- tired: 0.323
- sat: 0.053
- The: 0.048

Weighted value update:
- animal: 0.404
- action: 0.047
- state: 0.328
- syntax: 0.178

Observation
===========
The attention weights show where value information is read from.
The weighted update shows one simple way that information can mix.
The weights alone do not prove what information was moved or used later.
```
