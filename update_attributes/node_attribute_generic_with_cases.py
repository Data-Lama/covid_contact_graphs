# Generic Node Attribute that includes cases

from node_attribute_generic import GenericNodeAttribute
from attribute_generic import GenericWeeklyAttribute
import pandas as pd
import utils
import numpy as np
import positive_db_functions as pos_fun


class GenericNodeAttributeWithCases(GenericNodeAttribute):
    '''
    Class for the Generic Graph Attribute with Cases
    '''

    def __init__(self, property_values):
        # Initilizes the super class
        GenericNodeAttribute.__init__(self, property_values)  


        self.df_codes =  utils.get_geo_codes(self.client, location_id = None)
        self.df_codes.index = self.df_codes.location_id
        
        # Gets the max date of symptoms for each supported location        
        self.max_dates = pos_fun.get_positive_max_dates(self.client) 
        self.min_dates = pos_fun.get_positive_min_dates(self.client)
        

    def location_id_supported(self, location_id):
        '''
        OVERWRITTEN
        # ---------------
        
        Does a generic check to see if the location id has cases
        
        params
            - location_id (str)
            - current_date (pd.datetime): the current datetime

        returns
            Boolean
        '''

        global_support = GenericWeeklyAttribute.location_id_supported(self, location_id)

        return( global_support and pos_fun.has_positives_database(self.client, location_id, self.df_codes))
    

        
    def location_id_supported_on_date(self, location_id, current_date):
        '''
        OVERWRITTEN
        # --------------
        
        Does a generic check to see if the location id has cases in the given dates
        
        params
            - location_id (str)
            - current_date (pd.datetime): the current datetime

        returns
            Boolean
        '''
        
        # Checks global
        global_support = GenericWeeklyAttribute.location_id_supported_on_date(self, location_id, current_date)
        
        # Cases check
        up_to_date = pos_fun.positives_inside_date(self.client, location_id, current_date, self.df_codes, self.max_dates, self.min_dates)
        
        return(up_to_date and global_support)
            