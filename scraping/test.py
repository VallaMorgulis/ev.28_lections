import requests

cookies = {
    'qrator_ssid': '1689263921.026.yiyZFIFpS2eLfh1j-5k2c2to1caripijrfjcpf2i9u29oe2ok',
    'lang': 'ru',
    'city_path': 'moscow',
    'current_path': '9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D',
    'rrpvid': '405529711154843',
    '_gid': 'GA1.2.1534562514.1689263924',
    'phonesIdent': 'f2fd78f5f334c70b216550bc2ecd72559f87b95db300ccda0f2db393bfc69610a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22c28e9db5-b85d-47e0-8bd3-b3c8ae3fbb87%22%3B%7D',
    '_gcl_au': '1.1.381601177.1689263924',
    'cartUserCookieIdent_v3': '956f6d3d85d583b41bcef719ae7b8e74ccc97a2ba44baa62b422ecf28c7ebb97a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2209a1bd27-04c5-3aaf-88af-741558b9f6b5%22%3B%7D',
    'rcuid': '64b01f341835345864ca2d31',
    'tmr_lvid': '527a085b8ca655861121dc244ef209cb',
    'tmr_lvidTS': '1689263924239',
    '_ym_uid': '16892639251590388',
    '_ym_d': '1689263925',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'PHPSESSID': '3cb8b874b06c8afb5c05de3f807ae800',
    '_csrf': '2c96dba9eabc377ea51477adfb82526ed64652844a68cf3364b761014c6600daa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Lr-S6XpoOPyvYtxV-4MKwVGrc0koeRfw%22%3B%7D',
    '_gaexp': 'GAX1.2.HzNMGjxOTSSpXmaTZ2RAdw.19583.1',
    'qrator_jsid': '1689263919.867.aZFxREfX1PRXaEDj-m7hvic94d45kerds0qnmvb6hj4lisc6f',
    'banners-hidden': '%7B%22fd1747f5-f367-47e4-bd93-c97408025730%22%3A%5B%224ce52745-fcd0-41e6-98a3-8220b03b9d05%22%5D%7D',
    'tmr_detect': '0%7C1689264132257',
    'catalogRsuSwitch': 'a39d14cc4c2417faa93ea0c1af2eb88c1706ee8a74e8d8afae7ea2bc04741f56a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22catalogRsuSwitch%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D',
    'rsu-configuration-id': '8070af74fb68abc0d4506ae9b769056a21b6f0cfb2436e3756c11a30253dc513a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22rsu-configuration-id%22%3Bi%3A1%3Bs%3A36%3A%228067df8c-de28-4d99-988d-f3f8eb069c57%22%3B%7D',
    'rr-testCookie': 'testvalue',
    '_gat': '1',
    '_gat_%5Bobject%20Object%5D': '1',
    '_ga': 'GA1.1.199728197.1689263924',
    '_ga_FLS4JETDHW': 'GS1.1.1689263923.1.1.1689264436.58.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,ky;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'qrator_ssid=1689263921.026.yiyZFIFpS2eLfh1j-5k2c2to1caripijrfjcpf2i9u29oe2ok; lang=ru; city_path=moscow; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; rrpvid=405529711154843; _gid=GA1.2.1534562514.1689263924; phonesIdent=f2fd78f5f334c70b216550bc2ecd72559f87b95db300ccda0f2db393bfc69610a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22c28e9db5-b85d-47e0-8bd3-b3c8ae3fbb87%22%3B%7D; _gcl_au=1.1.381601177.1689263924; cartUserCookieIdent_v3=956f6d3d85d583b41bcef719ae7b8e74ccc97a2ba44baa62b422ecf28c7ebb97a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2209a1bd27-04c5-3aaf-88af-741558b9f6b5%22%3B%7D; rcuid=64b01f341835345864ca2d31; tmr_lvid=527a085b8ca655861121dc244ef209cb; tmr_lvidTS=1689263924239; _ym_uid=16892639251590388; _ym_d=1689263925; _ym_isad=2; _ym_visorc=b; PHPSESSID=3cb8b874b06c8afb5c05de3f807ae800; _csrf=2c96dba9eabc377ea51477adfb82526ed64652844a68cf3364b761014c6600daa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Lr-S6XpoOPyvYtxV-4MKwVGrc0koeRfw%22%3B%7D; _gaexp=GAX1.2.HzNMGjxOTSSpXmaTZ2RAdw.19583.1; qrator_jsid=1689263919.867.aZFxREfX1PRXaEDj-m7hvic94d45kerds0qnmvb6hj4lisc6f; banners-hidden=%7B%22fd1747f5-f367-47e4-bd93-c97408025730%22%3A%5B%224ce52745-fcd0-41e6-98a3-8220b03b9d05%22%5D%7D; tmr_detect=0%7C1689264132257; catalogRsuSwitch=a39d14cc4c2417faa93ea0c1af2eb88c1706ee8a74e8d8afae7ea2bc04741f56a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22catalogRsuSwitch%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; rsu-configuration-id=8070af74fb68abc0d4506ae9b769056a21b6f0cfb2436e3756c11a30253dc513a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22rsu-configuration-id%22%3Bi%3A1%3Bs%3A36%3A%228067df8c-de28-4d99-988d-f3f8eb069c57%22%3B%7D; rr-testCookie=testvalue; _gat=1; _gat_%5Bobject%20Object%5D=1; _ga=GA1.1.199728197.1689263924; _ga_FLS4JETDHW=GS1.1.1689263923.1.1.1689264436.58.0.0',
    'Referer': 'https://www.dns-shop.ru/catalog/88f4ff1d39dee00e/osnovnye-komplektuyushhie-dlya-pk/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

response = requests.get('https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/', cookies=cookies, headers=headers)

with open('result.html', 'w') as file:
    file.write(response.text)