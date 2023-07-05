from android_env import loader
from absl import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.set_verbosity('info')
logging.set_stderrthreshold('info')


with loader.load(
    avd_name=os.getenv("AVD_NAME"),
    android_avd_home=os.getenv("ANDROID_AVD_HOME"),
    android_sdk_root=os.getenv("ANDROID_SDK_ROOT"),
    emulator_path=os.getenv("EMULATOR_PATH"),
    adb_path=os.getenv("ADB_PATH"),
    task_path="tasks/classic_2048.textproto"
) as env:
    _ = env.reset()

    stall = input("Enter something to stop the emulator")