@echo off
echo Installing required libraries (pip is needed)

timeout 3 > nul

pip install pyqt5

timeout 3 > nul

cls
echo Done ! Closing in 3 seconds
timeout 1 > nul
cls
echo Done ! Closing in 2 seconds
timeout 1 > nul
cls
echo Done ! Closing in 1 seconds
timeout 1 > nul
exit