

class MyResponse():
    def __init__(self):
        self.status=100
        self.msg='成功'
    @property
    def get_dict(self):
        return self.__dict__


if __name__ == '__main__':
    res=MyResponse()
    res.status=101
    res.msg='查询失败'
    # res.data={'name':'lqz'}
    print(res.get_dict)