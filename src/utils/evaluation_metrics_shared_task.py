# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.

def mean_average_precision_at_k(substitues, gold_standard, k=10):
    """
    Calculates the mean average precision at k.

    Args:
        substitues (List[str]): The list of substitutes.
        gold_standard (List[str]): The list of gold standard substitutes.
        k (int): The value of k.

    Returns:
        float: The mean average precision at k.
    """
    return sum(average_precision_at_k(substitues, gold_standard, k) for substitues, gold_standard in zip(substitues, gold_standard)) / len(substitues)

def average_precision_at_k(substitues, gold_standard, k=10):

    """
    Calculates the average precision at k.

    Args:
        substitues (List[str]): The list of substitutes.
        gold_standard (List[str]): The list of gold standard substitutes.
        k (int): The value of k.

    Returns:
        float: The average precision at k.
    """ 
    if len(substitues) > k:
        substitues = substitues[:k]

    score = 0.0
    num_hits = 0.0

    for i, substitute in enumerate(substitues):
        if substitute in gold_standard and substitute not in substitues[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)
    
    if not gold_standard:
        return 0.0
    
    return score / min(len(gold_standard), k)    

def potential_at_k(substitues, gold_standard, k=10):
    """
    Calculates the potential at k.

    Args:
        substitues (List[str]): The list of substitutes.
        gold_standard (List[str]): The list of gold standard substitutes.
        k (int): The value of k.

    Returns:
        float: The potential at k.
    """
    # TODO: Implement the calculation
    pass


def accuracy_at_k_top_1(substitues, gold_standard, k):
    """
    Calculates the accuracy at k at top 1.

    Args:
        k (int): The value of k.

    Returns:
        float: The accuracy at k at top 1.
    """
    # TODO: Implement the calculation
    pass
