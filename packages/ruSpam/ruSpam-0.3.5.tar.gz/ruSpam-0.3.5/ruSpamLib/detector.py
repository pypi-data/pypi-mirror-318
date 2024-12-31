import requests


class SpamChecker:
    def __init__(self, user_token, model_name="ruSpam-turbo-test"):

        self.user_token = user_token
        self.model_name = model_name
        self.selected_server = "https://neurospacex-ruspam.hf.space/api/check_spam"

    def check_spam(self, message):

        if not self.user_token:
            print("API token is required for authentication.")
            return {
                "is_spam": False,
                "confidence": 0.0,
                "model_used": self.model_name,
                "tokens_used": 0,
                "cost": 0.0,
                "api_key": None,
            }

        if not self.selected_server:
            print("No server initialized.")
            return {
                "is_spam": False,
                "confidence": 0.0,
                "model_used": self.model_name,
                "tokens_used": 0,
                "cost": 0.0,
                "api_key": self.user_token,
            }

        headers = {"api-key": self.user_token}
        data = {"message": message, "model_name": self.model_name}

        try:
            response = requests.post(self.selected_server, json=data, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"Response received from server: {self.selected_server}")
                return {
                    "is_spam": result.get("is_spam", 0) == 1,
                    "confidence": result.get("confidence", 0.0),
                    "model_used": result.get("model_used", self.model_name),
                    "tokens_used": result.get("tokens_used", 0),
                    "cost": result.get("cost", 0.0),
                    "api_key": result.get("api_key", self.user_token),
                }
            else:
                print(
                    f"Server at {self.selected_server} failed with status code {response.status_code}."
                )
                if response.status_code == 400:
                    result = response.json()
                    if "error" in result:
                        print(f"Error: {result['error']}")
        except requests.exceptions.RequestException as e:
            print(f"Network error while connecting to {self.selected_server}: {e}")

        print("Failed to process the request.")
        return {
            "is_spam": False,
            "confidence": 0.0,
            "model_used": self.model_name,
            "tokens_used": 0,
            "cost": 0.0,
            "api_key": self.user_token,
        }
