# -*- coding: utf-8 -*-
"""
用途：
    遍历某目录，并查找指定类型文件，复制到指定文件夹
"""
import shutil, os

def get_dir(path, fileType):
    """
    :param path: 路径
    :param fileType: 需要复制的文件类型，前面需要加 .
    :return:null
    """
    # 查看当前目录文件列表（包含文件夹）
    allfilelist = os.listdir(path)

    for file in allfilelist:
        print(file, '\n')
        filepath = os.path.join(path, file)
        # 判断是否是文件夹，如果是则继续遍历，否则复制指定类型文件到相应文件夹
        if os.path.isdir(filepath):
            get_dir(filepath, '.po')
        else:
            if filepath.endswith(fileType):
                print('找到文件：' + filepath)
                # 复制filepath找到的文件到copypath目录
                # 由于我本次复制文件的路径有相同的地方，故做了替换处理
                # 如果你所替换的是完全不同的路径，故可以用 shutil.copy(filepath, distPath)这句替换下边四行代码
                path_rep = path.replace('E:\\roke\odoo\\odoo_github\\odoo12\\addons', '')
                copypath = ''
                copypath = distPath + path_rep
                shutil.copy(filepath, copypath)


if __name__ == '__main__':
    # 查找指定文件的路径
    path = 'E:\\roke\odoo\\odoo_github\\odoo12\\addons'
    # 需要复制到的文件夹路径
    distPath = 'E:\\roke\\odoo\\odoo\\odoo_12.0\\odoo\\addons'
    get_dir(path, '.po')



