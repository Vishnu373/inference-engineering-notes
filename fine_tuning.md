# Fine Tuning

Taking a pre-trained foundation model and adapting it to a specific use case by introducing new data. Changes the model weights while the model architecture remains the same.

If you can fine-tune a small model to pass your evals, you set yourself up for an easier time hitting your latency and cost targets for inference.

## Why Small Fine-Tuned Models Win on Inference

Small models are faster and cheaper to run than large ones. Smaller models have fewer parameters → less computation per forward pass:

- Less data moving through the network
- Fewer matrix multiplications
- Less memory bandwidth needed

All of this means the model generates each token faster, which directly reduces latency.
