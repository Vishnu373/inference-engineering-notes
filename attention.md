Attention:
Calculates a relevance score for each token against every other token.
- For each token, how relevant is this token to every other token?

**Example**

"The animal didn't cross the street because **it** was too tired."
Question: What does **"it"** refer to? The animal or the street?

Attention mechanism does the following:-
"it" vs "The"     → low score
"it" vs "animal"  → HIGH score  ✓
"it" vs "street"  → medium score
"it" vs "tired"   → high score

Answer: "it" refers to animal.

"it" is ambiguous in isolation. Attention solves it by looking at the full context (each and every other token) and determines where "it" is most strongly connected.
Same word, different sentence -> different attention score -> different meaning.

The self attention inputs:
For each token the following are calculated:-
- **Query** — what the token is **searching for**.
- **Key** — what the token **says it is** (tags/headings related)
- **Value** — what the token **actually gives out** (content inside those tags/headings)

Attention score equation:
Step 1: Dot product (Q vs K)
- score = Q · K
- High result → they're similar → high relevance  
- Low result → they're different → low relevance
Note: Dot product -> multiply each element and sum them up.

Step 2: Scale it down
- The scores can get very large, which causes problems later. So we divide by √d (square root of the vector size):
- score = (Q · K) / √d

Step 3: Apply softmax activation function
- Converts all scores into probabilities (0 to 1)
- All scores add up to 1

Example
"it" vs "animal" → 0.5
"it" vs "tired"  → 0.3
"it" vs "street" → 0.1
"it" vs "the"    → 0.1
0.5 + 0.3 + 0.1 + 0.1 = 1

Step 4: Multiply by V
- output = 0.5 × V_animal + 
		 0.3 × V_tired + 
		 0.1 × V_street +
		 0.1 × V_the
- This is the final output for "it" — a weighted blend of all Values.
	- The token with the highest score contributes the most to the final output. That's how the model determines what "it" is most strongly connected to.

Full formula:
Attention(Q, K, V) = softmax(Q·K / √d) × V