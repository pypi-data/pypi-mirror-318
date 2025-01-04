import json

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *
from lark_oapi.api.wiki.v2 import *
from lark_oapi.api.docs.v1 import *
from lark_oapi.api.docx.v1 import *
from tabulate import tabulate
import time
from cli.lark import LarkAPI
import yaml

# 引入环境变量
from dotenv import load_dotenv
load_dotenv()
import os

app_id = os.getenv("app_id")
app_secret = os.getenv("app_secret")
app_token = os.getenv("app_token")

lark_api = LarkAPI(app_id, app_secret)

files_template = {
    "需求文档": ['xxx需求说明书'],
    "原型文档": [],
    "接口文档": ['xxxAPI文档', 'xxx2API文档'],
    "设计文档": []
}

def init_project(space_id, root_node_token):
    for file_type, file_names in files_template.items():
        node_info = lark_api.create_space_node(space_id, "origin", file_type, parent_node_token=root_node_token)
        print(yaml.dump(node_info, allow_unicode=True))

        parent_node_token = node_info['node']['node_token']

        for file_name in file_names:
            lark.logger.debug('创建云文档:')
            node_info = lark_api.create_space_node(space_id, "origin", file_name, parent_node_token=parent_node_token)
            print(yaml.dump(node_info, allow_unicode=True))
            time.sleep(0.5)
    nodes = lark_api.get_node_topology(space_id, parent_node_token=root_node_token)
    return nodes

def main():
    lark.logger.debug('获取知识库列表:')
    # 构造请求对象
    spaces = lark_api.list_spaces()
    print(tabulate(spaces, headers="keys", tablefmt="plain"))

    # 选中名称为"xxx项目"的知识库
    space = next((space for space in spaces if space['name'] == 'ChatFlow'), None)
    print(yaml.dump(space, allow_unicode=True))

    space_id = space['space_id']

    lark.logger.debug('获取知识空间子节点列表:')
    nodes = lark_api.list_space_children(space_id)
    print(tabulate(nodes, headers="keys", tablefmt="plain"))

    node = lark_api.find_space_node(nodes, '需求文档')
    print(yaml.dump(node, allow_unicode=True))

    document_id = node['obj_token']

    lark.logger.debug('获取知识空间节点信息:')
    node_info = lark_api.get_node_info(document_id)
    print(yaml.dump(node_info, allow_unicode=True))

    lark.logger.debug('获取云文档内容:')
    content = lark_api.get_doc_content(document_id)
    print(yaml.dump(content, allow_unicode=True))

    # lark.logger.debug('获取文档纯文本内容:')
    # content = lark_api.get_doc_raw_content(document_id)
    # print(yaml.dump(content, allow_unicode=True))

    node_token = node_info['node']['node_token']
    lark.logger.debug('获取知识空间节点列表:')
    document_nodes = lark_api.list_space_children(space_id, parent_node_token=node_token)
    print(json.dumps(document_nodes, indent=2, ensure_ascii=False))

    # lark.logger.debug('初始化项目:')
    node_info = lark_api.create_space_node(space_id, "origin", "xxx项目")
    print(yaml.dump(node_info, allow_unicode=True))
    root_node_token = node_info['node']['node_token']
    nodes = init_project(space_id, root_node_token)
    print(json.dumps(nodes, indent=2, ensure_ascii=False))

    lark.logger.debug('获取知识空间节点拓扑:')
    all_nodes = lark_api.get_node_topology(space_id, parent_node_token='')
    print(json.dumps(all_nodes, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
