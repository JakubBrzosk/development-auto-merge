from system import random

server = Server()
server.HttpClient.Url = "klipo.pl"

if system.IsTestEnv:
    server.TimeOut = random.next(100, 200)

server.start()