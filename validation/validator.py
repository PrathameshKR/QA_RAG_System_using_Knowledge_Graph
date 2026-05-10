def schema_validation(triples):
    return [
        t for t in triples
        if all(k in t for k in ["subject", "relation", "object", "time"])
    ]

def remove_duplicates(triples):
    seen = set()
    unique = []

    for t in triples:
        key = (t["subject"], t["relation"], t["object"], t["time"])
        if key not in seen:
            seen.add(key)
            unique.append(t)

    return unique

def validate_triples(triples):
    triples = schema_validation(triples)
    triples = remove_duplicates(triples)
    return triples