import datetime
import time
import pytz  # 时区处理库，需要安装：pip install pytz

import tarfile

FILE="time.tar"
def read_tar_file(tar_path):
    """
    读取 .tar 文件并列出其中的文件内容。

    :param tar_path: .tar 文件的路径
    """
    try:
        # 打开 .tar 文件
        with tarfile.open(tar_path, 'r') as tar:
            print(f"成功打开文件: {tar_path}")
            
            # 列出 .tar 文件中的所有成员（文件/目录）
            print("文件列表:")
            for member in tar.getmembers():
                print(f" - {member.name} (大小: {member.size} 字节)")

            # 提取并读取文件内容（可选）
            print("\n文件内容:")
            for member in tar.getmembers():
                if member.isfile():  # 只处理文件，跳过目录
                    print(f"\n读取文件: {member.name}")
                    file = tar.extractfile(member)
                    if file:
                        content = file.read()
                        print(content.decode('utf-8'))  # 假设文件是文本文件，使用 UTF-8 解码
                    else:
                        print(f"无法读取文件: {member.name}")
    except tarfile.TarError as e:
        print(f"读取 .tar 文件时出错: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")


def timestamp_to_datetime(timestamp, tz=None):
    """
    将时间戳转换为 datetime 对象。

    Args:
        timestamp: 时间戳（秒）。
        tz: 时区字符串，例如 'Asia/Shanghai'、'UTC'。如果为 None，则使用本地时区。

    Returns:
        datetime 对象，如果转换失败则返回 None。
    """
    try:
        if tz:
            tz_obj = pytz.timezone(tz)
            dt = datetime.datetime.fromtimestamp(timestamp, tz=tz_obj)
        else:
            dt = datetime.datetime.fromtimestamp(timestamp)
        return dt
    except (ValueError, OSError, pytz.exceptions.UnknownTimeZoneError):
        return None

def datetime_to_timestamp(dt):
    """
    将 datetime 对象转换为时间戳。

    Args:
        dt: datetime 对象。

    Returns:
        时间戳（秒），如果转换失败则返回 None。
    """
    try:
        timestamp = dt.timestamp()
        return timestamp
    except AttributeError: #处理python3.6没有timestamp()方法
        timestamp = time.mktime(dt.timetuple())
        return timestamp
    except (ValueError, OSError):
        return None

def str_to_datetime(date_str, format_str, tz=None):
    """
    将字符串转换为 datetime 对象。

    Args:
        date_str: 日期字符串。
        format_str: 格式字符串，例如 '%Y-%m-%d %H:%M:%S'。
        tz: 时区字符串。

    Returns:
        datetime 对象，如果转换失败则返回 None。
    """
    try:
        if tz:
            tz_obj = pytz.timezone(tz)
            dt = datetime.datetime.strptime(date_str, format_str).replace(tzinfo=tz_obj)
        else:
            dt = datetime.datetime.strptime(date_str, format_str)
        return dt
    except (ValueError, TypeError, pytz.exceptions.UnknownTimeZoneError):
        return None

def datetime_to_str(dt, format_str):
    """
    将 datetime 对象转换为字符串。

    Args:
        dt: datetime 对象。
        format_str: 格式字符串。

    Returns:
        日期字符串，如果转换失败则返回 None。
    """
    try:
        return dt.strftime(format_str)
    except (ValueError, TypeError):
        return None

def timestamp_to_str(timestamp, format_str, tz=None):
  """
  将时间戳转换为字符串
  """
  dt = timestamp_to_datetime(timestamp, tz)
  if dt:
    return datetime_to_str(dt, format_str)
  return None

def str_to_timestamp(date_str, format_str, tz=None):
  """
  将字符串转换为时间戳
  """
  dt = str_to_datetime(date_str, format_str, tz)
  if dt:
    return datetime_to_timestamp(dt)
  return None

# 示例用法
timestamp = time.time()
