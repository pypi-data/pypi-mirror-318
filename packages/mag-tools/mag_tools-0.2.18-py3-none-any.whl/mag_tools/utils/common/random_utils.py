import random
import string
import datetime


class RandomUtils:

    @staticmethod
    def random_text(length:int)->str:
        """
            生成指定长度的随机字母字符串
            参数：
            length 字符串长度
        """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def random_string(length:int)->str:
        """
            生成指定长度的随机字符串，包括大小写字母、可见字符和数字
            参数：
            length 字符串长度
        """
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def random_chinese(length:int)->str:
        """
            生成指定长度的随机汉字字符串
            参数：
            length 字符串长度
        """
        return ''.join(RandomUtils.__generate_chinese() for _ in range(length))

    @staticmethod
    def random_number(length:int)->str:
        """
        生成指定长度的由数字构成的字符串

        参数:
        length (int): 字符串的长度

        返回:
        str: 由数字构成的字符串
        """
        digits = '0123456789'
        numeric_string = ''.join(random.choice(digits) for _ in range(length))
        return numeric_string

    @staticmethod
    def random_date(year:int)->datetime:
        """
        生成指定年份的随机日期字符串

        参数:
        year (int): 指定的年份

        返回:
        str: 随机日期
        """
        # 指定年份的起始和结束日期
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)

        # 计算起始和结束日期之间的天数
        days_between_dates = (end_date - start_date).days

        # 生成随机天数
        random_number_of_days = random.randint(0, days_between_dates)

        # 生成随机日期
        return start_date + datetime.timedelta(days=random_number_of_days)


    @staticmethod
    def __generate_chinese()->str:
        return chr(random.randint(0x4e00, 0x9fa5))