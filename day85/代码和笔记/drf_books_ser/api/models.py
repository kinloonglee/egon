from django.db import models




from django.contrib.auth.models import AbstractUser
class BaseModel(models.Model):
    is_delete=models.BooleanField(default=False)
    # auto_now_add=True 只要记录创建，不需要手动插入时间，自动把当前时间插入
    create_time=models.DateTimeField(auto_now_add=True)
    # auto_now=True,只要更新，就会把当前时间插入
    last_update_time=models.DateTimeField(auto_now=True)
    # import datetime
    # create_time=models.DateTimeField(default=datetime.datetime.now)
    class Meta:
        # 单个字段，有索引，有唯一
        # 多个字段，有联合索引，联合唯一
        abstract=True  # 抽象表，不再数据库建立出表




class Book(BaseModel):
    id=models.AutoField(primary_key=True)
    # verbose_name admin中显示中文
    name=models.CharField(max_length=32,verbose_name='书名',help_text='这里填书名')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    # 一对多的关系一旦确立，关联字段写在多的一方
    #to_field 默认不写，关联到Publish主键
    #db_constraint=False  逻辑上的关联，实质上没有外键练习，增删不会受外键影响，但是orm查询不影响
    publish=models.ForeignKey(to='Publish',on_delete=models.DO_NOTHING,db_constraint=False)

    # 多对多，跟作者，关联字段写在 查询次数多的一方

    # 什么时候用自动，什么时候用手动？第三张表只有关联字段，用自动    第三张表有扩展字段，需要手动写
    # 不能写on_delete
    authors=models.ManyToManyField(to='Author',db_constraint=False)
    class Meta:
        verbose_name_plural='书表'  # admin中表名的显示

    def __str__(self):
        return self.name

    @property
    def publish_name(self):
        return self.publish.name
    # def author_list(self):
    def author_list(self):
        author_list=self.authors.all()
        # ll=[]
        # for author in author_list:
        #     ll.append({'name':author.name,'sex':author.get_sex_display()})
        # return ll
        return [ {'name':author.name,'sex':author.get_sex_display()}for author in author_list]

class Publish(BaseModel):
    name = models.CharField(max_length=32)
    addr=models.CharField(max_length=32)
    def __str__(self):
        return self.name


class Author(BaseModel):
    name=models.CharField(max_length=32)
    sex=models.IntegerField(choices=((1,'男'),(2,'女')))
    # 一对一关系，写在查询频率高的一方
    #OneToOneField本质就是ForeignKey+unique，自己手写也可以
    authordetail=models.OneToOneField(to='AuthorDetail',db_constraint=False,on_delete=models.CASCADE)

class AuthorDetail(BaseModel):
    mobile=models.CharField(max_length=11)

# 二、表断关联
# 1、表之间没有外键关联，但是有外键逻辑关联(有充当外键的字段)
# 2、断关联后不会影响数据库查询效率，但是会极大提高数据库增删改效率（不影响增删改查操作）
# 3、断关联一定要通过逻辑保证表之间数据的安全，不要出现脏数据，代码控制
# 4、断关联
# 5、级联关系
#       作者没了，详情也没：on_delete=models.CASCADE
#       出版社没了，书还是那个出版社出版：on_delete=models.DO_NOTHING
#       部门没了，员工没有部门(空不能)：null=True, on_delete=models.SET_NULL
#       部门没了，员工进入默认部门(默认值)：default=0, on_delete=models.SET_DEFAULT