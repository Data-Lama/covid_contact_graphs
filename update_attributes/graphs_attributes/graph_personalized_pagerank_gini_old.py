# Gini Index over the personalized pagerank values of the nodes


from graph_attribute_generic_with_cases import GenericGraphAttributeWithCases
import pandas as pd
import numpy as np
import utils
import positive_db_functions as pos_fun


# Dictionary to include property values
property_values = {}

# Attribute name
property_values['attribute_name'] = 'personalized_pagerank_gini_index_old'

# Starting dates
property_values['starting_date'] = pd.to_datetime("2020-03-01")




class GraphPersonalizedPageRankGiniOld(GenericGraphAttributeWithCases):
    '''
    Script that computes the gini index of the nodes personalized pagerank.
    
    This script uses the results from the pagerank node attribute. If nothing is found will return None and writes a warning
    '''

    def __init__(self):
        # Initilizes the super class
        GenericGraphAttributeWithCases.__init__(self, property_values)
        
        
    def compute_attribute(self, nodes, edges):
        '''
        Main Method to Implement
        
        This method must be implemented by the subclass. It receives compact nodes and edges and 
        must output the corresponding attribute. This method must return unique identifiers and it's good 
        practice to include all identifiers. In case its a graph attribute the dataframe must contain only one row and the
        identifier column is ignored

        params
            nodes (pd.DataFrame) Pandas Dataframe with the nodes of the graph:
                - identifier (str): Id of the node
                - weight (int): Weight of the node (see get_compact_nodes) 
            edges (pd.DataFrame) Pandas dataFrame with the grouped edglist (undirected)
                - id1 (str) 
                - id2 (str)
                - weight (num) Weight od the edge (see get_compact_edgelist)      

        
        returns
            pd.DataFrame with the following structure
                - attribute_name (str): The attribute nam            
                - value (float): The value of the attribute
        '''
    
        raise ValueError('Should not enter here')
    
    

    def location_id_supported(self, location_id):
        '''
        OVERWRITTEN
        # ---------------
        
        Only Bogota and localities are supported
        
        params
            - location_id (str)
            - current_date (pd.datetime): the current datetime

        returns
            Boolean
        '''

        is_bogota = location_id == "colombia_bogota"
        is_locality = "_localidad_" in location_id

        return( is_bogota or is_locality)
    

        
    def location_id_supported_on_date(self, location_id, current_date):
        '''
        OVERWRITTEN
        # --------------
        
        Only computes over specific dates
        
        params
            - location_id (str)
            - current_date (pd.datetime): the current datetime

        returns
            Boolean
        '''
        
        min_date = pd.to_datetime("2020-03-01")
        max_date = pd.to_datetime("2021-05-28")
        
        return(current_date >= min_date and current_date <= max_date)


    def compute_attribute_for_interval(self, location_id, start_date_string, end_date_string):
        '''
        Method that computes the attribute of the class for the given dates. Edit this method if the attributes requieres more than just the nodes and
        the ids. See weighted_pagerank for an example.

        parameters
            - location_id(str): The graph id
            - start_date_string (str): Start date in %Y-%m-%d
            - end_date_string (str): End date in %Y-%m-%d

        returns
            pd.DataFrame with the structure of the output of the method compute_attribute   
        '''
                
        query = f"""
            SELECT location_id, identifier, attribute_name, attribute_value
            FROM {utils.nodes_attribute_table}
            WHERE location_id = "{location_id}" AND attribute_name = "personalized_pagerank_centrality_old" AND date = "{end_date_string}"
        """
        
        df = utils.run_simple_query(self.client, query)
        
        if df.shape[0] == 0:
            print('             ' + f'No Personalized Pagerank Centrality found for {location_id} on {end_date_string}')
            return(pd.DataFrame({'value':None, 'attribute_name':[self.attribute_name] }))
        
        
        # Computes the Gini Index
        gini_inex = utils.gini(df.attribute_value.values)
        
        df_response = pd.DataFrame({'value':[gini_inex], 'attribute_name':[self.attribute_name] })

        
        return(df_response)
    