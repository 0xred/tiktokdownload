import requests,re #coding bye RedShadow
###########################################
# this for link started woth https://vm.tiktok.com/
xurl = input(" add url: to chack: ")
###########################################
if "https://vm.tiktok.com/" in xurl:
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
###########################################
# #finish get url video no watermark
###########################################
    # for download
    rr = requests.get(videourl)
    with open(f'{videoid}.mp4', 'wb') as f:
        f.write(rr.content)
        print(" [+] finish")

######################################################################################
# this for link started woth https://www.tiktok.com/@"
######################################################################################
elif "https://www.tiktok.com/@" in xurl:
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
###########################################
# #finish get url video no watermark
###########################################
    # for download
    rr = requests.get(videourl)
    with open(f'{videoid2}.mp4', 'wb') as f:
        f.write(rr.content)
        print(" [+] finish")
else:    
    print("invalid link")
###########################################
###########################################
