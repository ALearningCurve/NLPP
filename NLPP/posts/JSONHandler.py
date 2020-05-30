import json
import enum
from . import models


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


def update_database(_request, _method, _post_pk, _text):
    post = models.Post.objects.get(id=_post_pk)
    post_member = post.post_asignees.filter(user = _request.user)[0]
    post_info = post_member.post_info

    # Depending on the method used it will change a different JSON
    if (_method == Methods.OneClick) :
        data = json.loads(post_info.single_clicks)
        add_value(_text, data)
        post_info.single_clicks = json.dumps(data)
    elif (_method == Methods.TwoClick):
        data = json.loads(post_info.double_clicks)
        add_value(_text, data)
        post_info.double_clicks = json.dumps(data)
    post_info.save()

class Methods(enum.Enum):
    OneClick = 1
    TwoClick = 2
