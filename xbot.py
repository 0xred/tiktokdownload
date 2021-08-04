import logging,requests,re
from aiogram import Bot, Dispatcher, executor, types
################################################################
#################################################################
headers = requests.utils.default_headers() #header
headers.update({'User-Agent': 'Mozilla/5.0 (X22; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
##########################################################
API_TOKEN = 'add token here' 
##########################################################
# Configure logging
logging.basicConfig(level=logging.INFO)
##########################################################
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
##########################################################
@dp.message_handler()
async def echo(message: types.Message):
    username = message.chat # this your username in telegram
    xurl = message.text # full url...
        ###########################################
    if "https://vm.tiktok.com/" in xurl:
        await message.answer("[+] Please Wait")
        r = requests.get(xurl, allow_redirects=False, headers={
            'Referer': 'https://tiktok.com'
        })
        e = r.headers
        d = e['location']
        s =  re.findall(r"(https://m.tiktok.com/v/[0-9]+)",d)
        h = str(s)
        videoid = h[25:][:-2]
    ###########################################
    # #finish get video id
    ###########################################
        d = (f"https://toolav.herokuapp.com/id/?video_id={videoid}")
        o = requests.get(d)
        w = o.content
        rr = str(w)
        ee =  re.findall(r'(?P<url>https://api-h2.tiktokv.com?[^\s]+)',rr)
        dd = ee[1]
        ss = str(dd)
        videourl = str(ss.replace("\"]},", ""))
        await message.answer("[+] Done! "+videourl)
    ###########################################
    ######################################################################################
    # this for link started woth https://www.tiktok.com/@"
    ######################################################################################
    elif "https://www.tiktok.com/@" in xurl:
        await message.answer("[+] Please Wait")
        eex =  re.findall(r'(/video/?/[0-9]+)',xurl)
        eex = str(eex)
        videoid2 = eex[9:][:-2]
    ###########################################
    # #finish get video id
    ###########################################
        d = (f"https://toolav.herokuapp.com/id/?video_id={videoid2}")
        o = requests.get(d)
        w = o.content
        rr = str(w)
        ee =  re.findall(r'(?P<url>https://api-h2.tiktokv.com?[^\s]+)',rr)
        dd = ee[1]
        ss = str(dd)
        videourl = str(ss.replace("\"]},", ""))
        await message.answer("[+] Done! "+videourl)
    ###########################################
    else:    
        await message.answer("[+] invalid url")
    ###########################################
    ###########################################
##########################################################

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
