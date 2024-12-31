from typing import Any, Dict

import pytest

from mag_test.bean.base_test import BaseTest
from mag_test.bean.case import Case
from mag_test.model.test_component_type import TestComponentType


class Module(BaseTest):
    def __init__(self, home_dir, plan_id, name, cases, index=None):
        super().__init__(home_dir, name, index, TestComponentType.MODULE, None, None)
        self.__plan_id = plan_id
        self.__cases = cases

    @pytest.mark.benchmark
    def start(self, driver):
        for case in self.__cases:
            driver = case.start(driver)

        super()._report()
        return driver

    def append(self, case):
        self.__cases.append(case)

    @staticmethod
    def from_map(home_dir:str, plan_id:str, index:int, data:Dict[str, Any]):
        name = data.get('name', '')
        module = Module(home_dir, plan_id, name, [], index)

        for case_index, case_item in enumerate(data.get('cases'), start=1):
            case = Case.from_map(home_dir, plan_id, case_index, case_item)
            module.append(case)

        return module
