import requests

api_arizona = "https://api.arizona-five.com/launcher/servers"

class ArizonaAPI:
    def __init__(self):
        try:
            self.api = api_arizona
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def get_all_servers(self):
        response = requests.get(self.api)
        return response.json()

    def get_arizona_servers(self):
        response = requests.get(self.api)  
        arizona_data = response.json().get('arizona', [])  
        return arizona_data
    def get_rodina_servers(self):
        response = requests.get(self.api)  
        rodina_data = response.json().get('rodina', [])  
        return rodina_data
    def get_arizonav_servers(self):
        response = requests.get(self.api)  
        arizonav_data = response.json().get('arizonav', [])  
        return arizonav_data
    def get_village_servers(self):
        response = requests.get(self.api)
        village_data = response.json().get('village', [])
        return village_data
    def get_arizona_staging_servers(self):
        response = requests.get(self.api)
        arizona_staging_data = response.json().get('arizona_staging', [])
        return arizona_staging_data
    
if __name__ == "__main__":
    api = ArizonaAPI()
