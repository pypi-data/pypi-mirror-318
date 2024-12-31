from pytest_mongodb import plugin

class TestDemo:
    '''
    测试发送接口请求
    '''

    def test_demo1(self, data):
        # 生成请求管理对象
        print(data)