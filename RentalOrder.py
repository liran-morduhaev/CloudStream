from User import User
from PremiumFamilyPlan import PremiumFamilyPlan
from ResolutionNotAllowedError import ResolutionNotAllowedError

class RentalOrder:
    RESOLUTION = {"SD", "HD", "4K"}
    STATUS = {"PENDING", "PAID", "CANCELLED"}
    def __init__(self, order_id, items, user: User, resolution, status="PAID"):
        self.order_id = order_id
        self.user = user
        self.items = list(items)
        self.resolution = resolution
        self.status = status

        if self.resolution == "4K":
            if not isinstance(self.user.subscription, PremiumFamilyPlan):
                raise ResolutionNotAllowedError("4K streaming requires an active PremiumFamilyPlan.")

        self.final_price = self.calculate_total_price()

        history_titles = {media.title for media in self.user.watch_history}
        for item in self.items:
            if item.title not in history_titles:
                self.user.watch_history.append(item)
                history_titles.add(item.title)

    def calculate_total_price(self):
        total = sum(item.calculate_access_fee(self.resolution) for item in self.items)
        if self.user.subscription:
            discount = self.user.subscription.get_discount_rate()
            total -= total * discount
        return round(total, 2)