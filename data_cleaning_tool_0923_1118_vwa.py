# 代码生成时间: 2025-09-23 11:18:03
import pandas as pd
import numpy as np
from datetime import datetime

"""
数据清洗和预处理工具

该模块提供了数据清洗和预处理的功能，包括缺失值处理、异常值处理、数据标准化等。
"""

class DataCleaningTool:
    """数据清洗和预处理工具类"""

    def __init__(self, data):
        """初始化方法"""
        self.data = data
        self.original_data = data.copy()

    def handle_missing_values(self, method='mean'):
        """处理缺失值"""
        if method == 'mean':
            self.data = self.data.fillna(self.data.mean())
        elif method == 'median':
            self.data = self.data.fillna(self.data.median())
        elif method == 'mode':
            self.data = self.data.fillna(self.data.mode().iloc[0])
        else:
            raise ValueError('无效的方法')

    def handle_outliers(self, method='z-score', threshold=3):
# 扩展功能模块
        """处理异常值"""
        if method == 'z-score':
            z_scores = np.abs(self.data.sub(self.data.mean()).div(self.data.std()))
            self.data = self.data[(z_scores < threshold).all(axis=1)]
        elif method == 'iqr':
            Q1 = self.data.quantile(0.25)
            Q3 = self.data.quantile(0.75)
            IQR = Q3 - Q1
            self.data = self.data[~((self.data < (Q1 - 1.5 * IQR)) | (self.data > (Q3 + 1.5 * IQR))).any(axis=1)]
        else:
# 改进用户体验
            raise ValueError('无效的方法')
# 增强安全性

    def standardize_data(self):
        """数据标准化"""
        self.data = (self.data - self.data.mean()) / self.data.std()

    def restore_original_data(self):
        """恢复原始数据"""
        self.data = self.original_data.copy()

    def save_cleaned_data(self, filename):
        """保存清洗后的数据"""
        try:
            self.data.to_csv(filename, index=False)
            print('数据已保存到', filename)
        except Exception as e:
            print('保存数据时出错:', e)

    def load_data(self, filename):
# 优化算法效率
        """加载数据"""
        try:
            self.data = pd.read_csv(filename)
            print('数据已加载')
# 增强安全性
        except Exception as e:
            print('加载数据时出错:', e)

# 示例用法
if __name__ == '__main__':
# NOTE: 重要实现细节
    # 加载数据
# 增强安全性
    filename = 'data.csv'
# NOTE: 重要实现细节
    cleaning_tool = DataCleaningTool(pd.read_csv(filename))

    # 处理缺失值
# 添加错误处理
    cleaning_tool.handle_missing_values(method='mean')

    # 处理异常值
    cleaning_tool.handle_outliers(method='z-score', threshold=3)

    # 数据标准化
    cleaning_tool.standardize_data()

    # 保存清洗后的数据
    cleaned_filename = 'cleaned_data.csv'
    cleaning_tool.save_cleaned_data(cleaned_filename)
