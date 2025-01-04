import pytest
from src.todo import add_task, load_tasks, save_tasks


def test_add_task():
    save_tasks([])  # Clear tasks before the test
    add_task("Test task")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Test task"
    assert tasks[0]["done"] == False
