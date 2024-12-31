# payment.py
from dataclasses import dataclass
import stripe
from typing import Optional, Dict

@dataclass
class PriceConfig:
   FINETUNE = 100  # $100
   FEATURES = 200  # $200

class StripeManager:
   def __init__(self, api_key: str):
       self.stripe = stripe
       self.stripe.api_key = api_key

   async def create_customer(self, email: str) -> stripe.Customer:
       return await self.stripe.Customer.create(email=email)

   async def create_subscription(
       self, 
       customer_id: str,
       price_id: str
   ) -> stripe.Subscription:
       return await self.stripe.Subscription.create(
           customer=customer_id,
           items=[{"price": price_id}]
       )

   async def charge(
       self,
       amount: int,
       customer_id: Optional[str] = None,
       metadata: Optional[Dict] = None
   ) -> stripe.Charge:
       charge_data = {
           "amount": amount * 100,  # Convert to cents
           "currency": "usd",
           "metadata": metadata or {}
       }
       if customer_id:
           charge_data["customer"] = customer_id
       
       return await self.stripe.Charge.create(**charge_data)

   async def get_charges(self, customer_id: str) -> stripe.ListObject:
       return await self.stripe.Charge.list(customer=customer_id)