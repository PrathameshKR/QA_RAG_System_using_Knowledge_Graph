from extraction.llm_extractor import extract_triples
from validation.validator import validate_triples
from graph.builder import build_graph
from retrieval.query_mapper import map_query_to_entity
from retrieval.reasoning import get_paths, format_paths
from rag.graph_rag import generate_answer
from utils.storage import update_knowledge_graph

def run():
    text = """
    Reaction turbines work by channeling a fluid through a set of blades that expand the fluid,
    converting pressure into force on the blades. Each blade receives the same load. 
    A reaction turbine can have multiple sets of rotors, called stages, that are optimized for the pressure in that part of the fluid flow.
    The most visible types of reaction turbines are wind turbines and gas turbines used for jet engines. 
    Most steam turbines and natural gas power turbines are reaction turbines. 
    Reaction turbines use a shroud or case to position the fluid flow through the turbine blades. 
    The flow in reaction turbines undergoes a significant pressure drop as the fluid moves through the turbine.
    """

    year = "2021"

    # Step 1: Extract
    triples = extract_triples(text, year)

    # Step 2: Validate
    triples = validate_triples(triples)

    all_triples = update_knowledge_graph(triples)

    print("Triples:", triples)

    # Step 3: Build Graph
    G = build_graph(all_triples)

    # Step 4: Query
    query = "What are types of Reaction Turbines?"

    entity = map_query_to_entity(query, G.nodes)

    if not entity:
        print("No entity found")
        return

    paths = get_paths(G, entity)
    context = format_paths(G, paths)

    print("\nReasoning Paths:\n", context)

    # Step 5: Graph-RAG
    answer = generate_answer(query, context)

    print("\nFinal Answer:\n", answer)

if __name__ == "__main__":
    run()