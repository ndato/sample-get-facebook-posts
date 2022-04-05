import json
 
from pyfacebook import GraphAPI
 
def read_creds(filename):
    '''
    Store API credentials in a safe place.
    If you use Git, make sure to add the file to .gitignore
    '''
    with open(filename) as f:
        credentials = json.load(f)
    return credentials
 
credentials = read_creds('credentials.json')

# Generate Access Token
api = GraphAPI(access_token=credentials['access_token'])

# Get all of my posts.
posts = api.get_object('me', fields="posts")
print(json.dumps(posts, indent=4))

# Get all of a page's posts.
# To find the Page ID of a Facebok Page,
# go to that Facebook Page > About > Page ID
# page_id = '107049890702460' # This is PizzaPy's Page ID
# posts = api.get_object(page_id, fields="posts")
# print(json.dumps(posts, indent=4))