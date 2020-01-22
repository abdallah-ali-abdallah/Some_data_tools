'''
This script used to generate a random array in c/c++ formate used as test data
'''

import numpy as np

arry1 = np.random.randint(-1000, 7000, 1000)
arry2 = np.random.randint(low=30, high=5000, size=1000)
arry3 = np.random.randint(low=1000, high=1100000, size=1000)

# Function to conver the array to printable string with some identification data that describe it's content 

def convert_array_to_string(dataArray):
    min_value = ""
    max_value = ""

    #check to ensure that min/max value will not add negative sign "-" in the array name
    if np.amin(dataArray) < 0:
        min_value = "n" + str((-1 * np.amin(dataArray)))
    else:
        min_value =  str(np.amin(dataArray))
    
    if np.amax(dataArray) < 0:
        max_value = "n" + str((-1 * np.amax(dataArray)))
    else:
        max_value =  str(np.amax(dataArray))

    theresultString = "test_data_size_"
    theresultString += str(dataArray.size) + "_min_" + min_value +  "_max_" + max_value
    theresultString += "[" + str(dataArray.size)+ "]"
    theresultString +=" = {"
    for element_index in range (0,dataArray.size):
        if element_index != (dataArray.size -1):
            theresultString += str(dataArray[element_index])
            theresultString += ","
        else:
            theresultString += str(dataArray[element_index])
    theresultString += "};"
    return theresultString


string_1 = "int " + convert_array_to_string(arry1)
string_2 = "uint16_t " + convert_array_to_string(arry2)
string_3 = "uint32_t " + convert_array_to_string(arry3)

print(string_1)

        