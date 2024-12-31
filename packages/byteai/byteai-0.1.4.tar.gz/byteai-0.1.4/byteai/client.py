# byteai/client.py
from .payment import StripeManager
from .tokenizer import TokenizerTool

class ByteClient:
    def __init__(self, api_key: str):
        self.stripe = StripeManager(api_key)
        self.api_url = "https://api.byteai.dev"
        
    async def finetune(self, dataset: str, config: dict) -> str:
        tokens = TokenizerTool().process_file(dataset)
        payment = await self.stripe.charge("finetune", 100)
        return await self._post("/finetune", {
            "tokens": tokens,
            "config": config,
            "payment_id": payment.id
        })

    async def extract_features(self, model_id: str) -> list:
        payment = await self.stripe.charge("features", 200)
        return await self._post("/features", {
            "model_id": model_id,
            "payment_id": payment.id
        })
    
    def tokenize(self, dataset:str):
        tokens = TokenizerTool().process_file(dataset)
