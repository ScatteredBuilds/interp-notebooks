# Attention Heads Study Notes

## Key Terms

- **Token:** A chunk of text the model processes, such as a word, word part, punctuation mark, or special marker.
- **Attention head:** A small routing mechanism inside a transformer layer that lets each token gather information from other tokens.
- **Query:** What the current token is looking for.
- **Key:** What each token offers as a match target.
- **Value:** The information that gets copied or mixed in when a token is attended to.
- **Attention pattern:** A table or heatmap showing which tokens attend to which other tokens.
- **Multi-head attention:** Many attention heads running in parallel, each able to learn a different information-routing pattern.
- **Residual stream:** The shared information channel that carries updated token representations through the transformer.

## Important Ideas

- Attention heads are easier to think about as routing components than as full reasoning components.
- An attention head does not usually produce a human-readable fact by itself. It moves information from some token positions into other token positions.
- Multiple heads let the model track several relationships at once, such as nearby words, matching punctuation, subject-object relationships, or repeated tokens.
- Attention patterns are useful evidence because they show where information may be moving.
- Attention patterns are incomplete evidence because they do not show how the moved information is used later.
- A high attention score is not automatically an explanation. It is a clue that needs context.

## Common Misconceptions

- **Misconception:** Attention is the same thing as explanation.
  **Correction:** Attention shows possible information flow, not the full cause of an output.

- **Misconception:** One attention head equals one clean human concept.
  **Correction:** Some heads have interpretable patterns, but many are mixed, context-dependent, or hard to name.

- **Misconception:** The model only attends to important words.
  **Correction:** A token may attend to punctuation, position markers, repeated words, or structural tokens for reasons that are not obvious from reading the sentence.

- **Misconception:** If a token attends strongly to another token, that other token caused the final answer.
  **Correction:** Attention is one step in a larger computation. Later layers can amplify, transform, ignore, or overwrite the information.

- **Misconception:** More heads always means more understandable behavior.
  **Correction:** More heads gives the model more routing capacity, but it can also make behavior harder to inspect.

## Why Attention Is Useful but Incomplete

Attention is useful for interpretability because it gives a visible handle on information movement. If a token attends to another token, the model may be routing information from the attended token into the current token's representation.

But attention does not provide a complete explanation of model behavior. It does not show the exact content being moved, how later layers use that content, or whether the attention pattern was necessary for the final output. Treat attention as a map of possible routes, not as the whole story.

## Questions for Future Investigation

- How stable are attention patterns across similar prompts?
- Which heads show simple, repeated patterns across many examples?
- When does an attention pattern reflect syntax, position, repeated tokens, or task-specific behavior?
- How does information from an attention head interact with the residual stream?
- What kinds of behavior can be understood from attention alone, and what requires looking at later computations?
- How can beginner-friendly visualizations avoid implying that attention is a complete explanation?
