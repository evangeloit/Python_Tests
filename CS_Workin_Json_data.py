"""Java Script Object Notation"""


import json

# json valid
people_string = '''
{
    "people": [
        { 
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },

        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
        
    ]
}

'''

data = json.loads(people_string) # Conversion from json to python objects
print(type(data['people'])) # people key is a list now

for person in data['people']: # loop through
    print(person['name']) # access the name key
    del person['phone'] # Remove phone numbers
# print(data)

new_string = json.dumps(data, indent=2, sort_keys=True) # Dump back to a string/
                                        #  indent : seperates every level to have a clear view of the file
                                        # sorting : Sorts the Keys alphabetically
print(new_string)

