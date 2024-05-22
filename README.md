# Multilingual lexical simplification
Lexical simplification aims at replacing single words with their simpler synonyms. The MLSP shared tasks provides resources for lexical simplification across many languages. In this project, we use these resources to build our own pipelines. The project gives great opportunities to contribute to the latest research problems with your own ideas!

## Students
* Ganahl, Carolin
* Lindenbauer, Tobias
* Wiedmann, Luis

## Task description
We will use the material provided by the [MLSP Shared Task](https://sites.google.com/view/mlsp-sharedtask-2024). Although the task is already over, you can still create your owm pipelines and compare them to winning models.  
Have a look at their task description and provided material. Then come up with your own ideas how you could takle the problem of lexical simplification.

## Recommended literature
- [An LLM-Enhanced Adversarial Editing System for Lexical Simplification](https://arxiv.org/abs/2402.14704)

## Identified pain points
- Datasets are small and of mixed quality
- Proprietary models exhibit SOTA performance with simple prompt engineering techniques, but their **cost and privacy issues** make their use in public domain projects difficult

# Approach
We have decided to focus on the latter pain point and build a comprehensive benchmarking suite to **speed up research** 
by reducing the need to re-implement boilerplate code and **evaluate existing approaches on open-source models** to
enable transfer of SOTA techniques to production.

With, we aim find a "working" approach that does not have SOTA performance but adds value to the community.

## Goals
1. set up an evaluation pipeline: How does performance change when using small open-source models or incorporating more complex architectures?
2. iterations of the architectures:
    1. models: 
        1. GermanBERT
        2. phi-3
        3. tinyLlama
    2. architectures:
        1. prompting only e.g. "Identify and replace the difficult word in this sentence with an easier synonym: ..."
        2. fine-tuning of the underlying model with easy language dataset (https://live.european-language-grid.eu/catalogue/corpus/22646/overview/)
        3. fine-tuning of the underlying model with Lexical Substitution Dataset (https://live.european-language-grid.eu/catalogue/corpus/14292/download/)
        4. adaptation of "**An LLM-Enhanced Adversarial Editing System for Lexical Simplification "**
    
    ⇒ should be realisable with existing resources
    
    ⇒ Combinations of different models / architectures that we can iterate and benchmark through the evaluation pipeline
    
    ⇒ Does a low resource / open source approach make sense for the specific task
    
    Outcome: Comparison of the performance of systems consisting of small models 
    
    (model alone vs. fine-tuning vs. architecture enhancements vs. combinations of all)

Translated with DeepL.com (free version)