from abc import ABC, abstractmethod

class MediaItem(ABC):
    def __init__(self, item_id, title, base_rental_price, genres):
        self.item_id = item_id
        self.title = title
        self.base_rental_price = base_rental_price
        self.genres = list(genres)

    @abstractmethod
    def calculate_access_fee(self, resolution_quality):
        pass

    def __str__(self):
        return f'Item ID: {self.item_id}, Title: {self.title}, Base Rental Price: {self.base_rental_price}, Genres{self.genres}'

    def __repr__(self):
        return f'item (ID={self.item_id}, Title={self.title}, Price={self.base_rental_price}, Genres={self.genres})'

