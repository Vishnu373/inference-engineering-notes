## Attention

Calculates a relevance score for each token against every other token.

- For each token: how relevant is this token to every other token?

**Example**

"The animal didn't cross the street because it was too tired."
Question: What does "it" refer to? The animal or the street?

Attention scores for "it":

- "it" vs "The"    -> low score
- "it" vs "animal" -> HIGH score
- "it" vs "street" -> medium score
- "it" vs "tired"  -> high score

Answer: "it" refers to animal.

"it" is ambiguous in isolation. Attention solves it by looking at the full context and determining where "it" is most strongly connected.
Same word, different sentence -> different attention score -> different meaning.

## Self-Attention Inputs

For each token, three values are computed:

- Query -> what the token is searching for
- Key -> what the token says it is (like a label or tag)
- Value -> what the token actually gives out (the content)

## Attention Score Equation

Step 1: Dot product (Q vs K)

- score = Q · K
- High result -> they're similar -> high relevance
- Low result -> they're different -> low relevance
- Dot product -> multiply each element and sum them up

Step 2: Scale it down

- Large scores cause problems in softmax, so divide by √d (square root of vector size)
- score = (Q · K) / √d

Step 3: Apply softmax

- Converts all scores into probabilities (0 to 1)
- All scores sum to 1

Example:

- "it" vs "animal" -> 0.5
- "it" vs "tired"  -> 0.3
- "it" vs "street" -> 0.1
- "it" vs "the"    -> 0.1

Step 4: Multiply by V

- output = 0.5 × V_animal + 0.3 × V_tired + 0.1 × V_street + 0.1 × V_the
- Final output for "it" is a weighted blend of all Values
- Token with the highest score contributes the most — that's how the model resolves what "it" refers to

## Full Formula

- Attention(Q, K, V) = softmax(Q · K / √d) × V
