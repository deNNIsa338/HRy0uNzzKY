# 代码生成时间: 2025-10-08 03:32:25
import pandas as pd

"""
代币经济模型程序

该程序旨在模拟和管理代币经济模型。
它包括代币的创建、分配和交易等功能。
"""

class TokenEconomyModel:
    """代币经济模型类"""
    def __init__(self, initial_supply):
        """初始化代币经济模型
        
        参数：
        initial_supply (int): 初始化代币供应量
        """
        self.tokens = pd.Series([initial_supply], index=['TotalSupply'])
        self.balances = pd.DataFrame(columns=['Address', 'Balance'])

    def create_token(self, amount):
        """创建新代币
        
        参数：
        amount (int): 要创建的代币数量
        """
        if amount < 0:
            raise ValueError("创建代币数量不能为负")
        
        self.tokens.loc['TotalSupply'] += amount
        self.tokens.loc['NewTokens'] = amount
        self.tokens.drop('NewTokens', inplace=True)
        print(f"成功创建{amount}个代币")

    def distribute_tokens(self, address, amount):
        """分配代币
        
        参数：
        address (str): 接收代币的地址
        amount (int): 要分配的代币数量
        """
        if amount < 0:
            raise ValueError("分配代币数量不能为负")
        
        self.balances = self.balances._append(
            {'Address': address, 'Balance': amount},
            ignore_index=True
        )
        self.tokens.loc['TotalSupply'] -= amount
        print(f"成功向地址{address}分配{amount}个代币")

    def transfer_tokens(self, from_address, to_address, amount):
        """代币转账
        
        参数：
        from_address (str): 转账发起地址
        to_address (str): 转账接收地址
        amount (int): 转账金额
        """
        if amount < 0:
            raise ValueError("转账金额不能为负")
        
        if self.balances.loc[self.balances['Address'] == from_address, 'Balance'].sum() < amount:
            raise ValueError("转账金额超过账户余额")
        
        self.balances.loc[self.balances['Address'] == from_address, 'Balance'] -= amount
        self.balances = self.balances._append(
            {'Address': to_address, 'Balance': amount},
            ignore_index=True
        )
        print(f"成功从地址{from_address}向地址{to_address}转账{amount}个代币")

    def show_token_supply(self):
        """显示代币供应量"""
        print(f"当前代币供应量：{self.tokens.loc['TotalSupply']}个")

    def show_balances(self):
        """显示账户余额"""
        print(self.balances)

# 示例用法
if __name__ == '__main__':
    model = TokenEconomyModel(1000)
    model.create_token(500)
    model.distribute_tokens('地址1', 100)
    model.distribute_tokens('地址2', 200)
    model.transfer_tokens('地址1', '地址3', 50)
    model.show_token_supply()
    model.show_balances()