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
        {"question": "How many artists are there?"},
        {"question": "Which actors played in the movie Casino?"},
        {"question": "How many movies has Tom Hanks acted in?"},
        {"question": "List all the genres of the movie Schindler's List"},
        {"question": "Which actors have worked in movies from both the comedy and action genres?"},
        {"question": "Which directors have made movies with at least three different actors named 'John'?"},
        {"question": "Identify movies where directors also played a role in the film."},
        {"question": "Find the actor with the highest number of movies in the database."},
        {"question": "Which actors have acted in movies spanning at least three different genres?"},
    ]
    return jsonify({"examples": examples_list}), 200


if __name__ == '__main__':
    app.run(debug=True)
