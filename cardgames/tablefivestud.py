########
#Class for specific needs of the table for Five Card Stud
########

from table import Table

class TableFiveStud(Table):
    
    def __init__(self):
        self.__init__(10) #set the max players at table to 10 for five card stud
        
        