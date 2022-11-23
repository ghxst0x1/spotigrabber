import os, requests, json
from dotenv import load_dotenv

load_dotenv()

# To fetch spotify_playlist data
def fetchJson():
    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    AUTH_URL = "https://accounts.spotify.com/api/token"
    # POST
    auth_response = requests.post(
        AUTH_URL,
        {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    playlist_id = input("Paste playlist id here: ")
    # convert the response to JSON
    auth_response_data = auth_response.json()
    # save the access token
    access_token = auth_response_data["access_token"]
    BASE_URL = f"https://api.spotify.com/v1/playlists/{playlist_id}?market=ES"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(access_token),
    }
    response = requests.get(BASE_URL, headers=headers)
    print(response)
    data = response.json()
    print(type(data))
    num = len(data["tracks"]["items"])
    print(f"Total Songs in the Playlist: {num}\n")
    for i in range(num):
        print(data["tracks"]["items"][i]["track"]["name"],end=" by ")
        print(data["tracks"]["items"][i]["track"]["artists"][0]["name"])
        print("\r")
    return data


# data = fetchJson()


# To save Json to a file
def jsonSave():
    try:
        data = fetchJson()
        with open("test.json", "w") as json_file:
            json.dump(data, json_file)
        print("Json saved successfully.")
    except:
        print("Failed to Save json.")


# Opening JSON file
def jsonRead():
    with open("list.json", encoding="utf8") as json_file:
        new_data = json.load(json_file)

        # print(type(data))
        num = len(new_data["tracks"]["items"])
        for i in range(num):
            print(new_data["tracks"]["items"][i]["track"]["name"])
            print(new_data["tracks"]["items"][i]["track"]["artists"][0]["name"])
            print("\r")


def main():
    menu = """
    1 = fetch json
    2 = json save
    3 = json read
    """
    print(menu)
    choice = input("Enter your choice: ")
    print(choice)
    match int(choice):
        case 1:
            fetchJson()
        case 2:
            return jsonSave()
        case 3:
            return jsonRead()


if __name__ == "__main__":
    main()
