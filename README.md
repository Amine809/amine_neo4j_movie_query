# Backend for Movie Neo4j Project

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
   git clone https://github.com/Amine809/amine_neo4j_movie_query.git
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
Create a `.env` file in the `backend` folder with the following environment variables,add your current neo4j crediantials and GROQ_API_KEY:
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
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Frontend for Amine Neo4j Project

## Overview
The frontend is built using **React** and **Material-UI** to create an interactive user interface that communicates with the backend API. It provides a seamless experience to query the Neo4j graph database via RESTful API endpoints, using **Flask** on the backend.

## Features
- **React Framework**: A powerful JavaScript library for building user interfaces.
- **Material-UI**: A popular React component library for designing beautiful, responsive UI components.
- **Flask Query UI**: React components that allow users to submit queries to the Flask backend and visualize results.
- **Responsive Design**: Ensures optimal viewing and interaction across various devices.
- **State Management**: Uses **React Hooks** and **Context API** for managing state effectively.

## Prerequisites
Before running this frontend, ensure you have:
- **Node.js** (version 20 or above) installed.
- **npm** (Node Package Manager) installed.

## Installation
1. Move to frontend folder and current react folder app :
   ```bash
   cd frontend
   cd flask-query-ui
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Starting the frontend server,keep flask app running to test results:
   ```bash
   npm start
   ```
## Feature explained
- **1)Query Interface:**
  - **Description**:A user-friendly interface that allows users to input natural language queries.
  - **Users input a query into the text box:**
    
    -Users input a query into the text box.

    
    -The query is sent via a POST request to the Flask backend.

    -The backend processes the query using Neo4j and returns the   results.

- **2)Responsive design:**
  - **Description**:The UI is designed to be responsive across various screen sizes (desktop, tablet, mobile).

- **3)Query example:**
```bash
{
    "query": "Which actors have acted together in the movie Jumanji?"
}


````
- **4)Response example:**
```bash
{
    "response": {
        "query": "Which actors have acted together in the movie Jumanji?",
        "result": "Bradley Pierce, Robin Williams, Kirsten Dunst, and Jonathan Hyde  have acted together in the movie Jumanji.  \n"
    }
}


````

## Dependencies Used:
-**React**: A JavaScript library for building user interfaces.

-**Material-UI**: A popular React component library for UI design.

-**axios:**: For making HTTP requests to the Flask backend.
















