# -*- coding: utf-8 -*-
"""
Project Name: zyt_auto_tools
File Created: 2025.01.02
Author: ZhangYuetao
File Name: auto_update_ctime.py
Update: 2025.01.02
"""

import os
from datetime import datetime


def is_file_modified_today(file_path):
    """
    检查文件是否在今天被修改过。

    :param file_path: 文件路径
    :return: 如果文件在今天被修改过，返回 True；否则返回 False。
    """
    # 获取文件的最后修改时间
    mtime = os.path.getmtime(file_path)
    # 转换为日期对象
    mtime_date = datetime.fromtimestamp(mtime).date()
    # 获取今天的日期
    today_date = datetime.now().date()
    # 判断是否相同
    return mtime_date == today_date


def update_file_update_date(file_path):
    """
    更新文件中 `Update` 日期为今天的日期。

    :param file_path: 文件路径
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 检查文件开头是否符合要求
    if len(lines) >= 6 and lines[0].startswith("# -*- coding: utf-8 -*-") and lines[1].strip() == '"""':
        # 查找 `Update` 行
        for i, line in enumerate(lines):
            if line.strip().startswith("Update:"):
                # 更新 `Update` 日期为今天的日期
                today_date = datetime.now().strftime("%Y.%m.%d")
                lines[i] = f"Update: {today_date}\n"
                break

        # 将更新后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print(f"Updated: {file_path}")
    else:
        print(f"Skipped: {file_path} (不符合文件开头格式)")


def update_files_in_directory(directory):
    """
    遍历指定目录下的所有 `.py` 文件，并更新今天修改过的文件的 `Update` 日期。

    :param directory: 目录路径
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                # 检查文件是否在今天被修改过
                if is_file_modified_today(file_path):
                    update_file_update_date(file_path)
                else:
                    print(f"Skipped: {file_path} (今天未修改)")


def main():
    # 这里可以调用你的主逻辑
    target_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    update_files_in_directory(target_directory)


if __name__ == "__main__":
    main()
