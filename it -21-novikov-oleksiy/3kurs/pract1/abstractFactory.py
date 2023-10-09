class Window:
    __toolkit = ""  # Змінна для збереження назви інструментарію
    __purpose = ""  # Змінна для збереження призначення вікна

    def __init__(self, toolkit, purpose):
        self.__toolkit = toolkit
        self.__purpose = purpose

    def getToolkit(self):
        return self.__toolkit

    def getType(self):
        return self.__purpose

class GtkToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, "Вікно інструментів")

class GtkLayersWindow(Window):
    def __init__(self):
        Window.__init__(self,  "Вікно шарів")

class GtkMainWindow(Window):
    def __init__(self):
        Window.__init__(self,  "Головне вікно")


class QtToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self,  "Вікно інструментів")

class QtLayersWindow(Window):
    def __init__(self):
        Window.__init__(self, "Вікно шарів")

class QtMainWindow(Window):
    def __init__(self):
        Window.__init__(self,  "Головне вікно")

# Абстрактний клас фабрики
class UIFactory:
    def getToolboxWindow(self): pass
    def getLayersWindow(self): pass
    def getMainWindow(self): pass

class GtkUIFactory(UIFactory):
    def getToolboxWindow(self):
        return GtkToolboxWindow()

    def getLayersWindow(self):
        return GtkLayersWindow()

    def getMainWindow(self):
        return GtkMainWindow()

class QtUIFactory(UIFactory):
    def getToolboxWindow(self):
        return QtToolboxWindow()

    def getLayersWindow(self):
        return QtLayersWindow()

    def getMainWindow(self):
        return QtMainWindow()

if __name__ == "__main__":
    gnome = True  # Перевірка, чи використовуємо оточення GNOME
    kde   = not gnome  # Перевірка, чи використовуємо оточення KDE

    # Яке оточення доступно?
    if gnome:
        ui = GtkUIFactory()
    elif kde:
        ui = QtUIFactory()

    # Побудова користувацького інтерфейсу
    toolbox = ui.getToolboxWindow()
    layers  = ui.getLayersWindow()
    main    = ui.getMainWindow()

    # Виведення інформації про отримані вікна
    print(toolbox.getToolkit(), toolbox.getType())
    print(layers.getToolkit(), layers.getType())
    print(main.getToolkit(), main.getType())

