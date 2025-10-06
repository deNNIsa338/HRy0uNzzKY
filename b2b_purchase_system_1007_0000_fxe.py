# 代码生成时间: 2025-10-07 00:00:29
import pandas as pd
from datetime import datetime

"""
B2B采购系统

这个程序实现了一个简单的B2B采购系统，使用Pandas框架来处理数据。
包含了数据的读取、查询、插入和更新操作。
"""

# 数据文件路径
DATA_FILE = 'purchase_data.csv'

class B2BPurchaseSystem:
    """
    B2B采购系统类
    """
    def __init__(self):
        # 初始化时读取数据文件
        try:
            self.data = pd.read_csv(DATA_FILE)
        except FileNotFoundError:
            print(f"Error: 数据文件{DATA_FILE}不存在。")
            self.data = pd.DataFrame(columns=['SupplierID', 'ProductID', 'PurchaseDate', 'Quantity', 'Price'])

    def search_purchases(self, supplier_id=None, product_id=None):
        """
        根据供应商ID和产品ID查询采购记录
        """
        mask = pd.Series([True] * len(self.data), index=self.data.index)
        if supplier_id:
            mask &= self.data['SupplierID'] == supplier_id
        if product_id:
            mask &= self.data['ProductID'] == product_id
        return self.data.loc[mask]

    def add_purchase(self, supplier_id, product_id, purchase_date, quantity, price):
        """
        添加一条采购记录
        """
        new_record = pd.Series([supplier_id, product_id, purchase_date, quantity, price], 
                             index=['SupplierID', 'ProductID', 'PurchaseDate', 'Quantity', 'Price'])
        try:
            self.data = self.data.append(new_record, ignore_index=True)
            self.data.to_csv(DATA_FILE, index=False)
        except Exception as e:
            print(f"Error: 添加采购记录失败。{e}")

    def update_purchase(self, record_id, quantity=None, price=None):
        """
        更新一条采购记录
        """
        try:
            if quantity:
                self.data.loc[record_id, 'Quantity'] = quantity
            if price:
                self.data.loc[record_id, 'Price'] = price
            self.data.to_csv(DATA_FILE, index=False)
        except Exception as e:
            print(f"Error: 更新采购记录失败。{e}")

# 示例用法
if __name__ == '__main__':
    system = B2BPurchaseSystem()
    print("供应商1的所有采购记录：")
    print(system.search_purchases(supplier_id=1))
    print("
添加一条新的采购记录：")
    system.add_purchase(supplier_id=2, product_id=101, purchase_date=datetime.now().date(), quantity=100, price=10.5)
    print(system.search_purchases(supplier_id=2))
    print("
更新供应商2的第一条采购记录的价格：")
    system.update_purchase(record_id=0, price=11.0)
    print(system.search_purchases(supplier_id=2))
