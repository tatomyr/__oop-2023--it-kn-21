from UI import selectUI

def main() -> None:
    # Створюємо екземпляр класу CommandLineUI
    ui = selectUI()

    # Запускаємо інтерфейс
    ui.run()
    

if __name__ == "__main__":
    main()

