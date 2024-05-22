# Discussion goals


# Input

- **Tobias**
    - Implemented architecture and first PoC with German BERT
        - There were 2 versions
        - https://huggingface.co/dbmdz/bert-base-german-cased
    - The Power of Scale for Parameter-Efficient Prompt Tuning
    Brian Lester Rami Al-Rfou Noah Constant
    Google Research
        - Prompt tuning paper show that the learned prompts can be close to the domain of the task, making a strong case for the idea I had about prepending the domain of the sentence
    - Evaluation testdrive
        - Added BERT in english since BenchLS is implemented
        - Try to get a first idea of what our ballpark performance is
    - How many datasets and languages do we want to support.
        - Caro: Spanish seems good to add bc its a large language
        - Luis: DE-EN and modular architecture
        - Other languages more of a strech goal Caro
        - EN-DE support all common datasets to make as useful as possible
        - NNSeval
        - LexMturk
        - are they in BenchLs?
    - What do we want to support in the Benchmark Suite?
        - Uses n DataProviders and a LexicalSimplifier
        - Support as many

# Meeting outcomes

- Datasets
    - What are the most common benchmarks?
    - Support as many common ones as possible to make our suite as comparable as possible.
- BenchmarkSuite and architecture are agreed upon
    - BenchmarkSuite acts as “controller” and utilizes n DataProviders for m languages and a LexicalSimplifier that it benchmarks
    - The output is persisted via CSV or JSON
- Evaluation
    - Support metrics from shared task in addition to standard precision, recall, acc, f1