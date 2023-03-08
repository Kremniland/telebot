import redis
from config import REDIS_PORT, REDIS_HOST


class RedisClient:
    '''Для коммуникации с redis'''
    def __init__(self):
        '''создаем подключение'''
        self.client = self._get_redis_client()

    @staticmethod
    def _get_redis_client():
        '''создаем подключение'''
        try:
            client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
            ping = client.ping()
            if ping:
                return client
        except redis.AuthenticationError:
            print('Ошибка подключения к Redis')
            raise redis.AuthenticationError
        except Exception as e:
            print(e)
            raise Exception

    def _create_caching_key(self, user_tg_id):
        '''делаем ключ типа строка'''
        return f'{user_tg_id}'

    def cache_user_data(self, user_tg_id, data):
    # async def cache_user_data(self, user_tg_id, data):
        '''сохраняем данные ключ: {значения}'''
        key = self._create_caching_key(user_tg_id)
        self.client.hmset(key, mapping=data)
        # await self.client.hmset(key, mapping=data)

    def get_user_data(self, user_tg_id):
    # async def get_user_data(self, user_tg_id):
        '''получаем данные по ключу = user_tg_id'''
        key = self._create_caching_key(user_tg_id)
        return self.client.hgetall(key)
        # return await self.client.hgetall(key)

    def delete_user_data(self, user_tg_id):
        '''Удаление данных по ключу key'''
        key = self._create_caching_key(user_tg_id)
        self.client.delete(key)

    def _create_film_key(self, user_tg_id):
        '''создаем ключ для хранения фильма который сейчас угадывает юзер'''
        return f'film_{user_tg_id}'

    def cache_user_film(self, user_tg_id, data):
        '''сохраняем фильм который сейчас угадывает юзер'''
        key = self._create_film_key(user_tg_id)
        self.client.hmset(key, mapping=data)

    def get_user_film(self, user_tg_id):
        '''достаем фильм который сейчас угадывает юзер'''
        key = self._create_film_key(user_tg_id)
        return self.client.hgetall(key)

    def delete_user_film(self, user_tg_id):
        '''удаляем фильм который сейчас угадывает юзер'''
        key = self._create_film_key(user_tg_id)
        self.client.delete(key)


# создаем объект класса для импорта
redis_client = RedisClient()

data_film = {'id': 1, 'text': 'qwe'}
user_tg_id = 123
redis_client.cache_user_film(user_tg_id, data_film)
film = redis_client.get_user_film(user_tg_id)
print(film)
