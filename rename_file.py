import os


def rename_file(old_file_path: str, new_file_path: str) -> bool:
    """ファイルのリネーム処理を行う関数。

    Args:
        old_file_path (str): リネームするファイルの元のファイルパス
        new_file_path (str): リネーム後のファイルパス

    Returns:
        bool: リネームに成功したらTrue、失敗したらFalseを返す。
    """
    if os.path.exists(old_file_path):
        try:
            os.rename(old_file_path, new_file_path)
            return True
        except Exception as e:
            print(f'{old_file_path}のリネームに失敗しました。')
            print(e)
            return False
    return False
