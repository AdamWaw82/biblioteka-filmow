class Movies:
    def __init__(self, title, publication_date, gender, number_of_plays):
        self.title = title
        self.publication_date =publication_date
        self.gender = gender
        self.number_of_plays = number_of_plays

    def play(self):
        self.number_of_plays += 1

    def __str__(self):
        return f"{self.title} ({self.publication_date})"


class Series(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"



media_list = []
