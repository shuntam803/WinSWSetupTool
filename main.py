import os 
import urllib.request
import shutil
from download import download
import textwrap
from rename_file import rename_file
from overwrite_xml_file import overwrite_xml_file
from win_sw_file_builder import create_files
from rich.progress import track
from rich.console import Console
from rich.prompt import Prompt

def main():
    console = Console()
        
    # 実行開始メッセージの表示
    console.print('WinSWSetupToolを開始します...')
    # 進捗バーの表示

    url_exe = 'https://github.com/winsw/winsw/releases/download/v2.12.0/WinSW-x64.exe'
    url_xml = 'https://github.com/winsw/winsw/releases/download/v2.12.0/sample-minimal.xml'
    dir_path = 'C:/WinSW'

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # WinSW-x64.exeのダウンロードとコピー
    winsw_path = os.path.join(dir_path, 'WinSW-x64.exe')
    console.print('[bold cyan]WinSW-x64.exeをダウンロードしています...[/bold cyan]')
    download(url_exe, winsw_path)
    shutil.copy(winsw_path, os.path.join(dir_path, 'webdav_noise.exe'))
    shutil.copy(winsw_path, os.path.join(dir_path, 'webdav_vibration.exe'))

    # sample-minimal.xmlのダウンロードとリネーム
    winsw_xml_path = os.path.join(dir_path, 'sample-minimal.xml')
    console.print('[bold cyan]sample-minimal.xmlをダウンロードしています...[/bold cyan]')
    download(url_xml, winsw_xml_path)
    shutil.copy(winsw_xml_path, os.path.join(dir_path, 'webdav_noise.xml'))
    shutil.copy(winsw_xml_path, os.path.join(dir_path, 'webdav_vibration.xml'))

    # WinSW-x64.exeとsample-minimal.xmlを削除
    os.remove(winsw_path)
    os.remove(winsw_xml_path)
    
    
    for i in track(range(100), description='処理中', console=console):
        pass
    
    xml_data_noise = textwrap.dedent('''
    <service>
      <id>webdav_noise</id>
      <name>WebDAV 騒音計</name>
      <description>WebDAV server using WSGI</description>
      <executable>C:/WinSW/pyenv/Scripts/wsgidav.exe</executable>
      <arguments>--host=0.0.0.0 --port=8083 --root="D:\" --auth=nt</arguments>
      <logpath>log</logpath>
      <logmode>roll</logmode>
      <onfailure action="restart" delay="10 sec"/>
    </service>
    ''')

    xml_data_vibration = textwrap.dedent('''
    <service>
      <id>webdav_vibration</id>
      <name>WebDAV 振動計</name>
      <description>WebDAV server using WSGI</description>
      <executable>C:/WinSW/pyenv/Scripts/wsgidav.exe</executable>
      <arguments>--host=0.0.0.0 --port=8084 --root="E:\" --auth=nt</arguments>
      <logpath>log</logpath>
      <logmode>roll</logmode>
      <onfailure action="restart" delay="10 sec"/>
    </service>
    ''')

    overwrite_xml_file(os.path.join(dir_path, 'webdav_noise.xml'), xml_data_noise)
    overwrite_xml_file(os.path.join(dir_path, 'webdav_vibration.xml'), xml_data_vibration)

    # create files in bin folder
    create_files(os.path.join(dir_path))

    # 完了メッセージを出力し、キー入力待ちにする
    console.print('[bold magenta]処理が完了しました。[/bold magenta]')
    Prompt.ask('[bold cyan]何かキーを押して終了してください。[/bold cyan]', show_choices=False)

if __name__ == '__main__': 
    main()
