from android_env import loader

# env = loader.load(
#     avd_name=os.getenv("AVD_NAME"),
#     android_avd_home=os.getenv("ANDROID_AVD_HOME"),
#     android_sdk_root=os.getenv("ANDROID_SDK_ROOT"),
#     emulator_path=os.getenv("EMULATOR_PATH"),
#     adb_path=os.getenv("ADB_PATH"),
#     task_path=r"D:\05 Programming\GitHub\AndroidInstructRL\classic_2048.textproto",
# )

env = loader.load(
    avd_name='Pixel_6_Pro_API_34',
    android_avd_home='/mnt/c/Users/Sawyer/.android/avd',
    android_sdk_root='/mnt/c/Users/Sawyer/AppData/Local/Android/Sdk',
    emulator_path='/mnt/c/Users/Sawyer/AppData/Local/Android/Sdk/emulator/emulator',
    adb_path='/mnt/c/Users/Sawyer/AppData/Local/Android/Sdk/platform-tools/adb.exe',
    task_path=r"classic_2048.textproto",
)
