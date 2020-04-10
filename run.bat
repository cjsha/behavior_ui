@echo off

pyuic5 -x sql\sqlUi.ui -o sql\sqlUi.py

pyuic5 -x mouse\mouseUi.ui -o mouse\mouseUi.py
pyuic5 -x mouse\newMouseConfirmUi.ui -o mouse\newMouseConfirmUi.py
pyuic5 -x mouse\oldMouseConfirmUi.ui -o mouse\oldMouseConfirmUi.py

pyuic5 -x parameters\parametersUi.ui -o parameters\parametersUi.py
pyuic5 -x parameters\parametersConfirmUi.ui -o parameters\parametersConfirmUi.py

pyuic5 -x task\taskSettingsUi.ui -o task\taskSettingsUi.py
pyuic5 -x task\taskSettingsConfirmUi.ui -o task\taskSettingsConfirmUi.py

pyuic5 -x task\taskMainUi.ui -o task\taskMainUi.py

python  main.py