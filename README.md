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
- **Literature reports results on distinct datasets and different metrics**, making comparability difficult
- Proprietary models exhibit SOTA performance with simple prompt engineering techniques, but their **cost and privacy issues** make their use in public domain projects difficult

# Approach
We have decided to focus on the last two pain points and build a comprehensive benchmarking suite to **speed up research** 
by reducing the need to re-implement boilerplate code.

This empowers researchers to easily benchmark their approaches on common datasets and metrics,
enabling comparability with a wide range of literature. 

Furthermore, we **evaluate existing approaches on open-source models** to
enable transfer of SOTA techniques to production with Free Open-Source (FOS) models. We aim find a "working" approach that does not have SOTA performance but adds value to the community.

With our benchmarking suite in place, we investigate whether we can improve lexical simplification performance by ...

- **Fine-tuning** open-source models on lexical simplification datasets of other language datasets. We call this approach Leave-One-Out Cross-Validation (LOOCV) training.
- **Enhancing** the prompt with the topics or domain of the sentence to provide additional context.
- **Evaluate** the performance of GPT-4o, BERT-based models and Phi-3 on the lexical simplification task.

## How to use the system
We recommend running the code in Google Colab or using a GPU to speed up inference. In particular the notebooks are designed to
be run in Google Colab. The stability of the notebooks is not guaranteed on local machines.

### Setup Environment
We use Anaconda as a dependency manager and provide our `environment.yml`. You can setup the local environment by running:
- `conda env create -n multilingual-lexical-simplification-benchmarking -f environment.yml`
- `conda activate multilingual-lexical-simplification-benchmarking`
- To verify the installation, run ``conda env list``

### System Architecture
Our system consists of three core components:
1. `LexicalSimplifier` interface
2. `DataProvider` interface
3. `BenchmarkSuite` class

``LexicalSimplifier`` is an interface that defines the methods that a lexical simplifier must implement. It is used to abstract the implementation of the simplification model from the evaluation pipeline. This allows us to easily swap out different models and compare their performance.

``DataProvider`` is an interface that defines the methods that a data provider must implement. It is used to abstract the implementation of the data loading and preprocessing from the evaluation pipeline. This allows us to easily swap out different datasets and evaluate a models performance in a unified manner across all provided datasets.

``BenchmarkSuite`` is a class that is used to evaluate the performance of a lexical simplifier. The class constructor takes 
- a ``LexicalSimplifier``, the `testee_model`
- a dictionary of ``language_configurations``, the keys of which are the languages that the model is evaluated on (see the `Language` class) and the value is a dictionary specifying the configuration. A configuration consists of a `pattern` which is used to generate a `prompt` by the `LexicalSimplifier` and `exemplars`, which are prepended to the prompt for `few-shot` prompting.
- a boolean flag ``should_pass_topc`` to toggle topic aware prompting. **This is currently only supported for English.**

To summarize, the `BenchmarkSuite` class is the controller of our system and supports language specific configurations of prompts, including exemplars. Currently, we **benchmark a model on available datasets of a language, if the language is present in the configuration**.

Supported Languages and datasets are:

- English: BenchLS, LexMTurk, NNseval, TsarEN
- German: Germeval, Our new synthetic dataset
- Spanish: Alexsis
- Portuguese: PorSimplesSent

**Adding a new dataset**

To add a new dataset to our evaluation framework, simply implement the ``DataProvider`` interface in your dataset by inheriting from it. Then, add the dataset to the ``_AVAILABLE_DATASETS`` dictionary in the ``BenchmarkSuite`` class. The evaluation pipeline will automatically pick up the new dataset and evaluate the model on it. If your dataset is of a new language,
you must also add the language to the ``Language`` class and a new language to the `_AVAILABLE_DATASETS` dictionary in the `BenchmarkSuite` class.

**Adding a new model wrapper**

To add a new model wrapper to our evaluation framework, for example to benchmark your new, custom architecture on the provided datasets, simply inherit from the `LexicalSimplifier` interface and implement the required methods. Then, pass an instance of your model to the `BenchmarkSuite` class with your desired configuration and run the benchmark suite.


### Evaluation Pipeline: The ``BenchmarkSuite`` class
We provide a ``main.py`` script that demonstrates how to use the ``BenchmarkSuite`` class to evaluate a text-generation LM locally using our `LLMLexicalSimplifier` wrapper. Note that if you want to evaluate a remote LLM, use the `GPTLexicalSimplifier` wrapper instead.
Since the script runs locally, we use DistilGPT2 in our example, the performance of this model is quite poor and this is expected. For a more realistic evaluation, we recommend running the script in Google Colab, using a more potent model and a GPU.

### Provided Notebooks
The **notebooks provided by us are for documentation purposes only** in the context of the lab course that this project was developed. Except for the following notebooks, which also serve as demonstrations for potential users, we make no guarantee of the stability of the implementation:
- ``topic_aware_substitutions.ipynb``: Demonstrates how to use the topic aware substitutions feature for English, also shows that our system is able to dynamically toggle topic awareness between English and other languages.
- `evaluation_experimentation.ipynb`: Demonstrates how to use the `BenchmarkSuite` class to evaluate the Phi-3 LLM and a fill-mask BERT model.

## Investigated models
### German
- [GermanBERT](https://huggingface.co/dbmdz/bert-base-german-cased)
- [DistilGermanBERT](https://huggingface.co/distilbert/distilbert-base-german-cased): Distilled version of the above model
### English
- [BERT](https://huggingface.co/google-bert/bert-base-cased)
### Multilingual
- [BERT multilingual](https://huggingface.co/google-bert/bert-base-multilingual-cased)
- [Distilbert multilingual](https://huggingface.co/distilbert/distilbert-base-multilingual-cased)
- [XLM-RoBERTa](https://huggingface.co/FacebookAI/xlm-roberta-base)
### Finetuned
- [Distillbert multilingual ft DE (LeiKo)](https://huggingface.co/lusxvr/distilbert-base-multilingual-cased-finetuned-leiko)
- [Distillbert multilingual ft EN, PT, ES](https://huggingface.co/lusxvr/distilbert-base-multilingual-cased-finetuned-en_pt_es)
- [Distillbert multilingual ft EN, DE, PT](https://huggingface.co/lusxvr/distilbert-base-multilingual-cased-finetuned-en_de_pt)
- [Distillbert multilingual ft EN, DE, ES](https://huggingface.co/lusxvr/distilbert-base-multilingual-cased-finetuned-en_de_es)
- [Distillbert multilingual ft DE, PT, ES](https://huggingface.co/lusxvr/distilbert-base-multilingual-cased-finetuned-de_pt_es)

## Note on use of AI in this project
Generative AI assistants (e.g., GitHub Copilot, JetBrains AI Assistant) were used in the development of this project. The use of AI assistants was limited to code completion and refactoring tasks. The AI assistants were not used to generate any core logic or algorithms in this project. The use of AI assistants was limited to the following tasks:
- Code completion
- Generation of documentation templates