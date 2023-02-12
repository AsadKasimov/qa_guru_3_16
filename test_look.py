from selene import have
from selene.support.shared import browser


def test_click_pick():
    browser.open('https://look.online/')

    browser.element('.BlockSlide_blockSlide__media__dTAt_').click()
    browser.element('.CollapseBtn_collapseBtn__9scPr').click()


def test_filter():
    browser.open('https://look.online/')

    browser.element('.FilterBtn_filter__DF0L_').click()
    browser.element('//*[@id="page_wrap"]/div/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div[1]/button').click()
    browser.element('//label[text()="Платья"]').click()
    browser.element('[class="Button_button__NAeWF Button_button_blue__fHcCt"]').click()


def test_transition_to_sale():
    browser.open('https://look.online/')

    browser.all('a[href="/sale"]').element_by(have.text('SALE')).click()
    browser.element('a[href="/"]').click()
