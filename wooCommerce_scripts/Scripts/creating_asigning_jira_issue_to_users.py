import json
import csv


Create_issue_url = "https://ssqafrontiers.atlassian.net/rest/api/2/issue"
get_issue_url = "https://ssqafrontiers.atlassian.net/rest/api/2/issue/{issueKey}"

assign_issue_url = "https://ssqafrontiers.atlassian.net/rest/api/2/issue/{issueKey}/assignee"

# Jira API endpoint URLs

username = "bruktawit0101@gmail.com"
api_token = "ATATT3xFfGF0Q1-BxaIxm_aQXeSqUWPZMeYejmIGJkmBl6_H8uqQUxcXBu-f5vvWCtJd1jijufQH84W33WNV9h5LeJAavhcMQdAFI5MfEEMBeijN31WMpZm6fb5oXvEYYrYe2ZaW7lKkrbDS2dny5zJTf5fBIsiTd9RGB_16TyOs-eqgB4BO4lI=45AAC7E9"

# Headers for API requests
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps(
    {
        "fields": {
            "project": {
                "key": "MFJP"
            },
            "summary": "Use jira API to clone a story.",
            "description": "Creating a Python script that will clone a story and assign it to users. Use Jira API.",
            "issuetype": {
                "name": "Task"

            }
        }
    }

)

response = requests.post(Create_issue_url, headers=headers, data=payload, auth=(username, api_token))

if response.status_code == 201:

    # get the clone issue key
    cloned_issue_key = response.json().get("key")

    # get the issue details
    get_issue_response = requests.get(get_issue_url.format(issueKey=cloned_issue_key), headers=headers, auth=(username, api_token))
    if get_issue_response.status_code == 200:
        issue_data = get_issue_response.json()
        print(issue_data)

    else:
        print(f"failed to get issue data")
    # Assign the issue to users
    users_to_assign = []
    with open('my_users_list.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            user = row[0]
            users_to_assign.append(user)

    for user in users_to_assign:
        assign_url = assign_issue_url.format(issueKey=cloned_issue_key)

        assign_payload = {
            "accountId": user
        }
        assign_response = requests.put(assign_url, headers=headers, json=assign_payload, auth=(username, api_token))

        if assign_response.status_code == 204:
            print(f"Issue assigned to {user}")

        else:
            print(F"Failed to assign the issue to {user}. Status code: {assign_response.status_code}")
