
#------test1--------
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))
#------test2--------
# import urllib.parse
# import urllib.request
#
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data)
# print(response.read())
#------test3--------
# import urllib.request
#
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())
#------test4--------
# import urllib.request
# import urllib.error
# import socket
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
#------test5--------
# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
#------test6--------
# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


