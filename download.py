import urllib.request
import os


def download(url: str, file_path: str) -> bool:
    """ダウンロード処理を行う関数。

    Args:
        url (str): ダウンロードするファイルのURL
        file_path (str): 保存先のファイルパス

    Returns:
        bool: ダウンロードに成功したらTrue、失敗したらFalseを返す。
    """
    try:
        urllib.request.urlretrieve(url, file_path)
        return True
    except urllib.error.HTTPError as e:
        print(f'{file_path}のダウンロードに失敗しました。')
        print(e)
        return False
