# 代码生成时间: 2025-10-30 21:24:33
import pandas as pd

"""
关卡编辑器：用于创建和管理关卡数据的程序。
该程序允许用户添加、编辑和保存关卡信息。
"""

class LevelEditor:
    """
    关卡编辑器的主要类，负责处理关卡数据。
    """

    def __init__(self):
        """
        初始化关卡编辑器，创建一个空的关卡数据框架。
        """
        self.levels = pd.DataFrame(columns=['LevelID', 'LevelName', 'Difficulty', 'Description'])

    def add_level(self, level_id, level_name, difficulty, description):
        """
        添加一个新的关卡到数据框架中。

        :param level_id: 关卡的唯一标识符
        :param level_name: 关卡的名称
        :param difficulty: 关卡的难度级别
        :param description: 关卡的描述
        """
        new_level = {'LevelID': level_id, 'LevelName': level_name, 'Difficulty': difficulty, 'Description': description}
        self.levels = self.levels.append(new_level, ignore_index=True)
        print(f"关卡 '{level_name}' 已添加。")

    def edit_level(self, level_id, level_name=None, difficulty=None, description=None):
        """
        编辑现有的关卡信息。

        :param level_id: 关卡的唯一标识符
        :param level_name: 新的关卡名称（可选）
        :param difficulty: 新的难度级别（可选）
        :param description: 新的关卡描述（可选）
        """
        level_found = self.levels[self.levels['LevelID'] == level_id]
        if not level_found.empty:
            if level_name:
                level_found['LevelName'] = level_name
            if difficulty:
                level_found['Difficulty'] = difficulty
            if description:
                level_found['Description'] = description
            print(f"关卡 '{level_id}' 已更新。")
        else:
            print(f"未找到关卡 '{level_id}'。")

    def save_levels(self, file_path):
        """
        将关卡数据保存到CSV文件中。

        :param file_path: CSV文件的路径
        """
        try:
            self.levels.to_csv(file_path, index=False)
            print(f"关卡数据已保存到 '{file_path}'。")
        except Exception as e:
            print(f"保存关卡数据时发生错误：{e}")

    def load_levels(self, file_path):
        """
        从CSV文件中加载关卡数据。

        :param file_path: CSV文件的路径
        """
        try:
            self.levels = pd.read_csv(file_path)
            print(f"关卡数据已从 '{file_path}' 加载。")
        except Exception as e:
            print(f"加载关卡数据时发生错误：{e}")

# 示例用法
if __name__ == '__main__':
    editor = LevelEditor()
    editor.add_level('001', '初级关卡', '简单', '这是初级关卡的描述。')
    editor.add_level('002', '中级关卡', '中等', '这是中级关卡的描述。')
    editor.edit_level('001', level_name='新手关卡')
    editor.save_levels('levels.csv')
    editor.load_levels('levels.csv')
