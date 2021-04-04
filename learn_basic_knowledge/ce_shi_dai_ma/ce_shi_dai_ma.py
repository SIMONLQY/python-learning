import unittest

from name_function import get_formatted_name


### 这个测试的东西只能在命令行运行
# 1.模块unittest提供了代码测试工具
# 单元测试用于核实函数的某个方面没有问题
# 测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求
# 全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。

# 2.测试用例先导入模块unittest以及要测试的函数
# 再创建一个集成unittest.TestCase的类
# 并编写一系列方法对函数不同行为进行测试
# 3.自动运行test开头的方法
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_fist_last_name(self):
        """能够正确处理像Janis Joplin这样的名字"""
        fomatted_name = get_formatted_name('janis', 'joplin')
        print(fomatted_name)
        self.assertEqual(fomatted_name, 'Janis Joplin')


unittest.main()
