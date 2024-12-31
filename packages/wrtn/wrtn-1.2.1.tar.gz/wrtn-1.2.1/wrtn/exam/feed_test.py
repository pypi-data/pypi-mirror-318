from wrtn import Wrtn

client = Wrtn(refresh_token='<refresh_TOKEN>')

print(client.feed.ranking(client,2,client.DAILY)['characters'][0])