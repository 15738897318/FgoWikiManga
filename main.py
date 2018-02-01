import requests


def Regu(length, number):
    if length > len(str(number)):
        return '0' * (length - len(str(number))) + str(number)


s = requests.session()
i, j, k = 1, 1, 1
counter = 1
flag = 0
while True:
    url = 'http://fgowiki.com/comics/comic/' + str(counter)  # referer
    headers = {
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
    }
    print(i, j, k, counter)
    url_request = s.get(url)
    if url_request.content.decode().find('http://manhua.fgowiki.com/Fate_Grand_Order_' + Regu(2, i) + '/' + Regu(3, j) + '/' + Regu(3, k) + '.png_middle') == -1:
        k = 1
        j += 1
        counter += 1
        flag += 1
        if flag > 1:
            i += 1
            j = 1
            k = 1
            counter -= 1
    else:
        flag = 0
        r = s.get(
            'http://manhua.fgowiki.com/Fate_Grand_Order_' + Regu(2, i) + '/' + Regu(3, j) + '/' + Regu(3, k) + '.png_middle', headers=headers)
        with open('.\\FgoWikiManga\\{}_{}_{}.jpg'.format(i, j, k), "wb") as f:
            print('>>>', i, j, k)
            f.write(r.content)
        k += 1
