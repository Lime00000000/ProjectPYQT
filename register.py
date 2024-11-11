from PyQt6.QtWidgets import QInputDialog


def reg(self, bd):
    check = False
    items = ["Я уже смешарик", "Я хочу стать смешариком"]
    item, ok = QInputDialog.getItem(self, 'register', 'Вы зарегистрированы?', items, 0, False)
    if item and ok:
        while True:
            login, ok = QInputDialog.getText(self, ' ', 'Введите логин')
            if ok and login:
                while True:
                    password, ok = QInputDialog.getText(self, ' ', 'Введите пароль')
                    if ok and password:
                        check = True
                        break
                break
    if item == items[0]:
        try:
            return (check, login, password)
        except Exception:
            return 0
    else:
        pass

