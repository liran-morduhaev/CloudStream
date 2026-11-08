# 🎬 CloudStream - Media Streaming & Rental Platform

A robust, object-oriented digital media streaming and rental engine built with Python.  
The project demonstrates clean software architecture and core **Object-Oriented Programming (OOP)** principles: **Inheritance**, **Polymorphism**, **Abstraction**, **Encapsulation**, and **Custom Exception Handling**.

---

## 🚀 Key Features & OOP Implementation

* **Media Hierarchy (Inheritance & Polymorphism):**
  * `MediaItem` serves as an Abstract Base Class (`ABC`) defining core media attributes and the contract method `calculate_access_fee(resolution_quality)`.
  * `Movie` dynamically calculates rental pricing based on streaming quality (`SD`, `HD`, `4K`).
  * `SeriesEpisode` overrides fee calculations with flat discounted episode rates.

* **Subscription Model (Polymorphism & Abstraction):**
  * `SubscriptionPlan` abstract class enforces discount rates and offline support behaviors.
  * `StandardPlan` provides baseline streaming with standard pricing.
  * `PremiumFamilyPlan` unlocks a 25% order discount, up to 5 concurrent streams, and access to 4K content.

* **Order Processing & Quality Security:**
  * `RentalOrder` aggregates items, calculates final prices with subscription discounts, and handles deduplicated watch history logging.
  * **Strict Resolution Guard:** Custom exception `ResolutionNotAllowedError` is raised if a non-premium user attempts to rent or stream in `4K`.

* **User Management & Deduplication:**
  * `User` manages customer credentials, active subscriptions, and promo perks.
  * Automatic title-level deduplication prevents identical media items from polluting user watchlists or watch history.
  * Supports mock voucher claiming and redemption routines (`claim_promo`, `redeem_all_promos`).

---

## 📁 Project Structure

```text
CloudStream/
│
├── MediaItem.py                   # Abstract base class for all catalog items
├── Movie.py                       # Movie subclass with resolution-scaled pricing
├── SeriesEpisode.py               # Series episode subclass with flat pricing
├── SubscriptionPlan.py            # Abstract base class for subscription tiers
├── StandardPlan.py                # Standard subscription tier (SD/HD only)
├── PremiumFamilyPlan.py           # Premium subscription tier (25% discount, 4K)
├── User.py                        # User profile, watchlist, history, and perks
├── RentalOrder.py                 # Order processing, pricing logic, and resolution checks
├── ResolutionNotAllowedError.py   # Custom exception for unauthorized quality tiers
├── main.py                        # Simulation scenario demonstrating end-to-end functionality
└── README.md                      # Project documentation