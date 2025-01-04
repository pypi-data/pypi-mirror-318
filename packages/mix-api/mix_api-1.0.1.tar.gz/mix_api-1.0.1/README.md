# MixAPI

MixAPI — это асинхронная библиотека Python для взаимодействия с API сервиса Mix. Она предоставляет удобные методы для получения баланса, перевода средств и просмотра истории транзакций.

## Установка

Установите библиотеку с помощью pip:
```bash
pip install mix-api
```

## Пример использования
```python
import asyncio
from mix_api import MixAPI

async def main():
    token = "your_api_token_here"
    user_id = 12345
    
    async with MixAPI(token) as api:
        # Получить баланс пользователя
        balance = await api.get_balance(user_id)
        print("Баланс:", balance)

        # Перевести средства другому пользователю
        transfer_result = await api.transfer(to_id=67890, amount=100)
        print("Результат перевода:", transfer_result)

        # Получить историю транзакций
        transactions = await api.get_transactions(type_=1)
        print("История транзакций:", transactions)

asyncio.run(main())
```

## Методы

### `get_balance(user_id: int) -> Dict[str, Union[str, Dict]]`

Получает баланс указанного пользователя.

**Аргументы:**
- `user_id` (int): ID пользователя, чей баланс нужно получить.

**Возвращает:**
- Словарь с информацией о балансе или ошибкой.

---

### `transfer(to_id: int, amount: int) -> Dict[str, Union[str, Dict]]`

Переводит MIX средства другому пользователю.

**Аргументы:**
- `to_id` (int): ID получателя.
- `amount` (int): Количество MIX для перевода.

**Возвращает:**
- Словарь с результатом операции.

---

### `get_transactions(type_: int = 1) -> Dict[str, Union[str, List]]`

Получает историю транзакций.

**Аргументы:**
- `type_` (int, optional): Тип транзакций. Возможные значения:
  - `1`: Входящие транзакции (по умолчанию).
  - `2`: Исходящие транзакции.

**Возвращает:**
- Словарь со списком транзакций.

## Примечания
- Убедитесь, что вы используете валидный `token` для взаимодействия с API.
- Для работы требуется библиотека `aiohttp`. Она устанавливается автоматически с `mix-api`.

