import pytest
from src.utils import load_tasks, save_tasks, clear_tasks, get_task_count


def test_save_and_load_tasks():
    # Clear tasks before the test
    clear_tasks()

    # Save a test task and check if it loads correctly
    test_tasks = [{"task": "Test Task", "done": False}]
    save_tasks(test_tasks)
    tasks = load_tasks()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Test Task"
    assert tasks[0]["done"] == False


def test_clear_tasks():
    # Clear tasks and check the count
    save_tasks([{"task": "Sample Task", "done": False}])
    clear_tasks()
    assert get_task_count() == 0


def test_get_task_count():
    # Verify task count is accurate
    clear_tasks()
    save_tasks([{"task": "Task 1", "done": False}, {"task": "Task 2", "done": True}])
    assert get_task_count() == 2
