from streamlit import secrets
import requests
import json

def get_gist_content():
    gist_id = '7788770a3b330f697c8f18c3d1eff39c'
    url = f"https://api.github.com/gists/{gist_id}"
    response = requests.get(url)
    if response.status_code == 200:
        gist_data = response.json()
        filename = 'songs.json'
        content = gist_data['files'][filename]['content']
        content = json.load(content)
        return content
    else:
        print(f"Failed to retrieve Gist content, status code: {response.status_code}")
        return None

def update_gist(key, value):
    gist_id = '7788770a3b330f697c8f18c3d1eff39c'
    filename = 'songs.json'
    token = secrets['github_api_key']
    existing_content = get_gist_content()

    if existing_content is None:
        return 'Failed to retrieve existing Gist content'

    try:
        content_dict = json.loads(existing_content)
    except json.JSONDecodeError:
        return 'Existing Gist content is not valid JSON'

    content_dict[key] = value
    updated_content = json.dumps(content_dict)

    data = {
        "files": {
            filename: {
                "content": updated_content
            }
        }
    }

    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Gist updated successfully")
    else:
        print(f"Failed to update Gist, status code: {response.status_code}")
    return response.status_code

def remove_gist_key(key):
    gist_id = '7788770a3b330f697c8f18c3d1eff39c'
    filename = 'songs.json'
    token = secrets['github_api_key']
    existing_content = get_gist_content()

    if existing_content is None:
        return 'Failed to retrieve existing Gist content'

    try:
        content_dict = json.loads(existing_content)
    except json.JSONDecodeError:
        return 'Existing Gist content is not valid JSON'

    if key in content_dict:
        del content_dict[key]
    else:
        return 'Key not found in Gist'

    updated_content = json.dumps(content_dict)

    data = {
        "files": {
            filename: {
                "content": updated_content
            }
        }
    }

    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Gist key removed successfully")
    else:
        print(f"Failed to remove Gist key, status code: {response.status_code}")
    return response.status_code