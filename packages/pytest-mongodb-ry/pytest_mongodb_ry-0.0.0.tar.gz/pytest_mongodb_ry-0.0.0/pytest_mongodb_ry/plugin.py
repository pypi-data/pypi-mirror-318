import json
from typing import Optional, List, Dict
import pymongo


class MongoClient(object):
    _alive = {}

    def __new__(cls, url , *args, **kwargs):
        '''
        享元模式处理
        :param url:
        :param args:
        :param kwargs:
        '''
        if url in cls._alive.keys():
            return cls._alive.get(url)
        else:
            NewObject = object.__new__(cls)
            cls._alive.update({url: NewObject})
            return NewObject

    def __init__(self, url, Database):
        '''
        生成访问mongodb的实例
        :param url: mongodb的地址
        '''
        self.client = pymongo.MongoClient(f"mongodb://{url}")[Database]

    def insert(self, table, documents: Optional[List[Dict]]):
        '''
        新增数据至mongodb，返回对应新增的id值
        :param table:
        :param documents:
        :return:
        '''
        collection = self.client[table]
        x = collection.insert_many(documents)
        return x.inserted_ids

    def select(self, table, data: dict):
        '''
        从mongodb对应文档中查询数据查询对应数据
        :param table:文档名
        :param data:指定的查询条件
        :return:
        '''
        collection = self.client[table]
        result = collection.find(data)
        return result.to_list()


def pytest_addoption(parser):
    '''
    新增对应参数
    :param parser:
    :return:
    '''
    parser.addini(
        name="is_Mongodb",
        default="",
        help="是否开启对应mongodb开关"
    )
    parser.addini(
        name="MongoDb_url",
        default="",
        help="mongodb对应路径"
    )
    parser.addini(
        name="MgTable",
        default="",
        help="mongodb的库名"
    )
    parser.addini(
        name="Collection",
        default="",
        help="mongodb的Collection名"
    )
    parser.addini(
        name="MongoDb_SQL",
        default="",
        help="mongodb的查询SQL"
    )

    parser.addoption(
        "--is_Mongodb",
        default="",
        help="是否开启对应mongodb开关"
    )
    parser.addoption(
        "--MongoDb_url",
        default="",
        help="mongodb对应路径"
    )
    parser.addoption(
        "--MgTable",
        default="",
        help="mongodb的库名"
    )
    parser.addoption(
        "--Collection",
        default="",
        help="mongodb的Collection名"
    )
    parser.addoption(
        "--MongoDb_SQL",
        default="",
        help="mongodb的查询SQL"
    )


def pytest_generate_tests(metafunc):
    # 获取对应配置信息
    Config_dict = {
        "is_MongoDb": metafunc.config.inicfg.get("is_Mongodb") if not (metafunc.config.option.is_Mongodb) else (metafunc.config.option.is_Mongodb),
        "url": metafunc.config.inicfg.get("MongoDb_url") if not (metafunc.config.option.MongoDb_url) else (metafunc.config.option.MongoDb_url),
        "database": metafunc.config.inicfg.get("MgTable") if not (metafunc.config.option.MgTable) else (metafunc.config.option.MgTable),
        "collection": metafunc.config.inicfg.get("Collection") if not (metafunc.config.option.Collection) else (metafunc.config.option.Collection),
        "Sql_Path": metafunc.config.inicfg.get("MongoDb_SQL") if not (metafunc.config.option.MongoDb_SQL) else (metafunc.config.option.MongoDb_SQL)
    }
    if Config_dict['is_MongoDb'].upper() == "TRUE":
        # 获取项目对应路径
        rootdir = metafunc.config._parser.extra_info['rootdir']
        jsondir = rootdir+f"/{Config_dict["Sql_Path"]}"
        # 开启对应进程
        Client = MongoClient(Config_dict['url'], Config_dict['database'])
        with open(jsondir, encoding="utf-8") as f:
            SQL_data = json.loads(f.read())
        test_data = []
        for i in SQL_data['select']:
            test_data += Client.select(Config_dict["collection"], i)
        if "data" in metafunc.fixturenames:
            metafunc.parametrize("data", test_data)