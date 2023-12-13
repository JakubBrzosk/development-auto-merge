from system import random

server = Server()
server.HttpClient.Url = "klipo.com"
server.HttpClient.AlwaysAuth = True

if system.IsTestEnv:
    server.TimeOut = random.next(100, 200)

server.start()