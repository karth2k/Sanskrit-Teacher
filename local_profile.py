import json


class LocalProfile:
    def __init__(self, filename):
        self.filename = filename
        self.profiles = self.load_profiles()

    def load_profiles(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return {}
        
    def save_profiles(self):
        with open(self.filename, 'w') as file:
            json.dump(self.profiles, file)
    
    def create_profile(self, username):
        self.profiles[username] = {'score' : {'correct': 0, 'wrong':0}}
        self.save_profiles()
    
    def update_score(self, username, is_correct=None):
        if username in self.profiles:
            if is_correct == True:
                self.profiles[username]['score']['correct'] += 1
            
            elif is_correct == False:
                self.profiles[username]['score']['wrong'] += 1
            
            self.save_profiles()

    def get_score(self, username):
        return self.profiles.get(username, {}).get('score', {'correct': 0, 'wrong': 0})
    
