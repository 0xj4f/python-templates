# Python Style Guides

List Comprehension Readability
```py

Yes:
  result = [mapping_expr for value in iterable if filter_expr]

  result = [{'key': value} for value in iterable
            if a_long_filter_expression(value)]

  result = [complicated_transform(x)
            for x in iterable if predicate(x)]

  descriptive_name = [
      transform({'key': key, 'value': value}, color='black')
      for key, value in generate_iterable(some_input)
      if complicated_condition_is_met(key, value)
  ]

  result = []
  for x in range(10):
      for y in range(5):
          if x * y > 10:
              result.append((x, y))

  return {x: complicated_transform(x)
          for x in long_generator_function(parameter)
          if x is not None}

  squares_generator = (x**2 for x in range(10))

  unique_names = {user.name for user in users if user is not None}

  eat(jelly_bean for jelly_bean in jelly_beans
      if jelly_bean.color == 'black')

```


## ASYNC 

### ASYNC HTTP POST

v1
```python
import asyncio
import aiohttp
async def login(url, user, password):
    async with aiohttp.ClientSession() as session:
        data = {'user': user, 'password': password}
        async with session.post(url, data=data) as response:
            return await response.json()
async def main():
    url = 'example.api/api/login'
    wordlist = ['user1', 'user2', 'user3']
    tasks = [login(url, user, 'word') for user in wordlist]
    results = await asyncio.gather(*tasks)
    print(results)
if __name__ == '__main__':
    asyncio.run(main())
```
