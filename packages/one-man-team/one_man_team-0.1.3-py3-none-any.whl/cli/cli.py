import click
import os
from dotenv import load_dotenv, set_key
from cli.lark import LarkAPI
import json
from pathlib import Path
from cli.completion import completion
from tabulate import tabulate
import yaml
import shutil
import time

# 默认配置文件路径
DEFAULT_ENV_PATH = os.path.join(os.path.expanduser("~"), ".omt", ".env")

# 在文件开头添加
OUTPUT_FORMAT_KEY = "output_format"
DEFAULT_OUTPUT_FORMAT = "yaml"
DEFAULT_SPACE_KEY = "default_space"

def ensure_config_dir():
    """确保配置目录存在"""
    config_dir = os.path.dirname(DEFAULT_ENV_PATH)
    os.makedirs(config_dir, exist_ok=True)
    if not os.path.exists(DEFAULT_ENV_PATH):
        Path(DEFAULT_ENV_PATH).touch()

def load_config():
    """加载配置"""
    ensure_config_dir()
    load_dotenv(DEFAULT_ENV_PATH)

load_config()

# 创建 LarkAPI 实例
api = LarkAPI(
    app_id=os.getenv("app_id"),
    app_secret=os.getenv("app_secret"),
    app_token=os.getenv("app_token") if os.getenv("app_token") else None
)

def format_output(data, format=None):
    """Format output based on configuration"""
    if format is None:
        format = os.getenv(OUTPUT_FORMAT_KEY, DEFAULT_OUTPUT_FORMAT)
    
    if format.lower() == 'json':
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:  # yaml
        return yaml.dump(data, allow_unicode=True)

@click.group()
def cli():
    """One Man Team CLI tool"""
    pass

# Config 相关命令组
@cli.group()
def config():
    """Manage OMT configurations"""
    pass

@config.command("set")
@click.option('-i', '--app-id', help='Feishu/Lark App ID')
@click.option('-s', '--app-secret', help='Feishu/Lark App Secret')
@click.option('-t', '--app-token', help='Feishu/Lark App Token')
@click.option('-o', '--output-format', type=click.Choice(['yaml', 'json'], case_sensitive=False),
              help='Output format (yaml/json)')
@click.option('-d', '--default-space', help='Default space name')
def set_config(app_id, app_secret, app_token, output_format, default_space):
    """Set configuration values"""
    ensure_config_dir()
    
    if app_id:
        set_key(DEFAULT_ENV_PATH, "app_id", app_id)
        click.echo("App ID updated")
    
    if app_secret:
        set_key(DEFAULT_ENV_PATH, "app_secret", app_secret)
        click.echo("App Secret updated")
    
    if app_token:
        set_key(DEFAULT_ENV_PATH, "app_token", app_token)
        click.echo("App Token updated")
    
    if output_format:
        set_key(DEFAULT_ENV_PATH, OUTPUT_FORMAT_KEY, output_format.lower())
        click.echo("Output format updated")
    
    if default_space:
        set_key(DEFAULT_ENV_PATH, DEFAULT_SPACE_KEY, default_space)
        click.echo("Default space updated")

@config.command("get")
def get_config():
    """Get current configuration"""
    config = {
        "app_id": os.getenv("app_id"),
        "app_secret": os.getenv("app_secret"),
        "app_token": os.getenv("app_token"),
        "output_format": os.getenv(OUTPUT_FORMAT_KEY, DEFAULT_OUTPUT_FORMAT),
        "default_space": os.getenv(DEFAULT_SPACE_KEY, "")
    }
    click.echo(format_output(config))

# Project 相关命令组
@cli.group()
def project():
    """Manage OMT projects"""
    pass

@project.command("init")
@click.argument('project-name')
@click.option('-s', '--space-name', help='Space name to initialize project in')
def init_project(project_name: str, space_name: str):
    """Initialize a new project"""
    doc_dir = 'dev-docs'    
    
    # 如果没有指定空间名称，使用默认空间
    if not space_name:
        space_name = os.getenv(DEFAULT_SPACE_KEY)
        if not space_name:
            click.echo("No space name specified and no default space configured")
            click.echo("Please specify a space name with --space-name or set a default space:")
            click.echo("  omt config set --default-space SPACE_NAME")
            return
        click.echo(f"Using default space: {space_name}")
    
    # 创建项目目录
    os.makedirs(doc_dir, exist_ok=True)
    
    # 创建项目级 .env 文件
    env_path = os.path.join(doc_dir, ".env")
    if not os.path.exists(env_path):
        with open(env_path, 'w') as f:
            f.write(f"PROJECT_NAME={project_name}\n")
        click.echo(f"Created project configuration file: {env_path}")
    
    # 如果指定了 space_name，在知识库中初始化项目
    if space_name:
        click.echo(f"Initializing project in space '{space_name}'...")
        result = api.init_project_space(space_name, project_name)
        
        if not result:
            click.echo("❌ Failed to initialize project space")
            return
        
        if "message" in result:
            if "not found" in result["message"]:
                click.echo(f"❌ {result['message']}")
                click.echo("\nTip: Use the following commands to manage spaces:")
                click.echo("  omt space list                # List all spaces")
                click.echo("  omt space create SPACE_NAME   # Create a new space")
            else:
                click.echo(f"⚠️  {result['message']}")
            return
        
        click.echo("✅ Project space structure created successfully:")
        click.echo(f"\n📁 Space: {result['space']['name']}")
        click.echo(f"🔑 Space ID: {result['space']['space_id']}")
        click.echo(f"\n📂 Root Node: {result['root_node']['node']['title']}")
        
        # 显示文档结构
        click.echo("\n📑 Created document structure:")
        def print_node(node, level=0):
            prefix = "  " * level
            icon = "📁" if node.get('has_child') else "📄"
            click.echo(f"{prefix}{icon} {node['title']}")
            if node.get('children'):
                for child in node['children']:
                    print_node(child, level + 1)
        
        for node in result['topology']:
            print_node(node)
    
    click.echo(f"\n✨ Project '{project_name}' initialized successfully")

@project.command("clone")
@click.argument('project-name')
@click.option('-s', '--space-name', help='Space name to clone project from')
@click.option('-f', '--force', is_flag=True, help='Force overwrite existing files')
def clone_project(project_name: str, space_name: str, force: bool):
    """Clone project from space to local directory"""
    doc_dir = 'dev-docs'
    
    # 如果没有指定空间名称，使用默认空间
    if not space_name:
        space_name = os.getenv(DEFAULT_SPACE_KEY)
        if not space_name:
            click.echo("No space name specified and no default space configured")
            click.echo("Please specify a space name with --space-name or set a default space:")
            click.echo("  omt config set --default-space SPACE_NAME")
            return
        click.echo(f"Using default space: {space_name}")
    
    # 1. 获取知识库信息
    spaces = api.list_spaces()
    if not spaces:
        click.echo("Failed to get spaces")
        return
    
    space = api.find_space(spaces, space_name)
    if not space:
        click.echo(f"Space '{space_name}' not found")
        return
    
    # 2. 获取项目根节点
    nodes = api.list_space_children(space['space_id'])
    if not nodes:
        click.echo("Failed to get nodes")
        return
    
    project_node = api.find_space_node(nodes, project_name)
    if not project_node:
        click.echo(f"Project '{project_name}' not found in space '{space_name}'")
        return
    
    # 3. 获取项目结构
    topology = api.get_node_topology(space['space_id'], project_node['node_token'])
    if not topology:
        click.echo("Failed to get project structure")
        return
    
    # 4. 创建本地目录结构并下载文档
    os.makedirs(doc_dir, exist_ok=True)
    
    # 创建项目级 .env 文件
    env_path = os.path.join(doc_dir, ".env")
    if not os.path.exists(env_path) or force:
        with open(env_path, 'w') as f:
            f.write(f"PROJECT_NAME={project_name}\n")
        click.echo(f"Created project configuration file: {env_path}")

    # 清空目录，删除除.env文件外的所有文件和目录
    for item in os.listdir(doc_dir):
        item_path = os.path.join(doc_dir, item)
        if item != '.env':
            try:
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                click.echo(f"⚠️  Failed to remove {item}: {str(e)}")
                return
    
    def process_node(node, current_path=''):
        """递归处理节点，创建目录和下载文档"""
        node_path = os.path.join(current_path, node['title'])
        full_path = os.path.join(doc_dir, node_path)
        
        if node.get('has_child'):
            # 创建目录
            os.makedirs(full_path, exist_ok=True)
            click.echo(f"📁 Created directory: {node_path}")
            
            # 处理子节点
            if node.get('children'):
                for child in node['children']:
                    process_node(child, node_path)
        else:
            # 下载文档
            content = api.get_doc_content(node['obj_token'])
            if content:
                with open(full_path + '.md', 'w', encoding='utf-8') as f:
                    f.write(content['content'])
                click.echo(f"📄 Downloaded document: {node_path}.md")
            else:
                click.echo(f"❌ Failed to download document: {node_path}")
    
    # 5. 开始下载
    click.echo(f"\n🚀 Cloning project '{project_name}' from space '{space_name}'...")
    # 第一层全部为目录，不需要判断是否有has_child，直接创建目录
    for node in topology:
        if node.get('has_child'):
            pass
        else:
            node['has_child'] = True
            node['children'] = []
        process_node(node)
    
    click.echo(f"\n✨ Project '{project_name}' cloned successfully to {doc_dir}/")

# Space 相关命令组
@cli.group()
def space():
    """Manage Feishu/Lark Spaces"""
    pass

@space.command("list")
@click.option('-p', '--page-size', default=10, help='Number of spaces per page')
@click.option('-l', '--lang', default="zh", help='Language (zh/en)')
def list_spaces(page_size: int, lang: str):
    """List all spaces"""
    spaces = api.list_spaces()
    if spaces:
        click.echo(tabulate(spaces, headers="keys", tablefmt="plain"))
    else:
        click.echo("No spaces found or error occurred")

def get_default_space_name() -> str:
    """获取默认空间名称，如果未设置则提示用户"""
    space_name = os.getenv(DEFAULT_SPACE_KEY)
    if not space_name:
        click.echo("No space name specified and no default space configured")
        click.echo("Please specify a space name or set a default space:")
        click.echo("  omt config set --default-space SPACE_NAME")
        return None
    click.echo(f"Using default space: {space_name}")
    return space_name

@space.command("get")
@click.argument('space-name', required=False)
def get_space(space_name: str):
    """Get space by name"""
    if not space_name:
        space_name = get_default_space_name()
        if not space_name:
            return

    spaces = api.list_spaces()
    if not spaces:
        click.echo("Failed to get spaces")
        return
    
    space = api.find_space(spaces, space_name)
    if space:
        click.echo(format_output(space))
    else:
        click.echo(f"Space '{space_name}' not found")

@space.command("nodes")
@click.argument('space-name', required=False)
@click.option('-p', '--parent-token', default='', help='Parent node token')
def list_nodes(space_name: str, parent_token: str):
    """List nodes in a space"""
    if not space_name:
        space_name = get_default_space_name()
        if not space_name:
            return

    spaces = api.list_spaces()
    if not spaces:
        click.echo("Failed to get spaces")
        return
    
    space = api.find_space(spaces, space_name)
    if not space:
        click.echo(f"Space '{space_name}' not found")
        return
    
    nodes = api.list_space_children(space['space_id'], parent_node_token=parent_token)
    if nodes:
        new_nodes = []
        for node in nodes:
            del node['space_id']
            del node['creator']
            del node['owner']
            del node['node_creator']
            del node['obj_create_time']
            del node['origin_space_id']
            del node['node_type']
            del node['origin_node_token']
            del node['node_create_time']
            node['obj_edit_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(node['obj_edit_time'])))
            new_nodes.append(node)
        click.echo(tabulate(nodes, headers="keys", tablefmt="plain"))
    else:
        click.echo("No nodes found or error occurred")

@space.command("topology")
@click.argument('space-name', required=False)
def get_topology(space_name: str):
    """Get space node topology"""
    if not space_name:
        space_name = get_default_space_name()
        if not space_name:
            return

    spaces = api.list_spaces()
    if not spaces:
        click.echo("Failed to get spaces")
        return
    
    space = api.find_space(spaces, space_name)
    if not space:
        click.echo(f"Space '{space_name}' not found")
        return
    
    topology = api.get_node_topology(space['space_id'])
    if topology:
        click.echo(format_output(topology))
    else:
        click.echo("Failed to get topology")

# @space.command("create")
# @click.argument('space-name')
# def create_space(space_name: str):
#     """Create a new space"""
#     result = api.create_space(space_name)
#     if result:
#         click.echo(json.dumps(result, indent=2, ensure_ascii=False))
#     else:
#         click.echo(f"Failed to create space '{space_name}'")

@space.command("create-node")
@click.argument('space-name', required=False)
@click.argument('node-title')
@click.option('-p', '--parent-token', help='Parent node token')
@click.option('-t', '--node-type', default="origin", help='Node type (default: origin)')
@click.option('-o', '--obj-type', default="docx", help='Object type (default: docx)')
def create_node(space_name: str, node_title: str, parent_token: str, node_type: str, obj_type: str):
    """Create a new node in space"""
    if not space_name:
        space_name = get_default_space_name()
        if not space_name:
            return

    spaces = api.list_spaces()
    if not spaces:
        click.echo("Failed to get spaces")
        return
    
    space = api.find_space(spaces, space_name)
    if not space:
        click.echo(f"Space '{space_name}' not found")
        return
    
    result = api.create_space_node(
        space_id=space['space_id'],
        node_type=node_type,
        title=node_title,
        obj_type=obj_type,
        parent_node_token=parent_token if parent_token else None
    )
    
    if result:
        click.echo(format_output(result))
    else:
        click.echo(f"Failed to create node '{node_title}'")

# Node 相关命令组
@cli.group()
def node():
    """Manage Feishu/Lark Nodes"""
    pass

@node.command("info")
@click.argument('obj-token')
def get_node(obj_token: str):
    """Get node info by obj_token"""
    node = api.get_node_info(obj_token)
    if not node:
        click.echo("Failed to get node")
        return
    
    if node:
        click.echo(format_output(node))
    else:
        click.echo(f"Node '{obj_token}' not found")

@node.command("content")
@click.argument('obj-token')
@click.option('-f', '--format', type=click.Choice(['markdown', 'raw']), default='markdown',
              help='Content format (default: markdown)')
def get_content(obj_token: str, format: str):
    """Get node content"""
    if format == 'markdown':
        content = api.get_doc_content(obj_token=obj_token)
    else:
        content = api.get_doc_raw_content([obj_token])
    
    if content:
        click.echo(format_output(content))
    else:
        click.echo("Failed to get content")

# 在现有的 cli 组中添加 completion 命令组
cli.add_command(completion)

# Completion 命令组
@completion.command()
@click.option('--shell', type=click.Choice(['bash', 'zsh', 'fish']), default='bash',
              help='Shell type for completion script')
def show(shell):
    """Show completion script"""
    # ...

@completion.command()
@click.option('--shell', type=click.Choice(['bash', 'zsh', 'fish']), default='bash',
              help='Shell type for completion script')
def install(shell):
    """Install completion script"""
    # ...

if __name__ == '__main__':
    cli()
