def format_temporal_context(G, paths):
    context = ""

    for path in paths:
        for i in range(len(path) - 1):
            subj = path[i]
            obj = path[i + 1]
            edge = G[subj][obj]

            context += f"{subj} --{edge['relation']}--> {obj} (time: {edge['time']})\n"

    return context