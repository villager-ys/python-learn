# os库练习
from pathlib import Path
import os
print(os.path.abspath('.'))
print(os.path.exists('/Users'))
print(os.path.isdir('/Users'))
print(os.path.isfile('/Users/yuanshuai/workspace/python-learn/os_test.py'))
# 路径拼接
print(os.path.join("/Users", 'a/c', 'b'))

p = Path('.')
print(p.resolve())
print(p.is_dir())
q = Path('/Users/a')
# parents=False 如果a目录不存在就会报错
Path.mkdir(q, parents=True)
