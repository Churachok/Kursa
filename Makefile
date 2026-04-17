APP_NAME = vp
MAIN_SCRIPT = back.py
BUILD_DIR = build
DIST_DIR = dist
INSTALL_PREFIX = /usr/local
EXECUTABLE = $(DIST_DIR)/$(APP_NAME)
VENV_DIR = .venv

PYINSTALLER_CMD = $(VENV_DIR)/bin/pyinstaller

.PHONY: all build install uninstall clean help

all: build


build: install-dependencies
	@echo "Сборка приложения с PyInstaller..."
	@$(PYINSTALLER_CMD) --onefile --name $(APP_NAME) --distpath $(DIST_DIR) --workpath $(BUILD_DIR)/work --specpath $(BUILD_DIR) $(MAIN_SCRIPT)
	@echo "Исполняемый файл: $(EXECUTABLE)"


install-dependencies:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		python -m venv $(VENV_DIR); \
	fi
	$(VENV_DIR)/bin/pip install --upgrade pip
	@if [ -f "requirements.txt" ]; then \
		echo "Установка зависимостей..."; \
		$(VENV_DIR)/bin/pip install -r requirements.txt; \
	else \
		echo "Файл requirements.txt не найден."; \
	fi
	$(VENV_DIR)/bin/pip install pyinstaller

install: build
	@echo "Установка в $(INSTALL_PREFIX)/bin..."
	@sudo cp $(EXECUTABLE) $(INSTALL_PREFIX)/bin/
	@echo "Великие Пятнашки установлены. Запускайте игру командой: $(APP_NAME)"

uninstall:
	@echo "Удаление из $(INSTALL_PREFIX)/bin..."
	@sudo rm -f $(INSTALL_PREFIX)/bin/$(APP_NAME)
	@echo "Великие Пятнашки удалены =("

clean:
	@rm -rf $(BUILD_DIR) $(DIST_DIR) *.spec $(VENV_DIR)
