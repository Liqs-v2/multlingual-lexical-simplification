# ALEXSIS
ALEXSIS:  A Dataset for Benchmarking Lexical Simplification for Spanish

## Description

The ALEXSIS Spanish Dataset for Lexical Simplification contains 381 instances. Each instance is composed by a sentence, a target complex word, and 25 candidate substitutions. The dataset format is similar to that of LexMturk (Horn et al., 2014) but in ALEXSIS the sentences are not tokenized. 
A total of 380 instances of the 381 have only 1 appearance of the complex word in the sentence.
There is only one instance with two appearances of the complex word in the sentence. This is the case of the instance in line 263.
The special sentence is: "Limita al norte con el paraje Árbol Solo, al sur con el paraje San Vicente, al este con la localidad de San Andrés y al oeste con el Canal San Martín." The complex word is "paraje". The first appearance of the complex word "paraje" was the one marked in bold for the annotators.

The instances have the following format in UTF8:

\<SENTENCE\>\<TAB\>\<COMPLEX_WORD_IN_SENTENCE\>\<TAB\>\<SUBSTITUTION_1\>\<TAB\>...\<TAB\>\<SUBSTITUTION_25\><br/>

See below an instance of the dataset.

\_\_\_\_\_\_\_\_\_\_<br/>
Sufrió una importante reducción en su capacidad para poder acogerse a las normas de la FIFA para los estadios de fútbol. acogerse adaptarse sumarse incorporarse obedecer apegarse adaptarse adaptarse ampararse ampararse adaptarse apegarse aceptar asimilarse adaptarse aplicarse aceptarse incorporarse refugiarse amparar recurrir aceptar refugiarse cumplir con adaptarse admitirse<br/>
\_\_\_\_\_\_\_\_\_\_<br/>

The ALEXSIS Spanish Dataset for Lexical Simplification can also be found at github:  [https://github.com/LaSTUS-TALN-UPF/ALEXSIS](https://github.com/LaSTUS-TALN-UPF/ALEXSIS) <br/>
<br/>


## Citation

If you make use of the ALEXSIS dataset for Spanish, please cite the following paper:

Daniel Ferrés and Horacio Saggion.<br/>
[ALEXSIS: A Dataset for Lexical Simplification in Spanish.](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.383.pdf)<br/>
Proceedings of the Language Resources and Evaluation Conference (LREC) 2022.<br/>

[Link to the bibtex format file in bib format](http://www.lrec-conf.org/proceedings/lrec2022/bib/2022.lrec-1.383.bib)

```console
@inproceedings{ferres-saggion@LREC2022,
    title = "ALEXSIS: A Dataset for Lexical Simplification in Spanish.",
    author = "Ferrés, Daniel  and Saggion, Horacio",
    booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
    month          = {June},
    year           = {2022},
    address        = {Marseille, France},
    publisher      = {European Language Resources Association},
    pages     = {3582--3594},
    url       = {https://aclanthology.org/2022.lrec-1.383}
}
```

 <br/>


The ALEXSIS dataset is also published at Zenodo:<br/> [https://doi.org/10.5281/zenodo.5837149](https://doi.org/10.5281/zenodo.5837149)


## Related Work

### TSAR-2022 Shared Task on Lexical Simplification

ALEXSIS has been used in the [TSAR-2022 Shared Task on Lexical Simplification](https://taln.upf.edu/pages/tsar2022-st/) as a dataset to evaluate Lexical Simplification systems in Spanish.
12 instances were used in the trial-dataset and 368 instances were used in the test dataset. The instance with two appearances of the complex word was not used.
In this evaluation the systems were evaluated with the 368 instances of the TSAR-ES test dataset.
[https://github.com/LaSTUS-TALN-UPF/TSAR-2022-Shared-Task](https://github.com/LaSTUS-TALN-UPF/TSAR-2022-Shared-Task)


### Experiments with ALEXSIS and similar datasets for English and Portuguese (ALEXSIS-PT)

A paper describing the compilation of the TSAR-2022 Shared Task datasets for English, Portuguese (ALEXSIS-PT) and Spanish (ALEXSIS) that includes several experiments with two state-of-the-art approaches for Lexical Simplification has been published at this link:
https://www.frontiersin.org/articles/10.3389/frai.2022.991242
In this paper two approaches (LSBert (Qiang et al., 2021) adapted for Spanish and TUNER (Ferrés et al., 2017)) were evaluated with the 381 instances of the ALEXSIS dataset.

[Lexical Simplification Benchmarks for English, Portuguese, and Spanish](https://www.frontiersin.org/articles/10.3389/frai.2022.991242).<br/>
Sanja Štajner, Daniel Ferrés, Matthew Shardlow, Kai North, Marcos Zampieri and  Horacio Saggion.<br/>
Front. Artif. Intell. Sec. Natural Language Processing. <br/>
doi: 10.3389/frai.2022.991242



## References

Ferrés, D., Saggion, H., and Gómez Guinovart, X. (2017b).<br/>
An adaptable lexical simplification architecture for Major Ibero-Romance languages. <br/>
In Proceedings of the First Workshop on Building Linguistically Generalizable
NLP Systems (Copenhagen: Association for Computational Linguistics), 40–47.<br/>
doi: 10.18653/v1/W17-5406

Horn, C., Manduca, C., and Kauchak, D. (2014). <br/>
Learning a Lexical Simplifier Using Wikipedia. <br/>
In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 458–463, Baltimore, Maryland, June. Association for Computational Linguistics.

LexMturk dataset: [https://cs.pomona.edu/~dkauchak/simplification/lex.mturk.14/lex.mturk.14.tar.gz](https://cs.pomona.edu/~dkauchak/simplification/lex.mturk.14/lex.mturk.14.tar.gz)


J. Qiang, Y. Li, Y. Zhu, Y. Yuan, Y. Shi and X. Wu.<br/>
LSBert: Lexical Simplification Based on BER.<br/>
In IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 3064-3076, 2021<br/>
doi: 10.1109/TASLP.2021.3111589.


## Licence

The ALEXSIS dataset is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License CC-BY-NC-SA-4.0.




## Contact

LaSTUS lab at TALN at UPF (Universitat Pompeu Fabra)

Daniel Ferrés - daniel.ferres[at]upf.edu <br/>
Horacio Saggion - horacio.saggion[at]upf.edu   (corresponding author)

ConMuTeS project Link: [https://www.upf.edu/web/conmutes](https://www.upf.edu/web/conmutes)


## Acknowledgements

- ConMuTeS project: Context-aware Multilingual Text Simplification (ConMuTeS) PID2019-109066GB-I00/AEI/10.13039/501100011033
- Ministerio de Ciencia, Innovación y Universidades (MCIU) of Spain
- Agencia Estatal de Investigación (AEI) of Spain
