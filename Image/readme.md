### Best Practices for Image Generations and Associated Models


1. [Dreambooth training](https://huggingface.co/blog/dreambooth) Best Practices:


   a. Effect of Schedulers : DDIM

   b. Fine-tuned text encoder much better than Frozen
   
   c. Using Prior Preservation gives somewhat better results for faces
   
   d. High learning rates and too many training steps will lead to overfitting. The model will mostly generate images from your training data, no matter what prompt is used.
   
   e. Low learning rates and too few steps will lead to underfitting: the model will not be able to generate the concept we were trying to incorporate.     
   f. Faces are harder to train. In our experiments, a learning rate of 2e-6 with 400 training steps works well for objects but faces required 1e-6 (or 2e-6) with ~1200 steps.
   



