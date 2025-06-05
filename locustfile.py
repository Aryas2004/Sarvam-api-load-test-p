from locust import HttpUser, task, between
import random

LANGUAGES = {
    "hi-IN": "नमस्ते",     
    "ta-IN": "வணக்கம்",    
    "bn-IN": "হ্যালো",     
    "te-IN": "హలో",     
    "ml-IN": "ഹലോ"     
}

class SarvamUser(HttpUser):
    wait_time = between(1, 2)
    
    
    host = "https://api.sarvam.ai"  

    @task
    def transliterate(self):
      
        lang = random.choice(list(LANGUAGES.keys()))
        text = LANGUAGES[lang]

        payload = {
            "input": text,
            "source_language_code": lang,
            "target_language_code": "en-IN"
        }

       
        headers = {
            "Content-Type": "application/json",
            "api-subscription-key": "sk_owys4a3c_xDr3l3EqAUa824YAQHfCiLBX"  
        }

     
        with self.client.post(
            "/transliterate",
            json=payload,
            headers=headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status {response.status_code}")
