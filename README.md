# My Demo App - Automated Testing

Mobile test automation project for My Demo App on Android, built with Appium and Python following the Page Object Model (POM) pattern.

## Technologies

- Python 3.13
- Appium 2.x
- UiAutomator2
- Pytest
- Android Emulator (Pixel 9a - Android 16)

## Project Structure

```
MyDemoAppAutomatedTesting/
├── pages/
│   ├── catalog_page.py
│   ├── login_page.py
│   └── menu_page.py
├── tests/
│   └── test_login.py
├── .env.example
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Prerequisites

- Python 3.13+
- Node.js
- Appium 2.x (`npm install -g appium`)
- Appium UiAutomator2 driver (`appium driver install uiautomator2`)
- Android Studio with an emulator configured
- Java JDK 17+

## Setup

1. Clone the repository
```bash
git clone https://github.com/gtamie/MyDemoAppAutomatedTesting.git
cd MyDemoAppAutomatedTesting
```

2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Download the APK from the [official repository](https://github.com/saucelabs/my-demo-app-android/releases), version 2.2.0, mda-2.2.0-25.apk


5. Configure environment variables
```bash
cp .env.example .env
```
Edit `.env` with your settings:
```
LOGIN_USERNAME=bod@example.com
LOGIN_PASSWORD=10203040
APK_PATH=/path/to/your.apk
```

## Running the Tests

1. Start the Android emulator via Android Studio

2. Start the Appium server
```bash
appium
```

3. Run the tests
```bash
pytest tests/ -v
```

