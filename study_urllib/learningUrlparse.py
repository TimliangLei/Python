from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)

result = urlparse('www.baidu.com/index.html;user?id=5#commnt',scheme='https')
print(result)

result = urlparse('http://www.baidu.com/index.html;user?id=5#commnt',scheme='https')
print(result)