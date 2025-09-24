# 代码生成时间: 2025-09-24 15:14:46
import os
import zipfile
import tarfile
import gzip
from pathlib import Path

"""
文件解压工具

这个程序可以解压zip, tar, 和gzip格式的文件。
"""

class FileDecompressor:
    def __init__(self, archive_path):
        """
        初始化解压对象

        :param archive_path: 要解压的文件的路径
        """
        self.archive_path = Path(archive_path)

    def extract_zip(self):
        """
        解压zip文件

        :return: 解压后文件夹路径
        """
        if not self.archive_path.exists():
            raise FileNotFoundError(f"文件{self.archive_path}不存在")

        extract_to_path = self.archive_path.parent / self.archive_path.stem
        if extract_to_path.exists():
            raise FileExistsError(f"目标文件夹{extract_to_path}已存在")

        with zipfile.ZipFile(self.archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_path)

        return extract_to_path

    def extract_tar(self):
        """
        解压tar文件

        :return: 解压后文件夹路径
        """
        if not self.archive_path.exists():
            raise FileNotFoundError(f"文件{self.archive_path}不存在")

        extract_to_path = self.archive_path.parent / self.archive_path.stem
        if extract_to_path.exists():
            raise FileExistsError(f"目标文件夹{extract_to_path}已存在")

        with tarfile.TarFile(self.archive_path, 'r') as tar_ref:
            tar_ref.extractall(extract_to_path)

        return extract_to_path

    def extract_gzip(self):
        """
        解压gzip文件

        :return: 解压后文件路径
        """
        if not self.archive_path.exists():
            raise FileNotFoundError(f"文件{self.archive_path}不存在")

        extract_to_path = self.archive_path.parent / self.archive_path.stem
        with gzip.open(self.archive_path, 'rb') as file:
            with open(extract_to_path, 'wb') as out_file:
                out_file.write(file.read())

        return extract_to_path

    def decompress(self):
        """
        根据文件格式解压文件

        :return: 解压后文件或文件夹路径
        """
        if not self.archive_path.exists():
            raise FileNotFoundError(f"文件{self.archive_path}不存在")

        if self.archive_path.suffix == '.zip':
            return self.extract_zip()
        elif self.archive_path.suffix == '.tar' or self.archive_path.suffix == '.tar.gz':
            return self.extract_tar()
        elif self.archive_path.suffix == '.gz':
            return self.extract_gzip()
        else:
            raise ValueError(f"不支持的文件格式：{self.archive_path.suffix}")

# 示例用法
if __name__ == '__main__':
    archive_path = '/path/to/your/archive/file.zip'  # 替换为实际文件路径
    decompressor = FileDecompressor(archive_path)
    try:
        extracted_path = decompressor.decompress()
        print(f"文件已解压到：{extracted_path}")
    except Exception as e:
        print(f"解压失败：{str(e)}")