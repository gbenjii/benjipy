import requests

class joke:
    API_URL = "https://benjii.eu/api/pythonapi/api.php"
    
    @staticmethod
    def _api_lekeres(tipus):
        try:
            params = {'type': tipus}
            response = requests.get(joke.API_URL, params=params)
            if response.status_code == 200:
                return response.text.strip()
            return None
        except requests.RequestException:
            return None
        
    @staticmethod
    def hu():
        return joke._api_lekeres('jk.hu') or "ERROR"
    
    @staticmethod
    def en():
        return joke._api_lekeres('jk.en') or "ERROR"