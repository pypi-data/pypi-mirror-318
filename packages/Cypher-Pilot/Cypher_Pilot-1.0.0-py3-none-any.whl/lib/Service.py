import json
from Domain.Controller import Controller
from Logger import Logger


class Service:
    """
    This class interacts with the Controller class to manage database interactions and data processing.
    It provides methods for initializing the database connection,querying data, saving it,
    extracting it to CSV, and retrieving data from the repository. handles with exceptions and decides what to do in case of it.
    """

    def __init__(self,uri,user,password):
        """
        This is the constructor for the Service class. It initializes
        the Controller and Logger objects using the provided connection parameters for the database.
         :param uri:(str) The URI for the Neo4j database
        :param user: (str) The username for authentication
        :param password:(str) The password for authentication
        """
        self.controller = Controller(uri,user,password)
        self.logger = Logger().get_logger()  # Initialize logger

    def init_DB(self):
        """
        This method initializes the database connection by calling the initialize_DB method from the Controller class.
        Logs the success or failure of the initialization process.
        """
        self.logger.debug("Entering initDB method.")
        try:
            self.controller.initialize_DB()
            self.logger.info("Database connection initialized successfully.")
        except Exception as e:
            self.logger.exception(f"Error initializing database: {str(e)}")
            return None

    def get_by_param(self, dict):
        """
        This method retrieves data based on parameters provided in the dict.
        It calls the get_by_param method in the Controller class, retrieves the results,
        and saves the data to the repository. It logs the success or failure of the data retrieval process.
        :param dict:A dictionary containing the parameters for the query. It should include a "name" key, which is used to save the data.
        :return: The result of the query, in format of list fill with containing objects of type Record of Neo4j
        in case of an error returns None
        """
        self.logger.debug(f"Entering getbyparam method with parameters: {dict}")
        results = None
        try:
            results = self.controller.get_by_param(dict)
            self.controller.save_data_repository(dict["name"], results)
            self.logger.info(f"Data retrieved and saved for query name: {dict['name']}")
        except Exception as e:
            self.logger.exception(f"Error retrieving or saving data for {dict['name']}: {str(e)}")
        finally:
            return results

    def get_data_from_repository(self, value, filter="data"):
        """
         This method retrieves data from the repository based on a filter.
        It calls the get_data_by_filter method from the Controller class.
        :param value:(str) The value used in the filter to query the repository.
        :param filter:(str, optional): The filter type to use when querying the repository. Defaults to "data"
        :return:The data retrieved from the repository, or None if an error occurred.
        """
        self.logger.debug(f"Entering getDataFromRepo method with value: {value} and filter: {filter}")
        data = None
        try:
            data = self.controller.get_data_by_filter(filter, value)
            self.logger.info(f"Data retrieved from repository for value: {value} using filter: {filter}")
        except Exception as e:
            self.logger.error(f"Unable to retrieve data from repository for value: {value}. Error: {str(e)}")
            return None
        finally:
            return data

    def extract_CSV(self,dict):
        """
         This method extracts data to a CSV file.
         calls the to_CSV method in the Controller class to perform the extraction.
        :param dict:A dictionary that includes configurations for CSV extraction.
        :return:None. Logs the result of the CSV extraction process.
        """
        name=dict["name"]
        if "source_columns" in dict:
            source_columns=dict["source_columns"]
        if "target_columns" in dict:
            target_columns=dict["target_columns"]
            self.logger.debug(f"Entering extractCSV method with name: {name}, source_columns: {source_columns}, target_columns: {target_columns}")
        try:
            self.controller.to_CSV(dict)
            self.logger.info(f"CSV extraction completed for query name: {name}")
        except Exception as e:
            self.logger.error(f"Unable to extract data for query name: {name}. Error: {str(e)}")


    def get_relations(self,dict):
        """
        This method retrieves relationships from the database using the get_relations method
        from the Controller class.It then saves the results to the repository.
        :param dict: A dictionary containing the query parameters. Must include the "name" key for saving the data.
        :return:The data retrieved from the repository, or None if an error occurred.
        """
        results = None
        try:
            results = self.controller.get_relations()
            self.controller.save_data_repository(dict["name"], results)
        except Exception as e:
            self.logger.exception(f"Error while trying to get all relations {e}")
            return results
        finally:
            return results

    def get_nodes_labels(self,dict):
        """
        This method retrieves node labels from the database using the get_nodes_labels method from the Controller class.
        It then saves the results to the repository.
        :param dict: A dictionary containing the query parameters. Must include the "name" key for saving the data.
        :return:The data retrieved from the repository, or None if an error occurred.
        """
        results = None
        try:
            results = self.controller.get_nodes_labels()
            self.controller.save_data_repository(dict["name"], results)
        except Exception as e:
            self.logger.exception(f"Error while trying to get all nodes labels {e}")
            return results
        finally:
            return results

    def get_data_properties(self,nodes):
        results=None
        try:
            results = self.controller.get_data_properties(nodes)
        except Exception as e:
            self.logger.exception(f"Error while trying to get data properties of nodes")
            return results
        finally:
            return results
