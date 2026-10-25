from SubscriptionPlan import SubscriptionPlan
from MediaItem import MediaItem

class User:
    def __init__(self, user_id, username, email, subscription=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.subscription = subscription
        self.saved_watchlist: list[MediaItem] = [] #עם רמז טיפוס (נקי ומסודר יותר ב-OOP)
        self.watch_history: list[MediaItem] = []
        self.perks_box: list = []


    def upgrade_subscription(self, new_plan: SubscriptionPlan):
        self.subscription = new_plan


    def add_to_watchlist(self, item: MediaItem):
        for saved_item in self.saved_watchlist:
            if saved_item.title == item.title:
                return
        self.saved_watchlist.append(item)

    def remove_from_watchlist(self, item_id):
        for item in self.saved_watchlist:
            if item.item_id == item_id:
                self.saved_watchlist.remove(item)
                break


    def claim_promo(self, promo_voucher):
        self.perks_box.append(promo_voucher)

    def redeem_all_promos(self):
        for perk in self.perks_box:
            perk.redeem()
        self.perks_box.clear()




