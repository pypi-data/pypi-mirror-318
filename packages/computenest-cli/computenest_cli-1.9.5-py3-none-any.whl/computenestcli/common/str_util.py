import re


class StrUtil:
    def __init__(self):
        pass

    # 将输入参数改为计算巢部署物允许的格式
    @staticmethod
    def sanitize_name(name):
        # 只允许字母、数字、下划线、和中划线
        pattern = r'[^\w-]+'
        # 替换不符合的字符为下划线
        sanitized_name = re.sub(pattern, '_', name)
        return sanitized_name

    # 将字符串首字符lower
    @staticmethod
    def lower_first_char(name):
        if not name:
            return name
        return name[0].lower() + name[1:]

    @staticmethod
    def capitalize_keys(data):
        """
        递归地对字典的所有键进行首字符大写。

        :param data: 输入的数据结构，可以是列表、字典、字符串等
        :return: 更新后的数据结构
        """
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                # 将键的首字符大写
                new_key = key[0].upper() + key[1:] if isinstance(key, str) else key
                # 递归处理值
                new_dict[new_key] = StrUtil.capitalize_keys(value)
            return new_dict
        elif isinstance(data, list):
            return [StrUtil.capitalize_keys(element) for element in data]
        else:
            return data
