# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.

def mean_average_precision_at_k(substitues, gold_standard, k):
    """
    Calculates the mean average precision at k.

    Args:
        substitues (List[str]): The list of substitutes.
        gold_standard (List[str]): The list of gold standard substitutes.
        k (int): The value of k.

    Returns:
        float: The mean average precision at k.
    """

    if len(substitues) > 0:
        return sum(average_precision_at_k(substitues, gold_standard, k) for substitues, gold_standard in zip(substitues, gold_standard)) / len(substitues)
    else:
        return 0

def average_precision_at_k(substitues, gold_standard, k):

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
    
    if k == 1:
        print(score / min(len(gold_standard),k))
    return score / min(len(gold_standard), k)    

def potential_at_k(substitues, gold_standard, k):
    """
    Calculates the potential at k.

    Args:
        substitues (List[str]): The list of substitutes.
        gold_standard (List[str]): The list of gold standard substitutes.
        k (int): The value of k.

    Returns:
        bool: The potential at k.
    """
    if len(substitues) > k:
        substitues = substitues[:k]

    for substitute in substitues:
        if any (substitute== value for value in gold_standard):
            return True   
        
    return False


def accuracy_at_k_top_1(substitues, gold_standard, k):
    """
    Calculates the accuracy at k at top 1.

    Args:
        substitues (List[str]): The list of substitutes.
        gold_standard (List[str]): The list of gold standard substitutes.
        k (int): The value of k.

    Returns:
        bool: The accuracy at k at top 1.
    """
    if len(substitues) > k:
        substitues = substitues[:k] 
    
    return gold_standard[0] in substitues
