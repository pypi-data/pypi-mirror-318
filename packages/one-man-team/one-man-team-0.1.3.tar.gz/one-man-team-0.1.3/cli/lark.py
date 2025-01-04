# -*- coding: utf-8 -*-
# flake8: noqa: E501
import lark_oapi as lark
from lark_oapi.api.drive.v1 import *
from lark_oapi.api.wiki.v2 import *
from lark_oapi.api.docs.v1 import *
from lark_oapi.api.docx.v1 import *
import json
import os
import time
from dotenv import load_dotenv
import yaml
from typing import Optional, List, Dict, Union, Any

load_dotenv()

class LarkAPI:
    def __init__(self, app_id: str, app_secret: str, app_token: Optional[str] = None) -> None:
        self.client = lark.Client.builder().app_id(app_id)\
            .app_secret(app_secret)\
            .log_level(lark.LogLevel.INFO).build()
        if app_token:
            self.set_app_token(app_token)
        self.yaml = yaml
    
    def set_app_token(self, app_token: str) -> None:
        self.app_token = app_token

    # 获取表格ID
    def get_table_id(self, name: str) -> str:
        request = lark.BaseRequest.builder() \
            .http_method(lark.HttpMethod.GET) \
            .uri(f"/open-apis/bitable/v1/apps/{self.app_token}/tables") \
            .token_types({lark.AccessTokenType.TENANT}) \
            .build()
        response = self.client.request(request)
        if not response.success():
            lark.logger.error(
                f"client.request failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
            return ''
        tables = json.loads(response.raw.content)['data']['items']
        for table in tables:
            if table['name'] == name:
                return table['table_id']
        return ''

    # 添加记录
    def add_record(self, table_id: str, fields: Dict[str, Any]) -> Any:
        body = {
            "fields": fields
        }
        request = lark.BaseRequest.builder() \
            .http_method(lark.HttpMethod.POST) \
            .uri(f"/open-apis/bitable/v1/apps/{self.app_token}/tables/{table_id}/records") \
            .token_types({lark.AccessTokenType.TENANT}) \
            .body(body) \
            .build()
        response = self.client.request(request)
        if not response.success():
            lark.logger.error(
                f"client.request failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        # lark.logger.info(str(response.raw.content, lark.UTF_8))
        return response

    # 批量添加记录
    def  batch_add_records(self, table_id: str, records: List[Dict[str, Any]]) -> Any:
        new_records = []
        for record in records:
            new_records.append({
                "fields": record
            })
        body = {
            "records": new_records
        }
        request = lark.BaseRequest.builder() \
            .http_method(lark.HttpMethod.POST) \
            .uri(f"/open-apis/bitable/v1/apps/{self.app_token}/tables/{table_id}/records/batch_create") \
            .token_types({lark.AccessTokenType.TENANT}) \
            .body(body) \
            .build()
        response = self.client.request(request)
        if not response.success():
            lark.logger.error(
                f"client.request failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        # lark.logger.info(str(response.raw.content, lark.UTF_8))
        return response

    # 获取记录
    def get_records(self, table_id, page_token=None):
        query = {"page_size": "500"}
        if page_token:
            query['page_token'] = page_token
            # query = {"page_token": page_token}
        print('query:', query)
        request = lark.BaseRequest.builder() \
            .http_method(lark.HttpMethod.POST) \
            .uri(f"/open-apis/bitable/v1/apps/{self.app_token}/tables/{table_id}/records/search") \
            .token_types({lark.AccessTokenType.TENANT}) \
            .queries(query) \
            .body({}) \
            .build()
        response = self.client.request(request)
        print('get_records response has_more:', json.loads(response.raw.content)['data']['has_more'])
        # print('get_records response page_token:', json.loads(response.raw.content)['data']['page_token'])
        print('get_records response:', len(json.loads(response.raw.content)['data']['items']))
        if not response.success():
            lark.logger.error(
                f"client.request failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        # lark.logger.info(str(response.raw.content, lark.UTF_8))
        return response
    
    # 获取所有记录
    def get_records_all(self, table_id):
        page_token_all = []

        response_all = []
        response = self.get_records(table_id)
        # print('get_records_all response:', response)
        if not response.success():
            lark.logger.error(
                f"client.request failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        # lark.logger.info(str(response.raw.content, lark.UTF_8))

        response_all.append(json.loads(response.raw.content)['data']['items'])

        has_more = json.loads(response.raw.content)['data']['has_more']

        if has_more:
            page_token = json.loads(response.raw.content)['data']['page_token']

            while has_more and page_token not in page_token_all:
                response_next = self.get_records(table_id, page_token)
                page_token_all.append(page_token)
                if not response_next.success():
                    lark.logger.error(
                        f"client.request failed, code: {response_next.code}, msg: {response_next.msg}, log_id: {response_next.get_log_id()}")
                has_more = json.loads(response_next.raw.content)['data']['has_more']
                time.sleep(0.2)
                if has_more:
                    page_token = json.loads(response_next.raw.content)['data']['page_token']
                
                response_all.append(json.loads(response_next.raw.content)['data']['items'])

        all_records = []  
        for all_records_raw in response_all:
            for record in all_records_raw:
                fields = {}
                # fields['_id'] = record['record_id']
                fields_raw = record['fields']
                for field in fields_raw:
                    # print('field:', field)
                    # fields_raw[field]的数据类型
                    field_type = type(fields_raw[field])
                    # print('field_type:', field_type)

                    is_text = True if (field_type == list and 'type' in fields_raw[field][0]) else False
                    is_dict = True if field_type == dict else False
                    if is_text:
                        fields[field] = fields_raw[field][0]['text']
                    elif is_dict and 'type' in fields_raw[field]:
                        pass
                    else:
                        fields[field] = fields_raw[field]
                record['fields'] = fields
                all_records.append(record)
        # print('all_records:', all_records)
        return all_records
    
    # 批量更新记录
    def batch_update_records(self, table_id: str, records: List[Dict[str, Any]]) -> Any:

        if 'record_id' not in records[0]:
            new_records = []
            for record in records:
                record_id = record['_id']
                del record['_id']
                new_records.append({
                    "record_id": record_id,
                    "fields": record
                })
            records = new_records
        body = {
            "records": records
        }
        request = lark.BaseRequest.builder() \
            .http_method(lark.HttpMethod.POST) \
            .uri(f"/open-apis/bitable/v1/apps/{self.app_token}/tables/{table_id}/records/batch_update") \
            .token_types({lark.AccessTokenType.TENANT}) \
            .body(body) \
            .build()
        response = self.client.request(request)
        if not response.success():
            lark.logger.error(
                f"client.request failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        # lark.logger.info(str(response.raw.content, lark.UTF_8))
        return response

    # 获取文件夹中的文件清单
    def list_files_in_folder(self, folder_token: str, page_size: int = 50, 
                            order_by: str = "EditedTime", 
                            direction: str = "DESC") -> Optional[List[Dict[str, Any]]]:
        request = ListFileRequest.builder() \
            .page_size(page_size) \
            .folder_token(folder_token) \
            .order_by(order_by) \
            .direction(direction) \
            .user_id_type("open_id") \
            .build()

        response = self.client.drive.v1.file.list(request)
        if not response.success():
            lark.logger.error(
                f"client.drive.v1.file.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
            return None

        files = self.expando_to_dict(response.data.files)
        return files

    # 创建文件夹
    def create_folder(self, folder_name: str, folder_token: str) -> Optional[Any]:
        request = CreateFolderFileRequest.builder() \
            .request_body(CreateFolderFileRequestBody.builder() \
                .name(folder_name) \
                .folder_token(folder_token) \
                .build()) \
            .build()
        response = self.client.drive.v1.file.create_folder(request)
        if not response.success():
            lark.logger.error(
                f"client.drive.v1.file.create_folder failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
            return None
        return response
    
    # 创建云文档
    def create_doc(self, folder_token: str, doc_name: str) -> Any:
        request = CreateDocumentRequest.builder() \
            .request_body(CreateDocumentRequestBody.builder() \
                .folder_token(folder_token) \
                .title(doc_name) \
                .build()) \
            .build()
        response = self.client.docx.v1.document.create(request)
        return response 

    # 获取知识库列表
    def list_spaces(self, page_size: int = 50, lang: str = "zh") -> Optional[List[Dict[str, Any]]]:
        request = ListSpaceRequest.builder() \
            .page_size(page_size) \
            .lang(lang) \
            .build()

        response = self.client.wiki.v2.space.list(request)
        if not response.success():
            lark.logger.error(
                f"client.wiki.v2.space.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
            return None

        spaces = self.expando_to_dict(response.data.items)
        return spaces
    
    # 通过知识库名称获取知识库信息
    def find_space(self, spaces: List[Dict[str, Any]], space_name: str) -> Optional[Dict[str, Any]]:
        return next((space for space in spaces if space['name'] == space_name), None)

    # 获取知识空间节点信息
    def get_node_info(self, obj_token: str) -> Optional[Dict[str, Any]]:
        # 构造请求对象
        request: GetNodeSpaceRequest = GetNodeSpaceRequest.builder() \
            .token(obj_token) \
            .obj_type("docx") \
            .build()

        # 发起请求
        response = self.client.wiki.v2.space.get_node(request)
        if not response.success():
            lark.logger.error(
                f"client.wiki.v2.space.get_node failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
            return None
        node_info = self.expando_to_dict(response.data)
        return node_info
        
    # 获取知识空间子节点列表
    def list_space_children(self, space_id: str, page_token: str = '', 
                           parent_node_token: str = '') -> Optional[List[Dict[str, Any]]]:
        request = ListSpaceNodeRequest.builder() \
            .space_id(space_id) \
            .page_size(50) \
            .page_token(page_token) \
            .parent_node_token(parent_node_token) \
            .build()

        response = self.client.wiki.v2.space_node.list(request)
        if not response.success():
            lark.logger.error(
                f"client.wiki.v2.space_node.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
            return None
        nodes = self.expando_to_dict(response.data.items)
        return nodes
    
    # 通过知识空间节点名称获取知识空间节点信息
    def find_space_node(self, nodes: List[Dict[str, Any]], 
                        node_name: str) -> Optional[Dict[str, Any]]:
        return next((node for node in nodes if node['title'] == node_name), None)
    
    # 获取知识空间节点拓扑
    def get_node_topology(self, space_id: str, 
                         parent_node_token: str = '') -> List[Dict[str, Any]]:
        nodes = self.list_space_children(space_id, parent_node_token=parent_node_token)
        if not nodes:  # 如果返回None或空列表，直接返回空列表
            return []
            
        # print('nodes:', nodes)
        for node in nodes:
            if node['has_child']:  # 修复语法错误
                node['children'] = self.get_node_topology(space_id, node['node_token'])
            time.sleep(0.5)
        return nodes

    # 获取云文档内容
    def get_doc_content(self, obj_token: str, doc_type: str = "docx", 
                       content_type: str = "markdown", 
                       lang: str = "zh") -> Optional[Dict[str, Any]]:
        request = GetContentRequest.builder() \
            .doc_token(obj_token) \
            .doc_type(doc_type) \
            .content_type(content_type) \
            .lang(lang) \
            .build()

        response = self.client.docs.v1.content.get(request)
        if not response.success():
            lark.logger.error(
                f"client.docs.v1.content.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
            return None

        content = self.expando_to_dict(response.data)
        return content
    
    # 获取文档纯文本内容
    def get_doc_raw_content(self, doc_token: str) -> Optional[Dict[str, Any]]:
        request = RawContentDocumentRequest.builder() \
            .document_id(doc_token) \
            .lang(0) \
            .build()
        response = self.client.docx.v1.document.raw_content(request)
        content = self.expando_to_dict(response.data)
        return content
    
    # 创建知识空间节点
    def create_space_node(self, space_id: str, node_type: str, title: str,
                         obj_type: str = "docx", 
                         parent_node_token: Optional[str] = None) -> Optional[Dict[str, Any]]:
        request = CreateSpaceNodeRequest.builder() \
            .space_id(space_id) \
            .request_body(Node.builder() \
                .obj_type(obj_type) \
                .node_type(node_type) \
                .parent_node_token(parent_node_token) \
                .title(title) \
                .build()) \
            .build()
        response = self.client.wiki.v2.space_node.create(request)
        if not response.success():
            lark.logger.error(
                f"client.wiki.v2.space_node.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
            return None
        node_info = self.expando_to_dict(response.data)
        return node_info

    # 将expando对象转换为dict
    def expando_to_dict(self, obj: Any) -> Union[Dict[str, Any], List[Any], Any]:
        if isinstance(obj, dict):
            return {k: self.expando_to_dict(v) for k, v in obj.items()}
        elif hasattr(obj, '__dict__'):
            return {k: self.expando_to_dict(v) for k, v in obj.__dict__.items()}
        elif isinstance(obj, list):
            return [self.expando_to_dict(item) for item in obj]
        else:
            return obj

    # 创建知识库
    def create_space(self, name: str) -> Optional[Dict[str, Any]]:
        """Create a new space"""
        request = CreateSpaceRequest.builder() \
            .request_body(Space.builder() \
                .name(name) \
                .build()) \
            .build()
        
        response = self.client.wiki.v2.space.create(request)
        if not response.success():
            lark.logger.error(
                f"client.wiki.v2.space.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
            return None
        
        return self.expando_to_dict(response.data)

    # 初始化项目知识库结构
    def init_project_space(self, space_name: str, project_name: str) -> Optional[Dict[str, Any]]:
        """Initialize project space structure"""
        # 1. 检查知识库是否存在
        spaces = self.list_spaces()
        space = self.find_space(spaces, space_name)
        if not space:
            return {
                "message": f"Space '{space_name}' not found. Please create it first."
            }
        
        space_id = space['space_id']
        
        # 2. 检查项目节点是否已存在
        nodes = self.list_space_children(space_id)
        if nodes:
            existing_node = self.find_space_node(nodes, project_name)
            if existing_node:
                return {
                    "space": space,
                    "message": f"Project '{project_name}' already exists in space '{space_name}'"
                }
        
        # 3. 创建项目根节点
        root_node = self.create_space_node(space_id, "origin", project_name)
        if not root_node:
            return None
        
        root_node_token = root_node['node']['node_token']
        
        # 4. 创建标准项目结构
        nodes = []
        files_template = {
            "需求文档": ['需求规格说明书'],
            "原型文档": [],
            "接口文档": ['资源池API文档', '分布式训练任务API文档'],
            "设计文档": [],
        }
        
        # 创建文件夹和文档
        for folder_name, file_names in files_template.items():
            folder_node = self.create_space_node(
                space_id=space_id,
                node_type="origin",
                title=folder_name,
                parent_node_token=root_node_token
            )
            if folder_node:
                nodes.append(folder_node)
                folder_token = folder_node['node']['node_token']
                
                for file_name in file_names:
                    doc_node = self.create_space_node(
                        space_id=space_id,
                        node_type="origin",
                        title=file_name,
                        parent_node_token=folder_token
                    )
                    if doc_node:
                        nodes.append(doc_node)
                    time.sleep(0.5)
                
                time.sleep(0.5)
        
        # 5. 获取完整的节点拓扑结构
        topology = self.get_node_topology(space_id, root_node_token)
        
        return {
            "space": space,
            "root_node": root_node,
            "nodes": nodes,
            "topology": topology
        }

# 使用示例
if __name__ == "__main__":
    app_id = os.getenv("app_id")
    app_secret = os.getenv("app_secret")
    app_token = os.getenv("app_token")
    api = LarkAPI(app_id, app_secret, app_token)
    
    # 获取知识库列表
    spaces = api.list_spaces()
    if spaces:
        space_id = spaces[0]['space_id']
        # 获取知识库的节点拓扑结构
        topology = api.get_node_topology(space_id)
        print(json.dumps(topology, indent=2, ensure_ascii=False))
