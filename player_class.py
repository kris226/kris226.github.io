class Player:
    def __init__(self, name, team, nationality, position):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.position = position


    def __repr__(self):
        return self.name


    def is_from_nationality(self, country):
        if self.nationality == country:
            return True
        else:
            return False
        

    def is_from_team(self, team):
        if self.team == team:
            return True
        else:
            return False


    def is_from_position(self, position):
            
            if self.position == position:
                return True
            else:
                return False