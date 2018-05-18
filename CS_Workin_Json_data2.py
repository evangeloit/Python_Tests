

import json

# /////// LOAD FILE ///////
with open('states.json') as f:
    data = json.load(f) #load json file to a python object

# //////// LOOP and PRINT ////////
for state in data['states']: # loop through , access the state key
    print(state['name'],state['abbreviation'])

# ////// REMOVE KEYS FROM DATA ///////
    del state['area_codes']

# ////////WRITE TO ANOTHER FILE ////////////
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2) # convert from python obj to json file
