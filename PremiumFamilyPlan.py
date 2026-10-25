from SubscriptionPlan import SubscriptionPlan

class PremiumFamilyPlan(SubscriptionPlan):
    def __init__(self):
        super().__init__(plan_name="Premium Family",monthly_fee=19.99,max_concurrent_streams=5)

    def get_discount_rate(self) -> float:
        return 0.25

    def support_offline_downloads(self) -> bool:
        return True

