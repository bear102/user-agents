<p align="center">
  <img src="https://github.com/bear102/user-agents/blob/f4cc3bcbc1557a09af894d91d6466de7868c6a92/img/1314982.png" width="300" />
</p>

<p align="center">
  <img src="https://github.com/bear102/user-agents/blob/ced538313e8190031a29febbd63559270c74bf2a/img/8d6c8be135ef5f130110710feba8a2d2.png" alt="Logo">
</p>
<p align="center">
  <a href="https://github.com/bear102/tennis"><img src="https://img.shields.io/badge/GitHub-bear102-%2312100E.svg?style=flat&logo=github" alt="GitHub"></a>
  <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue" alt="Python">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"></a>
</p>

<p align="center">
  A repo of real user agents and scripts to get your own
</p>



## Overview

More and more, companies and websites are starting to innovate and discover new highly invasive tracking methods, such as [browser fingerprinting](https://restoreprivacy.com/browser-fingerprinting/). This could lead to less privacy and more intrusive advertising on the internet. One way to thwart the trackers is by switching up your User Agent, which allows you to maintain more online privacy.

Changing your user agent also proves useful when performing tasks like web scraping or creating bots, as it can help prevent you from getting blocked or banned.

Feel free to use these User agents in your futre projects!

## Files Explanation
In the `userAgents` folder, you will find more folders with different operating systems. Inside these subfolders, you will find the browser. For example, if you wanted Chrome and Windows agents, you would go to `userAgents/Windows/Chrome.txt`

An explanation on how to use the two python files can be found down below.


### How I sourced these agents

In Google, you can use search operators to find hidden or very specific files, including **Apache Server Logs**

For example, go to google and type in `inurl:access filetype:log`
You will see a bunch of server logs that look like this
```
66.249.67.197 - - [18/Jul/2011:03:35:52 -0500] "GET /robots.txt HTTP/1.1" 404 286 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.68.227 - - [18/Jul/2011:03:35:52 -0500] "GET / HTTP/1.1" 200 445 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
123.125.71.32 - - [18/Jul/2011:04:51:01 -0500] "GET / HTTP/1.1" 200 445 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
123.125.71.20 - - [18/Jul/2011:04:51:15 -0500] "GET /?C=D;O=A HTTP/1.1" 200 445 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
123.125.71.13 - - [18/Jul/2011:04:51:21 -0500] "GET /log/ HTTP/1.1" 200 516 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
123.125.71.12 - - [18/Jul/2011:04:51:27 -0500] "GET /?C=N;O=D HTTP/1.1" 200 443 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
```

As you can see, there are user agents. We are able to isolate these User agents and then use [this python url parser](https://github.com/selwin/python-user-agents) to classify and filter these user agents.

<br>

***

<br>

## Gathering Your Own User Agents

1. To find some server logs on google, simply google `inurl:access filetype:log` (note: not all logs will work. Dont worry, there are plenty :D)
2. Copy all the text and paste it into `logs.txt`
3. pip install pyyaml ua-parser user-agents
4. run `UAIdentifier.py`
5. run `UAInfoPyLib.py`

To create your own filters, visit [this repo](https://github.com/selwin/python-user-agents) to learn about the filters, then in `UAInfoPyLib.py`, you can edit this code

```python
for i in user_agents:
    ua_string = i
    if ua_string.endswith(")"):
        continue
    user_agent = parse(ua_string)
    oS = user_agent.os.family
    browser = user_agent.browser.family
    print(oS , ' : ' , browser)
    if not os.path.exists('userAgents/' + oS):
        os.makedirs('userAgents/' + oS)
    try:
        with open('userAgents/' + oS +'/'+ browser + '.txt', 'a+') as file:
            file.write(i + '\n')
    except:
        pass
```


## License

MIT
