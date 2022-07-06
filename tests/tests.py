from selene.support.shared import browser
from selene import be, have, command

birth_month = browser.element('.react-datepicker__month-select')
birth_year = browser.element('.react-datepicker__year-select')
birth_day = browser.element('.react-datepicker__month .react-datepicker__week .react-datepicker__day--009')
gender_mail = browser.element('[for="gender-radio-1"]')
subject = browser.element('#subjectsInput')
sports_hobby = browser.element('[for="hobbies-checkbox-1"]')
reading_hobby = browser.element('[for="hobbies-checkbox-2"]')
music_hobby = browser.element('[for="hobbies-checkbox-3"]')
state = browser.element('#state').element('#react-select-3-input')
city = browser.element('#city').element('#react-select-4-input')


def given_opened_text_box():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').should(
        have.size_greater_than_or_equal(2)).perform(command.js.remove)


def test_register_student():
    #WHEN
    given_opened_text_box()

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivanov@bk.ru')

    gender_mail.click()

    browser.element('#userNumber').type('8999999999')

    browser.element('#dateOfBirthInput').click()
    birth_month.element('[value="8"]').click()
    birth_year.element('[value="1999"]').click()
    birth_day.click()

    subject.type('Arts').press_tab()
    subject.type('History').press_tab()
    subject.type('Accounting').press_tab()
    subject.type('Physics').press_tab()

    sports_hobby.click()
    reading_hobby.click()
    music_hobby.click()

    browser.element('#uploadPicture').send_keys(upload_source('picture.jpg'))

    browser.element('#currentAddress').type('test')

    state.type('Rajasthan').press_tab()
    city.type('Jaipur').press_tab()

    browser.element('#submit').click()

    #THEN
    browser.all('.table-responsive').all('tr').element(1).should(have.text('Ivan Ivanov'))
    browser.all('.table-responsive').all('tr').element(2).should(have.text('ivanov@bk.ru'))
    browser.all('.table-responsive').all('tr').element(3).should(have.text('Male'))
    browser.all('.table-responsive').all('tr').element(4).should(have.text('8999999999'))
    browser.all('.table-responsive').all('tr').element(5).should(have.text('09 September,1999'))
    browser.all('.table-responsive').all('tr').element(6).should(have.text('Arts, History, Accounting, Physics'))
    browser.all('.table-responsive').all('tr').element(7).should(have.text('Sports, Reading, Music'))
    browser.all('.table-responsive').all('tr').element(8).should(have.text('picture.jpg'))
    browser.all('.table-responsive').all('tr').element(9).should(have.text('test'))
    browser.all('.table-responsive').all('tr').element(10).should(have.text('Rajasthan Jaipur'))


def upload_source(path):
    import demoqa_tests
    demoqa_tests.__file__
    from pathlib import Path
    return str(Path(demoqa_tests.__file__)
               .parent
               .parent
               .joinpath(f'demoqa_tests/{path}')
               )
