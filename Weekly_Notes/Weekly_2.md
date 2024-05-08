# Discussion goals

- **Tobias**
    - Which area of the pipeline are we targeting? Often CWI and SG are split, such as in the shared task 2022. Do we want to tackle both or only one? Should we start off by focusing on only one? If so which?
        - In the context of Miriams tool, wherein users select or highlight words they do not understand, CWI might be superfluous
    - What is SOTA for LS in German? Did people try to adopt LSBert or the like?
    - Which German datasets exist? How are they structured? Do they have multiple complex words? How many substitution candidates do they provide?
    - Did I recall correctly that the two directions Miriam laid out were:
        - Distill and compress existing architecture
            - To detect if there is a suitable candidate, instead of finding the best we want to know if there would even be any
        - Generate a dataset for improved benchmarking

# Input

- **Tobias**
    - Systems are moving away from parallel datasets and exploring other ways for lexical simplification. How could datasets still be useful? → They are still heavily used for benchmarking and evaluation.
    - We could use a high precision system or existing corpus to get initial CWI and suggestions and then use contextual embedding to mine for more “similar” data in the web for which we can then also by default re-use the replacement suggestions and have atleast one annotation.
    - EU law and proceedings documents should be available in multiple European languages and be rather precisely aligned with respect to its contents.
    - Same for countries with multiple official languages (Switzerland)
    - Check for popular high quality news outlets that might offer articles in simplified language or official state media outlets
    - Generate substitutions using (ensemble) of systems and just verify
    - Seems like the paradigm is to have many substitution candidates that are somehow ranked and less complex words or even instances overall.
    - There is a gap regarding the size of these datasets in the mid-low 1000s or 100s. This isnt really enough for modern approaches tbh.
    - Found an EU funded and hosted database of language data resources
        - [European Language Grid](https://live.european-language-grid.eu/catalogue/?&language__term=German)
        - [Lexical Substitution Dataset for German](https://live.european-language-grid.eu/catalogue/corpus/14292/overview/)
        - [OSCAR project - EU language resource we could use for training BERThold](https://oscar-project.org/)
    - Yimam et al 2017 find that with their setup CWI is transferable across languages (EN-DE) with drops in performance of just 1-4%
    
    Languages that could be useful: Spanish, French, Portuguese, Chinese, but also smaller European languages
    
    Might also be interesting to see how the approaches differ based on the size of the language community.
    
    ### Questions
    
    - Which popular datasets in other languages are there?
        - ALEXSIS - Spanish
        - ALEXSIS-PT - Portuguese
        - PorSimples - Portuguese
        - FrenLys - French
        - New CWI Yimam et. al 2017 - English, German, Spanish
    - How were they created?
        - What are the different creation paradigms?
            - Basically always manually annotated complex words and suggestions: ALEXSIS, HanLS, FrenLys, CWI shared task 2018, PorSimples, ALEXSIS-PT (based on PorSimples), New CWI Yimam et. al 2017:
                - Expert linguists
                - MTurk
                - FrenLys: Semi-automatic, provide suggestions (in line with the active learning paradigm)
        - Abrahamsson et. al 2014 Medical text: Non-parallel corpus of medical journal articles → Synonym replacement with medical domain specific dictionary/mapping and compound split search via substrings
    - What makes a dataset good or bad?
        - Many correct instances
        - many substitutions that are ranked
    - What order of magnitude are the dataset sizes typically?
        - ALEXSIS - 381 instances - almost exclusively single complex words
        - LSEval and LexMTurk → BenchLS → NNSEval progressively combined and filtered
            - At most 2510 sentences
        - EASIER - 5130 instances, but only 575 with atleast 3 substitution suggestions
        - CWI shared task 2016 - 9200 instances
        - PorSimples - 2915
        - ALEXSIS-PT - 387 instances
- Caro
    - Synsets für Deutsch gesucht
    - Synset gefunden GermaSet mit “Rover”
        - Steht auch drinnen falls es kein Synonym gibt
        - Gibt Python API (https://germanetpy.readthedocs.io/en/latest/germanetpy.html#germanetpy-icbased-similarity-module)
        - Wurde bei lexical simplification wohl noch nirgends mit eingebaut
        - Kann mit Unilogin alles beantragen, aber API würde wsl reichen
    - Lexical and text simplification landscape nicht viel gefunden, eher auch synsets dann gesucht
    - Gab Zeug dass eben wie in Englisch ablief bei lexical simplification
    - Leichte Sprache nur mit Nachrichtendatenset
- Luis
    - Probleme Modelle laufen zu lassen für GOV anwendungen
        - Phi-3 (3B)
        - Tinylama (1.1B)
        - Nur auf Englisch trainiert → Finetunen für Deutsch möglich?
        - Sind auf HuggingFace → leicht zu testen?

# Meeting outcomes

- Architektur oder Datenset
    - Luis und Caro finden Datenset nicht so spannend
    - Caro deutsche Papers fast alle gleiche Architektur
        - Miriams papers alle GermanBERT alles crossreffed
    - Caro Datenset kann man mehr machen
- Was genau ist unser Ziel?
    - Tobias: Teil unserer Aufgabe ein Ziel zu definieren
        - Sollten definieren woran wir arbeiten ab jetzt, weil sonst kommen wir nirgends hin
        - Wir haben nur beschränkt Zeit und sonst haben wir kein Resultat
- Was wollen wir machen - Entscheidung
    - Caro: Datenset - Bei Architektur nicht viel zu holen
        - Deutlich höhere Wahrscheinlichkeit einen positiven Outcome
    - Luis: Architektur
        - Was bekommen wir mit OpenSource Modellen hin
        - Brauchen keine Fancy idee
        - Architektur nachbauen mit OS Modell
    - Tobias:
        - Architektur, was ist die research questions?
            - Schaffen wir mit OS und low-resource ein Produkt zu bauen das kompetitiv ist
            - Luis würde es iterativ angehen, implementieren und dann auf English benchmarken
                - Dann auf Deutsch finetunen
        - Datenset
            - Kann leicht im Ansatz stecken bleiben

### Entscheidung

Implementierung und Evaluation von open-source und low resource Lexical Simplification Pipeline.

Evaluation ob wir einen “funktionierenden” Ansatz finden der zwar nicht SOTA-Performance hat aber in der Community einen Mehrwert bringt.

Ansatz: 

1. Aufbau einer Evaluationspipeline: Wie verändert sich die Performance wenn man kleine open-source modele verwendet oder komplexere Architekturen einbaut
2. Iterationen der Architekturen:
    1. Modelle: 
        1. GermanBERT
        2. Phi-3
        3. TinyLlama
    2. Architekturen:
        1. Nur Prompting z.b. “Identifiziere und ersetze in diesem Satz das schwere Wort durch ein leichteres Synonym: …”
        2. Fine-tuning des underlying models mit Leichte Sprache Datenset (https://live.european-language-grid.eu/catalogue/corpus/22646/overview/)
        3. Fine-tuning des underlying models mit Lexical Substitution Datenset (https://live.european-language-grid.eu/catalogue/corpus/14292/download/)
        4. Adaption von "**An LLM-Enhanced Adversarial Editing System for Lexical Simplification”**
    
    ⇒ sollte umsetzbar mit vorhandenen Ressourcen sein
    
    ⇒ Kombinationen aus verschiedenen Modellen / Architekturen die wir iterieren können und durch die Evaluationspipeline benchmarken
    
    ⇒ Macht ein low resource / open source Ansatz für den Spezifischen Task Sinn
    
    Outcome: Vergleich der Performance von Systemen bestehend aus kleinen Modellen 
    
    (Modell alleine vs. Fine-Tuning vs. Architektur-Enhancements vs. Kombinationen von allem)
