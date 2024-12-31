# 导入计算相关函数
from .test import calculate_sum, show_result

# 导入字符串处理相关函数
from .string_utils import reverse_string, count_chars

def hello_world():
    """
    一个简单的打招呼函数
    """
    print("你好！这是我的第一个Python包！")

# 可以定义 __all__ 来控制 from yang import * 时能导入哪些内容
__all__ = [
    'hello_world',
    'calculate_sum',
    'show_result',
    'reverse_string',
    'count_chars'
]

