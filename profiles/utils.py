# profiles/utils.py

import requests

def fetch_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    query = """
    {
      matchedUser(username: "%s") {
        username
        submitStats: submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
            submissions
          }
        }
      }
    }
    """ % username

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json={'query': query}, headers=headers)
    
    if response.status_code == 200:
        data = response.json().get('data', {}).get('matchedUser', {})
        return data
    else:
        return None
