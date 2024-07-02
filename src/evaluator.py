import utils.evaluation_metrics_shared_task as evaluation_metrics_shared_task

class Evaluator:
    """
    Provides evaluation functionality on a sample level. Every metric that is to be reported on the
    result of a benchmark should be computed in this class and returned in the 'evaluate' function.
    """

    # TODO Typing for args
    @classmethod
    def evaluate(cls, ground_truth_substitutions, predicted_substitutions):
        """
        Evaluates the predicted substitutions for a complex word with the provided ground truth
        substitutions with the metrics defined in the class.

        Args:
            ground_truth_substitutions: The ground truths which we evaluate with.
            predicted_substitutions: The model's substitution predictions. Might be an empty list.
            k: For evaluation metrics that require a top-k value. Specified how many of the substitutions
                to consider.
        Returns:
            Tuple containing all implemented metrics. Currently: Potential, Precision, Recall, F1, MAP@K, 
            Potential at K, Accuracy at K top 1  (in this order).
        """

        sample_potential = False
        sample_precision = 0
        sample_f1 = 0

        # Flatten the dict of gold standard substitutions
        ground_truth_substitutions = [word for sublist in ground_truth_substitutions.values() for word in sublist]

        # Check Potential & count Precision
        for prediction in predicted_substitutions:
            if any(prediction == values for values in ground_truth_substitutions):
                sample_potential = True
                sample_precision += 1
        sample_precision = sample_precision / len(predicted_substitutions) if len(predicted_substitutions) else 0

        # Calculate Recall
        true_positives = sum(1 for token in ground_truth_substitutions if token in predicted_substitutions)
        sample_recall = true_positives / len(ground_truth_substitutions) if ground_truth_substitutions else 0

        # Calculate F1
        if sample_precision + sample_recall != 0:
            sample_f1 = 2 * (sample_precision * sample_recall) / (sample_precision + sample_recall)

        #Calculate MAP@K
        map_at_1 = evaluation_metrics_shared_task.mean_average_precision_at_k(predicted_substitutions, ground_truth_substitutions, 1)
        map_at_5 = evaluation_metrics_shared_task.mean_average_precision_at_k(predicted_substitutions, ground_truth_substitutions, 5)
        map_at_10 = evaluation_metrics_shared_task.mean_average_precision_at_k(predicted_substitutions, ground_truth_substitutions, 10)

        #Calculate potential_at_k
        potential_at_1 = evaluation_metrics_shared_task.potential_at_k(predicted_substitutions, ground_truth_substitutions, 1)
        potential_at_5 = evaluation_metrics_shared_task.potential_at_k(predicted_substitutions, ground_truth_substitutions, 5)
        potential_at_10 = evaluation_metrics_shared_task.potential_at_k(predicted_substitutions, ground_truth_substitutions, 10)

        #Calculate accuracy_at_k_top_1
        accuracy_at_1_top_1 = evaluation_metrics_shared_task.accuracy_at_k_top_1(predicted_substitutions, ground_truth_substitutions, 1)
        accuracy_at_5_top_1 = evaluation_metrics_shared_task.accuracy_at_k_top_1(predicted_substitutions, ground_truth_substitutions, 5)
        accuracy_at_10_top_1 = evaluation_metrics_shared_task.accuracy_at_k_top_1(predicted_substitutions, ground_truth_substitutions, 10)

        return sample_potential, sample_precision, sample_recall, sample_f1, map_at_1, map_at_5, map_at_10,potential_at_1, potential_at_5, potential_at_10, accuracy_at_1_top_1, accuracy_at_5_top_1, accuracy_at_10_top_1