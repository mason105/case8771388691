from chalice import Chalice
from typing import List
import json
import requests


from chalicelib.cusclient import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models

app = Chalice(app_name='cloudmgr')
app.debug = True


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

@app.route('/')
def indexie():
        print("spot start")
        from Tea.core import TeaCore
        print("Tea.core")
        from chalicelib.cusclient import Client as Ecs20140526Client
        print("alibabacloud_ecs20140526.client")
        from alibabacloud_tea_openapi import models as open_api_models
        print("alibabacloud_tea_openapi")
        from chalicelib import alibabacloud_ecs20140526_models as ecs_20140526_models
        print("T alibabacloud_ecs20140526 models")
        from alibabacloud_tea_console.client import Client as ConsoleClient
        print("alibabacloud_tea_console")
        from alibabacloud_tea_util.client import Client as UtilClient
        print("alibabacloud_tea_util")
        print('123')
        access_key = app.current_request.query_params['access_key']
        security_key = app.current_request.query_params['security_key']
        access_key = app.current_request.query_params['access_key']
        security_key = app.current_request.query_params['security_key']

        client = Sample.create_client(access_key, security_key)
        describe_spot_price_history_request = ecs_20140526_models.DescribeSpotPriceHistoryRequest(
            region_id='ap-southeast-1',
            network_type='vpc',
            instance_type='ecs.n4.small'
        )
        
        # 复制代码运行请自行打印 API 的返回值
        str = client.describe_spot_price_history(describe_spot_price_history_request)
        print(type(str))
        print(str)

        return 'hello world'
'''
        app.log.debug("spot start")
        from Tea.core import TeaCore
        app.log.debug("Tea.core")
        from chalicelib.cusclient import Client as Ecs20140526Client
        app.log.debug("alibabacloud_ecs20140526.client")
        from alibabacloud_tea_openapi import models as open_api_models
        app.log.debug("alibabacloud_tea_openapi")
        from alibabacloud_ecs20140526 import models as ecs_20140526_models
        app.log.debug("T alibabacloud_ecs20140526 models")
        from alibabacloud_tea_console.client import Client as ConsoleClient
        app.log.debug("alibabacloud_tea_console")
        from alibabacloud_tea_util.client import Client as UtilClient
        app.log.debug("alibabacloud_tea_util")
        print('123')
        access_key = app.current_request.query_params['access_key']
        security_key = app.current_request.query_params['security_key']
        url='https://movie.douban.com/top250'
        res=requests.get(url) #requests模块会自动解码来自服务器的内容，可以使用res.encoding来查看编码
        html=res.text
        print(html)
        return json.dumps("ddd",default=lambda x: x.__dict__, sort_keys=True, indent=4)
 '''
@app.route('/spotprice')
def index():
        app.log.debug("spot start")
        from Tea.core import TeaCore
        app.log.debug("Tea.core")
        from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
        app.log.debug("alibabacloud_ecs20140526.client")
        from alibabacloud_tea_openapi import models as open_api_models
        app.log.debug("alibabacloud_tea_openapi")
        from alibabacloud_ecs20140526 import models as ecs_20140526_models
        app.log.debug("T alibabacloud_ecs20140526 models")
        from alibabacloud_tea_console.client import Client as ConsoleClient
        app.log.debug("alibabacloud_tea_console")
        from alibabacloud_tea_util.client import Client as UtilClient
        app.log.debug("alibabacloud_tea_util")
        print('123')
        access_key = app.current_request.query_params['access_key']
        security_key = app.current_request.query_params['security_key']
        url='https://movie.douban.com/top250'
        res=requests.get(url) #requests模块会自动解码来自服务器的内容，可以使用res.encoding来查看编码
        html=res.text
        print(html) 
        return json.dumps("ddd",default=lambda x: x.__dict__, sort_keys=True, indent=4)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
