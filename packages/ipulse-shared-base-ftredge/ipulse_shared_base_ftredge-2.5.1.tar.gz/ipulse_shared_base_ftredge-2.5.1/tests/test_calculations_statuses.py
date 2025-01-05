import unittest
from ipulse_shared_base_ftredge import (ProgressStatus,
                                        evaluate_combined_progress_status,
                                            calculate_progress_statuses_breakdown
                                        )

class TestCalculationsStatuses(unittest.TestCase):

    def test_evaluate_combined_progress_status_not_started_with_done(self):
        statuses = [ProgressStatus.NOT_STARTED, ProgressStatus.DONE]
        result = evaluate_combined_progress_status(statuses)
        self.assertEqual(result, ProgressStatus.IN_PROGRESS)

    def test_evaluate_combined_progress_status_unfinished_with_issues(self):
        statuses = [ProgressStatus.UNFINISHED, ProgressStatus.FINISHED_WITH_ISSUES]
        result = evaluate_combined_progress_status(statuses)
        self.assertEqual(result, ProgressStatus.FAILED)

    def test_evaluate_combined_progress_status_highest_priority(self):
        statuses = [ProgressStatus.IN_PROGRESS, ProgressStatus.DONE_WITH_WARNINGS]
        result = evaluate_combined_progress_status(statuses)
        self.assertEqual(result, ProgressStatus.IN_PROGRESS)

    def test_calculate_progress_statuses_breakdown(self):
        statuses = [
            ProgressStatus.NOT_STARTED,
            ProgressStatus.DONE,
            ProgressStatus.DONE_WITH_WARNINGS,
            ProgressStatus.UNFINISHED,
            ProgressStatus.FINISHED_WITH_ISSUES
        ]
        result = calculate_progress_statuses_breakdown(statuses)
        expected_result = {
            'detailed': {
                'NOT_STARTED': 1,
                'DONE': 1,
                'DONE_WITH_WARNINGS': 1,
                'UNFINISHED': 1,
                'FINISHED_WITH_ISSUES': 1
            },
            'by_category': {
                'pending_statuses':1,
                'success_statuses':2,
                'issue_statuses':2,
                'closed_statuses':4,
                'closed_or_skipped_statuses':4
            },
            'total_statuses': 5
        }


        print("Result : ",result)
        self.assertEqual(result, expected_result)

    def test_calculate_progress_statuses_breakdown_empty(self):
        statuses = []
        result = calculate_progress_statuses_breakdown(statuses)
        expected_result = {
            'detailed': {},
            'by_category': {},
            'total_statuses': 0
        }
        self.assertEqual(result, expected_result)

    def test_evaluate_combined_progress_status_all_done(self):
        statuses = [ProgressStatus.DONE, ProgressStatus.DONE]
        result = evaluate_combined_progress_status(statuses)
        self.assertEqual(result, ProgressStatus.DONE)

    def test_evaluate_combined_progress_status_all_not_started(self):
        statuses = [ProgressStatus.NOT_STARTED, ProgressStatus.NOT_STARTED]
        result = evaluate_combined_progress_status(statuses)
        self.assertEqual(result, ProgressStatus.NOT_STARTED)

    def test_calculate_progress_statuses_breakdown_mixed(self):
        statuses = [
            ProgressStatus.NOT_STARTED,
            ProgressStatus.IN_PROGRESS,
            ProgressStatus.DONE,
            ProgressStatus.FAILED,
            ProgressStatus.FINISHED_WITH_ISSUES
        ]
        result = calculate_progress_statuses_breakdown(statuses)
        expected_result = {
            'detailed': {
                'NOT_STARTED': 1,
                'IN_PROGRESS': 1,
                'DONE': 1,
                'FAILED': 1,
                'FINISHED_WITH_ISSUES': 1
            },
            'by_category': {
                'pending_statuses':2,
                'success_statuses':1,
                'issue_statuses':2,
                'closed_statuses':3,
                'closed_or_skipped_statuses':3
            },
            'total_statuses': 5
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()