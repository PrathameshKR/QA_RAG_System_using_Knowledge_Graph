def map_query_to_entity(query, nodes):
    query = query.lower()

    for node in nodes:
        if node.lower() in query:
            return node

    return None