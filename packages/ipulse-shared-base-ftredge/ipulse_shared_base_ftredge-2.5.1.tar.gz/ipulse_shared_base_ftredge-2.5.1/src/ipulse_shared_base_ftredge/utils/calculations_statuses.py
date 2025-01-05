from collections import defaultdict
from typing import Any, Dict, List
from ipulse_shared_base_ftredge import ProgressStatus
import inspect


def evaluate_combined_progress_status(statuses: List[ProgressStatus]) -> ProgressStatus:
    """Determine the overall status based on child statuses"""
    
    # Handle specific combinatory cases
    if ProgressStatus.NOT_STARTED in statuses:
        if any(status in statuses for status in [
            ProgressStatus.DONE_WITH_WARNINGS,
            ProgressStatus.DONE_WITH_NOTICES,
            ProgressStatus.DONE
        ]):
            return ProgressStatus.IN_PROGRESS
    
    if ProgressStatus.UNFINISHED in statuses and ProgressStatus.FINISHED_WITH_ISSUES in statuses:
        return ProgressStatus.FAILED

    # Determine the highest priority status based on enum value
    highest_priority_status = max(statuses, key=lambda status: status.value)

    return highest_priority_status

def calculate_progress_statuses_breakdown(statuses: List[ProgressStatus]) -> Dict[str, Any]:
    """
    Calculate counts of statuses in a list.
    Returns a dictionary with detailed status counts and category breakdowns.

    Categories are based on ProgressStatus class methods like:
    - pending_statuses()
    - success_statuses()
    - closed_issue_statuses()
    etc.
    """

    # Known category method names and their readable labels
    category_methods = [
        ('pending_statuses', 'pending_statuses'),
        ('skipped_statuses', 'skipped_statuses'),
        ('success_statuses', 'success_statuses'),
        ('issue_statuses', 'issue_statuses'),
        ('closed_statuses', 'closed_statuses'),
        ('closed_or_skipped_statuses', 'closed_or_skipped_statuses')
    ]

    # Initialize counters
    status_counts = {
        'total_statuses': len(statuses),
        'detailed': defaultdict(int),
    }

    # Count individual statuses
    for status in statuses:
        status_counts['detailed'][status.name] += 1

    # We'll build the by_category dict separately
    by_category = {}

    # Count categories using direct method calls
    for method_name, category_label in category_methods:
        category_method = getattr(ProgressStatus, method_name)
        category_statuses = category_method()

        category_count = sum(1 for status in statuses if status in category_statuses)

        # Only include the category if it has a non-zero count
        if category_count > 0:
            by_category[category_label] = category_count

    return {
        'detailed': dict(status_counts['detailed']),
        'by_category': by_category,
        'total_statuses': status_counts['total_statuses']
    }