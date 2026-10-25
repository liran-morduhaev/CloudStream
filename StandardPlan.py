from SubscriptionPlan import SubscriptionPlan

class StandardPlan(SubscriptionPlan):
    def __init__(self):
        super().__init__(plan_name="Standard",monthly_fee=9.99, max_concurrent_streams=2)

    def get_discount_rate(self):
        return 0.0

    def support_offline_downloads(self):
        return False

