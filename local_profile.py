class LocalProfile:
    def __init__(self):
        self.profiles = {}
    
    def create_profile(self, username):
        self.profiles[username] = {'score' : {'correct': 0, 'wrong':0}}
    
    def update_score(self, username, is_correct):
        if username in self.profiles:
            if is_correct:
                self.profiles[username]['score']['correct'] += 1
            
            else:
                self.profiles[username]['score']['wrong'] += 1

    def get_score(self, username):
        return self.profiles.get(username, {}).get('score', {'correct': 0, 'wrong': 0})
    
    