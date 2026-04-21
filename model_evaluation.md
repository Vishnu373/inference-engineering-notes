# Model evaluation or evals
measuring model intelligence.
- **Intelligence** = "how well the model performs on your specific use case?"
- Does it answer correctly, consistently, and reliably for your product.

Eg:- Does your customer service bot actually resolve issues correctly?

High conviction model evaluation is a prerequisite for inference engineering.
**High conviction** = you trust your eval results enough to make real decisions based on them. Like — "I'm confident enough in these results to switch from GPT-4 to Llama and deploy it to production."

How evals help inference engineers?
- Evals helps in ensuring that the model is useful.
- Require a baseline to compare against. Because some performance optimization techniques reduce model quality.
- Evals are tailored to specific products, domains, and tasks.

Tips for doing useful model evaluation:-
**Look at your data**
Don't just trust the numbers blindly. If the eval says the model is 95% accurate but your gut says the answers feel wrong — investigate. Your product intuition matters.

**Be precise**
Don't test everything generically. Find the hardest, most critical scenarios specific to your use case and focus eval there. A customer service bot should be tested on the trickiest customer complaints, not easy generic questions.

**Use tools**
Eval is a solved-enough problem — frameworks like RAGAS, LangSmith, Braintrust already exist. Don't build your own from scratch. Focus your energy on what's unique to your product.