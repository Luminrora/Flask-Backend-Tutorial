import datetime

def time_now():
    """
    获取当前时间字符串

    返回:
    str: 当前时间字符串
    格式: "YYYY-MM-DD HH:MM:SS"
    """
    result = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return result

def calculate_time_cost(start_time_str, end_time_str):
    """
    计算两个时间字符串之间的耗时（单位：秒）

    参数:
    start_time_str (str): 开始时间字符串，格式 "YYYY-MM-DD HH:MM:SS"
    end_time_str (str): 结束时间字符串，格式 "YYYY-MM-DD HH:MM:SS"

    返回:
    float: 耗时（秒），保留两位小数
    """
    time_format = "%Y-%m-%d %H:%M:%S"
    try:
        start_time = datetime.datetime.strptime(start_time_str, time_format)
        end_time = datetime.datetime.strptime(end_time_str, time_format)
        time_cost = (end_time - start_time).total_seconds()
        return round(time_cost, 2)
    except ValueError as e:
        raise ValueError(f"时间格式错误: {str(e)}。请确保时间格式为 'YYYY-MM-DD HH:MM:SS'")