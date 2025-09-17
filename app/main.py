from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None or "first_name" not in user:
            first = user["full_name"].strip().split()[0]
            user["first_name"] = first
