from poium import Page
from poium import NewPageElement as PageElement
from time import sleep


class BaiduPage(Page):
    setting = PageElement(css='div#u1 > a.pf')
    search_setting = PageElement(css=".setpref")
    search_setting_hint = PageElement(css="#sugConf th")


class DataTimePage(Page):
    frame = PageElement(id_="iframe")
    date = PageElement(id_="appDate")
    year = PageElement(css=".dwwo", index=0)
    mouth = PageElement(css=".dwwo", index=1)
    day = PageElement(css=".dwwo", index=2)


def test_move_to_element(browser):
    """
    测试鼠标悬停
    :param browser:
    :return:
    """
    page = BaiduPage(browser)
    page.get("https://www.baidu.com")
    page.setting.click_and_hold()
    page.search_setting.click()
    sleep(2)
    hint = page.search_setting_hint.text
    assert hint == "搜索框提示："


def test_drag_and_drop_by_offset(browser):
    """
    测试鼠标滑动日期控件
    :param browser:
    :return:
    """
    page = DataTimePage(browser)
    page.get("http://www.jq22.com/yanshi4976")

    page.frame.switch_to_frame()
    page.date.click()

    page.year.drag_and_drop_by_offset(0, 10)
    sleep(2)
    page.mouth.drag_and_drop_by_offset(0, 20)
    sleep(2)
    page.day.drag_and_drop_by_offset(0, 30)
    sleep(2)
