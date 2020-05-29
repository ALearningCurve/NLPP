import json

'''
This is a file to handle basic json editing that would be used in the posts' models.py
file
'''


# Sample data to test out the functions with
# data = {
#     "1": ["uno", "single", "one"],
#     "2": ["dos", "double", "two"],
#     "3": ["tres", "triple", "three"]
#     }


'''
Gets the Vaule and adds it to the json
If it is not there already then the word will go in
row "1", otherwise it will increase the row the word is in
'''
def add_value(toAdd, json):
    toAdd.lower()
    for row in json:
        for word in json[row]:
            if toAdd == word:
                json[row].remove(word)

                # Checks if the row already exists to prevent a Key Error
                # The would happen when trying to add to a new row
                try:
                    json[str(int(row)+1)].append(word)
                except KeyError:
                    json[str(int(row)+1)] = [word]
                return
    # If the loop finishes, it means that no copies of the word
    # were found so we just add the word to the array in row "1"
    json["1"].append(toAdd)



add_value("dos", data)
add_value("dos", data)
add_value("dos", data)
print(json.dumps(data))
