from datetime import date

class Media:
    def __init__(self, title, publication_date, genre):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.number_of_plays = 0

    def play(self):
        self.number_of_plays += 1

    def __repr__(self):
        return f"{self.title} ({self.publication_date})"

class Movie(Media):
   pass


class Series(Media):
    def __init__(self, title, publication_date, genre, episode, season):
        super().__init__(title, publication_date, genre)
        self.episode = episode
        self.season = season


    # Do klasy reprezentującej serial, dopisz funkcję zewnętrzną, która wyświetla liczbę odcinków danego serialu dostępnych w bibliotece. => Nie kumam co autor ma na myśli.... funkcję zewnętrzną w klasie, czy poza klasą...
    def count(self, series):
        print(f"{self.title} Odcinków w bazie: {len([serie.title for serie in series if serie.title == self.title])}")

    def __repr__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"
    



def main():
    media_list = []

    def get_movies()->list:
        movie_list = [item for item in media_list if isinstance(item, Movie)]
        sorted_movie_list = sorted(movie_list, key=lambda movie: movie.title)
        return sorted_movie_list

    def get_series()->list:
        series_list = [item for item in media_list if isinstance(item, Series)]
        sorted_movie_list = sorted(series_list, key=lambda serie: serie.title)
        return sorted_movie_list

    def search(for_search):
        founded = [item for item in media_list if for_search.lower() in item.title.lower() ]
        return founded


    def generate_views():
        import random
        random_media: Movie = random.choice(media_list)
        random_number = random.randint(0, 100)  
        random_media.number_of_plays += random_number

    def top_titles(content_type = None, count = None):
        if count is None:
            count = len(media_list)
        if content_type == 'movies':
            sorted_movies = sorted(get_movies(), key=lambda x: x.number_of_plays, reverse=True)
            return [str(movie) for movie in sorted_movies[:count]]
        elif content_type == 'series':
            sorted_series = sorted(get_series(), key=lambda x: x.number_of_plays, reverse=True)
            return [str(series) for series in sorted_series[:count]]
        else:
            sorted_content = sorted(media_list, key=lambda x: x.number_of_plays, reverse=True)
            return [str(item) for item in sorted_content[:count]]


    def generate_views_ten_times():
        for i in range(0, 10):
            generate_views()


    def add_season(title, publication_date, genre, episode, season):
        for episode_num in range(1, episode + 1):
            media_list.append(Series(title, publication_date, genre, episode_num, season))


    print("Biblioteka filmów")

    print("Wypełniam listę")
    media_list = [
        Movie("Pulp Fiction", 1994, "Crime"),
        Movie("The Dark Knight", 2008, "Action"),
        Movie("Inception", 2010, "Sci-Fi"),
        Movie("Interstellar", 2014, "Sci-Fi"),
        Movie("The Matrix", 1999, "Sci-Fi"),
        Movie("Fight Club", 1999, "Drama"),
        Movie("Forrest Gump", 1994, "Drama"),
        Movie("The Shawshank Redemption", 1994, "Drama"),
        Movie("The Godfather", 1972, "Crime"),
        Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Fantasy")
    ]

    
    add_season("Game of Thrones", 2011, "Fantasy", 10, 1)
    add_season("Game of Thrones", 2011, "Fantasy", 10, 2)
    add_season("Game of Thrones", 2011, "Fantasy", 10, 3)
    add_season("Game of Thrones", 2011, "Fantasy", 10, 4)
    add_season("Stranger Things", 2016, "Sci-Fi", 8, 1)
    add_season("Stranger Things", 2016, "Sci-Fi", 8, 2)
    add_season("Stranger Things", 2016, "Sci-Fi", 8, 3)
    add_season("Stranger Things", 2016, "Sci-Fi", 8, 4)

    generate_views_ten_times()
    today = date.today().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia <{today}>")

    print("Top 3 najpopularniejszych tytułów: ")

    print(top_titles(count=3))

if __name__ == "__main__":
    main()