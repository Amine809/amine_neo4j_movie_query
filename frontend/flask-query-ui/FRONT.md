# Frontend for Amine Tanit Project

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
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/amine_tanit.git
   cd frontend
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
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
















