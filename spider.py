from TikTokApi import TikTokApi
api = TikTokApi()
base_url = 'https://www.tiktok.com/@sophie.seddon/video/6913966519357852929'
username = 'sophie.seddon'
test_name ='memes'
proxies = { "http": "socks5://127.0.0.1:10808", 'https': 'socks5://127.0.0.1:10808'}
user_videos_counts = 10
# tiktok_dic = api.getTikTokByUrl(base_url, language='en', proxy=proxies)
# print(tiktok_dic)
user_id = '6675959103535744006'
obj = api.getTikTokById(user_id , proxy=proxies)
#
diggcount = obj['stats']['diggCount']
sharecount = obj['stats']['shareCount']
commentcount = obj['stats']['commentCount']
playcount = obj['stats']['playCount']
data = api.getData()
videos = api.get_Video_By_TikTok(data, language='en', proxy=proxies , custom_verifyFp="")
