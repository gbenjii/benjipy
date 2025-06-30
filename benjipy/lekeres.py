import requests

class lekeres:
    API_URL = "https://benjii.eu/api/pythonapi/api.php"
    
    @staticmethod
    def _api_lekeres(tipus):
        try:
            params = {'type': tipus}
            response = requests.get(lekeres.API_URL, params=params)
            if response.status_code == 200:
                return response.text.strip()
            return None
        except requests.RequestException:
            return None
     
    @staticmethod
    def ev():
        return lekeres._api_lekeres('ev') or "ERROR"
    
    @staticmethod
    def honap():
        return lekeres._api_lekeres('honap') or "ERROR"
    
    @staticmethod
    def nap():
        return lekeres._api_lekeres('nap') or "ERROR"
    
    @staticmethod
    def evhonapnap():
        return lekeres._api_lekeres('evhonapnap') or "ERROR"
    