from mag_tools.model.base_enum import BaseEnum


class MenuType(BaseEnum):
    DROP_DOWN = ("drop_down", "下拉菜单")
    POPUP = ("pop_menu", "弹出菜单")
    CONTEXT = ("context_menu", "上下文菜单")