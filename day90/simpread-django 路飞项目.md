> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.cnblogs.com](https://www.cnblogs.com/abldh12/p/15876174.html#top)

路飞项目
========

1.1 企业的 web 项目类型
-----------------------

1. 商城

   1.1 B2C 直销商城 商家与会员直接交易 (Business To Customer)

   1.2 B2B 批发商城 商家与商家直接交易

   1.3 B2B2C 购物平台 商家和会员在另一个商家提供的平台上面进行交易

   1.4 C2B 定制商城 会员向商家发起定制商品的需求，商家去完成。

   1.5 O2O 线上线下交易平台

   1.6 C2C 二手交易平台
2. 门户网站 [企业站和门户站]
3. 社交网络
4. 资讯论坛
5. 内部系统
6. 个人博客
7. 内容收费站

1.2 企业项目开发流程
--------------------

![](image/simpread-django路飞项目/1679072028447.png)

1.3 立项申请阶段
----------------

立项其实就是对产品项目能不能做和怎么做，提出理论基础。大的互联网公司都有比较正规的立项流程。

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

通常公司内部要研发一款软硬件的产品之前，都要经过市场评估和调研分析，产生一份 `产品项目立项报告`给公司。

产品项目立项报告一般包含以下内容：

```
项目概述需求市场需求分析和项目建设的必要性业务分析总体建设方案项目风险和风险管理可行性分析阶段


```

参考资料：[https://blog.csdn.net/m0_37370820/article/details/81077886](https://blog.csdn.net/m0_37370820/article/details/81077886)

2. 需求分析
   ========

2.1 首页
--------

功能：导航菜单、轮播图、退出登录

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.2 登录注册
------------

功能：用户登录、极验验证码、多条件登录、记住密码、短信发送、短信冷却倒计时、jwt 认证

![1679075189106](image/simpread-django路飞项目/1679075189106.png)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.3 课程列表
------------

功能：课程分类、课程列表、课程多条件筛选展示、课程分类展示、课程分页展示、课程章节课时展示、课程优惠策略

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.4 课程详情
------------

功能：课程信息展示、视频播放、富文本编辑器

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.5 购物车
----------

功能：购物车商品列表、添加商品、删除商品、勾选商品状态、商品结算、订单生成、唯一订单号生成

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.6 商品结算
------------

功能：订单商品信息列表、订单信息展示、积分计算功能、优惠券策略、课程有效期计算、第三方支付平台接口

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.7 购买成功
------------

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.8 个人中心
------------

功能列表：我的订单、订单状态改变

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

2.9 视频播放
------------

功能：视频加密播放

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

pip 换源
--------

```
1 pip3 install pymysql   国外很慢
2 pip3 install pymysql -i  地址
3 配置，以后pip3 install全走配好的源
	-来到C:\Users\oldboy\AppData\Roaming      %APPDATA% 
    -创建一个pip文件夹
    -新建一个文件pip.ini
    -写入
        [global]
        index-url = http://pypi.douban.com/simple
        [install]
        use-mirrors =true
        mirrors =http://pypi.douban.com/simple/
        trusted-host =pypi.douban.com


```

虚拟环境搭建
------------

### windows

##### 安装

```
# 建议使用pip3安装到python3环境下
pip3 install virtualenv
pip3 install virtualenvwrapper-win



```

##### 配置虚拟环境管理器工作目录

```
# 配置环境变量：
# 控制面板 => 系统和安全 => 系统 => 高级系统设置 => 环境变量 => 系统变量 => 点击新建 => 填入变量名与值
变量名：WORKON_HOME  变量值：自定义存放虚拟环境的绝对路径
eg: WORKON_HOME: D:\Virtualenvs

# 同步配置信息：
# 去向Python3的安装目录 => Scripts文件夹 => virtualenvwrapper.bat => 双击


```

### MacOS、Linux

##### 安装

```
# 建议使用pip3安装到python3环境下
pip3 install -i https://pypi.douban.com/simple virtualenv
pip3 install -i https://pypi.douban.com/simple virtualenvwrapper



```

##### 工作文件

```
# 先找到virtualenvwrapper的工作文件 virtualenvwrapper.sh，该文件可以刷新自定义配置，但需要找到它
# MacOS可能存在的位置 /Library/Frameworks/Python.framework/Versions/版本号文件夹/bin
# Linux可能所在的位置 /usr/local/bin  |  ~/.local/bin  |  /usr/bin
# 建议不管virtualenvwrapper.sh在哪个目录，保证在 /usr/local/bin 目录下有一份
# 如果不在 /usr/local/bin 目录，如在 ~/.local/bin 目录，则复制一份到 /usr/local/bin 目录
	-- sudo cp -rf ~/.local/bin/virtualenvwrapper.sh /usr/local/bin


```

##### 配置

```
# 在 ~/.bash_profile 完成配置，virtualenvwrapper的默认默认存放虚拟环境路径是 ~/.virtualenvs
# WORKON_HOME=自定义存放虚拟环境的绝对路径，需要自定义就解注
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

# 在终端让配置生效：
	-- source ~/.bash_profile


```

### 使用

```
# 在终端工作的命令

# 1、创建虚拟环境到配置的WORKON_HOME路径下
# 选取默认Python环境创建虚拟环境：
	-- mkvirtualenv 虚拟环境名称
# 基于某Python环境创建虚拟环境：
	-- mkvirtualenv -p python2.7 虚拟环境名称
	-- mkvirtualenv -p python3.6 虚拟环境名称

# 2、查看已有的虚拟环境
	-- workon

# 3、使用某个虚拟环境
	-- workon 虚拟环境名称

# 4、进入|退出 该虚拟环境的Python环境
	-- python | exit()

# 5、为虚拟环境安装模块
	-- pip或pip3 install 模块名

# 6、退出当前虚拟环境
	-- deactivate

# 7、删除虚拟环境(删除当前虚拟环境要先退出)
	-- rmvirtualenv 虚拟环境名称


```

### pycharm 使用

##### 新建项目

![1679107252638](image/simpread-django路飞项目/1679107252638.png)

##### 添加环境

![1679107280747](image/simpread-django路飞项目/1679107280747.png)

##### 使用环境

![1679107298770](image/simpread-django路飞项目/1679107298770.png)

后台：Django 项目创建
---------------------

### 环境

```
"""
为luffy项目创建一个虚拟环境
>: mkvirtualenv luffy
"""

"""
按照基础环境依赖
>: pip install django==2.0.7
>: pip install djangorestframework
>: pip install pymysql
"""


```

### 创建项目

```
"""
前提：在目标目录新建luffy文件夹
>: cd 建立的luffy文件夹
>: django-admin startproject luffyapi

开发：用pycharm打开项目，并选择提前备好的虚拟环境
"""


```

重构项目目录
------------

```
"""
├── luffyapi
	├── logs/				# 项目运行时/开发时日志目录 - 包
    ├── manage.py			# 脚本文件
    ├── luffyapi/      		# 项目主应用，开发时的代码保存 - 包
     	├── apps/      		# 开发者的代码保存目录，以模块[子应用]为目录保存 - 包
        ├── libs/      		# 第三方类库的保存目录[第三方组件、模块] - 包
    	├── settings/  		# 配置目录 - 包
			├── dev.py   	# 项目开发时的本地配置
			└── prod.py  	# 项目上线时的运行配置
		├── urls.py    		# 总路由
		└── utils/     		# 多个模块[子应用]的公共函数类库[自己开发的组件]
    └── scripts/       		# 保存项目运营时的脚本文件 - 文件夹
"""


```

配置开发环境
------------

```
"""
1.修改 wsgi.py 与 manage.py 两个文件：
# manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
# wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.prod')
# manage_prod.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.prod')

2.将settings.py删除或改名，内容拷贝到settings/dev.py中

3.修改dev.py文件内容
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

4.修改启动配置：见插图

5.在任何一个__init__.py文件中测试默认配置文件是否是dev.py文件
from django.conf import settings
print(settings)
"""


```

![1679107345321](image/simpread-django路飞项目/1679107345321.png)

环境变量
--------

#### dev

```
# 环境变量操作：小luffyapiBASE_DIR与apps文件夹都要添加到环境变量
import sys
sys.path.insert(0, BASE_DIR)
APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(1, APPS_DIR)


```

##### 在写项目直接导入 utils 文件夹也不’’错误提示’’

![1679107430197](image/simpread-django路飞项目/1679107430197.png)

封装 logger
-----------

#### dev.py

```
# 真实项目上线后，日志文件打印级别不能过低，因为一次日志记录就是一次文件io操作
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True, # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}


```

##### utils/logging.py

```
import logging
logger = logging.getLogger('django')


```

封装项目异常处理
----------------

##### utils/exception.py

```
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.views import Response
from rest_framework import status
from utils.logging import logger
import logging
logging.getLogger('django')
def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:
        # 记录服务器异常
        logger.critical('%s' % exc)
        response = Response({'detail': '服务器异常，请重试...'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response



```

```
# settings
REST_FRAMEWORK = {    'EXCEPTION_HANDLER': 'utils.exception.exception_handler',}


```

二次封装 Response 模块
----------------------

##### utils/response.py

```
from rest_framework.response import Response

class APIResponse(Response):
    def __init__(self, status=0, msg='ok', http_status=None, headers=None, exception=False, **kwargs):
        data = {
            'status': status,
            'msg': msg,
        }
        if kwargs:
            data.update(kwargs)
        super().__init__(data=data, status=http_status, headers=headers, exception=exception)


```

路由组件配置
------------

##### utils/router.py

```
from rest_framework.routers import Route, DynamicRoute, SimpleRouter as DRFSimpleRouter

class SimpleRouter(DRFSimpleRouter):
    routes = [
        # List route.  /资源s/
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',  # 群查
                'post': 'create',  # 单增、群增
                'put': 'multiple_update',  # 群整改
                'patch': 'multiple_partial_update',  # 群局改
                'delete': 'multiple_destroy',  # 群删
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
        # Detail route.  /资源s/(pk)/
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',  # 单查
                'put': 'update',  # 单整改
                'patch': 'partial_update',  # 单局改
                'delete': 'destroy'  # 单删
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
        # Dynamically generated detail routes. Generated using
        # @action(detail=True) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
    ]

# 对外提供十大接口的router对象
router = SimpleRouter()
# eg: router.register('users', UserModelViewSet, basename='user')
"""
/users/
'get': 'list',  # 群查
'post': 'create',  # 单增、群增
'put': 'multiple_update',  # 群整改
'patch': 'multiple_partial_update',  # 群局改
'delete': 'multiple_destroy',  # 群删

/users/(pk)/
'get': 'retrieve',  # 单查
'put': 'update',  # 单整改
'patch': 'partial_update',  # 单局改
'delete': 'destroy'  # 单删


```

数据库配置
----------

##### 创建数据库

```
"""
1.管理员连接数据库
>: mysql -uroot -proot

2.创建数据库
>: create database luffy default charset=utf8;

3.查看用户
>: select user,host,password from mysql.user;

# 5.7往后的版本
>: select user,host,authentication_string from mysql.user;
"""


```

##### 为指定数据库配置指定账户

```
"""
设置权限账号密码
# 授权账号命令：grant 权限(create, update) on 库.表 to '账号'@'host' identified by '密码'

1.配置任意ip都可以连入数据库的账户
>: grant all privileges on luffy.* to 'luffy'@'%' identified by 'Luffy123?';

2.由于数据库版本的问题，可能本地还连接不上，就给本地用户单独配置
>: grant all privileges on luffy.* to 'luffy'@'localhost' identified by 'Luffy123?';

3.刷新一下权限
>: flush privileges;

只能操作luffy数据库的账户
账号：luffy
密码：Luffy123?
"""


```

##### 配置文件配置

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'luffy',
        'USER': 'luffy',
        'PASSWORD': 'Luffy123?',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
import pymysql
pymysql.install_as_MySQLdb()


```

### Django 2.x 一些版本 pymysql 兼容问题

##### Django 不采用 2.0.7 版本很可能出现以下问题，需要修改源代码

![1679107554435](image/simpread-django路飞项目/1679107554435.png)

![1679107568316](image/simpread-django路飞项目/1679107568316.png)

创建 user 表
------------

```
前提：在 luffy 虚拟环境下

1.终端从项目根目录进入apps目录
>: cd luffyapi & cd apps

2.创建app
>: python ../../manage.py startapp user



```

创建 user 表对应 model:user/model
---------------------------------

```
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    # 需要pillow包的支持
    icon = models.ImageField(upload_to='icon', default='icon/default.png')

    class Meta:
        db_table = 'luffy_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


```

### 注册 user 模块，配置 User 表：dev.py

```
INSTALLED_APPS = [  
# ...    'user',]
# 自定义User表
AUTH_USER_MODEL = 'user.User'


```

### 配置 media

##### media 配置：dev.py

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



```

```
"""
├── luffyapi
    └──	luffyapi/
       	└──	media/  
			└──	icon 
				└── default.png
"""


```

##### 主路由：luffyapi/urls.py

```
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),

    re_path('^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
]


```

##### 子路由：user/urls.py

```
from django.urls import path, include
from utils.router import router

# 注册ViewSet的路由
# router.register()

urlpatterns = [
    path('', include(router.urls)),
]


```

### 数据库迁移

```
"""
1）去向大luffyapi所在目录的终端

2）安装pillow模块
pip install pillow

3）数据库迁移
python manage.py makemigrations
python manage.py migrate
"""


```

前台搭建
--------

#### vue

```
1.傻瓜式安装node: 
官网下载：https://nodejs.org/zh-cn/

2.安装cnpm: 
>: npm install -g cnpm --registry=https://registry.npm.taobao.org

3.安装vue最新脚手架: 
>: cnpm install -g @vue/cli

注：如果2、3步报错，清除缓存后重新走2、3步
>: npm cache clean --force


```

##### 创建项目

```
"""
前提：在目标目录新建luffy文件夹
>: cd 建立的luffy文件夹
>: vue create luffycity
"""


```

![1679108396201](image/simpread-django路飞项目/1679108396201.jpg)

![1679108380233](image/simpread-django路飞项目/1679108380233.jpg)

### 重构项目目录

```
"""
├── luffycity
	├── public/          			# 项目共有资源
		├── favicon.ico				# 站点图标
		└── index.html				# 主页
    ├── src/      					# 项目主应用，开发时的代码保存
    	├── assets/      			# 前台静态资源总目录
    		├── css/				# 自定义css样式
    			└── global.css		# 自定义全局样式
    		├── js/					# 自定义js样式
				└── settings.js		# 自定义配置文件
			└── img/				# 前台图片资源
		├── components/    			# 小组件目录
		├── views/  				# 页面组件目录
		├── App.vue	    			# 根组件
		├── main.js	    			# 入口脚本文件
		├── router  
			└── index.js			# 路由脚本文件
		store	  
			└── index.js			# 仓库脚本文件
    ├── vue.config.js	    		# 项目配置文件
    └── *.*							# 其他配置文件
"""


```

### 文件修订：目录中非配置文件的多余文件可以移除

#### App.vue

```
<template>
    <div id="app">
        <router-view/>
    </div>
</template>


```

##### router/index.js

```
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/home',
        redirect: '/',
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router


```

##### Home.vue

```
<template>
    <div class="home">
    </div>
</template>

<script>
    export default {
        name: 'home',
        components: {
        },
    }
</script>


```

全局配置：全局样式、配置文件
----------------------------

##### global.css

```
/* 声明全局样式和项目的初始化样式 */
body, h1, h2, h3, h4, h5, h6, p, table, tr, td, ul, li, a, form, input, select, option, textarea {
    margin: 0;
    padding: 0;
    font-size: 15px;
}

a {
    text-decoration: none;
    color: #333;
}

ul {
    list-style: none;
}

table {
    border-collapse: collapse; /* 合并边框 */
}


```

##### settings.js

```
export default {
    base_url: 'http://127.0.0.1:8000'
}


```

##### main.js

```
// 配置全局样式
import '@/assets/css/global.css'

// 配置全局自定义设置
import settings from '@/assets/js/settings'
Vue.prototype.$settings = settings;
// 在所有需要与后台交互的组件中：this.$settings.base_url + '再拼接具体后台路由'



```

目录介绍
--------

```
public
    -favicon.ico   # 
    -index.html    #整个项目的单页面
src
    -assets  #静态文件，js，css，img
    -components # 小组件，头部组件，尾部组件
    -router     # 路由相关
    -store      # vuex相关，状态管理器，临时存储数据的地方
    -views      # 页面组件
    -App.vue    # 根组件
    -main.js    # 配置文件（跟django的setting一样）
  
  
  
#任何一个组件都有三部分
	<template>
    	#html相关
	</template>
    <style>
		# css相关
	</style>

    <script>
		# js相关
    </script>


```

后台 Response 和异常和日志封装
------------------------------

```
# utils/response

from rest_framework.response import  Response


class APIResponse(Response):
    def __init__(self,code=1,msg='成功',result=None,status=None,headers=None,content_type=None,**kwargs):
        dic={
            'code':code,
            'msg':msg

             }
        if result:
            dic['result']=result
        dic.update(kwargs)

        #对象来调用对象的绑定方法，会自动传值
        super().__init__(data=dic,status=status,headers=headers,content_type=content_type)

        # 类来调用对象的绑定方法，这个方法就是一个普通函数，有几个参数就要传几个参数
        # Response.__init__(data=dic,status=status,headers=headers,content_type=content_type)


```

```
#utils/exceptions.py

#方法,加日志

from rest_framework.views import exception_handler
# from luffyapi.utils import response
from .response import APIResponse
from .logger import log
def common_exception_handler(exc, context):
    log.error('view是：%s ，错误是%s'%(context['view'].__class__.__name__,str(exc)))
    #context['view']  是TextView的对象，想拿出这个对象对应的类名
    print(context['view'].__class__.__name__)
    ret=exception_handler(exc, context)  # 是Response对象，它内部有个data

    if not ret:  #drf内置处理不了，丢给django 的，我们自己来处理
        # 好多逻辑，更具体的捕获异常
        if isinstance(exc,KeyError):
            return APIResponse(code=0, msg='key error')

        return APIResponse(code=0,msg='error',result=str(exc))
    else:
        return APIResponse(code=0,msg='error',result=ret.data)





```

```
# 封装logger
# setting.py
#日志的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 100,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True, # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}
#utils/logger

import logging
# log=logging.getLogger('名字') # 跟配置文件中loggers日志对象下的名字对应
log=logging.getLogger('django')


# 以后使用，导入直接用
from luffyapi.utils.logger import log
log.info('xxxxxx')  # 不要写print


```

2 跨域问题及解决
----------------

```
# xss：跨站脚本攻击，cors：跨域资源共享，csrf：跨站请求伪造

# 1 同源策略：请求的url地址,必须与浏览器上的url地址处于同域上,也就是域名,端口,协议相同.
# 2 CORS：跨域资源共享，允许不同的域来我的服务器拿数据
# 3 CORS请求分成两类：简单请求（simple request）和非简单请求（not-so-simple request）
	只要同时满足以下两大条件，就属于简单请求
    （1) 请求方法是以下三种方法之一：
        HEAD
        GET
        POST
     （2）HTTP的头信息不超出以下几种字段：
        Accept
        Accept-Language
        Content-Language
        Last-Event-ID
        Content-Type：只限于三个值application/x-www-form-urlencoded、multipart/form-data、text/plain
  
      #如果发送post请求，数据格式是json---》非简单请求，非简单请求发两次，一次OPTIONS请求，一次真正的请求
# 4 后端处理，开启cors，跨域资源共享（在中间中写）
class MyMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method == "OPTIONS":
            # 可以加*
            response["Access-Control-Allow-Headers"] = "Content-Type"
            response["Access-Control-Allow-Headers"] = "authorization"

        return response
#5 在setting的中间件中配置


#6使用第三方，django-cors-headers
-pip install django-cors-headers
-注册app：'corsheaders',
-配置中间件：corsheaders.middleware.CorsMiddleware
-setting中配置：
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
	'VIEW',
)
CORS_ALLOW_HEADERS = (
	'authorization',
	'content-type',
)




```

3 前后台打通
------------

```
#1 前台可以发送ajax的请求，axios
#2 cnpm install axios
#3 配置在main.js中
import axios from 'axios'   //导入安装的axios
//相当于把axios这个对象放到了vue对象中，以后用  vue对象.$axios
Vue.prototype.$axios = axios;

  
#4 使用（某个函数中）
      this.$axios.get('http://127.0.0.1:8000/home/home/'). 向某个地址发送get请求
      then(function (response) {  如果请求成功，返回的数据再response中
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
  
#5 es6的箭头函数
function (response) { console.log(response)}
response=>{ console.log(response)}


```

4 xadmin 后台管理
-----------------

![1682547421838](image/simpread-django路飞项目/1682547421838.jpg)

```
# 1 安装 pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
# 2 在app中注册
	 # xadmin主体模块
    'xadmin',
    # 渲染表格模块
    'crispy_forms',
    # 为模型通过版本控制，可以回滚数据
    'reversion',
  
# 3 数据迁移
python manage.py makemigrations
python manage.py migrate
# 4 主路由替换掉admin：主urls.py
    # xadmin的依赖
    import xadmin
    xadmin.autodiscover()
    # xversion模块自动注册需要版本控制的 Model
    from xadmin.plugins import xversion
    xversion.register_models()

    urlpatterns = [
        # ...
        path(r'xadmin/', xadmin.site.urls),
    ]
# 5 # 在项目根目录下的终端
python manage.py createsuperuser
# 账号密码设置：admin | Admin123



```

路飞项目头部组件
----------------

### 1.1 路由跳转的方式

```
#html中路由跳转
<router-link to="/">
<img src="../assets/img/head-logo.svg" alt="">
</router-link>
#js中控制路由跳转
this.$router.push('/');



```

### 1.2 头部组件 vue 代码

```
# 在components内新建Head.vue
<template>
    <div class="header">
        <div class="slogan">
            <p>老男孩IT教育 | 帮助有志向的年轻人通过努力学习获得体面的工作和生活</p>
        </div>
        <div class="nav">
            <ul class="left-part">
                <li class="logo">
                    <router-link to="/">
                        <img src="../assets/img/head-logo.svg" alt="">
                    </router-link>
                </li>
                <li class="ele">
                    <span @click="goPage('/free-course')" :class="{active: url_path === '/free-course'}">免费课</span>
                </li>
                <li class="ele">
                    <span @click="goPage('/actual-course')" :class="{active: url_path === '/actual-course'}">实战课</span>
                </li>
                <li class="ele">
                    <span @click="goPage('/light-course')" :class="{active: url_path === '/light-course'}">轻课</span>
                </li>
            </ul>

            <div class="right-part">
                <div>
                    <span>登录</span>
                    <span class="line">|</span>
                    <span>注册</span>
                </div>
    		</div>
        </div>
    </div>

</template>

<script>

    export default {
        name: "Header",
        data() {
            return {
                url_path: sessionStorage.url_path || '/',
            }
        },
        methods: {
            goPage(url_path) {
                // 已经是当前路由就没有必要重新跳转
                if (this.url_path !== url_path) {
                    this.$router.push(url_path);
                }
                sessionStorage.url_path = url_path;
            },
        },
        created() {
            sessionStorage.url_path = this.$route.path;
            this.url_path = this.$route.path;
        }
    }
</script>

<style scoped>
    .header {
        background-color: white;
        box-shadow: 0 0 5px 0 #aaa;
    }

    .header:after {
        content: "";
        display: block;
        clear: both;
    }

    .slogan {
        background-color: #eee;
        height: 40px;
    }

    .slogan p {
        width: 1200px;
        margin: 0 auto;
        color: #aaa;
        font-size: 13px;
        line-height: 40px;
    }

    .nav {
        background-color: white;
        user-select: none;
        width: 1200px;
        margin: 0 auto;

    }

    .nav ul {
        padding: 15px 0;
        float: left;
    }

    .nav ul:after {
        clear: both;
        content: '';
        display: block;
    }

    .nav ul li {
        float: left;
    }

    .logo {
        margin-right: 20px;
    }

    .ele {
        margin: 0 20px;
    }

    .ele span {
        display: block;
        font: 15px/36px '微软雅黑';
        border-bottom: 2px solid transparent;
        cursor: pointer;
    }

    .ele span:hover {
        border-bottom-color: orange;
    }

    .ele span.active {
        color: orange;
        border-bottom-color: orange;
    }

    .right-part {
        float: right;
    }

    .right-part .line {
        margin: 0 10px;
    }

    .right-part span {
        line-height: 68px;
        cursor: pointer;
    }
</style>


```

### 1.3 配置全局 css 和 setting

```
# 在main.js中配置
// 配置全局样式 @ 符号，代指src路径
import '@/assets/css/global.css'
// 配置全局自定义设置
import settings from '@/assets/js/settings'
Vue.prototype.$settings = settings;
// 在所有需要与后台交互的组件中：this.$settings.base_url + '再拼接具体后台路由'

# 在assets下的css中加入global.css
/* 声明全局样式和项目的初始化样式 */
body, h1, h2, h3, h4, h5, h6, p, table, tr, td, ul, li, a, form, input, select, option, textarea {
    margin: 0;
    padding: 0;
    font-size: 15px;
}

a {
    text-decoration: none;
    color: #333;
}

ul {
    list-style: none;
}

table {
    border-collapse: collapse; /* 合并边框 */
}


# 在assets下的js中加入settings.js
export default {
    base_url: 'http://127.0.0.1:8000'
}
 


```

### 1.4 前台配置

```
# 安装
cnpm install axios
cnpm install vue-cookies
cnpm install element-ui
cnpm install jquery
cnpm install bootstrap@3

#在main.js中配置
#axios配置
import axios from 'axios'
Vue.prototype.$axios = axios;
# vue-cookies配置
import cookies from 'vue-cookies'
Vue.prototype.$cookies = cookies;
# ElementUI的配置
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
# bootstrap配置
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

# jquery的配置，不太一样
项目根路径创一个 vue.config.js
const webpack = require("webpack");

module.exports = {
    configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $: "jquery",
                jQuery: "jquery",
                "window.jQuery": "jquery",
                "window.$": "jquery",
                Popper: ["popper.js", "default"]
            })
        ]
    }
};



```

2 路飞项目尾部组件
------------------

Footer.vue

```
<template>
    <div class="footer">
        <ul>
            <li>关于我们</li>
            <li>联系我们</li>
            <li>商务合作</li>
            <li>帮助中心</li>
            <li>意见反馈</li>
            <li>新手指南</li>
        </ul>
        <p>Copyright © luffycity.com版权所有 | 京ICP备17072161号-1</p>
    </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
    .footer {
        width: 100%;
        height: 128px;
        background: #25292e;
        color: #fff;
    }

    .footer ul {
        margin: 0 auto 16px;
        padding-top: 38px;
        width: 810px;
    }

    .footer ul li {
        float: left;
        width: 112px;
        margin: 0 10px;
        text-align: center;
        font-size: 14px;
    }

    .footer ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .footer p {
        text-align: center;
        font-size: 12px;
    }
</style>


```

3 轮播图接口
------------

```
####1  urls.py 
from rest_framework.routers import  SimpleRouter
router=SimpleRouter()
router.register('banner',views.BannerView,'banner')
urlpatterns = [
    # path('banner/', views.BannerView.as_view()),
    path('', include(router.urls)),
]

####2 views.py
from django.conf import settings
class BannerView(GenericViewSet,ListModelMixin):
    # 无论有多少条待展示的数据，最多就展示3条
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('display_order')[:settings.BANNER_COUNTER]
    serializer_class = serializer.BannerModelSerilaizer
  
### 3 serializer.py
from rest_framework import serializers
from . import models
class BannerModelSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Banner
        fields=['name','link','img']
  
### 4 models.py
from utils.models import BaseModel


class Banner(BaseModel):
    name=models.CharField(max_length=32,verbose_name='图片名字')
    img=models.ImageField(upload_to='banner',verbose_name='轮播图',help_text='图片尺寸必须是：3840*800',null=True)
    link=models.CharField(max_length=32,verbose_name='跳转连接')
    info=models.TextField(verbose_name='图片简介')
    # type=models.IntegerField(choices=)

    def __str__(self):
        return self.name
####5 utils/models.py

class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=True, verbose_name='是否展示')
    display_order = models.IntegerField()
    class Meta:
        abstract=True  # 一定不要忘了
  
### 6 settings/const.py
# 首页轮播图个数
BANNER_COUNTER=3

#### 7 settings/dev.py
from .const import *


```

4 轮播图组件
------------

Banner.vue

```
<template>

    <div id="banner">

        <el-carousel height="400px">
            <el-carousel-item v-for="item in banner_list">
                <!--<img src="../assets/img/banner1.png" alt="">-->
                <router-link :to="item.link">
                    <img :src="item.img" :alt="item.name">
                </router-link>

            </el-carousel-item>
        </el-carousel>
    </div>

</template>

<script>
    export default {
        name: "Banner",
        // data:function(){},
        data() {
            return {
                banner_list: []
            }
        },
        created() {
            //当banner组件一创建，就向后台发请求，拿回轮播图数据
            this.$axios.get(this.$settings.base_url + '/home/banner/').then(response => {
                console.log(response.data)
                this.banner_list=response.data
            }).catch(error => {
            })
        },

    }
</script>

<style scoped>
    .el-carousel__item {
        height: 400px;
        min-width: 1200px;
    }

    .el-carousel__item img {
        height: 400px;
        /*margin-left: 20px;*/
        /*margin-left: calc(50% - 1920px / 2);*/
    }
</style>


```

前端路由配置

```
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/free-course',
        name: 'FreeCourse',
        component: FreeCourse
    }, {
        path: '/light-course',
        name: 'LightCourse',
        component: LightCourse
    }, {
        path: '/actual-course',
        name: 'ActualCourse',
        component: ActualCourse
    },

]


```

5 git 的使用
------------

```
#1  协同开发，版本管理
#2 svn（集中式管理），git（分布式管理）
#3 git装完，既有客户端，又有服务的
#4 git工作流程
	-工作区，暂存区，版本库
#5 远程仓库：github，码云，公司内部（gitlab）

# 6 安装：一路下一步
# 7 右键--git bash here

# 8 git 命令
	-初始化：git init 文件夹名
    -初始化：git init   #当前路径全被管理

	-git status
    -git add a.txt  # 把a提交到暂存区
	-git add .
    -git commit -m '注释，我新增了a'      # 把暂存区的所有都提交到版本库
    -需要增加作者信息
      git config --global user.email "lqz@qq.com"
  	  git config --global user.name "lqz"
  
      git config  user.email "egon@qq.com"
  	  git config  user.name "egon"

	-把a的新增提交到版本管理
    -新建b，在a中新增一行
    -git checkout .   # 回复到提交版本的位置，a是空的，b没有被git管理，所有，是什么样，还是什么样
    -git log   # 查看版本管理的日志
    -git reflog # 查看日志，条数更多，内容更少
	-git reset --hard 版本号
# 红色表示未被管理
# 绿色表示提交到暂存区了

# 忽略文件
	-空文件夹不被管理
	-指定某些文件或者文件夹不被git管理
    -在项目根路径，跟.git文件夹一个路径，新建.gitignore.，在里面配置
    - 语法：
    	# 号是注释，没有用
        文件夹名字，表示文件夹忽略，不被管理
        /dist 表示根路径下的dist文件夹，不被管理
        *.py   表示后缀名为py的文件，都被忽略
        *.log*
# 分支操作
	-查看分支 git branch   查看所有分支，分支是绿的，表示在当前分支上
    -创建分支 git branch dev
    -创建并切换到 git checkout -b dev
    -删除分支 git branch -d dev
    -切换分支 git checkout dev
    -合并分支 git merge 分支名  # 把dev分支合并到master分支：切换到master分支，执行合并dev分支的命令
  



```

it 远程连接
-----------

```
# 1 码云（国内，快）
# 2 新建仓库的时候，不要勾选Readme初始化这个而仓库
# 3 现在什么都没有，新建仓库
    mkdir lqz_test
    cd lqz_test
    git init
    touch a.txt
    git add a.txt
    git commit -m "first commit"
    git remote add origin https://gitee.com/liuqingzheng/lqz_test.git  # 连接远程
    git push  origin master
# 4 已经有了仓库
    cd b
    git remote add origin https://gitee.com/liuqingzheng/lqz_test.git
    git push origin master
  
  
  
# 5 git 远程操作命令
	-git remote # 查看远程仓库（没有就看不到）
    -git remote add origin https://gitee.com/liuqingzheng/lqz_test.git # 跟远程仓库建立连接
    -git push origin master  # 把本地的master分支提交到远程的origin，需要输入用户名和密码（之前存的需要删掉）


```

2 git 项目创始者和开发者
------------------------

```
# 1 项目创始者，如上
# 2 项目开发者，参与者（换了一台电脑），把代码拉下来继续开发
	-git clone https://gitee.com/liuqingzheng/lqz_test.git
    -能看到完整的版本和日志控制
    -可以回复到任意版本
    	-git rest --hard 版本号
    -git checkout . # 表示回到指针指向的版本，因为已经用git rest --hard把指针移动了，所以checkout .就是当前再的版本上的东西
# 3 本地新增c.txt文件
	-提交到暂存区
    -提交到版本库（没有提交到远程，远程看不到）
    -提交到远程：git push origin master
  
  
# 4 让a文件夹中的代码成为最新的
	-git pull origin master
  
# 5 重点：每次再提交代码之前，一定要先更新代码（拉），如果不拉提不上去


```

3 ssh 连接和 https 连接
-----------------------

```
# 1 公司内部大部分用ssh连接
	-领导给你一个git地址（项目地址）
    -你 git clone 地址  到本地
    -改代码，改完了---》提交（禁止）
    -ssh配置，以后都不用输密码了
# 2 配置如何做
	-对称加密（加密和解密用同一套秘密）
    -非对称加密（公钥和私钥），公钥加密，私钥解密
  
    -生成一对公钥和私钥（用命令）
    	-https://gitee.com/help/articles/4181
        -ssh-keygen -t rsa -C "lqz@qq.com" 生成到用户家目录的.ssh文件夹下（一个公钥，一个私钥）  
        -把公钥复制出来，再码云上配置
 
# 跟远程操作有三个命令
git pull
git push
-git feacth（一般不用，他跟pull是一个东西，当作不知道）


```

### pycharm 操作 git

```
# 1 安装git
# 2 再pycharm中配置，setting---》git--->git.exe的地址
# 3 git clone --->等同于下图
# 4 使用pycharm创建本地分支（见下图）
# 5 拉取代码，如下图
# 6 push代码，如下图


```

4 协同开发
----------

```
# 1 协同开发出现冲突，如何解决
# 2 git pull origin master  拉下远程代码，同事和你修改了同一个位置，会冲突，如下
<<<<<<< HEAD
你的代码
=======
别人代码
>>>>>>> origin/master
# 3 处理方案
    -删除你的代码
    -删除同时代码
    -合并你们的代码


```

5 合并分支出现冲突
------------------

```
# 1 分支：本地分支，远程分支

# 2 创建本地分支
	-git checkout -b dev
# 3 把本地分支提交到远程
	-git push origin dev  



```

5 线上分支合并
--------------

```
# 如果看到可自动合并，表示合并后不会有冲突，正常操作即可
# 测试人员点通过，直接合并即可


```

6 线上回滚
----------

```
# 1 切换到master分支
# 2 回滚打某个版本  git reset --hard  版本号
# 3 强制提交代码 git push origin master -f



```

7 分支合并出现冲突解决
----------------------

```
# 1 远端创建一个dev分支
	-在远端直接创建
    -本地创建，提交到远端
    git checkout -b dev
    git push origin dev
# 2 本地新建一个dev_bug分支
	-dev_bug分支改了文件
    -dev分支改了同样的文件
    -合并就出冲突
    -git merge dev_bug （在dev分支上操作）
    -解决冲突（删你的，同事的，合并起来）
    -git add .  git commit 
    -正常了，冲突解决
 # 3 手动线下合并代码并提交到远程
	-git checkout master
    -git merge dev 
    -如果出冲突，解决
    -git add .
    -git commit 
    -git push..


```

7 vue 登录页面
--------------

```
# Login.vue
<template>
    <div class="login">
    <span @click="close_login">X</span>
    </div>
</template>

<script>
    export default {
        name: "Login",
        methods:{
            close_login(){
                //子传父组件 this.$emit,给父组件传递一个事件
                this.$emit("close")
            },

        },

    }
</script>

<style scoped>
.login{
    width: 100vw;
    height: 100vw;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 666;
    background-color: rgba(0,0,0,0.3);
}
    span{
        font-size: 30px;
        cursor: pointer;
    }
</style>

# Head.vue
#template中
<div class="right-part">
<div>
<span @click="pull_login">登录</span>
<span class="line">|</span>
<span>注册</span>
</div>
</div>
</div>

<Login v-if="is_login" @close="close"/>
<!--is_login是True就显示，false就不显示-->
</div>
# js中
pull_login(){
    this.is_login=true
},
close(){
    this.is_login=false
},


```

补充
====

1 pycharm 找回误删，修改的东西
------------------------------

2 git 的变基
------------

```
git rebase


```

登陆注册模态框
--------------

```
# Login.vue
<template>
    <div class="login">
        <div class="box">
            <i class="el-icon-close" @click="close_login"></i>
            <div class="content">
                <div class="nav">
                    <span :class="{active: login_method === 'is_pwd'}"
                          @click="change_login_method('is_pwd')">密码登录</span>
                    <span :class="{active: login_method === 'is_sms'}"
                          @click="change_login_method('is_sms')">短信登录</span>
                </div>
                <el-form v-if="login_method === 'is_pwd'">
                    <el-input
                            placeholder="用户名/手机号/邮箱"
                            prefix-icon="el-icon-user"
                            v-model="username"
                            clearable>
                    </el-input>
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-key"
                            v-model="password"
                            clearable
                            show-password>
                    </el-input>
                    <el-button type="primary">登录</el-button>
                </el-form>
                <el-form v-if="login_method === 'is_sms'">
                    <el-input
                            placeholder="手机号"
                            prefix-icon="el-icon-phone-outline"
                            v-model="mobile"
                            clearable
                            @blur="check_mobile">
                    </el-input>
                    <el-input
                            placeholder="验证码"
                            prefix-icon="el-icon-chat-line-round"
                            v-model="sms"
                            clearable>
                        <template slot="append">
                            <span class="sms" @click="send_sms">{{ sms_interval }}</span>
                        </template>
                    </el-input>
                    <el-button type="primary">登录</el-button>
                </el-form>
                <div class="foot">
                    <span @click="go_register">立即注册</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',
                mobile: '',
                sms: '',
                login_method: 'is_pwd',
                sms_interval: '获取验证码',
                is_send: false,
            }
        },
        methods: {
            close_login() {
                this.$emit('close')
            },
            go_register() {
                this.$emit('go')
            },
            change_login_method(method) {
                this.login_method = method;
            },
            check_mobile() {
                if (!this.mobile) return;
                if (!this.mobile.match(/^1[3-9][0-9]{9}$/)) {
                    this.$message({
                        message: '手机号有误',
                        type: 'warning',
                        duration: 1000,
                        onClose: () => {
                            this.mobile = '';
                        }
                    });
                    return false;
                }
                this.is_send = true;
            },
            send_sms() {

                if (!this.is_send) return;
                this.is_send = false;
                let sms_interval_time = 60;
                this.sms_interval = "发送中...";
                let timer = setInterval(() => {
                    if (sms_interval_time <= 1) {
                        clearInterval(timer);
                        this.sms_interval = "获取验证码";
                        this.is_send = true; // 重新回复点击发送功能的条件
                    } else {
                        sms_interval_time -= 1;
                        this.sms_interval = `${sms_interval_time}秒后再发`;
                    }
                }, 1000);
            }
        }
    }
</script>

<style scoped>
    .login {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .box {
        width: 400px;
        height: 420px;
        background-color: white;
        border-radius: 10px;
        position: relative;
        top: calc(50vh - 210px);
        left: calc(50vw - 200px);
    }

    .el-icon-close {
        position: absolute;
        font-weight: bold;
        font-size: 20px;
        top: 10px;
        right: 10px;
        cursor: pointer;
    }

    .el-icon-close:hover {
        color: darkred;
    }

    .content {
        position: absolute;
        top: 40px;
        width: 280px;
        left: 60px;
    }

    .nav {
        font-size: 20px;
        height: 38px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span {
        margin: 0 20px 0 35px;
        color: darkgrey;
        user-select: none;
        cursor: pointer;
        padding-bottom: 10px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span.active {
        color: black;
        border-bottom: 3px solid black;
        padding-bottom: 9px;
    }

    .el-input, .el-button {
        margin-top: 40px;
    }

    .el-button {
        width: 100%;
        font-size: 18px;
    }

    .foot > span {
        float: right;
        margin-top: 20px;
        color: orange;
        cursor: pointer;
    }

    .sms {
        color: orange;
        cursor: pointer;
        display: inline-block;
        width: 70px;
        text-align: center;
        user-select: none;
    }
</style>


```

```
# Register.vue
<template>
    <div class="register">
        <div class="box">
            <i class="el-icon-close" @click="close_register"></i>
            <div class="content">
                <div class="nav">
                    <span class="active">新用户注册</span>
                </div>
                <el-form>
                    <el-input
                            placeholder="手机号"
                            prefix-icon="el-icon-phone-outline"
                            v-model="mobile"
                            clearable
                            @blur="check_mobile">
                    </el-input>
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-key"
                            v-model="password"
                            clearable
                            show-password>
                    </el-input>
                    <el-input
                            placeholder="验证码"
                            prefix-icon="el-icon-chat-line-round"
                            v-model="sms"
                            clearable>
                        <template slot="append">
                            <span class="sms" @click="send_sms">{{ sms_interval }}</span>
                        </template>
                    </el-input>
                    <el-button type="primary">注册</el-button>
                </el-form>
                <div class="foot">
                    <span @click="go_login">立即登录</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                mobile: '',
                password: '',
                sms: '',
                sms_interval: '获取验证码',
                is_send: false,
            }
        },
        methods: {
            close_register() {
                this.$emit('close', false)
            },
            go_login() {
                this.$emit('go')
            },
            check_mobile() {
                if (!this.mobile) return;
                if (!this.mobile.match(/^1[3-9][0-9]{9}$/)) {
                    this.$message({
                        message: '手机号有误',
                        type: 'warning',
                        duration: 1000,
                        onClose: () => {
                            this.mobile = '';
                        }
                    });
                    return false;
                }
                this.is_send = true;
            },
            send_sms() {
                if (!this.is_send) return;
                this.is_send = false;
                let sms_interval_time = 60;
                this.sms_interval = "发送中...";
                let timer = setInterval(() => {
                    if (sms_interval_time <= 1) {
                        clearInterval(timer);
                        this.sms_interval = "获取验证码";
                        this.is_send = true; // 重新回复点击发送功能的条件
                    } else {
                        sms_interval_time -= 1;
                        this.sms_interval = `${sms_interval_time}秒后再发`;
                    }
                }, 1000);
            }
        }
    }
</script>

<style scoped>
    .register {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .box {
        width: 400px;
        height: 480px;
        background-color: white;
        border-radius: 10px;
        position: relative;
        top: calc(50vh - 240px);
        left: calc(50vw - 200px);
    }

    .el-icon-close {
        position: absolute;
        font-weight: bold;
        font-size: 20px;
        top: 10px;
        right: 10px;
        cursor: pointer;
    }

    .el-icon-close:hover {
        color: darkred;
    }

    .content {
        position: absolute;
        top: 40px;
        width: 280px;
        left: 60px;
    }

    .nav {
        font-size: 20px;
        height: 38px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span {
        margin-left: 90px;
        color: darkgrey;
        user-select: none;
        cursor: pointer;
        padding-bottom: 10px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span.active {
        color: black;
        border-bottom: 3px solid black;
        padding-bottom: 9px;
    }

    .el-input, .el-button {
        margin-top: 40px;
    }

    .el-button {
        width: 100%;
        font-size: 18px;
    }

    .foot > span {
        float: right;
        margin-top: 20px;
        color: orange;
        cursor: pointer;
    }

    .sms {
        color: orange;
        cursor: pointer;
        display: inline-block;
        width: 70px;
        text-align: center;
        user-select: none;
    }
</style>


```

```
#Head.vue
#template底部
<div class="right-part">
<div>
<span @click="put_login">登录</span>
<span class="line">|</span>
<span @click="put_register">注册</span>

</div>
</div>
<Login v-if="is_login" @close="close_login" @go="put_register"/>
<Register v-if="is_register" @close="close_register" @go="put_login"/>

# js
<script>
    import Login from './Login'
    import Register from './Register'

    export default {
        name: "Header",
        data() {
            return {
                url_path: sessionStorage.url_path || '/',
                is_login: false,
                is_register: false,
            }
        },
        methods: {
            goPage(url_path) {
                // 传入的路由如果不是当前所在路径，就跳转
                if (this.url_path !== url_path) {
                    this.$router.push(url_path);
                }
                sessionStorage.url_path = url_path;
            },
            put_login() {
                this.is_login = true;
                this.is_register = false;
            },
            put_register() {
                this.is_login = false;
                this.is_register = true;
            },
            close_login() {
                this.is_login = false;
            },
            close_register() {
                this.is_register = false;
            }
        },
        created() {
            sessionStorage.url_path = this.$route.path;
            this.url_path = this.$route.path;
        },
        components: {
            Login,
            Register
        }


    }
</script>



```

2 登陆注册接口分析
------------------

```
# 1 多方式登录接口
# 2 手机号登录接口
# 3 发送验证码接口
# 4 注册接口
# 5 校验手机号是否存在接口


```

3 多种登陆方式
--------------

```
# 路由
from django.urls import path,include
from . import views
from rest_framework.routers import SimpleRouter
router=SimpleRouter()
router.register('',views.LoginView,'login')
urlpatterns = [
    path('',include(router.urls) ),
]

# 视图类
from rest_framework.viewsets import ViewSet
from . import serializer
from luffyapi.utils.response import APIResponse
from rest_framework.decorators import action
class LoginView(ViewSet):
    @action(methods=['POST'],detail=False)
    def login(self,request,*args,**kwargs):
        ser=serializer.UserSerilaizer(data=request.data)
        if ser.is_valid():
            token=ser.context['token']
            username=ser.context['user'].username
            return APIResponse(token=token,username=username)
        else:
            return APIResponse(code=0,msg=ser.errors)
# 序列化类
from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError
class UserSerilaizer(serializers.ModelSerializer):
    username=serializers.CharField()
    class Meta:
        model=models.User
        fields=['username','password','id']
        extra_kwargs={
            'id':{'read_only':True},
            'password':{'write_only':True}
        }

    def validate(self, attrs):

        # 多种登录方式
        user=self._get_user(attrs)
        # 签发token
        token=self._get_token(user)
        # 放到context中，我在视图类中可以取出来
        self.context['token']=token
        self.context['user']=user


        return attrs


    def _get_user(self,attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        import re
        if re.match('^1[3-9][0-9]{9}$',username):
            user=models.User.objects.filter(telephone=username).first()
        elif re.match('^.+@.+$',username):  #邮箱
            user=models.User.objects.filter(email=username).first()
        else:
            user=models.User.objects.filter(username=username).first()
        if user:
            ret=user.check_password(password)
            if ret:
                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

    def _get_token(self,user):
        from rest_framework_jwt.serializers import jwt_payload_handler,jwt_encode_handler
        payload=jwt_payload_handler(user)  # 通过user对象获得payload
        token=jwt_encode_handler(payload) # 通过payload获得token
        return token


```

4 cookies 修改页面登陆状态
--------------------------

```
1 重点，cookie操作
    this.$cookies.set('key',value,过期时间秒)
    this.$cookies.get('key')
    this.$cookies.remove('key')
2 
# template
<el-button type="primary" @click="login_password">登录</el-button>
#js
login_password() {
    if (this.username && this.password) {
        //发送请求
        this.$axios.post(this.$settings.base_url + '/user/login/', {
            username: this.username,
            password: this.password


        }).then(response => {
            console.log(response.data)
            //把用户信息保存到cookie中
            // this.$cookies.set('key','value','过期时间,按s计')
            this.$cookies.set('token',response.data.token,'7d')
            this.$cookies.set('username',response.data.username,'7d')
            //关闭登录窗口(子传父)
            this.$emit('close')
            //给父组件，Head传递一个事件，让它从cookie中取出token和username
            this.$emit('loginsuccess')
        }).catch(errors => {
        })
    } else {
        this.$message({
            message: '用户名或密码必须填哦',
            type: 'warning',

        });
    }
},


```

5 前台注销
----------

```
# Head.vue
### template
<span @click="logout">注销</span>
### js
logout(){
    //清除cookie
    this.$cookies.remove('token')
    this.$cookies.remove('username')
    //把两个变量值为空
    this.username=''
    this.token=''
},


```

6 手机号是否存在接口
--------------------

```
# urls.py 如果不重写视图类不需要动
# views.py
class LoginView(ViewSet):
    @action(methods=['GET'], detail=False)
    def check_telephone(self,request,*args,**kwargs):
        import re
        telephone=request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}',telephone):
            return APIResponse(code=0,msg='手机号不合法')
        try:
            models.User.objects.get(telephone=telephone)
            return APIResponse(code=1)
        except:
            return APIResponse(code=0,msg='手机号不存在')


```

7 腾讯云短信服务
----------------

```
#0 注册一个公众号（）
	-https://mp.weixin.qq.com/
    -注册订阅号，一路下一步，申请个人
    -截一个图（首页）
#1 腾讯云，---注册---实名：-https://console.cloud.tencent.com/smsv2
#2 https://console.cloud.tencent.com/smsv2/csms-sign/create
	-把图传上去，认证
#3 创建模板（审核）
#4 应用管理（创建一个应用，记住appid和App Key）
#5 扣代码（https://cloud.tencent.com/document/product/382/11672）



# 7 帮助文档
	-API：一堆web接口，基于API接口来写
    -SDK：软件开发工具包软件,别人基于api接口，用不同语言封装的工具包，我们可以直接调用方法完成某些事


```

8 短信验证码接口
----------------

```
# lib/tx_sms
#__init__.py
from .send import  get_code,send_message
#send.py


from qcloudsms_py import SmsSingleSender
from luffyapi.utils.logger import log
from . import settings


# 生成一个四位随机验证码
def get_code():
    import random
    s_code=''
    for i in range(4):
        s_code+=str(random.randint(0,9))
    return s_code


def send_message(phone,code):

    ssender = SmsSingleSender(settings.appid, settings.appkey)
    params = [code, '3']  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone, settings.template_id, params, sign=settings.sms_sign, extend="", ext="")
        if result.get('result') == 0:
            return True
        else:
            return False
    except Exception as e:
        log.error('手机号：%s,短信发送失败,错误为：%s'%(phone,str(e)))

#settings.py

# 短信的配置
# 短信应用 SDK AppID
appid = 140039846  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "fd972f6da15add4de47b50b8dbe930"
# 短信模板ID，需要在短信控制台中申请
template_id = 66935  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "小猿取经"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请



# views.py
    @action(methods=['GET'], detail=False)
    def send(self,request,*args,**kwargs):
        '''
        发送验证码接口
        :return:
        '''
        import re
        from luffyapi.libs.tx_sms import get_code,send_message
        from django.core.cache import cache
        from django.conf import settings
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        code=get_code()
        result=send_message(telephone,code)
        # 验证码保存（保存到哪？）
        # sms_cache_%s
        cache.set(settings.PHONE_CACHE_KEY%telephone,code,180)
        if result:
            return APIResponse(code=1,msg='验证码发送成功')
        else:
            return APIResponse(code=0, msg='验证码发送失败')


```

短信接口频率限制
----------------

```
# throttlings.py
from rest_framework.throttling import SimpleRateThrottle
class SMSThrotting(SimpleRateThrottle):
    scope = 'sms'
    def get_cache_key(self, request, view):
        telephone = request.query_params.get('telephone')
        #'throttle_%(scope)s_%(ident)s'%{}
        return self.cache_format%{'scope':self.scope,'ident':telephone}
  
# 配置在视图类上
from .throttlings import SMSThrotting
class SendSmSView(ViewSet):
    throttle_classes = [SMSThrotting,]
  
# 早setting中配置
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES':{
        'sms':'1/m'  # key要跟类中的scop对应
    }
}


```

2 验证码登陆接口
----------------

```
# views.py
@action(methods=['POST'],detail=False)
def code_login(self,request,*args,**kwargs):
    ser = serializer.CodeUserSerilaizer(data=request.data)
    if ser.is_valid():
        token = ser.context['token']
        username = ser.context['user'].username
        return APIResponse(token=token, username=username)
    else:
        return APIResponse(code=0,msg=ser.errors)
  
# serializer
class CodeUserSerilaizer(serializers.ModelSerializer):
    code=serializers.CharField()
    class Meta:
        model = models.User
        fields = ['telephone', 'code']

    def validate(self, attrs):
        user=self._get_user(attrs)
        # 用户存在，签发token
        token = self._get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs


    def _get_user(self, attrs):
        from django.core.cache import cache
        from django.conf import settings
        import re
        telephone = attrs.get('telephone')
        code = attrs.get('code')

        # 取出原来的code
        cache_code=cache.get(settings.PHONE_CACHE_KEY%telephone)
        if code ==cache_code:
            # 验证码通过
            if re.match('^1[3-9][0-9]{9}$', telephone):
                user = models.User.objects.filter(telephone=telephone).first()
                if user:
                    # 把使用过的验证码删除
                    cache.set(settings.PHONE_CACHE_KEY % telephone,'')
                    return user
                else:
                    raise ValidationError('用户不存在')
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码错误')


    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)  # 通过user对象获得payload
        token = jwt_encode_handler(payload)  # 通过payload获得token
        return token



```

3 前台发送验证码
----------------

```
<template>
    <div class="login">
        <div class="box">
            <i class="el-icon-close" @click="close_login"></i>
            <div class="content">
                <div class="nav">
                    <span :class="{active: login_method === 'is_pwd'}"
                          @click="change_login_method('is_pwd')">密码登录</span>
                    <span :class="{active: login_method === 'is_sms'}"
                          @click="change_login_method('is_sms')">短信登录</span>
                </div>
                <el-form v-if="login_method === 'is_pwd'">
                    <el-input
                            placeholder="用户名/手机号/邮箱"
                            prefix-icon="el-icon-user"
                            v-model="username"
                            clearable>
                    </el-input>
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-key"
                            v-model="password"
                            clearable
                            show-password>
                    </el-input>
                    <el-button type="primary" @click="login_password">登录</el-button>
                </el-form>
                <el-form v-if="login_method === 'is_sms'">
                    <el-input
                            placeholder="手机号"
                            prefix-icon="el-icon-phone-outline"
                            v-model="mobile"
                            clearable
                            @blur="check_mobile">
                    </el-input>
                    <el-input
                            placeholder="验证码"
                            prefix-icon="el-icon-chat-line-round"
                            v-model="sms"
                            clearable>
                        <template slot="append">
                            <span class="sms" @click="send_sms">{{ sms_interval }}</span>
                        </template>
                    </el-input>
                    <el-button type="primary" @click="code_login">登录</el-button>
                </el-form>
                <div class="foot">
                    <span @click="go_register">立即注册</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',
                mobile: '',
                sms: '',
                login_method: 'is_pwd',
                sms_interval: '获取验证码',
                is_send: false,
            }
        },
        methods: {
            close_login() {
                this.$emit('close')
            },
            go_register() {
                this.$emit('go')
            },
            change_login_method(method) {
                this.login_method = method;
            },
            check_mobile() {
                if (!this.mobile) return;
                //字符串.match(/正则表达式/)
                if (!this.mobile.match(/^1[3-9][0-9]{9}$/)) {
                    this.$message({
                        message: '手机号有误',
                        type: 'warning',
                        duration: 1000,
                        onClose: () => {
                            this.mobile = '';
                        }
                    });
                    return false;
                }
                //发送axios请求
                // this.$axios.get(this.$settings.base_url+'/user/check_telephone/telephone='+this.mobile})
                this.$axios.get(this.$settings.base_url + '/user/check_telephone/', {params: {telephone: this.mobile}}).then(response => {
                    if (response.data.code) {
                        //手机号存在，允许发送验证码
                        this.is_send = true;
                    } else {
                        this.$message({
                            message: '手机号不存在',
                            type: 'warning',
                            duration: 1000,
                            onClose: () => {
                                this.mobile = '';
                            }
                        });
                    }
                }).catch(error => {
                    console.log(error)
                })

            },
            send_sms() {

                if (!this.is_send) return;
                this.is_send = false;
                let sms_interval_time = 60;
                this.sms_interval = "发送中...";

                this.$axios.get(this.$settings.base_url + '/user/send/', {params: {'telephone': this.mobile}})
                    .then(response => {
                        if (response.data.code) {
                            this.$message({
                                message: '发送验证码成功',
                                type: 'success',
                                duration: 1000,

                            });
                        }
                    })


                // setInterval(()=>{},100)
                //定时器：每隔一秒种，把数字减一，当减到小于1，按钮又能点了，显示获取验证码
                let timer = setInterval(() => {
                    if (sms_interval_time <= 1) {
                        clearInterval(timer);  //如果小于等于1，把定时器清除
                        this.sms_interval = "获取验证码";
                        this.is_send = true; // 重新回复点击发送功能的条件
                    } else {
                        sms_interval_time -= 1;
                        this.sms_interval = `${sms_interval_time}秒后再发`;
                    }
                }, 1000);
            },

            login_password() {
                if (this.username && this.password) {
                    //发送请求
                    this.$axios.post(this.$settings.base_url + '/user/login/', {
                        username: this.username,
                        password: this.password


                    }).then(response => {
                        console.log(response.data)
                        //把用户信息保存到cookie中
                        // this.$cookies.set('key','value','过期时间,按s计')
                        this.$cookies.set('token', response.data.token, '7d')
                        this.$cookies.set('username', response.data.username, '7d')
                        //关闭登录窗口(子传父)
                        this.$emit('close')
                        //给父组件，Head传递一个事件，让它从cookie中取出token和username
                        this.$emit('loginsuccess')
                    }).catch(errors => {
                    })
                } else {
                    this.$message({
                        message: '用户名或密码必须填哦',
                        type: 'warning',

                    });
                }
            },
            code_login() {

                if (this.mobile && this.sms) {
                    //发送请求
                    this.$axios.post(this.$settings.base_url + '/user/code_login/', {
                        telephone: this.mobile,
                        code: this.sms

                    }).then(response => {
                        console.log(response.data)
                        //把用户信息保存到cookie中
                        // this.$cookies.set('key','value','过期时间,按s计')
                        this.$cookies.set('token', response.data.token, '7d')
                        this.$cookies.set('username', response.data.username, '7d')
                        //关闭登录窗口(子传父)
                        this.$emit('close')
                        //给父组件，Head传递一个事件，让它从cookie中取出token和username
                        this.$emit('loginsuccess')
                    }).catch(errors => {
                    })
                } else {
                    this.$message({
                        message: '手机号或验证码必填',
                        type: 'warning',

                    });
                }

            },
        }
    }
</script>

<style scoped>
    .login {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .box {
        width: 400px;
        height: 420px;
        background-color: white;
        border-radius: 10px;
        position: relative;
        top: calc(50vh - 210px);
        left: calc(50vw - 200px);
    }

    .el-icon-close {
        position: absolute;
        font-weight: bold;
        font-size: 20px;
        top: 10px;
        right: 10px;
        cursor: pointer;
    }

    .el-icon-close:hover {
        color: darkred;
    }

    .content {
        position: absolute;
        top: 40px;
        width: 280px;
        left: 60px;
    }

    .nav {
        font-size: 20px;
        height: 38px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span {
        margin: 0 20px 0 35px;
        color: darkgrey;
        user-select: none;
        cursor: pointer;
        padding-bottom: 10px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span.active {
        color: black;
        border-bottom: 3px solid black;
        padding-bottom: 9px;
    }

    .el-input, .el-button {
        margin-top: 40px;
    }

    .el-button {
        width: 100%;
        font-size: 18px;
    }

    .foot > span {
        float: right;
        margin-top: 20px;
        color: orange;
        cursor: pointer;
    }

    .sms {
        color: orange;
        cursor: pointer;
        display: inline-block;
        width: 70px;
        text-align: center;
        user-select: none;
    }
</style>


```

4 前台验证码登陆
----------------

```
#详细代码看第三条，前台发送验证码


```

5 后台注册接口
--------------

```
# urls.py
router.register('register', views.RegisterView, 'register')  # /user/register   post请求就是新增

# views.py
class RegisterView(GenericViewSet,CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserRegisterSerilaizer
    def create(self, request, *args, **kwargs):
        response=super().create(request, *args, **kwargs)
        username=response.data.get('username')
        return APIResponse(code=1,msg='注册成功',username=username)
  
# serializer.py
class UserRegisterSerilaizer(serializers.ModelSerializer):
    code=serializers.CharField(max_length=4,min_length=4,write_only=True)
    class Meta:
        model = models.User
        fields = ['telephone', 'code','password','username']
        extra_kwargs = {
            'password': {'max_length': 18,'min_length':8},
            'username': {'read_only':True}
        }



    def validate(self, attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')
        # 取出原来的code
        cache_code = cache.get(settings.PHONE_CACHE_KEY % telephone)
        if code == cache_code:
            # 验证码通过
            if re.match('^1[3-9][0-9]{9}$', telephone):
                attrs['username']=telephone  # 把用户的名字设成手机号
                attrs.pop('code')
                return attrs
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码错误')


    # 重写create方法
    def create(self, validated_data):
        user=models.User.objects.create_user(**validated_data)
        return user


```

6 前台注册功能
--------------

```
# Register.vue
<template>
    <div class="register">
        <div class="box">
            <i class="el-icon-close" @click="close_register"></i>
            <div class="content">
                <div class="nav">
                    <span class="active">新用户注册</span>
                </div>
                <el-form>
                    <el-input
                            placeholder="手机号"
                            prefix-icon="el-icon-phone-outline"
                            v-model="mobile"
                            clearable
                            @blur="check_mobile">
                    </el-input>
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-key"
                            v-model="password"
                            clearable
                            show-password>
                    </el-input>
                    <el-input
                            placeholder="验证码"
                            prefix-icon="el-icon-chat-line-round"
                            v-model="sms"
                            clearable>
                        <template slot="append">
                            <span class="sms" @click="send_sms">{{ sms_interval }}</span>
                        </template>
                    </el-input>
                    <el-button type="primary" @click="register">注册</el-button>
                </el-form>
                <div class="foot">
                    <span @click="go_login">立即登录</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                mobile: '',
                password: '',
                sms: '',
                sms_interval: '获取验证码',
                is_send: false,
            }
        },
        methods: {
            close_register() {
                this.$emit('close', false)
            },
            go_login() {
                this.$emit('go')
            },
            check_mobile() {
                if (!this.mobile) return;
                //字符串.match(/正则表达式/)
                if (!this.mobile.match(/^1[3-9][0-9]{9}$/)) {
                    this.$message({
                        message: '手机号有误',
                        type: 'warning',
                        duration: 1000,
                        onClose: () => {
                            this.mobile = '';
                        }
                    });
                    return false;
                }
                this.$axios.get(this.$settings.base_url + '/user/check_telephone/', {params: {telephone: this.mobile}}).then(response => {
                    if (response.data.code) {
                        this.$message({
                            message: '您已经注册过了，快去登录把',
                            type: 'warning',
                            duration: 1000,
                            onClose: () => {
                                this.go_login()
                            }
                        });

                    } else {
                        this.is_send = true;
                        this.$message({
                            message: '该用户没有注册过，欢迎注册我们的平台',
                            type: 'success',
                            duration: 1000,
                        });
                    }
                }).catch(error => {
                    console.log(error)
                })

            },
            send_sms() {

                if (!this.is_send) return;
                this.is_send = false;
                let sms_interval_time = 60;
                this.sms_interval = "发送中...";

                this.$axios.get(this.$settings.base_url + '/user/send/', {params: {'telephone': this.mobile}})
                    .then(response => {
                        if (response.data.code) {
                            this.$message({
                                message: '发送验证码成功',
                                type: 'success',
                                duration: 1000,

                            });
                        }
                    })


                // setInterval(()=>{},100)
                //定时器：每隔一秒种，把数字减一，当减到小于1，按钮又能点了，显示获取验证码
                let timer = setInterval(() => {
                    if (sms_interval_time <= 1) {
                        clearInterval(timer);  //如果小于等于1，把定时器清除
                        this.sms_interval = "获取验证码";
                        this.is_send = true; // 重新回复点击发送功能的条件
                    } else {
                        sms_interval_time -= 1;
                        this.sms_interval = `${sms_interval_time}秒后再发`;
                    }
                }, 1000);
            },
            register() {
                if (this.mobile && this.sms && this.password) {
                    this.$axios.post(this.$settings.base_url + '/user/register/', {
                        telephone: this.mobile,
                        code: this.sms,
                        password: this.password
                    }).then(response => {
                        if (response.data.code) {
                            //注册成功，来个提示，跳转到登录
                            this.$message({
                                message: '注册成功',
                                type: 'success',
                                duration: 1000,
                                onClose: () => {
                                    this.go_login()
                                }
                            });
                        } else {
                            this.$message({
                                message: '未知错误',
                                type: 'error',
                                duration: 1000,
                                onClose: () => {
                                    this.mobile = ''
                                    this.sms = ''
                                    this.password = ''
                                }
                            });
                        }
                    })
                } else {
                    this.$message({
                        message: '你有没填的信息',
                        type: 'error',
                        duration: 1000,
                    });
                }
            },
        }
    }
</script>

<style scoped>
    .register {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .box {
        width: 400px;
        height: 480px;
        background-color: white;
        border-radius: 10px;
        position: relative;
        top: calc(50vh - 240px);
        left: calc(50vw - 200px);
    }

    .el-icon-close {
        position: absolute;
        font-weight: bold;
        font-size: 20px;
        top: 10px;
        right: 10px;
        cursor: pointer;
    }

    .el-icon-close:hover {
        color: darkred;
    }

    .content {
        position: absolute;
        top: 40px;
        width: 280px;
        left: 60px;
    }

    .nav {
        font-size: 20px;
        height: 38px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span {
        margin-left: 90px;
        color: darkgrey;
        user-select: none;
        cursor: pointer;
        padding-bottom: 10px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span.active {
        color: black;
        border-bottom: 3px solid black;
        padding-bottom: 9px;
    }

    .el-input, .el-button {
        margin-top: 40px;
    }

    .el-button {
        width: 100%;
        font-size: 18px;
    }

    .foot > span {
        float: right;
        margin-top: 20px;
        color: orange;
        cursor: pointer;
    }

    .sms {
        color: orange;
        cursor: pointer;
        display: inline-block;
        width: 70px;
        text-align: center;
        user-select: none;
    }
</style>


```

7 redis
-------

```
#1 key-value的存储方式，value有很多数据类型：5大：string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型
#2 内存数据库
#3 与Memcached比较：
	-1 Memcached只支持一种数据类型字符串
    -2 Memcached不支持持久化（不支持存到硬盘上，只要一断电，数据就没了）
  
# 4 使用Redis有哪些好处？
(1) 速度快，因为数据存在内存中，类似于HashMap，HashMap的优势就是查找和操作的时间复杂度都是O(1)
(2) 支持丰富数据类型，支持string，list，set，sorted set，hash
(3) 支持事务，操作都是原子性，所谓的原子性就是对数据的更改要么全部执行，要么全部不执行
(4) 丰富的特性：可用于缓存，消息，按key设置过期时间，过期后将会自动删除
# 5 单线程，单进程，不存在并发访问的问题（新版本已经不是了）
	-单线程为什么这么快
    	-数据在内存（最重要的）
        -io多路复用技术
        -因为没有进程，线程间的切换
# 6 redis适合的场景
	1 排行榜
    2 网站访问量，文章访问量
    3 缓存数据库（用的最多，就是做缓存）
    4 发布订阅
    5 去重
    6 分布式（blpop）
  
# 7 安装
	-Redis-x64-3.2.100.msi  安装包
    -redis-desktop-manager-0.9.3.817.exe 等同于navicate
  
  
# 8 使用
	-服务端和客户端
	-安装完，服务端自动启动：redis-server 配置文件.conf
	-redis-cli  ：客户端连接服务端(redis-cli -h 127.0.0.1 -p 6379)


```

Python 操作 Redis 之普通连接
----------------------------

```
# 1 pip3 install redis
# 简单使用
from redis import Redis
# conn=Redis()
#连接对象
conn=Redis(host='127.0.0.1', port=6379)
ret=conn.get('name')
print(ret)


```

2 Python 操作 Redis 之连接池
----------------------------

```
###### t_redis_pool.py
#redis连接池
import redis
#pool必须是单例的
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379,max_connections=100)  # 造一个池子,最多能放100个连接

#######t_redis_conn.py
#redis连接池
# import redis
# #pool必须是单例的
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379,max_connections=100)  # 造一个池子,最多能放100个连接
import redis
#包内的py文件，如果想右键运行，导包的时候不能带点
from t_redis_pool import POOL  # pycharm提示的错
r = redis.Redis(connection_pool=POOL)  # 只要执行这一句话，就是从池中拿出一个连接
ret=r.get('name')
print(ret)


```

3 操作之 String 操作
--------------------

```
#####字符串操作
####1 set的用法
# conn.set('height',180) #基本使用

# conn.set('height','190',nx=True)
# conn.set('height','190',xx=True)
# conn.set('height1','190',xx=True)
'''
ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行,值存在，就修改不了，执行没效果
     xx，如果设置为True，则只有name存在时，当前set操作才执行，值存在才能修改，值不存在，不会设置新值
 
'''

### 2
# setnx(name, value)
#
# 设置值，只有name不存在时，执行设置操作（添加）,如果存在，不会修改
# setex(name, value, time)
# # 设置值
# # 参数：
#     # time，过期时间（数字秒 或 timedelta对象）
# psetex(name, time_ms, value)
# # 设置值
# # 参数：
#     # time_ms，过期时间（数字毫秒 或 timedelta对象


# mset
# conn.mset({'name1':'11','name3':'dasfd'})

# ret=conn.mget(['name1','name','name3'])
# print(ret)

# ret=conn.getset('name1', '999')
# print(ret)

# ret=conn.getrange('name1',0,0) # 前闭后闭区间
# print(ret)

# conn.setrange('name1',1,88888)

# ret=conn.getbit('name1',9)
# print(ret)

#incr ：统计网站访问量，页面访问量，接口访问量
# conn.incr('name1')  # 只要一执行，数字加1
# conn.incr('name1')  # 只要一执行，数字加1
# conn.incr('name1')  # 只要一执行，数字加1
# conn.incr('name1')  # 只要一执行，数字加1

#decr
# conn.incr('name1',-2)
# conn.decr('name1',3)

# conn.append('name1','oo')
# conn.incr('name1')

##重点：
#set :很多参数
#get
#mset
#mget
#incr
#decr
#append


```

4 操作之 Hash 操作
------------------

```
# hash操作
# conn.hset('hash1','name','lqz')
# conn.hset('hash1','name2','lqz')
# conn.hset('hash1','name','lqz444')  # key不可以重复，

# ret=conn.hget('hash1','name')  #只能取一个
# print(ret)


# conn.hmset('hash2',{'key1':'value1','key2':'value2'})
# ret=conn.hmget('hash1','name','name2')
# ret=conn.hmget('hash1',['name','name2'])
# print(ret)

# ret=conn.hgetall('hash1')  # 尽量少用
# print(ret)

# ret=conn.hlen('hash1')
# ret=conn.hkeys('hash1')
# ret=conn.hexists('hash1','name1')
# ret=conn.hdel('hash1','name')

# conn.hset('hash1','name',12)
# ret=conn.hincrby('hash1','name')
#
# print(ret)


# 以后想取出hash类型内所有的数据，不建议用hgetall，建议用hscan_iter
# 一次性先取一部分回来（假设有1w条，先取回100条，把这100条做成了生成器）
# ret=conn.hscan_iter('hash1')
# print(ret)
# for i in ret:
#     print(i)

##重点掌握
# hset
# hget
#hmset
#hmget
# hincrby
# 区分hgetall和hscan_iter


```

5 操作之 List 操作
------------------

```
### 列表操作
# ret=conn.lpush('list1',1,2,3,4,5)
# ret=conn.rpush('list1',999)
# ret=conn.lpushx('list2',1)

# ret=conn.lpushx('list1',888)  # 必须有这个key才能放
# ret=conn.rpushx('list1',666)  # 我们猜，返回总长度
# ret=conn.llen('list1')

# ret=conn.linsert('list1','before','3','77777777')
# ret=conn.linsert('list1','after','3','66666666')



# ret=conn.lset('list1',3,'22222')  #从0开始计数
# ret=conn.lset('list1',0,'11111')

# ret=conn.lrem('list1',2,'5')  # 从前往后删除两个5
# ret=conn.lrem('list1',-1,'5') # 从后往前删除1个5
# ret=conn.lrem('list1',0,'5')   # 删除所有5

# ret=conn.lpop('list1')
# ret=conn.rpop('list1')

# ret=conn.lindex('list1',0)

# ret=conn.lrange('list1',0,2)  # 前闭后闭

# ret=conn.ltrim('list1',1,2)

# 重点block,阻塞,可以写一个超时时间
# ret=conn.blpop('list1',timeout=10)
# print(ret)


# 自定制分批取列表的数据
# conn.lpush('test',*[1,2,3,4,45,5,6,7,7,8,43,5,6,768,89,9,65,4,23,54,6757,8,68])
# conn.flushall()
def scan_list(name,count=2):
    index=0
    while True:
        data_list=conn.lrange(name,index,count+index-1)
        if not data_list:
            return
        index+=count
        for item in data_list:
            yield item
# print(conn.lrange('test',0,100))
for item in scan_list('test',5):
    print('---')
    print(item)

  
# 重点
lpush
lpop
blpop
lrange
llen


```

5 redsi 的其他使用
------------------

```
# 其他操作
# conn.delete('list1')
# ret=conn.delete('hash1')

# ret=conn.exists('hash2')
# ret=conn.keys('cache*')  #查询以cache开头的所有key

# ret=conn.expire('hash2',2)

# ret=conn.type('name3')
# ret=conn.type('test')
# ret=conn.type('test')
print(ret)


```

6 管道
------

```
# redis支持事务
# 管道。实现事务
# import redis
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# 
# conn = redis.Redis(connection_pool=pool)
# 
# # pipe = r.pipeline(transaction=False)
# pipe = conn.pipeline(transaction=True)
# pipe.multi()
# pipe.set('name', 'alex')
# 
# pipe.set('role', 'sb')
# 
# pipe.execute()  # 这句话，才真正的去执行


```

7 Django 中使用 redis
---------------------

```
# 方式一（通用方式）
# 方式二：django-redis
	-pip install django-redis
    -setting中配置
    	CACHES = {
                "default": {
                    "BACKEND": "django_redis.cache.RedisCache",
                    "LOCATION": "redis://127.0.0.1:6379",
                    "OPTIONS": {
                        "CLIENT_CLASS": "django_redis.client.DefaultClient",
                        "CONNECTION_POOL_KWARGS": {"max_connections": 100}
                        # "PASSWORD": "123",
                    }
                }
            }
   	-使用两种方式
    	1 使用cache
        from django.core.cache import cache
        cache.set('name',user) 
        2 直接使用conn对象
        from django_redis import get_redis_connection
        conn = get_redis_connection('default')
        print(conn.hgetall('xxx'))


```

8 接口缓存
----------

```
# 首页轮播图数据缓存到redis中
def list(self, request, *args, **kwargs):

    # response=super().list(request, *args, **kwargs)
    # 把data的数据加缓存
    # 1 先去缓存拿数据
    banner_list=cache.get('banner_list')
    if not banner_list:
        print('走数据库了')
        # 缓存中没有，去数据库拿
        response = super().list(request, *args, **kwargs)
        # 加到缓存
        cache.set('banner_list',response.data,60*60*24)
        return response

    return Response(data=banner_list)


```

9 celery 的使用
---------------

```
# 1 异步任务框架，执行异步任务，执行延迟任务，执行定时任务
# 2 Celery is a project with minimal funding, so we don’t support Microsoft Windows. Please don’t open any issues related to that platform.
# 3 使用
	-pip install celery
# 4 两种结构



```

### 9.1 基本结构

```
#1  只写一个py文件，内容如下celery_task.py：
from celery import Celery
broker='redis://127.0.0.1:6379/1'  #broker任务队列
backend='redis://127.0.0.1:6379/2'   # 结构存储，执行完的结果存在这
app=Celery(__name__,broker=broker,backend=backend)
#添加任务(使用这个装饰器装饰，@app.task)
@app.task
def add(x,y):
    print(x,y)
    return x+y
# 2启动worker
        # 用命令来执行
        # 非windows
        # 命令：celery worker -A celery_task -l info
        # windows：
        # pip3 install eventlet
        # celery worker -A celery_task -l info -P eventlet
  
# 3 添加任务
	from celery_task import add
    # add(3,4)  # 直接执行，不会被添加到broker中
    ret=add.delay(5,4)  #想broker中添加一个任务
    print(ret)
# 4 查看任务执行结果
	from celery_task import app
    from celery.result import AsyncResult
    id = '3e397fd7-e0c1-4c5c-999c-2655a96793bb'
    if __name__ == '__main__':
        async = AsyncResult(id=id, app=app)
        if async.successful():
            result = async.get()
            print(result)
        elif async.failed():
            print('任务失败')
        elif async.status == 'PENDING':
            print('任务等待中被执行')
        elif async.status == 'RETRY':
            print('任务异常后正在重试')
        elif async.status == 'STARTED':
            print('任务已经开始被执行')


```

### 9.2 包结构

```
#1 新建一个包，叫celery_task
    -celery_task
        -__init__.py
        -celery.py
        -task1.py
        -task2.py
# 2 celery.py
    from celery import Celery
    broker='redis://127.0.0.1:6379/1'  #broker任务队列
    backend='redis://127.0.0.1:6379/2'# 结构存储，执行完的结果存在这
    app=Celery(__name__,broker=broker,backend=backend,include=['celery_task.task1','celery_task.task2'])
  
# 3 task1.py
    from .celery import app
    @app.task
    def add(x,y):
        print(x,y)
        return x+y
# 4 task2.py
	from .celery import app
    @app.task
    def mutile(x,y):
        print(x,y)
        return x*y
# 5 添加任务（异步任务，延迟任务）
    from celery_task.task1 import add
    from celery_task.task2 import mutile
    #  提交异步
    ret=add.delay(6,7)
    print(ret)  # 2d4ad592-9548-4c7c-8df4-7f8583e8a1b1
  
    # 提交延迟任务
    from datetime import datetime, timedelta
    # 需要utc时间
    eta=datetime.utcnow() + timedelta(seconds=10)
    ret=add.apply_async(args=(240, 50), eta=eta)
    print(ret)

# 6获取结果同上



```

### 9.3 执行定时任务

```
#1 celery.py

    from celery import Celery
    broker='redis://127.0.0.1:6379/1'  #broker任务队列
    backend='redis://127.0.0.1:6379/2'   # 结构存储，执行完的结果存在这
    app=Celery(__name__,broker=broker,backend=backend,include=['celery_task.task1','celery_task.task2'])
    # 执行定时任务
    # 时区
    app.conf.timezone = 'Asia/Shanghai'
    # 是否使用UTC
    app.conf.enable_utc = False
    # 任务的定时配置
    from datetime import timedelta
    from celery.schedules import crontab
    app.conf.beat_schedule = {
        'add-task': {
            'task': 'celery_task.task1.add',
            # 'schedule': timedelta(seconds=3),
            'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
            'args': (300, 150),
        }
    }
  
# 2 启动worker，启动beat
	-celery worker -A celery_task -l info -P eventlet
	-celery beat -A celery_task -l info


```

首页轮播图异步更新
------------------

```
# celery.py
from celery import Celery

# 加载django环境
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyapi.settings.dev")
django.setup()

broker='redis://127.0.0.1:6379/1'  #broker任务队列
backend='redis://127.0.0.1:6379/2'   # 结构存储，执行完的结果存在这

app=Celery(__name__,broker=broker,backend=backend,include=['celery_task.home_task',])


# 执行定时任务
# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

# 任务的定时配置
from datetime import timedelta
from celery.schedules import crontab
app.conf.beat_schedule = {
    'add-task': {
        'task': 'celery_task.home_task.banner_update',
        'schedule': timedelta(seconds=30),
    }
}


# home_task.py
from .celery import app
@app.task
def banner_update():
    from home import serializer
    from home import models
    from django.conf import settings
    from django.core.cache import cache
    queryset_banner = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[
               :settings.BANNER_COUNTER]
    serializer_banner=serializer.BannerModelSerilaizer(instance=queryset_banner,many=True)
    # print(serializer_banner.data)
    for banner in serializer_banner.data:
        banner['img']='http://127.0.0.1:8000'+banner['img']
    cache.set('banner_list',serializer_banner.data)
    # import time
    # time.sleep(1)
    # banner_list=cache.get('banner_list')
    # print(banner_list)
    return True


```

2 课程表结构分析和优化
----------------------

```
#  ForeignKey的字段：
	-related_name 反向操作时，使用的字段名，用于代替原反向查询时的'表名_set'。
    -related_query_name ：反向查询操作时，使用的连接前缀，用于替换表名。
  
################1   course/models.py
from luffyapi.utils.models import BaseModel
# 实际路飞课程相关表，以免费课为例
class CourseCategory(BaseModel):
    """分类
    python,linux,go, 网络安全
    跟课程是一对多的关系

    """
    name = models.CharField(max_length=64, unique=True, verbose_)
    class Meta:
        db_table = "luffy_course_category"
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Course(BaseModel):
    """课程"""
    course_type = (
        (0, '付费'),
        (1, 'VIP专享'),
        (2, '学位课程')
    )
    level_choices = (
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    )
    status_choices = (
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    )
    # 原始字段
    name = models.CharField(max_length=128, verbose_)
    course_img = models.ImageField(upload_to="courses", max_length=255, verbose_, blank=True, null=True)
    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_)
    # 使用这个字段的原因
    brief = models.TextField(max_length=2048, verbose_, null=True, blank=True)
    level = models.SmallIntegerField(choices=level_choices, default=0, verbose_)
    pub_date = models.DateField(verbose_, auto_now_add=True)
    period = models.IntegerField(verbose_, default=7)
    attachment_path = models.FileField(upload_to="attachment", max_length=128, verbose_, blank=True, null=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_, default=0)

    # 优化字段
    students = models.IntegerField(verbose_, default=0)
    sections = models.IntegerField(verbose_, default=0)
    pub_sections = models.IntegerField(verbose_, default=0)

    # 关联字段
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_,db_constraint=False)
    course_category = models.ForeignKey("CourseCategory", on_delete=models.SET_NULL, db_constraint=False, null=True, blank=True,verbose_)
    class Meta:
        db_table = "luffy_course"
        verbose_name = "课程"
        verbose_name_plural = "课程"

    def __str__(self):
        return "%s" % self.name



class Teacher(BaseModel):
    """导师
    跟课程一对多，关联字段写在课程表中
    """
    role_choices = (
        (0, '讲师'),
        (1, '导师'),
        (2, '班主任'),
    )
    name = models.CharField(max_length=32, verbose_)
    role = models.SmallIntegerField(choices=role_choices, default=0, verbose_)
    title = models.CharField(max_length=64, verbose_name="职位、职称")
    signature = models.CharField(max_length=255, verbose_, blank=True, null=True)
    image = models.ImageField(upload_to="teacher", null=True, verbose_)
    brief = models.TextField(max_length=1024, verbose_)

    class Meta:
        db_table = "luffy_teacher"
        verbose_name = "导师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name



class CourseChapter(BaseModel):
    """章节
    章节跟课程是一（课程）对多（章节多）
    """
    course = models.ForeignKey("Course", related_,db_constraint=False)
    chapter = models.SmallIntegerField(verbose_, default=1)
    name = models.CharField(max_length=128, verbose_)
    summary = models.TextField(verbose_, blank=True, null=True)
    pub_date = models.DateField(verbose_, auto_now_add=True)

    class Meta:
        db_table = "luffy_course_chapter"
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s:(第%s章)%s" % (self.course, self.chapter, self.name)



class CourseSection(BaseModel):
    """课时
        章节和课时是一对多的关系，关联字段写在多的一方，课时
    """
    section_type_choices = (
        (0, '文档'),
        (1, '练习'),
        (2, '视频')
    )
    chapter = models.ForeignKey("CourseChapter", related_name='coursesections', on_delete=models.CASCADE,
                                verbose_,db_constraint=False)
    name = models.CharField(max_length=128, verbose_)
    orders = models.PositiveSmallIntegerField(verbose_)
    section_type = models.SmallIntegerField(default=2, choices=section_type_choices, verbose_)
    section_link = models.CharField(max_length=255, blank=True, null=True, verbose_,
                                    help_text="若是video，填vid,若是文档，填link")
    duration = models.CharField(verbose_, blank=True, null=True, max_length=32)  # 仅在前端展示使用
    pub_date = models.DateTimeField(verbose_, auto_now_add=True)
    free_trail = models.BooleanField(verbose_, default=False)

    class Meta:
        db_table = "luffy_course_Section"
        verbose_name = "课时"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.chapter, self.name)
  
  
################2 utils/models/BaseModel
from django.db import models
# 后期课程表，轮播图表，都会用到这些字段

class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=True, verbose_name='是否展示')
    # 修改成这样
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time  = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    orders = models.IntegerField()
    class Meta:
        abstract=True  # 一定不要忘了






################3 数据迁移
python manage.py makemigrations
python manage.py migrate



```

3 课程主页页面
--------------

```
# 不要忘了注册路由

# FreeCourse.vue
<template>
    <div class="course">
        <Header></Header>
        <div class="main">
            <!-- 筛选条件 -->
            <div class="condition">
                <ul class="cate-list">
                    <li class="title">课程分类:</li>
                    <li class="this">全部</li>
                    <li>Python</li>
                    <li>Linux运维</li>
                    <li>Python进阶</li>
                    <li>开发工具</li>
                    <li>Go语言</li>
                    <li>机器学习</li>
                    <li>技术生涯</li>
                </ul>

                <div class="ordering">
                    <ul>
                        <li class="title">筛        选:</li>
                        <li class="default this">默认</li>
                        <li class="hot">人气</li>
                        <li class="price">价格</li>
                    </ul>
                    <p class="condition-result">共21个课程</p>
                </div>

            </div>
            <!-- 课程列表 -->
            <div class="course-list">
                <div class="course-item">
                    <div class="course-image">
                        <img src="@/assets/img/course-cover.jpeg" alt="">
                    </div>
                    <div class="course-info">
                        <h3>Python开发21天入门 <span><img src="@/assets/img/avatar1.svg" alt="">100人已加入学习</span></h3>
                        <p class="teather-info">Alex 金角大王 老男孩Python教学总监 <span>共154课时/更新完成</span></p>
                        <ul class="lesson-list">
                            <li><span class="lesson-title">01 | 第1节：初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span></li>
                        </ul>
                        <div class="pay-box">
                            <span class="discount-type">限时免费</span>
                            <span class="discount-price">￥0.00元</span>
                            <span class="original-price">原价：9.00元</span>
                            <span class="buy-now">立即购买</span>
                        </div>
                    </div>
                </div>
                <div class="course-item">
                    <div class="course-image">
                        <img src="@/assets/img/course-cover.jpeg" alt="">
                    </div>
                    <div class="course-info">
                        <h3>Python开发21天入门 <span><img src="@/assets/img/avatar1.svg" alt="">100人已加入学习</span></h3>
                        <p class="teather-info">Alex 金角大王 老男孩Python教学总监 <span>共154课时/更新完成</span></p>
                        <ul class="lesson-list">
                            <li><span class="lesson-title">01 | 第1节：初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span></li>
                        </ul>
                        <div class="pay-box">
                            <span class="discount-type">限时免费</span>
                            <span class="discount-price">￥0.00元</span>
                            <span class="original-price">原价：9.00元</span>
                            <span class="buy-now">立即购买</span>
                        </div>
                    </div>
                </div>
                <div class="course-item">
                    <div class="course-image">
                        <img src="@/assets/img/course-cover.jpeg" alt="">
                    </div>
                    <div class="course-info">
                        <h3>Python开发21天入门 <span><img src="@/assets/img/avatar1.svg" alt="">100人已加入学习</span></h3>
                        <p class="teather-info">Alex 金角大王 老男孩Python教学总监 <span>共154课时/更新完成</span></p>
                        <ul class="lesson-list">
                            <li><span class="lesson-title">01 | 第1节：初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span></li>
                        </ul>
                        <div class="pay-box">
                            <span class="discount-type">限时免费</span>
                            <span class="discount-price">￥0.00元</span>
                            <span class="original-price">原价：9.00元</span>
                            <span class="buy-now">立即购买</span>
                        </div>
                    </div>
                </div>
                <div class="course-item">
                    <div class="course-image">
                        <img src="@/assets/img/course-cover.jpeg" alt="">
                    </div>
                    <div class="course-info">
                        <h3>Python开发21天入门 <span><img src="@/assets/img/avatar1.svg" alt="">100人已加入学习</span></h3>
                        <p class="teather-info">Alex 金角大王 老男孩Python教学总监 <span>共154课时/更新完成</span></p>
                        <ul class="lesson-list">
                            <li><span class="lesson-title">01 | 第1节：初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span> <span class="free">免费</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码</span></li>
                            <li><span class="lesson-title">01 | 第1节：初识编码初识编码</span></li>
                        </ul>
                        <div class="pay-box">
                            <span class="discount-type">限时免费</span>
                            <span class="discount-price">￥0.00元</span>
                            <span class="original-price">原价：9.00元</span>
                            <span class="buy-now">立即购买</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
    import Header from "@/components/Head"
    import Footer from "@/components/Footer"

    export default {
        name: "Course",
        data() {
            return {
                category: 0,
            }
        },
        components: {
            Header,
            Footer,
        }
    }
</script>

<style scoped>
    .course {
        background: #f6f6f6;
    }

    .course .main {
        width: 1100px;
        margin: 35px auto 0;
    }

    .course .condition {
        margin-bottom: 35px;
        padding: 25px 30px 25px 20px;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 2px 4px 0 #f0f0f0;
    }

    .course .cate-list {
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
        padding-bottom: 18px;
        margin-bottom: 17px;
    }

    .course .cate-list::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .cate-list li {
        float: left;
        font-size: 16px;
        padding: 6px 15px;
        line-height: 16px;
        margin-left: 14px;
        position: relative;
        transition: all .3s ease;
        cursor: pointer;
        color: #4a4a4a;
        border: 1px solid transparent; /* transparent 透明 */
    }

    .course .cate-list .title {
        color: #888;
        margin-left: 0;
        letter-spacing: .36px;
        padding: 0;
        line-height: 28px;
    }

    .course .cate-list .this {
        color: #ffc210;
        border: 1px solid #ffc210 !important;
        border-radius: 30px;
    }

    .course .ordering::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .ordering ul {
        float: left;
    }

    .course .ordering ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .ordering .condition-result {
        float: right;
        font-size: 14px;
        color: #9b9b9b;
        line-height: 28px;
    }

    .course .ordering ul li {
        float: left;
        padding: 6px 15px;
        line-height: 16px;
        margin-left: 14px;
        position: relative;
        transition: all .3s ease;
        cursor: pointer;
        color: #4a4a4a;
    }

    .course .ordering .title {
        font-size: 16px;
        color: #888;
        letter-spacing: .36px;
        margin-left: 0;
        padding: 0;
        line-height: 28px;
    }

    .course .ordering .this {
        color: #ffc210;
    }

    .course .ordering .price {
        position: relative;
    }

    .course .ordering .price::before,
    .course .ordering .price::after {
        cursor: pointer;
        content: "";
        display: block;
        width: 0px;
        height: 0px;
        border: 5px solid transparent;
        position: absolute;
        right: 0;
    }

    .course .ordering .price::before {
        border-bottom: 5px solid #aaa;
        margin-bottom: 2px;
        top: 2px;
    }

    .course .ordering .price::after {
        border-top: 5px solid #aaa;
        bottom: 2px;
    }

    .course .course-item:hover {
        box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
    }

    .course .course-item {
        width: 1100px;
        background: #fff;
        padding: 20px 30px 20px 20px;
        margin-bottom: 35px;
        border-radius: 2px;
        cursor: pointer;
        box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
        /* css3.0 过渡动画 hover 事件操作 */
        transition: all .2s ease;
    }

    .course .course-item::after {
        content: "";
        display: block;
        clear: both;
    }

    /* 顶级元素 父级元素  当前元素{} */
    .course .course-item .course-image {
        float: left;
        width: 423px;
        height: 210px;
        margin-right: 30px;
    }

    .course .course-item .course-image img {
        width: 100%;
    }

    .course .course-item .course-info {
        float: left;
        width: 596px;
    }

    .course-item .course-info h3 {
        font-size: 26px;
        color: #333;
        font-weight: normal;
        margin-bottom: 8px;
    }

    .course-item .course-info h3 span {
        font-size: 14px;
        color: #9b9b9b;
        float: right;
        margin-top: 14px;
    }

    .course-item .course-info h3 span img {
        width: 11px;
        height: auto;
        margin-right: 7px;
    }

    .course-item .course-info .teather-info {
        font-size: 14px;
        color: #9b9b9b;
        margin-bottom: 14px;
        padding-bottom: 14px;
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
    }

    .course-item .course-info .teather-info span {
        float: right;
    }

    .course-item .lesson-list::after {
        content: "";
        display: block;
        clear: both;
    }

    .course-item .lesson-list li {
        float: left;
        width: 44%;
        font-size: 14px;
        color: #666;
        padding-left: 22px;
        /* background: url("路径") 是否平铺 x轴位置 y轴位置 */
        background: url("/src/assets/img/play-icon-gray.svg") no-repeat left 4px;
        margin-bottom: 15px;
    }

    .course-item .lesson-list li .lesson-title {
        /* 以下3句，文本内容过多，会自动隐藏，并显示省略符号 */
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        display: inline-block;
        max-width: 200px;
    }

    .course-item .lesson-list li:hover {
        background-image: url("/src/assets/img/play-icon-yellow.svg");
        color: #ffc210;
    }

    .course-item .lesson-list li .free {
        width: 34px;
        height: 20px;
        color: #fd7b4d;
        vertical-align: super;
        margin-left: 10px;
        border: 1px solid #fd7b4d;
        border-radius: 2px;
        text-align: center;
        font-size: 13px;
        white-space: nowrap;
    }

    .course-item .lesson-list li:hover .free {
        color: #ffc210;
        border-color: #ffc210;
    }

    .course-item .pay-box::after {
        content: "";
        display: block;
        clear: both;
    }

    .course-item .pay-box .discount-type {
        padding: 6px 10px;
        font-size: 16px;
        color: #fff;
        text-align: center;
        margin-right: 8px;
        background: #fa6240;
        border: 1px solid #fa6240;
        border-radius: 10px 0 10px 0;
        float: left;
    }

    .course-item .pay-box .discount-price {
        font-size: 24px;
        color: #fa6240;
        float: left;
    }

    .course-item .pay-box .original-price {
        text-decoration: line-through;
        font-size: 14px;
        color: #9b9b9b;
        margin-left: 10px;
        float: left;
        margin-top: 10px;
    }

    .course-item .pay-box .buy-now {
        width: 120px;
        height: 38px;
        background: transparent;
        color: #fa6240;
        font-size: 16px;
        border: 1px solid #fd7b4d;
        border-radius: 3px;
        transition: all .2s ease-in-out;
        float: right;
        text-align: center;
        line-height: 38px;
    }

    .course-item .pay-box .buy-now:hover {
        color: #fff;
        background: #ffc210;
        border: 1px solid #ffc210;
    }
</style>


```

4 课程数据准备
--------------

```
-- 老师表
-- INSERT INTO luffy_teacher(id, orders, is_show, is_delete, created_time, updated_time, name, role, title, signature, image, brief) VALUES (1, 1, 1, 0, '2019-07-14 13:44:19.661327', '2019-07-14 13:46:54.246271', 'Alex', 1, '老男孩Python教学总监', '金角大王', 'teacher/alex_icon.png', '老男孩教育CTO & CO-FOUNDER 国内知名PYTHON语言推广者 51CTO学院2016\2017年度最受学员喜爱10大讲师之一 多款开源软件作者 曾任职公安部、飞信、中金公司、NOKIA中国研究院、华尔街英语、ADVENT、汽车之家等公司');
-- 
-- INSERT INTO luffy_teacher(id, orders, is_show, is_delete, created_time, updated_time, name, role, title, signature, image, brief) VALUES (2, 2, 1, 0, '2019-07-14 13:45:25.092902', '2019-07-14 13:45:25.092936', 'Mjj', 0, '前美团前端项目组架构师', NULL, 'teacher/mjj_icon.png', '是马JJ老师, 一个集美貌与才华于一身的男人，搞过几年IOS，又转了前端开发几年，曾就职于美团网任高级前端开发，后来因为不同意王兴(美团老板)的战略布局而出家做老师去了，有丰富的教学经验，开起车来也毫不含糊。一直专注在前端的前沿技术领域。同时，爱好抽烟、喝酒、烫头(锡纸烫)。 我的最爱是前端，因为前端妹子多。');
-- 
-- INSERT INTO luffy_teacher(id, orders, is_show, is_delete, created_time, updated_time, name, role, title, signature, image, brief) VALUES (3, 3, 1, 0, '2019-07-14 13:46:21.997846', '2019-07-14 13:46:21.997880', 'Lyy', 0, '老男孩Linux学科带头人', NULL, 'teacher/lyy_icon.png', 'Linux运维技术专家，老男孩Linux金牌讲师，讲课风趣幽默、深入浅出、声音洪亮到爆炸');

-- 课程分类表
-- INSERT INTO luffy_course_category(id, orders, is_show, is_delete, created_time, updated_time, name) VALUES (1, 1, 1, 0, '2019-07-14 13:40:58.690413', '2019-07-14 13:40:58.690477', 'Python');
-- 
-- INSERT INTO luffy_course_category(id, orders, is_show, is_delete, created_time, updated_time, name) VALUES (2, 2, 1, 0, '2019-07-14 13:41:08.249735', '2019-07-14 13:41:08.249817', 'Linux');


-- 课程表数据
-- INSERT INTO luffy_course(id, orders, is_show, is_delete, created_time, updated_time, name, course_img, course_type, brief, level, pub_date, period, attachment_path, status, students, sections, pub_sections, price, course_category_id, teacher_id) VALUES (1, 1, 1, 0, '2019-07-14 13:54:33.095201', '2019-07-14 13:54:33.095238', 'Python开发21天入门', 'courses/alex_python.png', 0, 'Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土', 0, '2019-07-14', 21, '', 0, 231, 120, 120, 0.00, 1, 1);
-- 
-- INSERT INTO luffy_course(id, orders, is_show, is_delete, created_time, updated_time, name, course_img, course_type, brief, level, pub_date, period, attachment_path, status, students, sections, pub_sections, price, course_category_id, teacher_id) VALUES (2, 2, 1, 0, '2019-07-14 13:56:05.051103', '2019-07-14 13:56:05.051142', 'Python项目实战', 'courses/mjj_python.png', 0, '', 1, '2019-07-14', 30, '', 0, 340, 120, 120, 99.00, 1, 2);
-- 
-- INSERT INTO luffy_course(id, orders, is_show, is_delete, created_time, updated_time, name, course_img, course_type, brief, level, pub_date, period, attachment_path, status, students, sections, pub_sections, price, course_category_id, teacher_id) VALUES (3, 3, 1, 0, '2019-07-14 13:57:21.190053', '2019-07-14 13:57:21.190095', 'Linux系统基础5周入门精讲', 'courses/lyy_linux.png', 0, '', 0, '2019-07-14', 25, '', 0, 219, 100, 100, 39.00, 2, 3);
-- 
-- 


-- 章节表数据
-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, pub_date, course_id) VALUES (1, 1, 1, 0, '2019-07-14 13:58:34.867005', '2019-07-14 14:00:58.276541', 1, '计算机原理', '', '2019-07-14', 1);
-- 
-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, pub_date, course_id) VALUES (2, 2, 1, 0, '2019-07-14 13:58:48.051543', '2019-07-14 14:01:22.024206', 2, '环境搭建', '', '2019-07-14', 1);
-- 
-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, pub_date, course_id) VALUES (3, 3, 1, 0, '2019-07-14 13:59:09.878183', '2019-07-14 14:01:40.048608', 1, '项目创建', '', '2019-07-14', 2);
-- 
-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, pub_date, course_id) VALUES (4, 4, 1, 0, '2019-07-14 13:59:37.448626', '2019-07-14 14:01:58.709652', 1, 'Linux环境创建', '', '2019-07-14', 3);


-- 课时表数据
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, pub_date, free_trail, chapter_id) VALUES (1, 1, 0, '2019-07-14 14:02:33.779098', '2019-07-14 14:02:33.779135', '计算机原理上', 1, 2, NULL, NULL, '2019-07-14 14:02:33.779193', 1, 1);
-- 
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, pub_date, free_trail, chapter_id) VALUES (2, 1, 0, '2019-07-14 14:02:56.657134', '2019-07-14 14:02:56.657173', '计算机原理下', 2, 2, NULL, NULL, '2019-07-14 14:02:56.657227', 1, 1);
-- 
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, pub_date, free_trail, chapter_id) VALUES (3, 1, 0, '2019-07-14 14:03:20.493324', '2019-07-14 14:03:52.329394', '环境搭建上', 1, 2, NULL, NULL, '2019-07-14 14:03:20.493420', 0, 2);
-- 
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, pub_date, free_trail, chapter_id) VALUES (4, 1, 0, '2019-07-14 14:03:36.472742', '2019-07-14 14:03:36.472779', '环境搭建下', 2, 2, NULL, NULL, '2019-07-14 14:03:36.472831', 0, 2);
-- 
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, pub_date, free_trail, chapter_id) VALUES (5, 1, 0, '2019-07-14 14:04:19.338153', '2019-07-14 14:04:19.338192', 'web项目的创建', 1, 2, NULL, NULL, '2019-07-14 14:04:19.338252', 1, 3);
-- 
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, pub_date, free_trail, chapter_id) VALUES (6, 1, 0, '2019-07-14 14:04:52.895855', '2019-07-14 14:04:52.895890', 'Linux的环境搭建', 1, 2, NULL, NULL, '2019-07-14 14:04:52.895942', 1, 4);


```

5 课程分类群查接口
------------------

```
# 路由
router = SimpleRouter()
router.register('categories', views.CourseCategoryView, 'categories')
router.register('free', views.CouresView, 'free')
urlpatterns = [
    path('', include(router.urls)),
]

# 视图views.py
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from . import models
from . import serializer
class CourseCategoryView(GenericViewSet,ListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False,is_show=True).order_by('orders')
    serializer_class = serializer.CourseCategorySerializer

# 序列化类
from rest_framework import serializers
from . import models
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseCategory
        fields=['id','name']


```

6 课程群查接口
--------------

```
# 路由
router = SimpleRouter()
router.register('categories', views.CourseCategoryView, 'categories')
router.register('free', views.CouresView, 'free')
urlpatterns = [
    path('', include(router.urls)),
]

# 视图 views.py
from .paginations import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from .filters import MyFilter
class CouresView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = models.Course.objects.filter(is_delete=False,is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    pagination_class = PageNumberPagination
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    ordering_fields=['id', 'price', 'students']

    filter_fields=['course_category','students']
  
 ###serializer
from rest_framework import serializers
from . import models


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('name', 'role_name', 'title', 'signature', 'image', 'brief')


class CourseModelSerializer(serializers.ModelSerializer):
    # 子序列化的方式
    teacher = TeacherSerializer()

    class Meta:
        model = models.Course
        fields=[
            'id',
            'name',
            'course_img',
            'brief',
            'attachment_path',
            'pub_sections',
            'price',
            'students',
            'period',
            'sections',
            'course_type_name',
            'level_name',
            'status_name',
            'teacher',
            'section_list',
        ]
 # models.py
class Course(BaseModel):
	...
    @property
    def course_type_name(self):
        return self.get_course_type_display()
    @property
    def level_name(self):
        return self.get_level_display()
    @property
    def status_name(self):
        return self.get_status_display()

    @property
    def section_list(self):
        ll=[]
        # 根据课程取出所有章节（正向查询，字段名.all()）
        course_chapter_list=self.coursechapters.all()
        for course_chapter in course_chapter_list:
            # 通过章节对象，取到章节下所有的课时（反向查询）
            # course_chapter.表名小写_set.all() 现在变成了course_chapter.coursesections.all()
            course_sections_list=course_chapter.coursesections.all()
            for course_section in course_sections_list:
                ll.append({
                    'name': course_section.name,
                    'section_link': course_section.section_link,
                    'duration': course_section.duration,
                    'free_trail': course_section.free_trail,
                })
                if len(ll)>=4:
                    return ll

        return ll


  
class Teacher(BaseModel):
	...
    def role_name(self):
        # 返回角色的中文
        return self.get_role_display()


```

7 搜索组件和过滤
----------------

```
'''
排序：
按id正序倒叙排序，按price正序倒叙排列
使用：http://127.0.0.1:8000/course/free/?ordering=-id
配置类：
    filter_backends=[OrderingFilter]
配置字段：
    ordering_fields=['id','price']
  
  
内置过滤：
使用：http://127.0.0.1:8000/course/free/?search=39
按照price过滤（表自有的字段直接过滤）
配置类：
    filter_backends=[SearchFilter]
配置字段：
    search_fields=['price']
  
扩展：django-filter
安装：
支持自由字段的过滤还支持外键字段的过滤
http://127.0.0.1:8000/course/free/?course_category=1   # 过滤分类为1 （python的所有课程）
配置类:
    filter_backends=[DjangoFilterBackend]
配置字段：
    filter_fields=['course_category']


'''


```

9 自定义过滤类
--------------

```
# filters.py
# 自定义过滤规则
from rest_framework.filters import BaseFilterBackend

class MyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # 真正的过滤规则
        # params=request.GET.get('teacher')
        # queryset.filter('''''')
        return queryset[:1]
 
# 使用：在视图类中配置
filter_backends=[DjangoFilterBackend,OrderingFilter,MyFilter]


```

区间过滤

```
# 借助django-filter实现区间过滤
# 实现区间过滤
##########1 filters.py
class CourseFilterSet(FilterSet):
    # 课程的价格范围要大于min_price，小于max_price
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gt')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model=models.Course
        fields=['course_category']
#####2 视图类中配置
     -filter_backends=[DjangoFilterBackend]
	 # 配置类：（自己写的类）
     -filter_class = CourseFilterSet



```

2 课程主页前端
--------------

```
<template>
    <div class="course">
        <Header></Header>
        <div class="main">
            <!-- 筛选条件 -->
            <div class="condition">
                <ul class="cate-list">
                    <li class="title">课程分类:</li>
                    <li :class="filter.course_category==0?'this':''" @click="filter.course_category=0">全部</li>
                    <li :class="filter.course_category==category.id?'this':''" v-for="category in category_list"
                        @click="filter.course_category=category.id" :key="category.name">{{category.name}}
                    </li>
                </ul>

                <div class="ordering">
                    <ul>
                        <li class="title">筛        选:</li>
                        <li class="default" :class="(filter.ordering=='id' || filter.ordering=='-id')?'this':''"
                            @click="filter.ordering='-id'">默认
                        </li>
                        <li class="hot" :class="(filter.ordering=='students' || filter.ordering=='-students')?'this':''"
                            @click="filter.ordering=(filter.ordering=='-students'?'students':'-students')">人气
                        </li>
                        <li class="price"
                            :class="filter.ordering=='price'?'price_up this':(filter.ordering=='-price'?'price_down this':'')"
                            @click="filter.ordering=(filter.ordering=='-price'?'price':'-price')">价格
                        </li>
                    </ul>
                    <p class="condition-result">共{{course_total}}个课程</p>
                </div>

            </div>
            <!-- 课程列表 -->
            <div class="course-list">
                <div class="course-item" v-for="course in course_list" :key="course.name">
                    <div class="course-image">
                        <img :src="course.course_img" alt="">
                    </div>
                    <div class="course-info">
                        <h3>
                            <router-link :to="'/free/detail/'+course.id">{{course.name}}</router-link>
                            <span><img src="@/assets/img/avatar1.svg" alt="">{{course.students}}人已加入学习</span></h3>
                        <p class="teather-info">
                            {{course.teacher.name}} {{course.teacher.title}} {{course.teacher.signature}}
                            <span v-if="course.sections>course.pub_sections">共{{course.sections}}课时/已更新{{course.pub_sections}}课时</span>
                            <span v-else>共{{course.sections}}课时/更新完成</span>
                        </p>
                        <ul class="section-list">
                            <li v-for="(section, key) in course.section_list" :key="section.name"><span
                                    class="section-title">0{{key+1}}  |  {{section.name}}</span>
                                <span class="free" v-if="section.free_trail">免费</span></li>
                        </ul>
                        <div class="pay-box">
                            <div v-if="course.discount_type">
                                <span class="discount-type">{{course.discount_type}}</span>
                                <span class="discount-price">￥{{course.real_price}}元</span>
                                <span class="original-price">原价：{{course.price}}元</span>
                            </div>
                            <span v-else class="discount-price">￥{{course.price}}元</span>
                            <span class="buy-now">立即购买</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="course_pagination block">
                <el-pagination
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                        :current-page.sync="filter.page"
                        :page-sizes="[2, 3, 5, 10]"
                        :page-size="filter.page_size"
                        layout="sizes, prev, pager, next"
                        :total="course_total">
                </el-pagination>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
    import Header from "@/components/Head"
    import Footer from "@/components/Footer"

    export default {
        name: "Course",
        data() {
            return {
                category_list: [], // 课程分类列表
                course_list: [],   // 课程列表
                course_total: 0,   // 当前课程的总数量
                filter: {
                    course_category: 0, // 当前用户选择的课程分类，刚进入页面默认为全部，值为0
                    ordering: "-id",    // 数据的排序方式，默认值是-id，表示对于id进行降序排列
                    page_size: 2,       // 单页数据量
                    page: 1,
                }
            }
        },
        created() {
            this.get_category();
            this.get_course();
        },
        components: {
            Header,
            Footer,
        },
        watch: {
            //当你监听的数据发生变化，就会执行函数
            "filter.course_category": function () {
                this.filter.page = 1;
                this.get_course();
            },
            "filter.ordering": function () {
                this.get_course();
            },
            "filter.page_size": function () {
                this.get_course();
            },
            "filter.page": function () {
                this.get_course();
            }
        },
        methods: {

            handleSizeChange(val) {
                // 每页数据量发生变化时执行的方法
                this.filter.page = 1;
                this.filter.page_size = val;
            },
            handleCurrentChange(val) {
                // 页码发生变化时执行的方法
                this.filter.page = val;
            },
            get_category() {
                // 获取课程分类信息
                this.$axios.get(`${this.$settings.base_url}/course/categories/`).then(response => {
                    this.category_list = response.data;
                }).catch(() => {
                    this.$message({
                        message: "获取课程分类信息有误，请联系客服工作人员",
                    })
                })
            },
            get_course() {
                // 排序
                let filters = {
                    ordering: this.filter.ordering, // 排序
                };
                // 判决是否进行分类课程的展示
                if (this.filter.course_category > 0) {
                    filters.course_category = this.filter.course_category;
                }

                // 设置单页数据量
                if (this.filter.page_size > 0) {
                    filters.page_size = this.filter.page_size;
                } else {
                    filters.page_size = 5;
                }

                // 设置当前页码
                if (this.filter.page > 1) {
                    filters.page = this.filter.page;
                } else {
                    filters.page = 1;
                }


                // 获取课程列表信息
                this.$axios.get(`${this.$settings.base_url}/course/free/`, {
                    params: filters
                }).then(response => {
                    // console.log(response.data);
                    this.course_list = response.data.results;
                    this.course_total = response.data.count;
                    // console.log(this.course_list);
                }).catch(() => {
                    this.$message({
                        message: "获取课程信息有误，请联系客服工作人员"
                    })
                })
            }
        }
    }
</script>

<style scoped>
    .course {
        background: #f6f6f6;
    }

    .course .main {
        width: 1100px;
        margin: 35px auto 0;
    }

    .course .condition {
        margin-bottom: 35px;
        padding: 25px 30px 25px 20px;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 2px 4px 0 #f0f0f0;
    }

    .course .cate-list {
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
        padding-bottom: 18px;
        margin-bottom: 17px;
    }

    .course .cate-list::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .cate-list li {
        float: left;
        font-size: 16px;
        padding: 6px 15px;
        line-height: 16px;
        margin-left: 14px;
        position: relative;
        transition: all .3s ease;
        cursor: pointer;
        color: #4a4a4a;
        border: 1px solid transparent; /* transparent 透明 */
    }

    .course .cate-list .title {
        color: #888;
        margin-left: 0;
        letter-spacing: .36px;
        padding: 0;
        line-height: 28px;
    }

    .course .cate-list .this {
        color: #ffc210;
        border: 1px solid #ffc210 !important;
        border-radius: 30px;
    }

    .course .ordering::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .ordering ul {
        float: left;
    }

    .course .ordering ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .ordering .condition-result {
        float: right;
        font-size: 14px;
        color: #9b9b9b;
        line-height: 28px;
    }

    .course .ordering ul li {
        float: left;
        padding: 6px 15px;
        line-height: 16px;
        margin-left: 14px;
        position: relative;
        transition: all .3s ease;
        cursor: pointer;
        color: #4a4a4a;
    }

    .course .ordering .title {
        font-size: 16px;
        color: #888;
        letter-spacing: .36px;
        margin-left: 0;
        padding: 0;
        line-height: 28px;
    }

    .course .ordering .this {
        color: #ffc210;
    }

    .course .ordering .price {
        position: relative;
    }

    .course .ordering .price::before,
    .course .ordering .price::after {
        cursor: pointer;
        content: "";
        display: block;
        width: 0px;
        height: 0px;
        border: 5px solid transparent;
        position: absolute;
        right: 0;
    }

    .course .ordering .price::before {
        border-bottom: 5px solid #aaa;
        margin-bottom: 2px;
        top: 2px;
    }

    .course .ordering .price::after {
        border-top: 5px solid #aaa;
        bottom: 2px;
    }

    .course .ordering .price_up::before {
        border-bottom-color: #ffc210;
    }

    .course .ordering .price_down::after {
        border-top-color: #ffc210;
    }

    .course .course-item:hover {
        box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
    }

    .course .course-item {
        width: 1100px;
        background: #fff;
        padding: 20px 30px 20px 20px;
        margin-bottom: 35px;
        border-radius: 2px;
        cursor: pointer;
        box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
        /* css3.0 过渡动画 hover 事件操作 */
        transition: all .2s ease;
    }

    .course .course-item::after {
        content: "";
        display: block;
        clear: both;
    }

    /* 顶级元素 父级元素  当前元素{} */
    .course .course-item .course-image {
        float: left;
        width: 423px;
        height: 210px;
        margin-right: 30px;
    }

    .course .course-item .course-image img {
        max-width: 100%;
        max-height: 210px;
    }

    .course .course-item .course-info {
        float: left;
        width: 596px;
    }

    .course-item .course-info h3 a {
        font-size: 26px;
        color: #333;
        font-weight: normal;
        margin-bottom: 8px;
    }

    .course-item .course-info h3 span {
        font-size: 14px;
        color: #9b9b9b;
        float: right;
        margin-top: 14px;
    }

    .course-item .course-info h3 span img {
        width: 11px;
        height: auto;
        margin-right: 7px;
    }

    .course-item .course-info .teather-info {
        font-size: 14px;
        color: #9b9b9b;
        margin-bottom: 14px;
        padding-bottom: 14px;
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
    }

    .course-item .course-info .teather-info span {
        float: right;
    }

    .course-item .section-list::after {
        content: "";
        display: block;
        clear: both;
    }

    .course-item .section-list li {
        float: left;
        width: 44%;
        font-size: 14px;
        color: #666;
        padding-left: 22px;
        /* background: url("路径") 是否平铺 x轴位置 y轴位置 */
        background: url("/src/assets/img/play-icon-gray.svg") no-repeat left 4px;
        margin-bottom: 15px;
    }

    .course-item .section-list li .section-title {
        /* 以下3句，文本内容过多，会自动隐藏，并显示省略符号 */
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        display: inline-block;
        max-width: 200px;
    }

    .course-item .section-list li:hover {
        background-image: url("/src/assets/img/play-icon-yellow.svg");
        color: #ffc210;
    }

    .course-item .section-list li .free {
        width: 34px;
        height: 20px;
        color: #fd7b4d;
        vertical-align: super;
        margin-left: 10px;
        border: 1px solid #fd7b4d;
        border-radius: 2px;
        text-align: center;
        font-size: 13px;
        white-space: nowrap;
    }

    .course-item .section-list li:hover .free {
        color: #ffc210;
        border-color: #ffc210;
    }

    .course-item {
        position: relative;
    }

    .course-item .pay-box {
        position: absolute;
        bottom: 20px;
        width: 600px;
    }

    .course-item .pay-box::after {
        content: "";
        display: block;
        clear: both;
    }

    .course-item .pay-box .discount-type {
        padding: 6px 10px;
        font-size: 16px;
        color: #fff;
        text-align: center;
        margin-right: 8px;
        background: #fa6240;
        border: 1px solid #fa6240;
        border-radius: 10px 0 10px 0;
        float: left;
    }

    .course-item .pay-box .discount-price {
        font-size: 24px;
        color: #fa6240;
        float: left;
    }

    .course-item .pay-box .original-price {
        text-decoration: line-through;
        font-size: 14px;
        color: #9b9b9b;
        margin-left: 10px;
        float: left;
        margin-top: 10px;
    }

    .course-item .pay-box .buy-now {
        width: 120px;
        height: 38px;
        background: transparent;
        color: #fa6240;
        font-size: 16px;
        border: 1px solid #fd7b4d;
        border-radius: 3px;
        transition: all .2s ease-in-out;
        float: right;
        text-align: center;
        line-height: 38px;
        position: absolute;
        right: 0;
        bottom: 5px;
    }

    .course-item .pay-box .buy-now:hover {
        color: #fff;
        background: #ffc210;
        border: 1px solid #ffc210;
    }

    .course .course_pagination {
        margin-bottom: 60px;
        text-align: center;
    }
</style>


```

3 课程详情页前端
----------------

```
# 1 新建FreeCourseDetail.vue
# 2 配置路由
	{
        path: '/free/detail/:pk',
        name: 'FreeCourseDetail',
        component: FreeCourseDetail
    },
#3 安装 vue-video播放器
	-cnpm install vue-video-player
	-在main.js中配置
        // vue-video播放器
        require('video.js/dist/video-js.css');
        require('vue-video-player/src/custom-theme.css');
        import VideoPlayer from 'vue-video-player'
        Vue.use(VideoPlayer);
#4 组件
<template>
    <div class="detail">
        <Header/>
        <div class="main">
            <div class="course-info">
                <div class="wrap-left">
                    <videoPlayer class="video-player vjs-custom-skin"
                                 ref="videoPlayer"
                                 :playsinline="true"
                                 :options="playerOptions"
                                 @play="onPlayerPlay($event)"
                                 @pause="onPlayerPause($event)">
                    </videoPlayer>
                </div>
                <div class="wrap-right">
                    <h3 class="course-name">{{course_info.name}}</h3>
                    <p class="data">{{course_info.students}}人在学    课程总时长：{{course_info.sections}}课时/{{course_info.pub_sections}}小时    难度：{{course_info.level_name}}</p>
                    <div class="sale-time">
                        <p class="sale-type">价格 <span class="original_price">¥{{course_info.price}}</span></p>
                        <p class="expire"></p>
                    </div>
                    <div class="buy">
                        <div class="buy-btn">
                            <button class="buy-now">立即购买</button>
                            <button class="free">免费试学</button>
                        </div>
                        <!--<div class="add-cart" @click="add_cart(course_info.id)">-->
														<!--<img src="@/assets/img/cart-yellow.svg" alt="">加入购物车-->
                        <!--</div>-->
                    </div>
                </div>
            </div>
            <div class="course-tab">
                <ul class="tab-list">
                    <li :class="tabIndex==1?'active':''" @click="tabIndex=1">详情介绍</li>
                    <li :class="tabIndex==2?'active':''" @click="tabIndex=2">课程章节 <span :class="tabIndex!=2?'free':''">(试学)</span>
                    </li>
                    <li :class="tabIndex==3?'active':''" @click="tabIndex=3">用户评论</li>
                    <li :class="tabIndex==4?'active':''" @click="tabIndex=4">常见问题</li>
                </ul>
            </div>
            <div class="course-content">
                <div class="course-tab-list">
                    <div class="tab-item" v-if="tabIndex==1">
                        <div class="course-brief" v-html="course_info.brief_text"></div>
                    </div>
                    <div class="tab-item" v-if="tabIndex==2">
                        <div class="tab-item-title">
                            <p class="chapter">课程章节</p>
                            <p class="chapter-length">共{{course_chapters.length}}章 {{course_info.sections}}个课时</p>
                        </div>
                        <div class="chapter-item" v-for="chapter in course_chapters" :key="chapter.name">
                            <p class="chapter-title"><img src="@/assets/img/enum.svg" alt="">第{{chapter.chapter}}章·{{chapter.name}}
                            </p>
                            <ul class="section-list">
                                <li class="section-item" v-for="section in chapter.coursesections" :key="section.name">
                                    <p class="name"><span class="index">{{chapter.chapter}}-{{section.orders}}</span>
                                        {{section.name}}<span class="free" v-if="section.free_trail">免费</span></p>
                                    <p class="time">{{section.duration}} <img src="@/assets/img/chapter-player.svg"></p>
                                    <button class="try" v-if="section.free_trail">立即试学</button>
                                    <button class="try" v-else>立即购买</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="tab-item" v-if="tabIndex==3">
                        用户评论
                    </div>
                    <div class="tab-item" v-if="tabIndex==4">
                        常见问题
                    </div>
                </div>
                <div class="course-side">
                    <div class="teacher-info">
                        <h4 class="side-title"><span>授课老师</span></h4>
                        <div class="teacher-content">
                            <div class="cont1">
                                <img :src="course_info.teacher.image">
                                <div class="name">
                                    <p class="teacher-name">{{course_info.teacher.name}}
                                        {{course_info.teacher.title}}</p>
                                    <p class="teacher-title">{{course_info.teacher.signature}}</p>
                                </div>
                            </div>
                            <p class="narrative">{{course_info.teacher.brief}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from "@/components/Head"
    import Footer from "@/components/Footer"

    // 加载组件
    import {videoPlayer} from 'vue-video-player';

    export default {
        name: "Detail",
        data() {
            return {
                tabIndex: 2,   // 当前选项卡显示的下标
                course_id: 0, // 当前课程信息的ID
                course_info: {
                    teacher: {},
                }, // 课程信息
                course_chapters: [], // 课程的章节课时列表
                playerOptions: {
                    aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                    sources: [{ // 播放资源和资源格式
                        type: "video/mp4",
                        src: "http://qe5smxg12.bkt.clouddn.com/3%20%E9%A6%96%E9%A1%B5%E8%BD%AE%E6%92%AD%E5%9B%BE%E5%BC%82%E6%AD%A5%E6%9B%B4%E6%96%B0.mp4" //你的视频地址（必填）
                    }],
                }
            }
        },
        created() {
            this.get_course_id();
            this.get_course_data();
            this.get_chapter();
        },
        methods: {
            onPlayerPlay() {
                // 当视频播放时，执行的方法
                console.log('视频开始播放')
                //加广告
            },
            onPlayerPause() {
                // 当视频暂停播放时，执行的方法
                console.log('视频暂停，可以打开广告了')
                //盖张图片
            },
            get_course_id() {
                // 获取地址栏上面的课程ID
                this.course_id = this.$route.params.pk || this.$route.query.pk;
                if (this.course_id < 1) {
                    let _this = this;
                    _this.$alert("对不起，当前视频不存在！", "警告", {
                        callback() {
                            _this.$router.go(-1);
                        }
                    });
                }
            },
            get_course_data() {
                // ajax请求课程信息
                this.$axios.get(`${this.$settings.base_url}/course/free/${this.course_id}/`).then(response => {
                    // window.console.log(response.data);
                    this.course_info = response.data;
                    console.log(this.course_info)
                }).catch(() => {
                    this.$message({
                        message: "对不起，访问页面出错！请联系客服工作人员！"
                    });
                })
            },

            get_chapter() {
                // 获取当前课程对应的章节课时信息
                // http://127.0.0.1:8000/course/chapters/?course=(pk)
                this.$axios.get(`${this.$settings.base_url}/course/chapters/`, {
                    params: {
                        "course": this.course_id,
                    }
                }).then(response => {
                    this.course_chapters = response.data;
                }).catch(error => {
                    window.console.log(error.response);
                })
            },
        },
        components: {
            Header,
            Footer,
            videoPlayer, // 注册组件
        }
    }
</script>

<style scoped>
    .main {
        background: #fff;
        padding-top: 30px;
    }

    .course-info {
        width: 1200px;
        margin: 0 auto;
        overflow: hidden;
    }

    .wrap-left {
        float: left;
        width: 690px;
        height: 388px;
        background-color: #000;
    }

    .wrap-right {
        float: left;
        position: relative;
        height: 388px;
    }

    .course-name {
        font-size: 20px;
        color: #333;
        padding: 10px 23px;
        letter-spacing: .45px;
    }

    .data {
        padding-left: 23px;
        padding-right: 23px;
        padding-bottom: 16px;
        font-size: 14px;
        color: #9b9b9b;
    }

    .sale-time {
        width: 464px;
        background: #fa6240;
        font-size: 14px;
        color: #4a4a4a;
        padding: 10px 23px;
        overflow: hidden;
    }

    .sale-type {
        font-size: 16px;
        color: #fff;
        letter-spacing: .36px;
        float: left;
    }

    .sale-time .expire {
        font-size: 14px;
        color: #fff;
        float: right;
    }

    .sale-time .expire .second {
        width: 24px;
        display: inline-block;
        background: #fafafa;
        color: #5e5e5e;
        padding: 6px 0;
        text-align: center;
    }

    .course-price {
        background: #fff;
        font-size: 14px;
        color: #4a4a4a;
        padding: 5px 23px;
    }

    .discount {
        font-size: 26px;
        color: #fa6240;
        margin-left: 10px;
        display: inline-block;
        margin-bottom: -5px;
    }

    .original {
        font-size: 14px;
        color: #9b9b9b;
        margin-left: 10px;
        text-decoration: line-through;
    }

    .buy {
        width: 464px;
        padding: 0px 23px;
        position: absolute;
        left: 0;
        bottom: 20px;
        overflow: hidden;
    }

    .buy .buy-btn {
        float: left;
    }

    .buy .buy-now {
        width: 125px;
        height: 40px;
        border: 0;
        background: #ffc210;
        border-radius: 4px;
        color: #fff;
        cursor: pointer;
        margin-right: 15px;
        outline: none;
    }

    .buy .free {
        width: 125px;
        height: 40px;
        border-radius: 4px;
        cursor: pointer;
        margin-right: 15px;
        background: #fff;
        color: #ffc210;
        border: 1px solid #ffc210;
    }

    .add-cart {
        float: right;
        font-size: 14px;
        color: #ffc210;
        text-align: center;
        cursor: pointer;
        margin-top: 10px;
    }

    .add-cart img {
        width: 20px;
        height: 18px;
        margin-right: 7px;
        vertical-align: middle;
    }

    .course-tab {
        width: 100%;
        background: #fff;
        margin-bottom: 30px;
        box-shadow: 0 2px 4px 0 #f0f0f0;

    }

    .course-tab .tab-list {
        width: 1200px;
        margin: auto;
        color: #4a4a4a;
        overflow: hidden;
    }

    .tab-list li {
        float: left;
        margin-right: 15px;
        padding: 26px 20px 16px;
        font-size: 17px;
        cursor: pointer;
    }

    .tab-list .active {
        color: #ffc210;
        border-bottom: 2px solid #ffc210;
    }

    .tab-list .free {
        color: #fb7c55;
    }

    .course-content {
        width: 1200px;
        margin: 0 auto;
        background: #FAFAFA;
        overflow: hidden;
        padding-bottom: 40px;
    }

    .course-tab-list {
        width: 880px;
        height: auto;
        padding: 20px;
        background: #fff;
        float: left;
        box-sizing: border-box;
        overflow: hidden;
        position: relative;
        box-shadow: 0 2px 4px 0 #f0f0f0;
    }

    .tab-item {
        width: 880px;
        background: #fff;
        padding-bottom: 20px;
        box-shadow: 0 2px 4px 0 #f0f0f0;
    }

    .tab-item-title {
        justify-content: space-between;
        padding: 25px 20px 11px;
        border-radius: 4px;
        margin-bottom: 20px;
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
        overflow: hidden;
    }

    .chapter {
        font-size: 17px;
        color: #4a4a4a;
        float: left;
    }

    .chapter-length {
        float: right;
        font-size: 14px;
        color: #9b9b9b;
        letter-spacing: .19px;
    }

    .chapter-title {
        font-size: 16px;
        color: #4a4a4a;
        letter-spacing: .26px;
        padding: 12px;
        background: #eee;
        border-radius: 2px;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-align: center;
        align-items: center;
    }

    .chapter-title img {
        width: 18px;
        height: 18px;
        margin-right: 7px;
        vertical-align: middle;
    }

    .section-list {
        padding: 0 20px;
    }

    .section-list .section-item {
        padding: 15px 20px 15px 36px;
        cursor: pointer;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
    }

    .section-item .name {
        font-size: 14px;
        color: #666;
        float: left;
    }

    .section-item .index {
        margin-right: 5px;
    }

    .section-item .free {
        font-size: 12px;
        color: #fff;
        letter-spacing: .19px;
        background: #ffc210;
        border-radius: 100px;
        padding: 1px 9px;
        margin-left: 10px;
    }

    .section-item .time {
        font-size: 14px;
        color: #666;
        letter-spacing: .23px;
        opacity: 1;
        transition: all .15s ease-in-out;
        float: right;
    }

    .section-item .time img {
        width: 18px;
        height: 18px;
        margin-left: 15px;
        vertical-align: text-bottom;
    }

    .section-item .try {
        width: 86px;
        height: 28px;
        background: #ffc210;
        border-radius: 4px;
        font-size: 14px;
        color: #fff;
        position: absolute;
        right: 20px;
        top: 10px;
        opacity: 0;
        transition: all .2s ease-in-out;
        cursor: pointer;
        outline: none;
        border: none;
    }

    .section-item:hover {
        background: #fcf7ef;
        box-shadow: 0 0 0 0 #f3f3f3;
    }

    .section-item:hover .name {
        color: #333;
    }

    .section-item:hover .try {
        opacity: 1;
    }

    .course-side {
        width: 300px;
        height: auto;
        margin-left: 20px;
        float: right;
    }

    .teacher-info {
        background: #fff;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px 0 #f0f0f0;
    }

    .side-title {
        font-weight: normal;
        font-size: 17px;
        color: #4a4a4a;
        padding: 18px 14px;
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
    }

    .side-title span {
        display: inline-block;
        border-left: 2px solid #ffc210;
        padding-left: 12px;
    }

    .teacher-content {
        padding: 30px 20px;
        box-sizing: border-box;
    }

    .teacher-content .cont1 {
        margin-bottom: 12px;
        overflow: hidden;
    }

    .teacher-content .cont1 img {
        width: 54px;
        height: 54px;
        margin-right: 12px;
        float: left;
    }

    .teacher-content .cont1 .name {
        float: right;
    }

    .teacher-content .cont1 .teacher-name {
        width: 188px;
        font-size: 16px;
        color: #4a4a4a;
        padding-bottom: 4px;
    }

    .teacher-content .cont1 .teacher-title {
        width: 188px;
        font-size: 13px;
        color: #9b9b9b;
        white-space: nowrap;
    }

    .teacher-content .narrative {
        font-size: 14px;
        color: #666;
        line-height: 24px;
    }
</style>


```

4 课程单查接口
--------------

```
class CouresView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = models.Course.objects.filter(is_delete=False,is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    pagination_class = PageNumberPagination

    # 过滤和排序
    # filter_backends=[DjangoFilterBackend,OrderingFilter,SearchFilter]
    # filter_backends=[DjangoFilterBackend,OrderingFilter,MyFilter]
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    # # filter_backends=OrderingFilter
    ordering_fields=['id', 'price', 'students']
    # # search_fields=['course_category']
    filter_fields=['course_category']


```

5 章节分类接口
--------------

```
#1 urls.py
router.register('chapters', views.CourseChapterView, 'coursechapter')

# 2 views.py
class CourseChapterView(GenericViewSet,ListModelMixin):
    queryset = models.CourseChapter.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializer.CourseChapterSerializer

    # 可以按照课程id来查
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']
  
  
  
# 3 serializer.py
class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseSection
        fields=['name','orders','duration','free_trail','section_link','section_type_name']
class CourseChapterSerializer(serializers.ModelSerializer):
    # 子序列化的方式
    coursesections=CourseSectionSerializer(many=True)
    class Meta:
        model=models.CourseChapter
        fields=['name','summary','chapter','coursesections']


```

6 七牛云视频托管
----------------

```
# 1 注册七牛云，实名认证
	https://www.qiniu.com/
# 2 登录---》管理控制台---》对象存储
# 3 新建空间----》上传视频--》拿到视频连接


```

7 后台搜索接口
--------------

```
# urls.py
router.register('search', views.CouresSearchView, 'search')
# views.py
class CouresSearchView(GenericViewSet,ListModelMixin):
    queryset = models.Course.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializer.CourseModelSerializer
    pagination_class = PageNumberPagination

    filter_backends=[SearchFilter]
    search_fields=['name']


```

8 前台搜索页面完成
------------------

```
# 0 在Head.vue中相应的配置


# 1  vue带给另一个页面值
    -路由：path: '/free/detail/:pk',this.$route.params.pk  从路径中取值
	-search?word=dsa  去this.$route.query.word   从？后面的取
  
  
# 2 样式
<template>
    <div class="search-course course">
        <Header/>
        <h1>总共搜索到 {{course_total}}课程</h1>
        <!-- 课程列表 -->
        <div class="main">
            <div v-if="course_list.length > 0" class="course-list">
                <div class="course-item" v-for="course in course_list" :key="course.name">
                    <div class="course-image">
                        <img :src="course.course_img" alt="">
                    </div>
                    <div class="course-info">
                        <h3>
                            <router-link :to="'/free/detail/'+course.id">{{course.name}}</router-link>
                            <span><img src="@/assets/img/avatar1.svg" alt="">{{course.students}}人已加入学习</span></h3>
                        <p class="teather-info">
                            {{course.teacher.name}} {{course.teacher.title}} {{course.teacher.signature}}
                            <span v-if="course.sections>course.pub_sections">共{{course.sections}}课时/已更新{{course.pub_sections}}课时</span>
                            <span v-else>共{{course.sections}}课时/更新完成</span>
                        </p>
                        <ul class="section-list">
                            <li v-for="(section, key) in course.section_list" :key="section.name"><span
                                    class="section-title">0{{key+1}}  |  {{section.name}}</span>
                                <span class="free" v-if="section.free_trail">免费</span></li>
                        </ul>
                        <div class="pay-box">
                            <div v-if="course.discount_type">
                                <span class="discount-type">{{course.discount_type}}</span>
                                <span class="discount-price">￥{{course.real_price}}元</span>
                                <span class="original-price">原价：{{course.price}}元</span>
                            </div>
                            <span v-else class="discount-price">￥{{course.price}}元</span>
                            <span class="buy-now">立即购买</span>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else style="text-align: center; line-height: 60px">
                没有搜索结果
            </div>
            <div class="course_pagination block">
                <el-pagination
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                        :current-page.sync="filter.page"
                        :page-sizes="[2, 3, 5, 10]"
                        :page-size="filter.page_size"
                        layout="sizes, prev, pager, next"
                        :total="course_total">
                </el-pagination>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from '../components/Head'

    export default {
        name: "SearchCourse",
        components: {
            Header,
        },
        data() {
            return {
                course_list: [],
                course_total: 0,
                filter: {
                    page_size: 10,
                    page: 1,
                    search: '',
                }
            }
        },
        created() {
            this.get_course()
        },
        watch: {
            '$route.query' () {
                this.get_course()
            }
        },
        methods: {
            handleSizeChange(val) {
                // 每页数据量发生变化时执行的方法
                this.filter.page = 1;
                this.filter.page_size = val;
            },
            handleCurrentChange(val) {
                // 页码发生变化时执行的方法
                this.filter.page = val;
            },
            get_course() {
                // 获取搜索的关键字
                this.filter.search = this.$route.query.word || this.$route.query.wd;

                // 获取课程列表信息
                this.$axios.get(`${this.$settings.base_url}/course/search/`, {
                    params: this.filter
                }).then(response => {
                    // 如果后台不分页，数据在response.data中；如果后台分页，数据在response.data.results中
                    this.course_list = response.data.results;
                    this.course_total = response.data.count;
                }).catch(() => {
                    this.$message({
                        message: "获取课程信息有误，请联系客服工作人员"
                    })
                })
            }
        }
    }
</script>

<style scoped>
    .course {
        background: #f6f6f6;
    }

    .course .main {
        width: 1100px;
        margin: 35px auto 0;
    }

    .course .condition {
        margin-bottom: 35px;
        padding: 25px 30px 25px 20px;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 2px 4px 0 #f0f0f0;
    }

    .course .cate-list {
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
        padding-bottom: 18px;
        margin-bottom: 17px;
    }

    .course .cate-list::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .cate-list li {
        float: left;
        font-size: 16px;
        padding: 6px 15px;
        line-height: 16px;
        margin-left: 14px;
        position: relative;
        transition: all .3s ease;
        cursor: pointer;
        color: #4a4a4a;
        border: 1px solid transparent; /* transparent 透明 */
    }

    .course .cate-list .title {
        color: #888;
        margin-left: 0;
        letter-spacing: .36px;
        padding: 0;
        line-height: 28px;
    }

    .course .cate-list .this {
        color: #ffc210;
        border: 1px solid #ffc210 !important;
        border-radius: 30px;
    }

    .course .ordering::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .ordering ul {
        float: left;
    }

    .course .ordering ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .course .ordering .condition-result {
        float: right;
        font-size: 14px;
        color: #9b9b9b;
        line-height: 28px;
    }

    .course .ordering ul li {
        float: left;
        padding: 6px 15px;
        line-height: 16px;
        margin-left: 14px;
        position: relative;
        transition: all .3s ease;
        cursor: pointer;
        color: #4a4a4a;
    }

    .course .ordering .title {
        font-size: 16px;
        color: #888;
        letter-spacing: .36px;
        margin-left: 0;
        padding: 0;
        line-height: 28px;
    }

    .course .ordering .this {
        color: #ffc210;
    }

    .course .ordering .price {
        position: relative;
    }

    .course .ordering .price::before,
    .course .ordering .price::after {
        cursor: pointer;
        content: "";
        display: block;
        width: 0px;
        height: 0px;
        border: 5px solid transparent;
        position: absolute;
        right: 0;
    }

    .course .ordering .price::before {
        border-bottom: 5px solid #aaa;
        margin-bottom: 2px;
        top: 2px;
    }

    .course .ordering .price::after {
        border-top: 5px solid #aaa;
        bottom: 2px;
    }

    .course .ordering .price_up::before {
        border-bottom-color: #ffc210;
    }

    .course .ordering .price_down::after {
        border-top-color: #ffc210;
    }

    .course .course-item:hover {
        box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
    }

    .course .course-item {
        width: 1100px;
        background: #fff;
        padding: 20px 30px 20px 20px;
        margin-bottom: 35px;
        border-radius: 2px;
        cursor: pointer;
        box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
        /* css3.0 过渡动画 hover 事件操作 */
        transition: all .2s ease;
    }

    .course .course-item::after {
        content: "";
        display: block;
        clear: both;
    }

    /* 顶级元素 父级元素  当前元素{} */
    .course .course-item .course-image {
        float: left;
        width: 423px;
        height: 210px;
        margin-right: 30px;
    }

    .course .course-item .course-image img {
        max-width: 100%;
        max-height: 210px;
    }

    .course .course-item .course-info {
        float: left;
        width: 596px;
    }

    .course-item .course-info h3 a {
        font-size: 26px;
        color: #333;
        font-weight: normal;
        margin-bottom: 8px;
    }

    .course-item .course-info h3 span {
        font-size: 14px;
        color: #9b9b9b;
        float: right;
        margin-top: 14px;
    }

    .course-item .course-info h3 span img {
        width: 11px;
        height: auto;
        margin-right: 7px;
    }

    .course-item .course-info .teather-info {
        font-size: 14px;
        color: #9b9b9b;
        margin-bottom: 14px;
        padding-bottom: 14px;
        border-bottom: 1px solid #333;
        border-bottom-color: rgba(51, 51, 51, .05);
    }

    .course-item .course-info .teather-info span {
        float: right;
    }

    .course-item .section-list::after {
        content: "";
        display: block;
        clear: both;
    }

    .course-item .section-list li {
        float: left;
        width: 44%;
        font-size: 14px;
        color: #666;
        padding-left: 22px;
        /* background: url("路径") 是否平铺 x轴位置 y轴位置 */
        background: url("/src/assets/img/play-icon-gray.svg") no-repeat left 4px;
        margin-bottom: 15px;
    }

    .course-item .section-list li .section-title {
        /* 以下3句，文本内容过多，会自动隐藏，并显示省略符号 */
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        display: inline-block;
        max-width: 200px;
    }

    .course-item .section-list li:hover {
        background-image: url("/src/assets/img/play-icon-yellow.svg");
        color: #ffc210;
    }

    .course-item .section-list li .free {
        width: 34px;
        height: 20px;
        color: #fd7b4d;
        vertical-align: super;
        margin-left: 10px;
        border: 1px solid #fd7b4d;
        border-radius: 2px;
        text-align: center;
        font-size: 13px;
        white-space: nowrap;
    }

    .course-item .section-list li:hover .free {
        color: #ffc210;
        border-color: #ffc210;
    }

    .course-item {
        position: relative;
    }

    .course-item .pay-box {
        position: absolute;
        bottom: 20px;
        width: 600px;
    }

    .course-item .pay-box::after {
        content: "";
        display: block;
        clear: both;
    }

    .course-item .pay-box .discount-type {
        padding: 6px 10px;
        font-size: 16px;
        color: #fff;
        text-align: center;
        margin-right: 8px;
        background: #fa6240;
        border: 1px solid #fa6240;
        border-radius: 10px 0 10px 0;
        float: left;
    }

    .course-item .pay-box .discount-price {
        font-size: 24px;
        color: #fa6240;
        float: left;
    }

    .course-item .pay-box .original-price {
        text-decoration: line-through;
        font-size: 14px;
        color: #9b9b9b;
        margin-left: 10px;
        float: left;
        margin-top: 10px;
    }

    .course-item .pay-box .buy-now {
        width: 120px;
        height: 38px;
        background: transparent;
        color: #fa6240;
        font-size: 16px;
        border: 1px solid #fd7b4d;
        border-radius: 3px;
        transition: all .2s ease-in-out;
        float: right;
        text-align: center;
        line-height: 38px;
        position: absolute;
        right: 0;
        bottom: 5px;
    }

    .course-item .pay-box .buy-now:hover {
        color: #fff;
        background: #ffc210;
        border: 1px solid #ffc210;
    }

    .course .course_pagination {
        margin-bottom: 60px;
        text-align: center;
    }
</style>  


```

9 支付宝
--------

```
# 沙箱环境：https://openhome.alipay.com/platform/appDaily.htm

# https://opendocs.alipay.com/open/291/106097/ 下载软件，生成秘钥（公钥私钥）
# 取出公钥，配置再支付宝平台，它会生成一个支付宝公钥



#代码
# pip install python-alipay-sdk


from alipay import AliPay


# app_private_key_string = open("/path/to/your/private/key.pem").read()
# alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEApkFnp38PSslhn4wvRarL40+WtVpan6tVT55FWzAzLfQ8PfqZE2qW7mCJy1/zM07+S5L+X0pC+F7BlT+0z4rlxraG5D23khWfHb4x+uDi0Wd94eaVB0PzQXCYYBChuORvNN5YLTspeP7rNQ2OcdpGx2KUzo9w59dVW+AweblFl7GqPkRSC0P5XbkJtwnEAd0Nc08HzJR0OWZT9HRFOA7coaude9uSwDsXmsdkSNGsGDcaGEY6aGk2Tj9Fyni9LJJcOXwGrUuGDpdcP2tYePrFUGMDml/feFR9QGUbExWh/ZNpb9lKLwOtXOhQj9slilp+YJek/rLlSgW9K1WrYpuuBwIDAQABAoIBADN1mRzKAjS2wmW84UDiDbus/cviTJyRTpWXOoZwE9dMen0AnPLakh70eJIff8pI0AMaW2upM7NmuOp2ToPSzS5FftkUlUY9NQPiw9uQUgRY0Sjj0wrtqFSAAlnxq+zrn9QwYgCWCE8wMCM6r/Vjh3bdd4u78EmCaCRI7xguFXFPB9NY9oCFiwsTFJtXPZo+DSIQjqIDnh8YtV3NzrA3Ln3DsKMAr+vnPMeljAL5US6Rt5tOQY0qa9bUi6RqQwTLADcANd49YOvlr7OLjwi5jkeJ16j1nKgpasAIg9V+rF085u+PEKkLL3WJHwmhiIxrA11bxCnm1fRdfHbyWZKY9yECgYEA0k3wS7A7rzhtpznc5ZfVGWIEQ5IahRkqVGbc6wFIXKXnypOtGKAFiRmEPwm9xRurlo8TJ1bjK4D4ljEANJhX2NnIZfK3YDdNEN6D4GnEvPFR641M8M47Z7ItvdRKre8P2/ThXhkMnq5/1y7e87xvE6/a1Tr44+hclHvQWPRrsPcCgYEAymFEy0/2xAX+si4S8pzrgLfBg3Ehjan8T6JZZNCKhR7b/IT+3/AWJimzEL6jYQMlhy7QzZbRb1ssIIzqPFcFQYjQE0n6fswJuN4+jayW9Jtjvar/zhHFjW3EODR5yEDTvS3CHqQLeG3ce+srMJSxVDJR2V9ortFeb+VPbWZ+t3ECgYEAxPYvvoNwcpuzvvGnW/RGpb4x5iL46Xz3MxMfho2t+u961jRW4oBEjvGx9OQnsmpG2vxm4Oo0WnMw3mFIIvonFDZrxGd8rQU+DTWJZ21Hz/lnUugEjmdoJacvxeEEjEAgp02CoQFu21Ls8li4gKgTk+mYVyojHjhqNLp9GELadWMCgYEAi0RSXgLCEnT5p03zdgcsPOC3ByfT6jO+0GItWCX2HNN2mRhAeIQ0CcEKW4yEy56ptZQu1jtiFlpMTH4MNse/czCd15hCC/2G9zPhIgdRvjQsd/nznLA4HTIbJH5gC8EotHeHrSRATHh1kMTtbLn2KbWTA54XYK3tad0IQoWUz9ECgYBBc+kCJsb0shaRIRP5nmeb5tZCH7Yq9DgriwcIlK74cxW9fvL94n91Y6M8vSZ6MC7vF5wmcXMj3K1of04qizKbbKxCCYeOIHhTh0dB+ualDxu5WBG/6mLWR3HVHazqRVri9qoZ/3zNDx5CRNi81VpzOPmVtuos5d9sZZaNR3lkRQ==
-----END RSA PRIVATE KEY-----
"""

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwU9mMZHHlQPE9FcxVtXOXhbWCtuDZLJRVCiofdbTVmRXrx47yGniPehwcKIsqhzhEaXBG2QhpIZUL8YsCav0mkrppoRvWOytuGyxNRESo8I6DWRs0aCq6P3AuiD9kSXET4dpAuRYT/+JrMXIZTycEts6vYYNAT9QivXJoa2FmiCQBAL3HP7F36pby9VstObilxXQcoBBJwEYGf2TK6moFFZ1dkloRr5Cfk/G82DpuVfrt1gr4OuIDWtcE3MZTrvDgTqtkRuwGF76FY3+8xUCUbJs1dL5cXYN7/b3jPcXVcdKXFj4WrOQd42ofE1BJWMxBW7L3Qlxue1vy+NGx/CuKwIDAQAB
-----END PUBLIC KEY-----
"""

alipay = AliPay(
    appid="2016092000554611",
    app_notify_url='http://127.0.0.1:8000/home/',  # the default notify path
    app_private_key_string=app_private_key_string,
    # alipay public key, do not use your own public key!
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2", # RSA or RSA2
    debug=True  # False by default
)


alipay_url='https://openapi.alipaydev.com/gateway.do?'
order_string = alipay.api_alipay_trade_page_pay    (
    out_trade_no="20161112www4334",
    total_amount=9999,
    subject='韩红版充气娃娃',
    return_url="https://www.luffycity.com/free-course",
    notify_url="https://www.luffycity.com/free-course"
)
print(alipay_url+order_string)






```

补充
====

```
# 1 全文检索引擎：elasticsearch，java封装的一个数据库，专注于大数据存储和搜索


```

支付宝二次封装
--------------

```
al_pay
    -pem
    -__init__.py
    -pay.py
    -setting.py
#__init__.py
from .pay import alipay,gateway
#pay.py

from alipay import AliPay
from . import setting
alipay = AliPay(
    appid=setting.APPID,
    app_notify_url=None,  # the default notify path
    app_private_key_string=setting.APP_PRIVATE_KEY_STRING,
    # alipay public key, do not use your own public key!
    alipay_public_key_string=setting.ALIPAY_PUBLIC_KEY_STRING,
    sign_type=setting.SIGN_TYPE, # RSA or RSA2
    debug=setting.DEBUG  # False by default
)
gateway=setting.GATEWAY
# setting.py
import os
APPID="2016092000554611"
APP_PRIVATE_KEY_STRING = open(os.path.join(os.path.dirname(__file__),'pem','private_key.pem')).read()
ALIPAY_PUBLIC_KEY_STRING = open(os.path.join(os.path.dirname(__file__),'pem','al_public_key.pem')).read()
SIGN_TYPE='RSA2'
DEBUG=True
GATEWAY='https://openapi.alipaydev.com/gateway.do?' if DEBUG else 'https://openapi.alipay.com/gateway.do?'


```

2 订单模块与表分析
------------------

```
# 订单表分析
	-订单表
    -订单详情
  
from django.db import models
from django.db import models
from user.models import User
from course.models import Course
# 订单表
class Order(models.Model):
    """订单模型"""
    status_choices = (
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '超时取消'),
    )
    pay_choices = (
        (1, '支付宝'),
        (2, '微信支付'),
    )
    subject = models.CharField(max_length=150, verbose_)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_, default=0)
    out_trade_no = models.CharField(max_length=64, verbose_, unique=True)
    trade_no = models.CharField(max_length=64, null=True, verbose_)  # 支付宝生成回来的
    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_)
    pay_type = models.SmallIntegerField(choices=pay_choices, default=1, verbose_)
    pay_time = models.DateTimeField(null=True, verbose_)
    # 一个用户可以下多个订单，一个订单只属于一个用户，一对多的关系，关联字段写在多个一方，写在order方
    user = models.ForeignKey(User, related_)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    class Meta:
        db_table = "luffy_order"
        verbose_name = "订单记录"
        verbose_name_plural = "订单记录"

    def __str__(self):
        return "%s - ￥%s" % (self.subject, self.total_amount)

    @property
    def courses(self):
        data_list = []
        for item in self.order_courses.all():
            data_list.append({
                "id": item.id,
                "course_name": item.course.name,
                "real_price": item.real_price,
            })
        return data_list

# 订单详情表
# 订单和详情是一对多，关联字段写在多个的一方，写在订单详情表中
class OrderDetail(models.Model):
    """订单详情"""
    order = models.ForeignKey(Order, related_)
    course = models.ForeignKey(Course, related_,null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_)
    real_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_)

    class Meta:
        db_table = "luffy_order_detail"
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"

    def __str__(self):
        try:
            return "%s的订单：%s" % (self.course.name, self.order.out_trade_no)
        except:
            return super().__str__()


```

3 订单模块接口分析
------------------

```
# 1 支付接口（生成订单,，生成支付连接，返回支付连接）
	-order表和orderdetail表插入数据，重写create方法
    -生成订单号（uuid）
    -登录后才能做（jwt认证）
    -当前登录用户就是下单用户，存到order表中
    -下了三个课程，总价格100，前端提交的价格是99，异常处理
     '''
        #1）订单总价校验
        # 2）生成订单号
        # 3）支付用户：request.user
        # 4）支付链接生成
        # 5）入库(两个表)的信息准备
    '''
# 2 支付宝异步回调的post接口（验证签名，修改订单状态）
# 3 当支付宝get回调前端，vue组件一创建，立马向后端发一个请求（get）


```

4 支付接口
----------

```
# 1 前端传什么格式数据
	-{course:[1,2,3],total_amount:100,subject:xx商品,pay_type:1,}
  
# 2 后端接到数据要校验
	-course:[1,2,3]===》course:[obj1，obj2，obj3]
    -在序列化类中： 					                  course=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True, many=True)
# 3 在序列化类的validate中处理一堆逻辑
        '''
        # 1）订单总价校验：
        	-一个个课程价格取出来累加看是否等于传入的总价格
        # 2）生成订单号
        	-通过uuid生成
        # 3）支付用户：request.user
        	-通过视图和序列化类之间的桥梁context对象传递
        	-重新视图类中的create方法，把request对象放入context
        	-self.context.get('request').user
        # 4）支付链接生成
        	-导入封装的支付宝支付，生成
        	order_string = alipay.api_alipay_trade_page_pay    (
            out_trade_no=out_trade_no,
            total_amount=total_amout,
            subject=subject,
            return_url=settings.RETURN_URL,  # get回调，前台地址
            notify_url=settings.NOTIFY_URL   # post回调，后台地址
        )
        # 5）入库(两个表)的信息准备
        	-把user放入attrs中
        	-把订单号，放入attrs中
        	attrs['user']=user
        	attrs['out_trade_no']=out_trade_no
        	self.context['pay_url']=pay_url
        '''
  
 # 4 重写序列化类的create方法
	-把course_list弹出来
    -order=models.Order.objects.create(**validated_data)


```

```
# urls.py
router = SimpleRouter()
router.register('pay', views.PayView, 'pay')
urlpatterns = [
    path('', include(router.urls)),
]

# views.py
class PayView(GenericViewSet,CreateModelMixin):
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    queryset = models.Order.objects.all()
    serializer_class = serializer.OrderSerializer

    # 重写create方法
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.context.get('pay_url'))
  
# serializer.py
class OrderSerializer(serializers.ModelSerializer):
    # 前端传什么数据过来{course:[1,2,3],total_amount:100,subject:xx商品,pay_type:1,}
    # user字段需要，但是不是传的，使用了jwt


    # 需要把course:[1,2,3] 处理成 course:[obj1,obj2,obj3]

    # 课时：[1,4,6,]===>课时：[obj1,obj4,obj6,]
    # course=serializers.CharField()
    course=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True, many=True)

    class Meta:
        model = models.Order
        fields = ['total_amount','subject','pay_type','course']
        extra_kwargs={
            'total_amount':{'required':True},
            'pay_type': {'required': True},
        }


    def _check_price(self,attrs):
        total_amount=attrs.get('total_amount')
        course_list=attrs.get('course')
        total_price=0
        for course in course_list:
            total_price+=course.price
        if total_price!=total_amount:
            raise ValidationError('价格不合法')
        return total_amount

    def _gen_out_trade_no(self):
        import uuid
        return str(uuid.uuid4()).replace('-','')

    def _get_user(self):
        # 需要request对象(需要视图通过context把reuqest对象传入。重写create方法)
        request=self.context.get('request')
        return request.user

    def _gen_pay_url(self,out_trade_no,total_amout,subject):
        # total_amout是Decimal类型，识别不了，需要转换成float类型
        from luffyapi.libs.al_pay import alipay,gateway
        order_string = alipay.api_alipay_trade_page_pay    (
            out_trade_no=out_trade_no,
            total_amount=float(total_amout),
            subject=subject,
            return_url=settings.RETURN_URL,  # get回调，前台地址
            notify_url=settings.NOTIFY_URL   # post回调，后台地址
        )
        return gateway+order_string

    def _before_create(self,attrs,user,pay_url,out_trade_no):
        attrs['user']=user
        attrs['out_trade_no']=out_trade_no

        self.context['pay_url']=pay_url
    def validate(self, attrs):
        '''
        # 1）订单总价校验
        # 2）生成订单号
        # 3）支付用户：request.user
        # 4）支付链接生成
        # 5）入库(两个表)的信息准备
        '''
        # 1）订单总价校验
        total_amout = self._check_price(attrs)
        # 2）生成订单号
        out_trade_no=self._gen_out_trade_no()
        # 3）支付用户：request.user
        user=self._get_user()
        # 4）支付链接生成
        pay_url=self._gen_pay_url(out_trade_no,total_amout,attrs.get('subject'))
        # 5）入库(两个表)的信息准备
        self._before_create(attrs,user,pay_url,out_trade_no)
        return attrs
    def create(self, validated_data):
        course_list=validated_data.pop('course')
        order=models.Order.objects.create(**validated_data)
        for course in course_list:
            models.OrderDetail.objects.create(order=order,course=course,price=course.price,real_price=course.price)

        return order


```

5 前后台回调接口配置
--------------------

```
# dev.py
# 上线后必须换成公网地址
# 后台基URL
BASE_URL = 'http://127.0.0.1:8000'
# 前台基URL
LUFFY_URL = 'http://127.0.0.1:8080'
# 支付宝同步异步回调接口配置
# 后台异步回调接口
NOTIFY_URL = BASE_URL + "/order/success/"
# 前台同步回调接口，没有 / 结尾
RETURN_URL = LUFFY_URL + "/pay/success"


```

6 前台生成订单并跳转
--------------------

```
# FreeCourse.vue
<span class="buy-now" @click="buy_now(course)">立即购买</span>
# script
 buy_now(course) {
                let token = this.$cookies.get('token')
                if (!token) {
                    this.$message({
                        message: "您还没有登录，请先登录",
                    })
                    return false
                }
                this.$axios({
                        method: 'post',
                        url: this.$settings.base_url + '/order/pay/',
                        data: {
                            "total_amount": course.price,
                            "subject": course.name,
                            "pay_type": 1,
                            "course": [
                                course.id,
                            ]
                        },
                        headers: {Authorization: 'jwt ' + token}
                    }
                ).then(response => {
                    console.log(response.data)
                    let pay_url=response.data
                    //前端发送get请求
                    open(pay_url,'_self')
                }).catch(error => {
                })

            },


```

7 前台支付成功页面
------------------

```
# 路由
{
        path: '/pay/success',
        name: 'PaySuccess',
        component: PaySuccess
    },

#PaySuccess.vue
<template>
    <div class="pay-success">
        <!--如果是单独的页面，就没必要展示导航栏(带有登录的用户)-->
        <Header/>
        <div class="main">
            <div class="title">
                <div class="success-tips">
                    <p class="tips">您已成功购买 1 门课程！</p>
                </div>
            </div>
            <div class="order-info">
                <p class="info"><b>订单号：</b><span>{{ result.out_trade_no }}</span></p>
                <p class="info"><b>交易号：</b><span>{{ result.trade_no }}</span></p>
                <p class="info"><b>付款时间：</b><span><span>{{ result.timestamp }}</span></span></p>
            </div>
            <div class="study">
                <span>立即学习</span>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from "@/components/Head"

    export default {
        name: "Success",
        data() {
            return {
                result: {},
            };
        },
        created() {
            // url后拼接的参数：?及后面的所有参数 => ?a=1&b=2
            // console.log(location.search);

            // 解析支付宝回调的url参数
            let params = location.search.substring(1);  // 去除? => a=1&b=2
            let items = params.length ? params.split('&') : [];  // ['a=1', 'b=2']
            //逐个将每一项添加到args对象中
            for (let i = 0; i < items.length; i++) {  // 第一次循环a=1，第二次b=2
                let k_v = items[i].split('=');  // ['a', '1']
                //解码操作，因为查询字符串经过编码的
                if (k_v.length >= 2) {
                    // url编码反解
                    let k = decodeURIComponent(k_v[0]);
                    this.result[k] = decodeURIComponent(k_v[1]);
                    // 没有url编码反解
                    // this.result[k_v[0]] = k_v[1];
                }

            }
            // 解析后的结果
            // console.log(this.result);


            // 把地址栏上面的支付结果，再get请求转发给后端
            this.$axios({
                url: this.$settings.base_url + '/order/success/' + location.search,
                method: 'get',
            }).then(response => {
                console.log(response.data);
            }).catch(() => {
                console.log('支付结果同步失败');
            })
        },
        components: {
            Header,
        }
    }
</script>

<style scoped>
    .main {
        padding: 60px 0;
        margin: 0 auto;
        width: 1200px;
        background: #fff;
    }

    .main .title {
        display: flex;
        -ms-flex-align: center;
        align-items: center;
        padding: 25px 40px;
        border-bottom: 1px solid #f2f2f2;
    }

    .main .title .success-tips {
        box-sizing: border-box;
    }

    .title img {
        vertical-align: middle;
        width: 60px;
        height: 60px;
        margin-right: 40px;
    }

    .title .success-tips {
        box-sizing: border-box;
    }

    .title .tips {
        font-size: 26px;
        color: #000;
    }


    .info span {
        color: #ec6730;
    }

    .order-info {
        padding: 25px 48px;
        padding-bottom: 15px;
        border-bottom: 1px solid #f2f2f2;
    }

    .order-info p {
        display: -ms-flexbox;
        display: flex;
        margin-bottom: 10px;
        font-size: 16px;
    }

    .order-info p b {
        font-weight: 400;
        color: #9d9d9d;
        white-space: nowrap;
    }

    .study {
        padding: 25px 40px;
    }

    .study span {
        display: block;
        width: 140px;
        height: 42px;
        text-align: center;
        line-height: 42px;
        cursor: pointer;
        background: #ffc210;
        border-radius: 6px;
        font-size: 16px;
        color: #fff;
    }
</style>


```

### 支付宝 get 回调参数

```
charset=utf-8&
out_trade_no=17fcf8cac17c442bbbc114df6004afff&
method=alipay.trade.page.pay.return&
total_amount=99.00&
sign=WfK2beWFKvVaTHXpREi8HqZtFRH3JbeIvkliReYvfuhAsqaxHguARKtW6jUqUdZinm7ZSaYE1NrBRQa3%2BLquMk6uMnxE0i%2FTXIu4%2FmNTCEqSUlG8fTRPwC2%2BuU4nN1Ym0eM4puzAc2TUnEJnXCGKP9UxMifN3cjqR5BP%2B3RRngZSS4IQeogjurpfdiIolLzed%2FHTWbc4HqvWlWn9JuLmFGTtKHvRRKFr1hqq8Pj%2Fe3Al8kieDN9Q7JhEdC6F5ROo9rLlmUJtevkjI22oRScrfJl5hb%2BeYosxNg3WktmYKlF5vsKeZKKnLayAvKGoySLvaWk90x0LijHzzf2%2F8a9s3w%3D%3D&
trade_no=2020072922001480160500851368&
auth_app_id=2016092000554611&
version=1.0&
app_id=2016092000554611&
sign_type=RSA2&
seller_id=2088102176466324&
timestamp=2020-07-29%2015%3A06%3A44


```

8 同步异步回调接口
------------------

```
class SuccessView(APIView):
    def get(self,request,*args,**kwargs):
        out_trade_no=request.query_params.get('out_trade_no')
        order=models.Order.objects.filter(out_trade_no=out_trade_no).first()
        if order.order_status==1:
            return Response(True)
        else:
            return Response(False)

    def post(self,request,*args,**kwargs):
        '''
        支付宝回调接口
        '''
        from luffyapi.libs.al_pay import alipay
        from luffyapi.utils.logger import log
        data = request.data
        out_trade_no=data.get('out_trade_no',None)
        gmt_payment=data.get('gmt_payment',None)
        signature = data.pop("sign")
        # 验证签名
        success = alipay.verify(data, signature)
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            models.Order.objects.filter(out_trade_no=out_trade_no).update(order_status=1,pay_time=gmt_payment)
            log.info('%s订单支付成功'%out_trade_no)
            return Response('success')
        else:
            log.info('%s订单有问题' % out_trade_no)
            return Response('error')


```

9 上线前准备
------------

```
# 前端执行 npm run build   把你写的vue代码编译成html，css，js

# 后端代码
	-修改setting中的pro.py
    -项目根路径新建一个manage_pro.py（把原来的manage.py复制改动上线的配置文件）
    -wsgi.py:改成线上的dev


```

阿里云购买
----------

```
# 1 写好的项目，在本地跑，别问访问不到，没有公网ip
# 2 远程连接阿里云的服务器47.103.156.13（xshell，finalShell）
# 3 ssh连接 
# 4 配置前后端项目
# 5 编译前端项目，要把前端项目传到服务器（可以用软件）
	scp -r dist root@47.103.156.13:~
# 6 


```

2 云服务器安装 redis
--------------------

```
1）前往用户根目录
>: cd ~

2）下载redis-5.0.5
>: wget http://download.redis.io/releases/redis-5.0.5.tar.gz
>: scp -r C:\Users\dell\Desktop\pkg\redis-5.0.5.tar.gz root@39.99.192.127:~

3）解压安装包
>: tar -xf redis-5.0.5.tar.gz

4）进入目标文件
>: cd redis-5.0.5

5）编译环境
>: make

6）复制环境到指定路径完成安装
>: cp -r ~/redis-5.0.5 /usr/local/redis


9）建立软连接
>: ln -s /usr/local/redis/src/redis-server /usr/bin/redis-server
>: ln -s /usr/local/redis/src/redis-cli /usr/bin/redis-cli

10）后台运行redis
>: cd /usr/local/redis
>: redis-server &

ctrl + c 停止

11）测试redis环境
>: redis-cli
ctrl + c

12）关闭redis服务
>: pkill -f redis -9


```

3 云服务器安装 mysql
--------------------

```
1）前往用户根目录
>: cd ~

2）下载mysql57
>: wget http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm

也可以本地上传，这条命令要在本地终端上执行
>: scp -r C:mysql57-community-release-el7-10.noarch.rpm root@39.99.192.127:~

3）安装mysql57
>: yum -y install mysql57-community-release-el7-10.noarch.rpm
>: yum -y install mysql-community-server

4）启动mysql57并查看启动状态
>: systemctl start mysqld.service
>: systemctl status mysqld.service

5）查看默认密码并登录
>: grep "password" /var/log/mysqld.log
>: mysql -uroot -p

6）修改密码
>: ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';


```

4 云服务器安装 python
---------------------

```
1）前往用户根目录
>: cd ~

2）下载 或 上传 Python3.6.7
# 服务器终端
>: wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz

# 本地终端，给服务器上传
>: scp -r 本地Python-3.6.7.tar.xz ssh root@39.99.192.127:服务器路径
>: scp -r C:\Users\dell\Desktop\pkg\Python-3.6.7.tar.xz ssh root@39.99.192.127~

3）解压安装包
>: tar -xf Python-3.6.7.tar.xz

4）进入目标文件
>: cd Python-3.6.7

5）配置安装路径：/usr/local/python3
>: ./configure --prefix=/usr/local/python3

6）编译并安装
>: make && sudo make install

7）建立软连接：终端命令 python3，pip3
>: ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
>: ln -s /usr/local/python3/bin/pip3.6 /usr/bin/pip3

8）删除安装包与文件：
>: rm -rf Python-3.6.7
>: rm -rf Python-3.6.7.tar.xz


```

5 云服务器安装 nginx
--------------------

```
1）前往用户根目录
>: cd ~

2）下载nginx1.13.7
>: wget http://nginx.org/download/nginx-1.13.7.tar.gz

3）解压安装包
>: tar -xf nginx-1.13.7.tar.gz

4）进入目标文件
>: cd nginx-1.13.7

5）配置安装路径：/usr/local/nginx
>: ./configure --prefix=/usr/local/nginx

6）编译并安装
>: make && sudo make install

7）建立软连接：终端命令 nginx
>: ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx

8）删除安装包与文件：
>: cd ~
>: rm -rf nginx-1.13.7
>: rm -rf nginx-1.13.7.tar.xz

9）测试Nginx环境，服务器运行nginx，本地访问服务器ip
>: nginx
>: 服务器绑定的域名 或 ip:80


#Nginx命令
1）启动
>: nginx

2）关闭nginx
>: nginx -s stop

3）重启nginx
>: nginx -s reload

4）查看端口，强行关闭
>: ps -aux|grep nginx
>: kill <pid:进程编号>
 

# 
	Nginx (engine x) 是一个高性能的HTTP和反向代理web服务器
	Apache和Nginx最核心的区别在于 apache 是同步多进程模型，一个连接对应一个进程；而 nginx 是异步的，多个连接（万级别）可以对应一个进程
  
   http请求转发
   反向代理服务器
   负载均衡
   动静分离


```

6 nginx 转发静态文件（前端项目）
--------------------------------

```
# 1 mv ~/dist /home/html
# 2 cd /usr/local/nginx/conf
# 3 vim nginx.conf
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    server {
        listen 80;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
            root /home/html; # html访问路径
            index index.html; # html文件名称
            try_files $uri $uri/ /index.html; # 解决单页面应用刷新404问题
        }
    }
}   

esc
:wq   # 保存并推出
  
# 重启nginx
nginx -s reload

# 前端项目就有了


```

7 云服务器转发动态请求（uwsgi+django 项目）
-------------------------------------------

```
# 1 mkdir /home/project
# 2 cd /home/project
# 3 git clone xxxx
# 4 安装虚拟环境，创建虚拟环境，安装项目依赖
pip install -r requirements.txt  （在指定的目录下）
# 5 pip install uwsgi （虚拟和真实环境都需要安装）
# 6 进行uwsgi服务配置，内容如下
vim /home/project/luffyapi/luffyapi.xml

<uwsgi>  
   <socket>127.0.0.1:8808</socket> <!-- 内部端口，自定义 --> 
   <chdir>/home/project/luffyapi/</chdir> <!-- 项目路径 -->  
   <module>luffyapi.wsgi</module>  <!-- luffyapi为wsgi.py所在目录名--> 
   <processes>4</processes> <!-- 进程数 -->   
   <daemonize>uwsgi.log</daemonize> <!-- 日志文件 -->
</uwsgi>

# 7 去向Nginx配置目录，备份配置，完全更新配置：填入下方内容
>: vim /usr/local/nginx/conf/nginx.conf

events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    server {
        listen 80;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
            root /home/html; # html访问路径
            index index.html; # html文件名称
            try_files $uri $uri/ /index.html; # 解决单页面应用刷新404问题
        }
    }
    # 新增的server
    server {
        listen 8000;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
           include uwsgi_params;
           uwsgi_pass 127.0.0.1:8808;  # 端口要和uwsgi里配置的一样
           uwsgi_param UWSGI_SCRIPT luffyapi.wsgi;  #wsgi.py所在的目录名+.wsgi
           uwsgi_param UWSGI_CHDIR /home/project/luffyapi/; # 项目路径
        }
    }
} 

  
#9 mysql的root用户，登录，创建表luffyapi，创建用户，授权
    1）管理员连接数据库
    >: mysql -uroot -p

    2）创建数据库
    >: create database luffyapi default charset=utf8;

    3）设置权限账号密码：账号密码要与项目中配置的一致
    >: grant all privileges on luffyapi.* to 'luffyapi'@'%' identified by 'Luffy123?';
    >: grant all privileges on luffyapi.* to 'luffyapi'@'localhost' identified by 'Luffy123?';
    >: flush privileges;

    4）退出mysql
    >: quit;
# 10 数据迁移创建超级用户
python manage_pro.py makemigraions
python manage_pro.py migrate
python manage_pro.py createsuperuser


#11 启动uwsgi和nginx（后端项目就可以了）
    1）启动uwsgi
    >: uwsgi -x /home/project/luffyapi/luffyapi.xml
    2）重启nginx
    >: nginx -s reload


```

补充
====

```
1 gitlab，zabbix（监控，php写），jekins（java写的，持续集成工具）,普罗尼修斯（go写的监控），docker，k8s，ansiable（python写的自动化运维工具），salstack（Python，自动化运维工具）
2 devops


```

### 购买服务器

```
# 购买阿里云服务器
# 短期或是测试使用，创建 按量收费 服务器，可以随时删除，删除后不再计费，但要保证账户余额100元以上


```

### 连接服务器

```
1）账号
>: ssh root@39.99.192.127

2）密码
>: ********


```

### 服务器命令

##### 管理员权限

```
1）以下所有的服务器命令均可以在管理员权限下执行
>: sudo 命令


```

##### 配置终端

```
1）编辑配置文件
>: vim ~/.bash_profile

2）将原来内容全部删除掉
>: ggdG

3）进入编辑状态：填入下方两行
>: i

export PATH=$PATH:$HOME/bin
PS1='Path:\w\n>:'

4）退出编辑状态
>: esc

5）保存修改并退出
>: :wq

6）生效配置
>: source ~/.bash_profile


```

重要
----

##### 更新系统软件包

```
>: yum update -y


```

##### 安装软件管理包和可能使用的依赖

```
>: yum -y groupinstall "Development tools"
>: yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel psmisc libffi-devel


```

##### 检测是否成功：会将 git 作为依赖安装号

```
>: git


```

### 安装 Mysql：Docker 安装了

```
1）前往用户根目录
>: cd ~

2）下载mysql57
>: wget http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm

也可以本地上传，这条命令要在本地终端上执行
>: scp -r C:\Users\dell\Desktop\pkg\mysql57-community-release-el7-10.noarch.rpm root@39.99.192.127:~

3）安装mysql57
>: yum -y install mysql57-community-release-el7-10.noarch.rpm
>: yum -y install mysql-community-server

4）启动mysql57并查看启动状态
>: systemctl start mysqld.service
>: systemctl status mysqld.service

5）查看默认密码并登录
>: grep "password" /var/log/mysqld.log
>: mysql -uroot -p

6）修改密码
>: ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';
>: ALTER USER 'root'@'localhost' IDENTIFIED BY 'Owen1234?';


```

### 安装 Redis：Docker 安装了

```
1）前往用户根目录
>: cd ~

2）下载redis-5.0.5
>: wget http://download.redis.io/releases/redis-5.0.5.tar.gz
>: scp -r C:\Users\dell\Desktop\pkg\redis-5.0.5.tar.gz root@39.99.192.127:~

3）解压安装包
>: tar -xf redis-5.0.5.tar.gz

4）进入目标文件
>: cd redis-5.0.5

5）编译环境
>: make

6）复制环境到指定路径完成安装
>: cp -r ~/redis-5.0.5 /usr/local/redis

7）配置redis可以后台启动：修改下方内容
>: vim /usr/local/redis/redis.conf

daemonize yes

8）完成配置修改
>: esc
>: :wq

9）建立软连接
>: ln -s /usr/local/redis/src/redis-server /usr/bin/redis-server
>: ln -s /usr/local/redis/src/redis-cli /usr/bin/redis-cli

10）后台运行redis
>: cd /usr/local/redis
>: redis-server ./redis.conf &

ctrl + c

11）测试redis环境
>: redis-cli
ctrl + c

12）关闭redis服务
>: pkill -f redis -9



```

### 安装 Python3.6

```
1）前往用户根目录
>: cd ~

2）下载 或 上传 Python3.6.7
# 服务器终端
>: wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz

# 本地终端，给服务器上传
>: scp -r 本地Python-3.6.7.tar.xz ssh root@39.99.192.127:服务器路径
>: scp -r C:\Users\dell\Desktop\pkg\Python-3.6.7.tar.xz ssh root@39.99.192.127~

3）解压安装包
>: tar -xf Python-3.6.7.tar.xz

4）进入目标文件
>: cd Python-3.6.7

5）配置安装路径：/usr/local/python3
>: ./configure --prefix=/usr/local/python3

6）编译并安装
>: make && sudo make install

7）建立软连接：终端命令 python3，pip3
>: ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
>: ln -s /usr/local/python3/bin/pip3.6 /usr/bin/pip3

8）删除安装包与文件：
>: rm -rf Python-3.6.7
>: rm -rf Python-3.6.7.tar.xz



```

### 配置 pip 源：阿里云不用配置，默认配置阿里源

```
1）创建pip配置路径
>: mkdir ~/.pip

2）进入目录编辑配置文件：填入下方内容
cd ~/.pip && vim pip.conf

[global]
index-url = http://pypi.douban.com/simple
[install]
use-mirrors =true
mirrors =http://pypi.douban.com/simple/
trusted-host =pypi.douban.com



```

### 安装 uwsgi

```
1）在真实环境下安装
pip3 install uwsgi

2）建立软连接
ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi



```

### 安装虚拟环境

```
1）安装依赖
>: pip3 install virtualenv
>: pip3 install virtualenvwrapper

2）建立虚拟环境软连接
>: ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv

3）配置虚拟环境：填入下方内容
>: vim ~/.bash_profile

VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/python3/bin/virtualenvwrapper.sh

4）退出编辑状态
>: esc

5）保存修改并退出
>: :wq

6）更新配置文件内容
>: source ~/.bash_profile

7）虚拟环境默认根目录：~/.virtualenvs



```

### 安装 Nginx

```
1）前往用户根目录
>: cd ~

2）下载nginx1.13.7
>: wget http://nginx.org/download/nginx-1.13.7.tar.gz

3）解压安装包
>: tar -xf nginx-1.13.7.tar.gz

4）进入目标文件
>: cd nginx-1.13.7

5）配置安装路径：/usr/local/nginx
>: ./configure --prefix=/usr/local/nginx

6）编译并安装
>: make && sudo make install

7）建立软连接：终端命令 nginx
>: ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx

8）删除安装包与文件：
>: cd ~
>: rm -rf nginx-1.13.7
>: rm -rf nginx-1.13.7.tar.xz

9）测试Nginx环境，服务器运行nginx，本地访问服务器ip
>: nginx
>: 服务器绑定的域名 或 ip:80



```

### Nginx 命令

```
1）启动
>: nginx

2）关闭nginx
>: nginx -s stop

3）重启nginx
>: nginx -s reload

4）查看端口，强行关闭
>: ps -aux|grep nginx
>: kill <pid:进程编号>



```

路飞项目部署：Nginx + uwsgi + django + vue
------------------------------------------

### 配置前台项目

#### 上线前配置

##### settings.js

```
base_url: 'http://39.99.192.127:8000',  // 真实环境：django项目就是跑在8000端口上的



```

#### 上线

```
"""
# 本地终端操作
1）本地项目打包，前往luffycity项目目录下
>: cnpm run build

2）本地终端上传
>: scp -r dist root@39.99.192.127:~

# 开始服务器连接，在服务器终端操作
3）移动并重命名
mv ~/dist /home/html

4）去向Nginx配置目录，备份配置，完全更新配置：填入下方内容
>: cd /usr/local/nginx/conf
>: mv nginx.conf nginx.conf.bak
>: vim nginx.conf
>: i

events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    server {
        listen 80;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
            root /home/html; # html访问路径
            index index.html; # html文件名称
            try_files $uri $uri/ /index.html; # 解决单页面应用刷新404问题
        }
    }
}   

5）退出
>: esc
>: :wq

6）重启nginx
>: nginx -s reload
"""



```

### 路飞后台部署

### 本地操作

#### 上线前配置

##### prod.py：上线的配置文件，内容拷贝 dev.py，前身就是 settings.py

```
# 关闭测试环境
DEBUG = False
ALLOWED_HOSTS = [
    '39.99.192.127'  # 公网ip地址
]

CORS_ORIGIN_ALLOW_ALL = True  # 允许所有跨域


# 静态文件配置：上线后还有额外配置，见下方 后台样式问题
STATIC_URL = '/static/'


# 后台http根路径
# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'http://39.99.192.127:8000'
# 前台http根路径
# LUFFY_URL = 'http://127.0.0.1:8080'
LUFFY_URL = 'http://39.99.192.127:80'
# 订单支付成功的后台异步回调接口
NOTIFY_URL = BASE_URL + '/order/success/'
# 订单支付成功的前台同步回调接口
RETURN_URL = LUFFY_URL + '/order/pay/success/'


REST_FRAMEWORK = {
    # 渲染模块
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # ...
}



```

##### wsgi.py 、manage_prod.py 该文件就是 manage.py 的一个副本)

```
# 需要做上线修改的内容
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.prod')



```

#### 导出项目环境

```
1）进入本地项目根目录
>: cd 项目根目录

2）本地导出项目环境
>: pip3 freeze > packages.txt

3）如果环境中有特殊的安装包，需要处理一下xadmin
packages.txt中的
	xadmin==2.0.1
要被替换为
	https://codeload.github.com/sshwsfc/xadmin/zip/django2



```

#### 项目提交到远程 git 仓库

```
1）去向本地项目仓库
>: cd 项目根目录

2）本地版本库操作
>: git status
>: git add .
>: git commit -m '项目2.0上线'

3）提交到远程版本库
>: git pull origin master
>: git push origin master



```

### 线上操作

#### git 同步上线项目

```
1）创建存放后台项目的目录
>: mkdir /home/project

2）进入后台项目管理目录同步git仓库中的项目
>: cd /home/project
>: git clone https://gitee.com/doctor_owen/luffyapi.git



```

#### 项目虚拟环境

```
1）创建线上luffy项目虚拟环境
>: mkvirtualenv luffy
>: workon luffy

2）安装所需环境，在packages.txt所在目录下安装执行packages.txt文件
>: pip install uwsgi
>: pip install -r /home/project/luffyapi/packages.txt



```

#### 完成 uwsgi 与 nginx 后台项目配置

```
"""
1）进行uwsgi服务配置，内容如下
>: vim /home/project/luffyapi/luffyapi.xml

<uwsgi>  
   <socket>127.0.0.1:8808</socket> <!-- 内部端口，自定义 --> 
   <chdir>/home/project/luffyapi/</chdir> <!-- 项目路径 -->  
   <module>luffyapi.wsgi</module>  <!-- luffyapi为wsgi.py所在目录名--> 
   <processes>4</processes> <!-- 进程数 -->   
   <daemonize>uwsgi.log</daemonize> <!-- 日志文件 -->
</uwsgi>

4）去向Nginx配置目录，备份配置，完全更新配置：填入下方内容
>: vim /usr/local/nginx/conf/nginx.conf

events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    server {
        listen 80;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
            root /home/html; # html访问路径
            index index.html; # html文件名称
            try_files $uri $uri/ /index.html; # 解决单页面应用刷新404问题
        }
    }
    # 新增的server
    server {
        listen 8000;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
           include uwsgi_params;
           uwsgi_pass 127.0.0.1:8808;  # 端口要和uwsgi里配置的一样
           uwsgi_param UWSGI_SCRIPT luffyapi.wsgi;  #wsgi.py所在的目录名+.wsgi
           uwsgi_param UWSGI_CHDIR /home/project/luffyapi/; # 项目路径
        }
    }
} 
"""



```

#### 数据库设置：docker 中操作

```
1）管理员连接数据库
>: mysql -uroot -pOwen1234?

2）创建数据库
>: create database luffyapi default charset=utf8;

3）设置权限账号密码：账号密码要与项目中配置的一致
>: grant all privileges on luffyapi.* to 'luffyapi'@'%' identified by 'Luffy123?';
>: grant all privileges on luffyapi.* to 'luffyapi'@'localhost' identified by 'Luffy123?';
>: flush privileges;

4）退出mysql
>: quit;



```

#### 完成项目的数据库迁移：Django 采用 2.0.7

```
# 必须在luffy环境下
1）数据库迁移
>: cd /home/project/luffyapi/
>: python manage_prod.py migrate

2）创建超级用户
>: python manage_prod.py createsuperuser
# 账号密码：admin|Admin123



```

#### 如何 Django 不是 2.0.7 的其他版本，数据库迁移保存解决方案：修改源码

```
1）修改base.py源码
>: vim /root/.virtualenvs/luffy/lib/python3.6/site-packages/django/db/backends/mysql/base.py

方案：36，37行注释掉

2）修改operations.py源码
>: vim /root/.virtualenvs/luffy/lib/python3.6/site-packages/django/db/backends/mysql/operations.py

方案：146行添加
	query = query.encode()



```

#### 启动 uwsgi，重启 nginx 测试

```
"""
1）启动uwsgi
>: uwsgi -x /home/project/luffyapi/luffyapi.xml

2）重启nginx
>: nginx -s reload
"""



```

#### 后台样式：admin、rest_framework、xadmin 等框架的静态样式也需要处理

##### 修改线上配置

```
1）编辑线上配置文件
>: vim /home/project/luffyapi/luffyapi/settings/prod.py


2）修改static配置，新增STATIC_ROOT、STATICFILES_DIRS
STATIC_URL = '/static/'
STATIC_ROOT = '/home/project/luffyapi/luffyapi/static'  
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

3）退出编辑
>: esc
>: :wq



```

##### 迁移静态样式：项目目录下

```
1）项目目录下没有 static 文件夹需要新建
>: mkdir /home/project/luffyapi/luffyapi/static

2）完成静态文件迁移
>: python /home/project/luffyapi/manage_prod.py collectstatic



```

##### Nginx 配置静态路径

```
1）修改nginx配置
>: vim /usr/local/nginx/conf/nginx.conf

events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    server {
        listen 80;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
            root /home/html; # html访问路径
            index index.html; # html文件名称
            try_files $uri $uri/ /index.html; # 解决单页面应用刷新404问题
        }
    }
    server {
        listen 8000;
        server_name  127.0.0.1; # 改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
           include uwsgi_params;
           uwsgi_pass 127.0.0.1:8808;  # 端口要和uwsgi里配置的一样
           uwsgi_param UWSGI_SCRIPT luffyapi.wsgi;  #wsgi.py所在的目录名+.wsgi
           uwsgi_param UWSGI_CHDIR /home/project/luffyapi/; # 项目路径
        }
        # 新增的配置静态文件
        location /static {
            alias /home/project/luffyapi/luffyapi/static;
        }
    }
}

2）退出
>: esc
>: :wq



```

##### 启动服务

```
1）关闭 uwsgi，重新启动 uwsgi
>: pkill -f uwsgi -9
>: uwsgi -x /home/project/luffyapi/luffyapi.xml

2）关闭 nginx，重新启动 nginx
>: nginx -s stop
>: nginx


```

线上项目测试
------------

```
1）本地浏览器访问xadmin后台
http://39.99.192.127:8000/xadmin

2）登录，录入测试数据
# 账号密码：admin|Admin123

3）或是导出本地数据库为sql，再在线上导入sql
>: mysql -h 39.99.192.127 -P 3306 -u luffy -p
>: Luffy123?
>: use luffy
>: 复制之前的数据备份


```

重点 重点 重点
--------------

```
# 1、真实环境和虚拟环境都要安装uwsgi，将真实环境下的uwsgi建立软连接

# 2、redis服务一定要后台启动：redis-server &

# 3、uwsgi启动django项目一定要进入虚拟环境下，因为环境都是安装在虚拟环境中

# 4、服务器的日志都会被记录在于uwsgi配置文件 luffyapi.xml 同类目下的 uwsgi.log 中


```
