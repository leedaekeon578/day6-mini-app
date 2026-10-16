TASKS = [
    ("주간 보고서 초안 작성", "HIGH", False),
    ("회의 자료 정리", "MID", False),
    ("책상 정리", "LOW", False),
    ("이메일 답장", "HIGH", True),
]

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}


def get_pending_tasks(tasks):
    return [task for task in tasks if not task[2]]


def sort_tasks(tasks):
    return sorted(tasks, key=lambda task: PRIORITY_ORDER[task[1]])


def show_tasks(tasks):
    for title, priority, _ in tasks:
        print(f"[{priority}] {title}")


def main():
    show_tasks(sort_tasks(get_pending_tasks(TASKS)))


if __name__ == "__main__":
    main()
