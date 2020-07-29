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

## 输入文件

## 前缀

Facebook: https://www.facebook.com/{Page ID}/

Twitter: https://twitter.com/{Page Name}/

列表内为 [Page ID, Page Name]
