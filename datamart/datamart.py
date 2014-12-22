import logging
import urllib
import json
import sys
import pickledb
import os.path
import time
import psycopg2
import StringIO

'''
    TODO: 
    - Other DB engines
    - Incremental data
    - Non-auto Dimensions
'''

class Dimension():
    ''' Dimension class
        holds all values of Dimension
    '''
    def __init__(self, name):
        self.name = name
        self.values={}
        self.id_value = 0
        self.is_degenerate = False

    def addDimensionLine(self, dimension_value):
        '''Adds a line to this dimension.
           An automatic surrogate key is created and returned.
        '''
        if self.values.has_key(dimension_value):
            return self.values[dimension_value]
        self.id_value += 1
        self.values[dimension_value] = self.id_value
        return self.id_value
        

class DegenerateDimension():
    ''' Degenerate Dimension class
        The value is stored in the Fact table, so nothig is stored
    '''
    def __init__(self, name):
        self.name = name
        self.is_degenerate = True

    def addDimensionLine(self, dimension_value):
        return dimension_value
        

class Fact():
    '''Fact class  
       Holds all values of Facts. Also keeps a list of related dimensions
    '''
    def __init__(self, name):
        self.name = name
        self.values = []
        self.dimensions = []
        self.degenerate_dimensions = []
        self.autoUpdateDimension = True
        self.id_value = 1
  
    def addDimension(self, dimension):
        self.dimensions.append(dimension)

    def addFactLine(self, fact_line_values):
        ''' Adds fact line
            If autoUpdateDimension is true, will also add dimensions as needed
            An automatic surrogate key is created.  
            Fact line is a tuple and needs to have as many values as the number of declared dimensions, on the same order
        '''
        converted_fact_line_values = [self.id_value]
        self.id_value += 1
        if self.autoUpdateDimension:
            for i in range(len(self.dimensions)):
                id_dimension=self.dimensions[i].addDimensionLine(fact_line_values[i])
                converted_fact_line_values.append(id_dimension)
        self.values.append(converted_fact_line_values)
 

class DataMart():
    ''' Datamart class
        Holds the facts and takes care of DB operations
    '''
    def __init__(self, connect_str):
        self.facts={}
        self.connect_str = connect_str

    def addFact(self, fact):
        self.facts[fact.name] = fact

    def LoadDB(self):
        '''Loads into the DB each fact and each dimension
        '''
        connection = psycopg2.connect(self.connect_str)
        cursor = connection.cursor()
        for fact in self.facts.values():
            self.clearTablesDB(cursor, fact.name)
            for dimension in fact.dimensions:
                if not dimension.is_degenerate:
                    self.clearTablesDB(cursor, dimension.name)
                    self.dumpValuesDB(cursor, dimension.name, [(dimension.values[key], key) for key in dimension.values.keys()])
            self.dumpValuesDB(cursor, fact.name, fact.values)
        print "END"
        connection.commit()
        
    def clearTablesDB(self, cursor, table_name):
        sql = "DELETE FROM "+table_name+";" # TODO: incremental possibility
        cursor.execute(sql)

    def dumpValuesDB(self, cursor, table_name, values):
        ''' Dumps all values to the DB.
            Should be fast.
        '''
        data_file = StringIO.StringIO()
        for value_line in values:
            data_file.write('\t'.join([utf8(item) for item in value_line]))
            data_file.write('\n')
        data_file.seek(0)
        cursor.copy_from(data_file, table_name)
        
       
def utf8(value):
    if type(value) is unicode:
        return value
    return unicode(str(value), encoding="utf-8", errors='replace')


def main(argv):
    print "datamart.py should not be directly called. Please see README."

# Call main if not imported
if __name__ == "__main__":
    main(sys.argv)
