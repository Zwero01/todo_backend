from src.schema.tasks import TaskBase


def item_to_task(item: TaskBase) -> dict:
    task = {"id": item.id, "description": item.description, "category": item.category, "deadline": item.deadline,
            "name": item.name}
    return task
