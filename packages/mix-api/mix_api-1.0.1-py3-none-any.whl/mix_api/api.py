import aiohttp
from typing import Optional, List, Dict, Union

class MixAPI:
    def __init__(self, token: str, base_url: str = "http://31.128.42.147:3333"):
        self.token = token
        self.base_url = base_url
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def _make_request(self,endpoint: str, data: dict) -> dict:
        if not self.session:
            self.session = aiohttp.ClientSession()
            
        url = f"{self.base_url}{endpoint}"
        async with self.session.post(url, json=data) as response:
            return await response.json()

    async def get_balance(self, user_id: int) -> Dict[str, Union[str, Dict]]:
        """
        Получить баланс пользователя
        
        Args:
            user_id: ID пользователя
            
        Returns:
            Dict с информацией о балансе или ошибкой
        """
        data = {"id": user_id}
        return await self._make_request("/api/v1/balance", data)

    async def transfer(self, to_id: int, amount: int) -> Dict[str, Union[str, Dict]]:
        """
        Перевести MIX другому пользователю
        
        Args:
            to_id: ID получателя
            amount: Количество MIX для перевода
            
        Returns:
            Dict с результатом операции
        """
        data = {
            "token": self.token,
            "id": to_id,
            "amount": amount
        }
        return await self._make_request("/api/v1/transfer", data)

    async def get_transactions(self, type_: int = 1) -> Dict[str, Union[str, List]]:
        """
        Получить историю транзакций
        
        Args:
            type_: Тип транзакций (1 - входящие, 2 - исходящие)
            
        Returns:
            Dict со списком транзакций
        """
        if type_ not in [1, 2]:
            raise ValueError("type_ должен быть 1 или 2")
            
        data = {
            "token": self.token,
            "type": type_
        }
        return await self._make_request("/api/v1/transactions", data)
