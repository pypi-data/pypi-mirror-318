import os
import pytest
from click.testing import CliRunner
from cli.cli import cli

# 测试数据
TEST_DATA = {
    "app_id": os.getenv("app_id"),
    "app_secret": os.getenv("app_secret"),
    "app_token": os.getenv("app_token"),
    "space_name": "ChatFlow",
    "project_name": "xxxx2",
    "node_title": "需求文档"
}

@pytest.fixture
def runner():
    return CliRunner()

class TestCLI:
    """测试 OMT CLI 工具的所有命令"""

    def test_config_commands(self, runner):
        """测试配置相关命令"""
        # 测试完整形式
        result = runner.invoke(cli, [
            'config', 'set',
            '--app-id', TEST_DATA['app_id'],
            '--app-secret', TEST_DATA['app_secret'],
            '--app-token', TEST_DATA['app_token'],
            '--output-format', 'yaml'
        ])
        assert result.exit_code == 0
        assert "updated" in result.output

        # 测试简写形式
        result = runner.invoke(cli, [
            'config', 'set',
            '-i', TEST_DATA['app_id'],
            '-s', TEST_DATA['app_secret'],
            '-t', TEST_DATA['app_token'],
            '-o', 'yaml'
        ])
        assert result.exit_code == 0
        assert "updated" in result.output

        # 测试 config get
        result = runner.invoke(cli, ['config', 'get'])
        assert result.exit_code == 0
        assert TEST_DATA['app_id'] in result.output

        # 测试设置默认空间
        result = runner.invoke(cli, [
            'config', 'set',
            '--default-space', TEST_DATA['space_name']
        ])
        assert result.exit_code == 0
        assert "updated" in result.output

        # 测试简写形式
        result = runner.invoke(cli, [
            'config', 'set',
            '-d', TEST_DATA['space_name']
        ])
        assert result.exit_code == 0
        assert "updated" in result.output

    def test_space_commands(self, runner):
        """测试知识库相关命令"""
        # 测试 space list
        result = runner.invoke(cli, ['space', 'list'])
        assert result.exit_code == 0

        # 测试 space get
        result = runner.invoke(cli, ['space', 'get', TEST_DATA['space_name']])
        assert result.exit_code == 0

        # 测试 space nodes（完整形式）
        result = runner.invoke(cli, [
            'space', 'nodes',
            TEST_DATA['space_name'],
            '--parent-token', ''
        ])
        assert result.exit_code == 0

        # 测试 space nodes（简写形式）
        result = runner.invoke(cli, [
            'space', 'nodes',
            TEST_DATA['space_name'],
            '-p', ''
        ])
        assert result.exit_code == 0

        # 测试 space topology
        result = runner.invoke(cli, ['space', 'topology', TEST_DATA['space_name']])
        assert result.exit_code == 0

    def test_project_commands(self, runner):
        """测试项目相关命令"""

        # 测试 project init（带知识库，完整形式）
        with runner.isolated_filesystem():
            result = runner.invoke(cli, [
                'project', 'init',
                TEST_DATA['project_name'],
                '--space-name', TEST_DATA['space_name']
            ])
            assert result.exit_code == 0

        # 测试 project init（带知识库，简写形式）
        with runner.isolated_filesystem():
            result = runner.invoke(cli, [
                'project', 'init',
                TEST_DATA['project_name'],
                '-s', TEST_DATA['space_name']
            ])
            assert result.exit_code == 0

    def test_node_commands(self, runner):
        """测试节点相关命令"""
        # 测试 node info
        result = runner.invoke(cli, [
            'node', 'info',
            'doccnxxxxxxxxxxxx'  # 使用一个示例 obj_token
        ])
        assert result.exit_code == 0

        # 测试 node content（完整形式）
        result = runner.invoke(cli, [
            'node', 'content',
            'doccnxxxxxxxxxxxx',
            '--format', 'markdown'
        ])
        assert result.exit_code == 0

        # 测试 node content（简写形式）
        result = runner.invoke(cli, [
            'node', 'content',
            'doccnxxxxxxxxxxxx',
            '-f', 'markdown'
        ])
        assert result.exit_code == 0

        # 测试 node content raw 格式
        result = runner.invoke(cli, [
            'node', 'content',
            'doccnxxxxxxxxxxxx',
            '--format', 'raw'
        ])
        assert result.exit_code == 0

    # def test_completion_commands(self, runner):
    #     """测试命令补全相关命令"""
    #     # 测试 completion show
    #     result = runner.invoke(cli, ['completion', 'show'])
    #     assert result.exit_code == 0
    #     assert "_omt_completion" in result.output

    #     # 测试不同 shell 的补全脚本
    #     for shell in ['bash', 'zsh', 'fish']:
    #         result = runner.invoke(cli, ['completion', 'show', '--shell', shell])
    #         assert result.exit_code == 0

    def test_project_clone(self, runner):
        """测试项目克隆命令"""
        # 测试完整形式
        with runner.isolated_filesystem():
            result = runner.invoke(cli, [
                'project', 'clone',
                TEST_DATA['project_name'],
                '--space-name', TEST_DATA['space_name']
            ])
            assert result.exit_code == 0
            assert os.path.exists('dev-docs')
            assert os.path.exists('dev-docs/.env')

        # 测试简写形式
        with runner.isolated_filesystem():
            result = runner.invoke(cli, [
                'project', 'clone',
                TEST_DATA['project_name'],
                '-s', TEST_DATA['space_name']
            ])
            assert result.exit_code == 0
            assert os.path.exists('dev-docs')
            assert os.path.exists('dev-docs/.env')

        # 测试强制覆盖
        with runner.isolated_filesystem():
            # 先创建一些已存在的文件
            os.makedirs('dev-docs/需求文档', exist_ok=True)
            with open('dev-docs/需求文档/需求规格说明书.md', 'w') as f:
                f.write('old content')
            
            result = runner.invoke(cli, [
                'project', 'clone',
                TEST_DATA['project_name'],
                '-s', TEST_DATA['space_name'],
                '-f'
            ])
            assert result.exit_code == 0
            assert os.path.exists('dev-docs/需求文档/需求规格说明书.md')
            with open('dev-docs/需求文档/需求规格说明书.md') as f:
                content = f.read()
                assert content != 'old content'

    def test_project_commands_with_default_space(self, runner):
        """测试使用默认空间的项目命令"""
        # 先设置默认空间
        runner.invoke(cli, ['config', 'set', '-d', TEST_DATA['space_name']])

        # 测试不指定空间名称的 project init
        with runner.isolated_filesystem():
            result = runner.invoke(cli, [
                'project', 'init',
                TEST_DATA['project_name']
            ])
            assert result.exit_code == 0
            assert "Using default space" in result.output

        # 测试不指定空间名称的 project clone
        with runner.isolated_filesystem():
            result = runner.invoke(cli, [
                'project', 'clone',
                TEST_DATA['project_name']
            ])
            assert result.exit_code == 0
            assert "Using default space" in result.output

def test_help_commands(runner):
    """测试所有命令的帮助信息"""
    # 测试主命令帮助
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert "Usage:" in result.output

    # 测试所有子命令帮助
    commands = ['config', 'project', 'space', 'completion']
    for cmd in commands:
        result = runner.invoke(cli, [cmd, '--help'])
        assert result.exit_code == 0
        assert "Usage:" in result.output

if __name__ == '__main__':
    pytest.main(['-v', 'test_cli.py']) 