#通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上
#1.这个独立文件名假设叫functions.py，在同级另一个文件中通过import functions即可引入里面的函数
      #缺点是，调用时要用functions.asdf来调用函数
#2.也可以通过from modulename import functionname 来引入函数
     #优点是不用.来调用函数，，缺点是要一个一个引入
#3.可以通过from modulename import *来引入所有函数
    #缺点是使用并非自己编写的大型模块时，建议不这样做，因为里面的函数名称可能与你自己编写的冲突

