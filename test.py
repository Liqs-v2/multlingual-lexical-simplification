from typing import List
from tqdm import tqdm

import numpy as np
from evaluation_metrics_shared_task import potential_at_k

def test_potential_at_10(substitues:List[str], gold_standard:List[str]):
    k = 10
    return potential_at_k(substitues, gold_standard, k)

def test_potential_at_5(substitues:List[str], gold_standard:List[str]):
    k = 5
    return potential_at_k(substitues, gold_standard, k) 

def test_potential_at_1(substitues:List[str], gold_standard:List[str]):
    k = 1
    return potential_at_k(substitues, gold_standard, k) 

def evaluate(benchmark_data: np.ndarray):
        potential_at_k = 0

        for sample in tqdm(benchmark_data, desc='Benchmarking'):
            sentence = sample[0]
            complex_word = sample[1]
            ground_truth_substitutions = sample[3]

            # To easily capture implementations not supporting a specific number of substitutions,
            # we do not pass top_k here and simply use the default in those cases.
            predicted_substitutions = self.testee_model.generate_substitutions_for(complex_word, sentence)
                                
def run_tests(substitues:List[str], gold_standard:List[str]):
    print("Potential at 10: ", test_potential_at_10(substitues, gold_standard))
    print("Potential at 5: ", test_potential_at_5(substitues, gold_standard))
    print("Potential at 1: ", test_potential_at_1(substitues, gold_standard))




