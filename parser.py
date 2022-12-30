from bs4 import BeautifulSoup as bs
import requests
import time
def parse(data1, data2):
    ulr = "https://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01010&UniDbQuery.From="+data1+"&UniDbQuery.To=" + data2
    print(ulr)
    try: 
        content = requests.get(ulr)
    except request.exception.Timeout as ex:
        raise SystemExit(ex)
    soup = bs(content.text, "html.parser")
    find_td = soup.find_all("td")
    arrDate = []
    arrCourse = []
    count  = 0
    for i in find_td:
        if count % 3 == 1:
            arrDate.append(i.text)
            count+=1
        elif count % 3 == 2:
            count+=1
        elif count % 3 == 0:
            if count > 0:
                arrCourse.append(i.text)
            count+=1
    print(list(zip(arrDate,arrCourse)))
    # print(content.text)
parse("04.11.2022", "07.12.2022")