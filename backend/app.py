from flask import Flask, request, jsonify
from neo4j import GraphDatabase
from langchain_groq import ChatGroq
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Flask app initialization
app = Flask(__name__)
CORS(app)

# Neo4j credentials and initialization
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
)

# LangChain and ChatGroq initialization
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

# Initialize GraphCypherQAChain
chain = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True  # Enable this for complex queries
)

# Define API routes
@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        natural_language_query = data.get("query")

        if not natural_language_query:
            return jsonify({"error": "Query is required"}), 400

        # Invoke the chain with the natural language query
        response = chain.invoke({"query": natural_language_query})

        return jsonify({"response": response}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/examples', methods=['GET'])
def examples():
    examples_list = [
        {"question": "Find the actor with the highest number of movies in the database."},
        {"question": "Who is the director of the movie Casino?"},
        {"question": "Which actors have acted together in Jumanji?"},
        {"question": "What is the genre of the movie Toy Story?"},
        {"question": "What are the movies that Martin Scorsese directed?"},
        {"question": "What are the actors of movie Sabrina"},
        

    ]
    return jsonify({"examples": examples_list}), 200


if __name__ == '__main__':
    app.run(debug=True)
