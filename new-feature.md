## 需求

将每日粉丝获取出现错误的主页进行排查，
如果重试之后获取到了，记录一下。
如果重试之后仍然出错，进入检查环节

检查 主页名称时候更换，主页是否不可访问等

### Facebook

FB-> 输出 设置失效

AC="EAAZAlx26seVwBAHZBYx5gpOY06GHZBor7Dix5ebLsjtKg8CMvlz90vhTt7ZCXI5XtdnQ6iUcuA9znJ15zAhLjQcP3oipSy9s4W0nnJCBmBlvLxZB9vi27cSnBQY7uVAAzF3ab9kjAk1tnNGsxT6jBF7xBjJNp3zghzHhKPvAWoQZDZD"

https://graph.facebook.com/v4.0/{FID}?fields=id,fan_count&access_token={AC}"

### Twitter

TW-> 访问一个网址,填充{TID}，获取新name, 获取不到 设置失效

https://tweeterid.com/
https://tweeterid.com/ajax.php

### Instagram Public

AC="EAAZAlx26seVwBAHZBYx5gpOY06GHZBor7Dix5ebLsjtKg8CMvlz90vhTt7ZCXI5XtdnQ6iUcuA9znJ15zAhLjQcP3oipSy9s4W0nnJCBmBlvLxZB9vi27cSnBQY7uVAAzF3ab9kjAk1tnNGsxT6jBF7xBjJNp3zghzHhKPvAWoQZDZD"

调用API
https://graph.facebook.com/v4.0/17841406338772941?fields=business_discovery.username({PageName}){id,name,username,followers_count,follows_count}&access_token={AC}

替换 PageName 和 AC

正常返回:

```json
{
  "business_discovery": {
    "id": "17841408044564662",
    "ig_id": 7957300152,
    "name": "Nokia Mobile",
    "username": "nokiamobilepl",
    "followers_count": 6033,
    "follows_count": 25
  },
  "id": "17841406338772941"
}
```

异常返回

``` json
{
  "error": {
    "message": "Invalid user id",
    "type": "OAuthException",
    "code": 110,
    "error_subcode": 2207013,
    "is_transient": false,
    "error_user_title": "找不到用户",
    "error_user_msg": "找不到帐号为 nokiamobil 的用户。",
    "fbtrace_id": "AaJdejqBZKoXBfXSZcpJhq7"
  }
}
```

处理同上

### Instagram pravite

参考 网站 https://commentpicker.com/instagram-username.php

使用 page id 交换新的name

进而的处理同上

### YouTube

API_KEY: AIzaSyD76JCSGXmMO-_rlAL_yGJuW_ZqsJX33Og

调用 API
https://www.googleapis.com/youtube/v3/channels?part=id&id={PageID}&key={API_KEY}

根据返回 对 异常主页进行处理

## 输入文件

## 前缀

Facebook: https://www.facebook.com/{Page ID}/

Twitter: https://twitter.com/{Page Name}/

列表内为 [Page ID, Page Name]
