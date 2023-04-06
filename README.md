# WinSWSetupTool

WinSWSetupToolは、Windows Service Wrapperの設定ファイルと、Wrapperに必要なファイルを作成するツールです。

## 必要な環境

- Windows OS
- Python 3.7以上
- pyinstaller

## インストール方法

1. このリポジトリをクローンします。
2. 必要なライブラリをインストールします。

```
pip install -r requirements.txt
```

3. `pyinstaller`をインストールします。

```
pip install pyinstaller
```

## 使い方

1. `main.py`を実行してください。
2. しばらく待つと、必要なファイルが作成されます。
3. `pyinstaller`を使用して、単一ファイルの実行可能ファイルを作成することもできます。

```
pyinstaller main.py --name WinSWSetupTool --onefile
```

## ファイルについて

- `main.py`：メインのスクリプトファイル
- `download.py`：ダウンロード処理を行うファイル
- `overwrite_xml_file.py`：XMLファイルの上書き処理を行うファイル
- `rename_file.py`：ファイルのリネーム処理を行うファイル
- `win_sw_file_builder.py`：Windows Service Wrapperに必要なファイルを作成するファイル
