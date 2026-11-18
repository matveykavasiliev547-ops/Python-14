import httpx

class AsyncJokesAPIClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url

    async def get_random_joke(self) -> dict:
        """Асинхронно получает случайную шутку через httpx"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/joke")
            response.raise_for_status()
            return response.json()

    async def add_joke(self, text: str) -> dict:
        """Асинхронно отправляет новую шутку через httpx"""
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/jokes", json={"text": text})
            response.raise_for_status()
            return response.json()