import json


def clean_json(text):
    return text.replace("```json", "").replace("```", "").strip()


def compute_diff(old_file, new_data):
    try:
        with open(old_file, "r") as f:
            old_data = json.load(f)
    except:
        return {"status": "No previous data"}

    changes = {}

    for comp in new_data:
        if comp not in old_data.get("competitor_insights", {}):
            changes[comp] = "New competitor added"
        elif new_data[comp] != old_data["competitor_insights"][comp]:
            changes[comp] = "Updated insights"

    return changes if changes else {"status": "No changes detected"}