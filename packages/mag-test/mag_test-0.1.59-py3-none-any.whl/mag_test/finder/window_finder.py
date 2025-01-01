import ctypes
from ctypes import wintypes
from selenium.webdriver.support import expected_conditions as EC

from mag_tools.log.logger import Logger
from mag_tools.model.log_type import LogType
# from selenium.common import InvalidSelectorException, NoSuchElementException, TimeoutException, WebDriverException

from selenium.webdriver.support.wait import WebDriverWait

from mag_test.core.app_driver import AppDriver

# 定义回调函数类型
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

# 定义 Windows API 函数
EnumWindows = ctypes.windll.user32.EnumWindows
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
GetWindowText = ctypes.windll.user32.GetWindowTextW
SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow

class WindowFinder:
    # @staticmethod
    # def switch_to_window_by_title(driver: AppDriver, window_title: str):
    #     window_title = window_title.strip()
    #
    #     if '.exe' in window_title.lower():
    #         driver = driver.new_driver(window_title)
    #     else:
    #         try:
    #             hwnd_list = WebDriverWait(driver, 10).until(lambda drv: WindowFinder.__find_window_by_title(window_title))
    #             if hwnd_list:
    #                 hwnd = hwnd_list[0]
    #                 ctypes.windll.user32.SetForegroundWindow(hwnd)
    #             else:
    #                 Logger.error(LogType.FRAME, f"未找到窗口: {window_title}")
    #         except InvalidSelectorException as e:
    #             Logger.error(LogType.FRAME, f"查找窗口[{window_title}]选择器无效: {str(e)}")
    #         except NoSuchElementException as e:
    #             Logger.error(LogType.FRAME, f"查找窗口[{window_title}]出错: {str(e)}")
    #         except TimeoutException as e:
    #             Logger.error(LogType.FRAME, f"查找窗口[{window_title}]超时: {str(e)}")
    #         except WebDriverException as e:
    #             Logger.error(LogType.FRAME, f"查找窗口[{window_title}]时通讯异常: {str(e)}")
    #         except Exception as e:
    #             Logger.error(LogType.FRAME, f"未知异常：{str(e)}")
    #
    #     return driver

    @staticmethod
    def __find_window_by_title(title: str):
        hwnd_list = []

        def enum_windows_proc(hwnd: wintypes.HWND):
            length = GetWindowTextLength(hwnd)
            if length > 0:
                window_title = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, window_title, length + 1)
                if title in window_title.value:
                    hwnd_list.append(hwnd)
            return True

        EnumWindows(EnumWindowsProc(enum_windows_proc), 0)
        return hwnd_list

    @staticmethod
    def switch_to_window_by_title(driver: AppDriver, title: str):
        title = title.strip()
        try:
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            windows = driver.window_handles
            for window in windows:
                driver.switch_to.window(window)
                if title in driver.title:
                    break
        except Exception as e:
            Logger.error(LogType.FRAME, f"未找到窗口: {title}")
