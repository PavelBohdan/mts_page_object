from selenium.webdriver.common.by import By


class MainPageLocators:
    USER_BUTTON_LOCATOR = (By.XPATH, '//button[@name="login"]')
    USER_NAME_LOCATOR = (By.XPATH, '//span[@data-name="userNameLogged"]')

    LOGIN_POP_UP_FRAME_LOCATOR = (By.XPATH, '//*[@id="cdk-overlay-3"]')
    LOGIN_POP_UP_LOCATOR = (By.XPATH, '//*[@id="mat-dialog-0"]')

    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@name="submitLogin"]')

    USERNAME_FIELD_LOCATOR = (By.XPATH, '//input[@name="username"]')
    PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password"]')

    LOGGED_USER_BUTTON_LOCATOR = (By.XPATH, '//button[@name="account"]')

    USER_MENU_POPUP_LOCATOR = (By.XPATH, '//div[@class="cdk-overlay-pane"]')
    USER_MENU_POPUP_FRAME_LOCATOR = (By.XPATH, '//div[@class="mat-menu-panel ng-trigger ng-trigger-transformMenu '
                                               'ng-tns-c191-30 mat-menu-below ng-star-inserted mat-elevation-z4 '
                                               'mat-menu-before"]')

    SIGN_OUT_BUTTON_LOCATOR = (By.XPATH, '//button[@name="logout"]')

    MENU_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/menu"]')

    BOOK_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/bookTable"]')



class MenuPageLocators:
    CHECK_BOX_TOFU_THAI_GREEN_CHICKEN_CURRY_LOCATOR = (By.XPATH, '/html/body/app-public-main/div/div/div/mat-sidenav-container/mat-sidenav-content/app-public-menu/div/app-public-menu-card[1]/mat-card/app-own-menu-card-details/div[4]/mat-checkbox[1]/label/span[1]')
    CHECK_BOX_EXTRA_CURRY_THAI_GREEN_CHICKEN_CURRY_LOCATOR = (By.XPATH, '/html/body/app-public-main/div/div/div/mat-sidenav-container/mat-sidenav-content/app-public-menu/div/app-public-menu-card[1]/mat-card/app-own-menu-card-details/div[4]/mat-checkbox[2]/label/span[1]')
    ADD_TO_ORDER_BUTTON_LOCATOR = (By.XPATH,
                                   '//button[@class="mat-focus-indicator addOrder mat-button mat-button-base mat-accent"]')
    RESUME_BOOKING_POP_UP_TITLE_LOCATOR = (By.XPATH, '//span[@class="sidenavTitleSpan"]')
    ADDITIONAL_OPTIONS_LOCATOR = (By.XPATH, '//span[@class="orderIngredients"]')
    SEND_BUTTON_LOCATOR = (By.XPATH, '//button[@name="orderSubmit"]')



class BookingPageLocator:
    pass