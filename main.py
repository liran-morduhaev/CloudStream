from Movie import Movie
from SeriesEpisode import SeriesEpisode
from StandardPlan import StandardPlan
from PremiumFamilyPlan import PremiumFamilyPlan
from User import User
from RentalOrder import RentalOrder
from ResolutionNotAllowedError import ResolutionNotAllowedError


class MockPromoVoucher:
    """Mock voucher class for testing perks."""

    def __init__(self, code: str):
        self.code = code

    def redeem(self):
        print(f"-> Promo voucher '{self.code}' redeemed.")


if __name__ == "__main__":
    # 1. Create media catalog items
    print("=== 1. Media Catalog ===")
    movie = Movie(
        item_id=1,
        title="Inception",
        base_rental_price=10.0,
        genres=["Sci-Fi", "Action"],
        duration_minutes=148,
        director="Christopher Nolan"
    )
    episode = SeriesEpisode(
        item_id=2,
        title="Breaking Bad S05E14",
        base_rental_price=5.0,
        genres=["Drama", "Crime"],
        series_name="Breaking Bad",
        season_number=5,
        episode_number=14
    )
    duplicate_movie = Movie(
        item_id=99,
        title="Inception",
        base_rental_price=15.0,
        genres=["Sci-Fi"],
        duration_minutes=148,
        director="Christopher Nolan"
    )
    print(f"Created: {movie.title} (${movie.base_rental_price})")
    print(f"Created: {episode.title} (${episode.base_rental_price})")

    # 2. Test User and Watchlist deduplication
    print("\n=== 2. User & Watchlist ===")
    user = User(user_id=101, username="liran_m", email="liran@example.com")

    user.add_to_watchlist(movie)
    user.add_to_watchlist(duplicate_movie)  # Skipped: duplicate title
    print(f"Watchlist count (expected 1): {len(user.saved_watchlist)}")

    user.remove_from_watchlist(item_id=1)
    print(f"Watchlist count after removal (expected 0): {len(user.saved_watchlist)}")

    # 3. Test Promo Perks
    print("\n=== 3. Perks & Rewards ===")
    user.claim_promo(MockPromoVoucher("DISCOUNT_50"))
    user.redeem_all_promos()
    print(f"Remaining perks (expected 0): {len(user.perks_box)}")

    # 4. Standard Plan Rental Order
    print("\n=== 4. Standard Plan Order ===")
    user.upgrade_subscription(StandardPlan())

    # Inception HD ($12.0) + Episode ($4.0) = $16.0 (no discount)
    order1 = RentalOrder(order_id=5001,user=user,items=[movie, episode],resolution="HD")
    print(f"Order total (expected 16.0): ${order1.final_price}")
    print(f"Watch history: {[item.title for item in user.watch_history]}")

    # 5. Validate 4K Resolution Restriction
    print("\n=== 5. 4K Security Check ===")
    try:
        RentalOrder(order_id=5002, user=user, items=[movie], resolution="4K", status="PAID")
    except ResolutionNotAllowedError as error:
        print(f"Caught expected error: {error}")

    # 6. Premium Plan Upgrade & 4K Order
    print("\n=== 6. Premium Upgrade & 4K Order ===")
    user.upgrade_subscription(PremiumFamilyPlan())

    # Inception 4K ($15.0) - 25% discount = $11.25
    order2 = RentalOrder(
        order_id=5003,
        user=user,
        items=[movie],
        resolution="4K"
    )
    print(f"Order total with 25% discount (expected 11.25): ${order2.final_price}")
    print(f"Total unique history count (expected 2): {len(user.watch_history)}")