from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from mag_test.core.app_driver import AppDriver
from mag_test.finder.element_finder_utils import ElementFinderUtils
from mag_test.model.control_type import ControlType


class TreeUtils:
    @staticmethod
    def expand_all(driver:AppDriver, tree:WebElement):
        try:
            actionChains = ActionChains(driver)

            # 查找所有展开按钮
            tree_items = ElementFinderUtils.find_elements_by_type(tree, None, ControlType.TREE_ITEM)

            for tree_item in tree_items:
                # 双击展开
                actionChains.double_click(tree_item).perform()
        except Exception as e:
            print(f"Error expanding nodes: {str(e)}")