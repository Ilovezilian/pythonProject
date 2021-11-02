import http.client
import ssl
import urllib.request
import urllib.response


class Main:
    __homePage = 'www.hifini.com/index.htm'

    def getHomePage(self):
        return self.__homePage

    def getPersonPageUrl(self):
        # 林俊杰
        return "www.hifini.com/tag-176.htm"

    def getPersonPage(self):
        context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        conn = http.client.HTTPSConnection(host="www.hifini.com", context=context)
        conn.request("Get", "/tag-176.htm")
        resp = conn.getresponse()
        print(resp.status, resp.reason)
        data = resp.read()
        print(len(data))
        conn.close()
        return data

    def getPersonPageWithUrlOpen(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }
        request = urllib.request.Request(url='https://www.hifini.com/tag-176.htm', method="GET", headers=headers)
        # request = urllib.request.Request(url='https://www.hifini.com/tag-176.htm', method="GET")
        with urllib.request.urlopen(request) as f:
            data = f.read()
            print(len(data))
        return None

    def pythonExamplePage(self):
        import http.client, urllib.parse
        params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn = http.client.HTTPConnection("bugs.python.org")
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)

        data = response.read()
        print(len(data))

        conn.close()


if __name__ == "__main__":
    # Main().pythonExamplePage()
    # Main().getPersonPage()
    Main().getPersonPageWithUrlOpen()
