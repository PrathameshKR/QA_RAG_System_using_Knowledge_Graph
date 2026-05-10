import json
import os

FILE_PATH = "kg_data.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(triples):
    with open(FILE_PATH, "w") as f:
        json.dump(triples, f, indent=2)
    
def update_knowledge_graph(new_triples):
    existing = load_data()

    # convert to set for duplicate check
    existing_set = {
        (t["subject"], t["relation"], t["object"], t["time"])
        for t in existing
    }

    for t in new_triples:
        key = (t["subject"], t["relation"], t["object"], t["time"])

        if key not in existing_set:
            existing.append(t)

    save_data(existing)

    return existing