APP_NAME = vp
MAIN_SCRIPT = front.py
BUILD_DIR = build
DIST_DIR = dist
INSTALL_PREFIX = /usr/local
EXECUTABLE = $(DIST_DIR)/$(APP_NAME)

.PHONY: all build install uninstall clean help

all: build

build: install-dependencies
	@echo "Сборка приложения с PyInstaller..."
	@pyinstaller --onefile \
		--name $(APP_NAME) \
		--distpath $(DIST_DIR) \
		--workpath $(BUILD_DIR)/work \
		--specpath $(BUILD_DIR) \
		$(MAIN_SCRIPT)
	@echo "Исполняемый файл: $(EXECUTABLE)"

install-dependencies:
	@if [ -f "requirements.txt" ]; then \
		echo "Установка зависимостей..."; \
		pip install -r requirements.txt; \
	else \
		echo "Файл requirements.txt не найден. Убедитесь, что все зависимости установлены."; \
	fi

install: build
	@echo "Установка в $(INSTALL_PREFIX)/bin..."
	@sudo cp $(EXECUTABLE) $(INSTALL_PREFIX)/bin/
	@echo "Великие Пятнашки установлены. Запускайте игру командой: $(APP_NAME)"

uninstall:
	@echo "Удаление из $(INSTALL_PREFIX)/bin..."
	@sudo rm -f $(INSTALL_PREFIX)/bin/$(APP_NAME)
	@echo "Великие Пятнашки удалены =("

clean:
	@rm -rf $(BUILD_DIR) $(DIST_DIR) *.spec
