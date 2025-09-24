# 代码生成时间: 2025-09-24 09:05:16
import pandas as pd

"""
用户权限管理系统

该系统使用Pandas框架实现用户权限管理，包括添加、删除用户，
分配和撤销权限等功能。
"""

class UserPermissionManager:
    """用户权限管理类"""

    def __init__(self):
        # 初始化一个空的DataFrame来存储用户权限数据
        self.users = pd.DataFrame(columns=['username', 'permissions'])

    def add_user(self, username, permissions=None):
        """添加用户

        Args:
            username (str): 用户名
            permissions (list, optional): 用户权限. Defaults to None.
        """
        if username in self.users['username'].values:
            raise ValueError(f"用户 {username} 已存在")
        if permissions is None:
            permissions = []
        self.users = self.users.append(
            {'username': username, 'permissions': permissions},
            ignore_index=True
        )

    def delete_user(self, username):
        """删除用户

        Args:
            username (str): 用户名
        """
        if username not in self.users['username'].values:
            raise ValueError(f"用户 {username} 不存在")
        self.users = self.users[self.users['username'] != username]

    def assign_permission(self, username, permission):
        """分配权限

        Args:
            username (str): 用户名
            permission (str): 权限
        """
        if username not in self.users['username'].values:
            raise ValueError(f"用户 {username} 不存在")
        user_permissions = self.users.loc[
            self.users['username'] == username, 'permissions'].values[0]
        if permission in user_permissions:
            raise ValueError(f"用户 {username} 已拥有权限 {permission}")
        user_permissions.append(permission)
        self.users.loc[self.users['username'] == username, 'permissions'] = user_permissions

    def revoke_permission(self, username, permission):
        """撤销权限

        Args:
            username (str): 用户名
            permission (str): 权限
        """
        if username not in self.users['username'].values:
            raise ValueError(f"用户 {username} 不存在")
        user_permissions = self.users.loc[
            self.users['username'] == username, 'permissions'].values[0]
        if permission not in user_permissions:
            raise ValueError(f"用户 {username} 不拥有权限 {permission}")
        user_permissions.remove(permission)
        self.users.loc[self.users['username'] == username, 'permissions'] = user_permissions

    def get_user_permissions(self, username):
        """获取用户权限

        Args:
            username (str): 用户名

        Returns:
            list: 用户权限列表
        """
        if username not in self.users['username'].values:
            raise ValueError(f"用户 {username} 不存在")
        return self.users.loc[
            self.users['username'] == username, 'permissions'].values[0]

# 示例用法
if __name__ == '__main__':
    manager = UserPermissionManager()
    manager.add_user('alice')
    manager.assign_permission('alice', 'read')
    manager.assign_permission('alice', 'write')
    print(manager.get_user_permissions('alice'))  # 输出: ['read', 'write']
    manager.revoke_permission('alice', 'write')
    print(manager.get_user_permissions('alice'))  # 输出: ['read']
    manager.delete_user('alice')
