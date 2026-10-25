from abc import ABC, abstractmethod

class SubscriptionPlan(ABC):
    def __init__(self, plan_name, monthly_fee, max_concurrent_streams):
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee
        self.max_concurrent_streams = max_concurrent_streams

    @abstractmethod
    def get_discount_rate(self):
        pass

    @abstractmethod
    def support_offline_downloads(self):
        pass