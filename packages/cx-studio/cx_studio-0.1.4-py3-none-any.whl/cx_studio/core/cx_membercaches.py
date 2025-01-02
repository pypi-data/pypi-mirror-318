import functools
import time
from collections import OrderedDict


class MemberCaches:
    def __init__(self, max_size=None):
        self._cache = OrderedDict()
        self.max_size = max_size

    def cache(self, key: str, expire=None):
        """
        定义一个装饰器函数，用于缓存函数的返回值。

        :param key: 缓存的键，用于唯一标识缓存项。
        :param expire: 缓存的过期时间，单位为秒。如果未指定，则缓存永不过期。
        :return: 装饰器函数。
        """

        def actual_decorator(func):
            """
            实际的装饰器函数，用于包装原始函数。

            :param func: 被装饰的原始函数。
            :return: 包装后的函数。
            """

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                """
                包装后的函数，用于检查缓存并返回缓存值或调用原始函数。

                :param args: 原始函数的位置参数。
                :param kwargs: 原始函数的关键字参数。
                :return: 缓存值或原始函数的返回值。
                """
                if key not in self._cache:
                    # 如果缓存中不存在指定的键，则调用原始函数并将结果和当前时间存储在缓存中
                    self._cache[key] = (func(*args, **kwargs), time.time())
                    # 如果设置了最大缓存大小，并且缓存大小超过了最大值，则删除最旧的缓存项（按照插入顺序）
                    if self.max_size and len(self._cache) > self.max_size:
                        self._cache.popitem(last=False)
                else:
                    # 如果缓存中存在指定的键，则获取缓存的值和时间戳
                    value, timestamp = self._cache[key]
                    # 如果设置了过期时间，并且当前时间减去时间戳超过了过期时间，则删除过期的缓存项并重新调用原始函数
                    if expire and time.time() - timestamp > expire:
                        del self._cache[key]
                        return self.cache(key, expire)(func)(*args, **kwargs)
                # 返回缓存中的值
                return self._cache[key][0]

            return wrapper

        return actual_decorator

    def clear(self, key: str = None):
        if key is None:
            self._cache.clear()
        elif key in self._cache:
            del self._cache[key]

    def __getitem__(self, item):
        return self._cache[item][0]

    def __setitem__(self, key, value):
        self._cache[key] = (value, time.time())

    def __delitem__(self, key):
        del self._cache[key]

    def __len__(self):
        return len(self._cache)

    def __iter__(self):
        return iter(self._cache)
