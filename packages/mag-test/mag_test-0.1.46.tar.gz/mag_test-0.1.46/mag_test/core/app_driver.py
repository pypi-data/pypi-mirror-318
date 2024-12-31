import logging
import threading
import time
from typing import Dict, List, Optional, Union

from appium import webdriver
from appium.webdriver import WebElement
from mag_tools.log.logger import Logger
from mag_tools.model.log_type import LogType
from mag_tools.model.message_type import MessageType
from mag_tools.utils.common.message_box import MessageBox
from mag_tools.model.control_type import ControlType
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException, InvalidArgumentException, \
    TimeoutException
from selenium.webdriver.common.by import By

from mag_tools.utils.common.process_utils import ProcessUtils
from mag_tools.utils.test.element_finder_utils import ElementFinderUtils


class AppDriver(webdriver.Remote):
    def __init__(self, url:str, capabilities:Dict[str,str], parent_driver:webdriver.Remote=None):
        logging.basicConfig(level=logging.DEBUG)

        self.app = capabilities["app"]
        self.parent_driver = parent_driver
        self.__stop_event = threading.Event()
        self.__url = url
        self.__capabilities = capabilities

        # 检查应用程序是否已经在运行
        proc = ProcessUtils.find_app(self.app)
        if proc:
            proc.terminate()

        try:
            self.root_driver = webdriver.Remote(command_executor=url,
                                            desired_capabilities={"platformName": "Windows",
                                                                  "deviceName": "WindowsPC",
                                                                  "app": "Root"})
        except SessionNotCreatedException:
            MessageBox.showinfo("会话未建立", "检查WinAppDriver是否已启动及网络是否正常！")
        except InvalidArgumentException:
            MessageBox.showinfo("参数无效", "检查参数是否正确！")
        except TimeoutException:
            MessageBox.showinfo("连接超时", "，检查WinAppDriver是否已启动及网络是否正常！")
        except WebDriverException:
            MessageBox.showinfo("连接出错", "检查WinAppDriver是否已启动及网络是否正常！")
        except Exception as e:
            MessageBox.showinfo("未知异常", str(e))

        # 初始化webdriver
        super().__init__(command_executor=url, desired_capabilities=capabilities)

    def new_driver(self, app):
        return AppDriver(self.__url, self.__get_capabilities(app), self)

    def check_alert(self)->List[Union[Optional[MessageType], Optional[str]]]:
        alert_result = self.__find_alert()
        if alert_result[0] is not None:
            alert_result[0].click()
        return alert_result[1:]

    def stop_checking_for_alert(self):
        self.__stop_event.set()

    def quit_app(self):
        try:
            if self.session_id:
                time.sleep(2)
                self.root_driver.quit()
                time.sleep(2)
                self.quit()
                Logger.info(LogType.FRAME, f"关闭'{self.app}' driver完毕")
        except AttributeError:
            Logger.error(LogType.FRAME, "No active session to quit")

    def __find_alert(self) -> List[Union[Optional[WebElement], Optional[MessageType], Optional[str]]]:
        alert_result = [None, None, None]
        try:
            exp = ElementFinderUtils.global_expression(None, None, '#32770', None, None, None)
            alerts = self.find_elements(By.XPATH, exp)
            if alerts is not None and len(alerts) > 0:
                alert = alerts[-1] # 获取最新弹出的对话框
                alert_title = alert.get_attribute("Name")

                keyword_found = next((keyword for keyword in ["警告", "错误", "确认", "HiSim"] if keyword in alert_title), None)
                if keyword_found is not None:
                    message_type = MessageType.of_code(keyword_found) if keyword_found else None

                    alert_label = alert.find_element(By.XPATH, f".//{ControlType.LABEL.code}")
                    message = alert_label.get_attribute("Name")
                    Logger.info(LogType.SERVICE, f'message: {message}')

                    element = alert.find_element(By.XPATH, f".//{ControlType.BUTTON.code}[@Name='确定(O)' or @Name='是(Y)' or @Name='确定']")

                    alert_result = [element, message_type, message]
        except Exception as e:
            Logger.error(LogType.FRAME, f"Exception: {str(e)}")

        return alert_result

    def __get_capabilities(self, app):
        return {
            'platformName': self.__capabilities['platformName'],
            'deviceName': self.__capabilities['deviceName'],
            'automationName': self.__capabilities['automationName'],
            'app': app,
            'appWorkingDir': self.__capabilities['appWorkingDir'],
        }