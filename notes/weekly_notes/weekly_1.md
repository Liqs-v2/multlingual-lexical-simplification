# Meeting goals

- 1-2 main ideas and directions to pursue
- Tasks until Monday

# Research input & discussion

## Luis

LLM-Enh Adv Gen Paper is mostly an architecture

Not that much of an E2E solution, more finicky

Re-implementation of this papers architecture could be a good start because we dont require parallel data

Even worse in foreign language

No concrete approaches or direction for how to improve their architecture

Try to work on one submodule

There was no code for the paper provided, how would a re-implementation factor into our workload and evaluation?

## Caro

Mostly in English

Spanish and french, etc difficult because we dont speak it

How do we still perform multilingual?

Papers werent super detailed

## Tobias

Overall: Largest lever is CWI. Low hanging fruit improve prompting for LLM guidance and utilization (domain-awareness). Distill into SLMs via adapters to improve compute and latency. Model contextual calibration to improve loss.

- Adapter for BERT in the Difficulty Aware SG module
- Adapter or different base for Edit Generator
    - CWI is where we seemingly have the most upside potential
- Use LLM or SLM ensemble to discriminate Edit Suggestions to generate dataset
- Issues I see with this architecture is probably a huge latency and the fact that it can only work on one sentence at a time, where each sentence require one API call to OpenAI
    - SLM that is fine tuned with adapters (Zhang et.al)
- Instead of saying simple and complex use the language guidelines (A, B, C)
    - Get data this way?
- Interesting open research avenue: How do we get a high precision
    - Methods usually overestimate amount of complex words
    - What matters most for actual use cases? Probably recall.
- Good parts/modules, but maybe architecture can be improved, since overall performance is quite a bit worse than that of the individual parts
- Prompting helped the difficulty aware SG module a lot, perhaps investigate better prompts
    - Improve context by specifying the domain
    - In typical applications this would be known
    - In real life, we would basically never want to simplify a single sentence **without context**
    - One-Shot approach with synonymy from databases given the context/domain
        - You are a “doctor, nurse, engineer, waiter” answering a repeat question to a “non-native, person with autism”.
    - Tags as an input instead of just Masking → Provides rationale
        - Actually the way they use this in the Text Simplification Tagging paper is mostly bc of what they already had, dont see a value add in having a tag for each word
    - Integrate heuristic enhanced prompts
    - Self-discover ablation to build optimal prompt for CWI
- Do we want to explore allowing removal of tokens instead of limiting to replacement?
    - What is Miriams take on this?
- Contextual calibration can significantly improve LLM accuracy, very useful for LLM guided loss because we are better at avoiding confusion at the loss.
- Contextual calibration in LSBert for CWI, or a span based approach to use the entire tokenization of a word.
- How does LLM enhanced Adv. Gen. perform on TSAR-2022?
- **Research Avenues (related)**
    - **(**Text) style transfer
    - Simplification
    - Adversarial Settings
    - Reasoning
    - Prompting

# Takeaways

- There was no code for the paper provided, how would a re-implementation factor into our workload and evaluation?
- Directions
    - Smaller and knowledge distillation (Adapters, open-source small LM)
    - Prompting improvements (Uni HD)
- SOTA is Prompting LLMs, but that costs money and needs compute, we have neither
- Even the paper provided uses an LLM call, so even re-implementing that is problematic
- OS-LLMs still need resources that are difficult to obtain and some of the properties of LLMs only emerge at >100B params which we cant fit into Colab

## Condensed

Two Options:

1. Improve State of the Art (without big new implementation):
    - Need compute / money since essentially SOTA is prompting SOTA Models
    
    ⇒ Mainly Prompt Engineering (Personal Learning might be small) 
    
2. Implement small-scale technical solution (without improving State of the Art):
    - Personal Learning might be more productive but SOTA will not be improved

⇒ Problem: SOTA will not be improved without compute / money because prompting SOTA models outperform all other technical approaches
