# Backend for Amine Tanit Project

## Overview
The backend is built using **Flask** and **Neo4j** to serve REST API endpoints for interacting with a graph database. This project integrates **LangChain** and **ChatGroq** to provide query functionalities over the Neo4j database.

## Features
- **Flask-based Backend**: A lightweight web framework to build RESTful APIs.
- **Neo4j Integration**: Connects to the Neo4j graph database to perform queries and retrieve data.
- **LangChain**: Utilizes LangChain for query chains and handling Cypher queries efficiently.
- **ChatGroq**: A plugin to support advanced language model queries.
- **Flask-CORS**: Cross-Origin Resource Sharing (CORS) for API security.

## Prerequisites
Before running this backend, ensure you have:
- **Python** (version 3.8 or above) installed.
- **Neo4j** running locally at `bolt://localhost:7687`.
- **Groq API Key** from your ChatGroq provider.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/amine_tanit.git
   cd backend
   ```
2. Set up virtual environment:
   ```bash
   venv\Scripts\activate
   ```
3. Install dependencies :
   ```bash
   pip install -r requirements.txt

   ```
## Configuration
Create a `.env` file in the `backend` folder with the following environment variables:
```bash
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=######
GROQ_API_KEY=######
```
## Running the backend
1. Start the flask server
```bash
python app.py
```
## API endpoints:
**1)Query Endpoints**
- **POST `/query`**: 
  - **Description**: Accepts natural language queries and returns results from the Neo4j graph.
  - **Request**:JSON payload with a "query" key.
  - **Response**: JSON containing the query results.
**2)Examples Endpoint**
- **GET `/examples`**
  - **Description**: Provides sample queries that can be used with the /query endpoint.
