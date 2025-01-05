# Cypher-Pilot
CypherPilot is a Python library designed to interface with a Neo4j database, enabling users to query the database and export results in CSV format. It is composed of the following main classes:
Gate: A high-level class for generating and executing queries.
Logger: A singleton class for logging messages and errors.
Service: A class that manages exceptions and error handling.
Controller: Coordinates interactions between components such as the database operator, query builder, data extractor, and repository.
Neo4jOpr: Handles connection and querying of the Neo4j database.
QueryBuilder: Constructs dynamic Cypher queries for Neo4j based on user input.
Repository: Stores data retrieved from the database for future use.
Extractor: Extracts data and writes it to CSV files.

Features:
Query Execution: Generate and execute complex queries on a Neo4j database.
Data Retrieval: Retrieve data from the database based on user-defined parameters.
CSV Export: Extract query results into CSV format.
Logging: Centralized logging for debugging and monitoring.

Requirements:
Ensure that the following Python libraries are installed:
neo4j: For interacting with the Neo4j database.
logging: Built-in Python module for logging.
Python 3.x

Data Transfer Standard for the Project:
Creating an Instance of the Gate Class:

Create an instance of the Gate class from the Presentation package, passing the database connection details (uri, user, password) as parameters.
Relevant Function in the Gate Class:

The Gate class has a function named query that receives parameters to generate a Cypher query, save it in the repository, and export it to CSV.
Function Input Standard: The query function accepts a list with the following parameters:

Source Label
Target Label
List of Source Data Properties
List of Target Data Properties
Full Path (True/False)
File Name
Comments (optional)
The query function will return a list of Neo4j Record objects or an exception if the input is invalid.

Usage Example:
Example 1:
gate = Gate(uri="bolt://localhost:7687", user="neo4j", password="qwerty")
param = ["cve", "cpe", ["original_id"], ["metadata_vendor", "metadata_product", "original_id"], False, "sample1"]
results = gate.query(param)
print(results)


CSV output:
Original_id_cve,metadata_vendor_cpe,metadata_product_cpe,original_id_cpe

Example 2:
gate = Gate(uri="bolt://localhost:7687", user="neo4j", password="qwerty")
param = ["cwe", None, ["original_id", "_key"], [], False, "sample2"]
results = gate.query(param)
print(results)

Example 3:
gate = Gate(uri="bolt://localhost:7687", user="neo4j", password="qwerty")
param = ["technique", "cve", ["original_id", "metadata_description"], ["original_id", "metadata_description"], True, "sample3"]
results = gate.query(param)
print(results)

Example 4:
gate = Gate(uri="bolt://localhost:7687", user="neo4j", password="qwerty")
param = ["nodes"]
results = gate.query(param)
print(results)

Example 5:
gate = Gate(uri="bolt://localhost:7687", user="neo4j", password="qwerty")
param = ["edges"]
results = gate.query(param)
print(results)
Notes:
Only one connection to the database is required for every use of the library.
Data must adhere to the input standard to avoid errors.
Each query execution returns a list of Neo4j Record objects and generates a corresponding CSV file.
If no results are returned, an empty list and CSV document will be generated.


Query Configuration Parameters:
A dictionary stores configurations or settings for graph, pathfinding, or network-related operations.

Explanation of each key:
startNode: Represents the starting node for the operation.
relatedlabels: A list of related labels (node types).
source_columns: Columns related to the starting node that should appear in the CSV.
target_columns: Columns related to the target node that should appear in the CSV.
flag_full_path: Boolean flag to indicate whether the full path should be considered.
name: A name associated with the query being processed.
asapath: Indicates whether a specific path type should be used.
limit: A value to limit the number of results.
numberoflayers: Controls the number of layers or depth levels to traverse during the operation.




Installation:
To install the CypherPilot library, follow these steps:

Clone the repository or download the package.
Install required dependencies using:
pip install -r requirements.txt
You can now use the library to interact with your Neo4j database!

