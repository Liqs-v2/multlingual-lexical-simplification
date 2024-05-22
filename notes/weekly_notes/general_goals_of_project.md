High Level Overview:

1. General Setup
    1. Setup GitLab with GoogleColab (GitHub works easy, idk how GitLab does)
2. Evaluation Pipeline
    
    Goal: “One-Click” Pipeline which takes an **implemented system** and **automatically evaluates** its **performance on a metric**
    
    1. Choose suitable Metric
    2. Choose suitable Test Dataset
    3. Define Framework specifying how a systems I/O has to look for the evaluation Pipeline to work
    4. Implement (Notebook/Entrypoint?) to the Evaluation Pipeline
3. Architecture
    
    Goal: Have some **fixed Model/System I/O** so we can **quickly iterate on different models/architectures** and evaluate them all with the **same pipeline**
    
    1. First “Architecture”: **Proof of Concept** and starting point to integrate Architecture and Evaluation: Just use **TinyLlama/GermanBERT from HF and a simple prompt**
        
        ⇒ not expected to perform well, just to get our system up and running
        
    2. Fine-Tune small models on “leichte Sprache” and “LS”
    3. Adapt principles from Miriams initial Paper