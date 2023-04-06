import os


def create_files(folder_path):
    # フォルダの作成
    bin_noise_path = os.path.join(folder_path, 'bin_noise')
    os.makedirs(bin_noise_path, exist_ok=True)

    bin_vibration_path = os.path.join(folder_path, 'bin_vibration')
    os.makedirs(bin_vibration_path, exist_ok=True)

    # ファイルの作成
    wrapper_file = '''@echo off
cd %~dp0..
webdav_noise %1
'''
    with open(os.path.join(bin_noise_path, 'wrapper.cmd'), 'w') as f:
        f.write(wrapper_file)

    service_install_file = '''@echo off
call wrapper install
'''
    with open(os.path.join(bin_noise_path, 'service-install.cmd'), 'w') as f:
        f.write(service_install_file)

    service_restart_file = '''@echo off
call wrapper restart
'''
    with open(os.path.join(bin_noise_path, 'service-restart.cmd'), 'w') as f:
        f.write(service_restart_file)

    service_start_file = '''@echo off
call wrapper start
'''
    with open(os.path.join(bin_noise_path, 'service-start.cmd'), 'w') as f:
        f.write(service_start_file)

    service_stop_file = '''@echo off
call wrapper stop
'''
    with open(os.path.join(bin_noise_path, 'service-stop.cmd'), 'w') as f:
        f.write(service_stop_file)

    service_uninstall_file = '''@echo off
call wrapper uninstall
'''
    with open(os.path.join(bin_noise_path, 'service-uninstall.cmd'), 'w') as f:
        f.write(service_uninstall_file)

    # ファイルの作成
    wrapper_file = '''@echo off
cd %~dp0..
webdav_vibration %1
'''
    with open(os.path.join(bin_vibration_path, 'wrapper.cmd'), 'w') as f:
        f.write(wrapper_file)

    service_install_file = '''@echo off
call wrapper install
'''
    with open(os.path.join(bin_vibration_path, 'service-install.cmd'), 'w') as f:
        f.write(service_install_file)

    service_restart_file = '''@echo off
call wrapper restart
'''
    with open(os.path.join(bin_vibration_path, 'service-restart.cmd'), 'w') as f:
        f.write(service_restart_file)

    service_start_file = '''@echo off
call wrapper start
'''
    with open(os.path.join(bin_vibration_path, 'service-start.cmd'), 'w') as f:
        f.write(service_start_file)

    service_stop_file = '''@echo off
call wrapper stop
'''
    with open(os.path.join(bin_vibration_path, 'service-stop.cmd'), 'w') as f:
        f.write(service_stop_file)

    service_uninstall_file = '''@echo off
call wrapper uninstall
'''
    with open(os.path.join(bin_vibration_path, 'service-uninstall.cmd'), 'w') as f:
        f.write(service_uninstall_file)
