##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

import pandas as pd
import unittest

#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################

class TestDataFrame(unittest.TestCase):
    
    def __init__(self, df, *args, **kwargs):
        super(TestDataFrame, self).__init__(*args, **kwargs)
        self.df = df
    
    def test_dataframe_shape(self):
        self.assertEqual(self.df.shape, (3, 3))
        
    def test_dataframe_colnames(self):
        self.assertListEqual(list(self.df.columns), ['A', 'B', 'C'])
        
    def test_dataframe_values(self):
        self.assertTrue((self.df.values == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]).all())
        
        
def test(input_df:pd.DataFrame) -> None:
      
      # Create the TestSuite object
      suite = unittest.TestSuite()
      
      # Add each instance of the TestPandas class with the DataFrame as an argument to the TestSuite
      suite.addTest(TestDataFrame(input_df, 'test_dataframe_shape'))
      suite.addTest(TestDataFrame(input_df, 'test_dataframe_colnames'))
      suite.addTest(TestDataFrame(input_df, 'test_dataframe_values'))
      
      # Run the tests
      unittest.TextTestRunner(verbosity=2).run(suite)
      return None


######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == '__main__':
    # Create the DataFrame outside the class
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    
    # Standard Test
    test(df)
    
    df.to_csv("sample_test.csv")