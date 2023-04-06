import os
import codecs


def overwrite_xml_file(file_path: str, xml_data: str) -> bool:
    """XMLファイルの上書き処理を行う関数。

    Args:
        file_path (str): 上書きするファイルパス
        xml_data (str): 書き込むXMLデータ

    Returns:
        bool: 上書きに成功したらTrue、失敗したらFalseを返す。
    """
    try:
        with codecs.open(file_path, 'w', 'utf-8') as f:
            f.write(xml_data)
        return True
    except Exception as e:
        print(f'{file_path}の上書きに失敗しました。')
        print(e)
        return False
