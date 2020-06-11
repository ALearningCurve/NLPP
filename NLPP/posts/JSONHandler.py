import json
import enum
from . import models
from datetime import datetime


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
    # clicks_to_complete
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

'''
Counts and adds up the total number of clicked words and returns that vaue
'''
def count_words(json):
    count = 0
    for row in json:
        count += int(row) * len(json[row])
    return count

'''
Uses the _post_pk and _request.user to find the post_info object to update with the _text that was clicked
and then uses the specified _method (see enum) to update the correct JSON
'''
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

'''
gets the specified JSON and checks to see if the work was completed and update table appropiatly (only checks on the 
method.OneClick so as to reduce repetitive check)
'''
def get_json(_info_object, _method):
    
    if (_method == Methods.OneClick) :
        # Check to see if assignment is complete
        if (not _info_object.post_member.has_completed_work):
            # if the clicked words is more than the required clicks, then update the completion date and completion boolean
            if (count_words(json.loads(_info_object.single_clicks)) >= _info_object.post_member.post.clicks_to_complete):
                _info_object.post_member.has_completed_work = True
                _info_object.post_member.completion_date = datetime.now()
                _info_object.post_member.save()
        return json.loads(_info_object.single_clicks)
    elif (_method == Methods.TwoClick):
        return json.loads(_info_object.double_clicks)
    else:
        return (ErrorCodes.r404)

# Holds two different columns in postmemberinteraction as ints
# so that it is easy to identify them
class Methods(enum.IntEnum):
    OneClick = 1
    TwoClick = 2


# Hold some basic error codes that can be returned through JSON
class ErrorCodes():
    # 404 error when the specified object is not found/invalid
    r404 = {
        "error": {
         "errors": [
          {
           "reason": "notFound",
           "message": "Not Found"
          }
         ],
         "code": 404,
         "message": "Not Found"
         }
    }

    # 403 error when the user does not have permissions to view material
    r403 = {
     "error": {
      "errors": [
       {
        "reason": "forbidden",
        "message": "Forbidden"
        }
      ],
      "code": 403,
      "message": "Forbidden"
     }
    }

    # 400 error when a bad request is made (such as missing param)
    r400 = {
     "error": {
      "errors": [
       {
        "reason": "bad request",
        "message": "Bad request syntax or missing values"
        }
      ],
      "code": 400,
      "message": "BadRequest"
     }
    }
