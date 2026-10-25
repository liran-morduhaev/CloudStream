from MediaItem import MediaItem

class Movie(MediaItem):
    def __init__(self, item_id, title, base_rental_price, genres, duration_minutes, director):
        super().__init__(item_id, title, base_rental_price, genres)
        self.duration_minutes = duration_minutes
        self.director = director

    def calculate_access_fee(self, resolution_quality):
        if resolution_quality == "4K":
            return float(self.base_rental_price * 1.5)
        elif resolution_quality == "HD":
            return float(self.base_rental_price * 1.2)
        else:
            return float(self.base_rental_price)

