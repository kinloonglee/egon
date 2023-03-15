
from rest_framework import serializers



class BookSerializer(serializers.Serializer):
    # book.publish
    # book.price
    # book.xxx--->book.title
    # book.authors.all

    xxx=serializers.CharField(source='title')
    price=serializers.CharField()
    pub_date=serializers.CharField(source='test')
    publish=serializers.CharField(source='publish.email')
    # book.publish.email  相当于
    # authors=serializers.CharField()
    authors=serializers.SerializerMethodField() #它需要有个配套方法，方法名叫get_字段名，返回值就是要显示的东西
    def get_authors(self,instance):
        # book对象
        authors=instance.authors.all()  # 取出所有作者
        ll=[]
        for author in authors:
            ll.append({'name':author.name,'age':author.age})
        return ll





