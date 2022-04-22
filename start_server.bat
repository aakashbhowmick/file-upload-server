@echo off

echo Android must be started before running this
set FLASK_APP=server

REM Forward all packets from from port 5000 of emulator android device to port 5000 of host machine
adb reverse tcp:5000 tcp:5000

REM Start server
flask run

