from MediaItem import MediaItem

class SeriesEpisode(MediaItem):
    def __init__(self, item_id, title, base_rental_price, genres, series_name, season_number, episode_number):
        super().__init__(item_id, title, base_rental_price, genres)
        self.series_name = series_name
        self.season_number = season_number
        self.episode_number = episode_number

    def calculate_access_fee(self, resolution_quality):
        return float(self.base_rental_price * 0.8)

