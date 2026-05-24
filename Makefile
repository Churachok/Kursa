PYTHON = python3
VENV = venv
VENV_PYTHON = $(VENV)/bin/python
VENV_PIP = $(VENV)/bin/pip
MAIN_SCRIPT = front.py
TEST_SCRIPT = test.py
REQUIREMENTS = requirements.txt
PROJECT_NAME = kursa
INSTALL_PATH = /usr/local/bin

.PHONY: all install run test clean build venv package install-global uninstall

all: venv install run

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	@echo "Установка зависимостей из $(REQUIREMENTS):"
	$(VENV_PIP) install -r $(REQUIREMENTS)

run: install
	@echo "Запуск игры Пятнашки:"
	$(VENV_PYTHON) $(MAIN_SCRIPT)

test: install
	$(VENV_PYTHON) $(TEST_SCRIPT)

build: install test
	@echo "Проект $(PROJECT_NAME) собран"

package: install
	@echo "Установка pyinstaller"
	$(VENV_PIP) install pyinstaller
	$(VENV_PYTHON) -m PyInstaller --onefile --name $(PROJECT_NAME) $(MAIN_SCRIPT)

install-global: package
	@if [ -f dist/$(PROJECT_NAME) ]; then \
		sudo cp dist/$(PROJECT_NAME) $(INSTALL_PATH)/; \
		sudo chmod +x $(INSTALL_PATH)/$(PROJECT_NAME); \
	else \
		echo "Исполняемый файл не найден. Сначала выполните 'make package'"; \
		exit 1; \
	fi

uninstall:
	sudo rm -f $(INSTALL_PATH)/$(PROJECT_NAME)

clean:
	rm -rf $(VENV) build dist *.spec
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true

reinstall: clean install-global
