@echo off
title JARVIS AI
color 0B

:jarvis
cls
echo =================================
echo         J.A.R.V.I.S 
echo =================================
echo.
set /p command=Sir, enter your command :

if /i "%command%"=="hello" goto hello
if /i "%command%"=="hi" goto hi 
if /i "%command%"=="time" goto time
if /i "%command%"=="youtube" goto youtube
if /i "%command%"=="google" goto google
if /i "%command%"=="notepad" goto notepad
if /i "%command%"=="exit" goto exit
if /i "%command%"=="song" goto song
if /i "%command%"=="bye" goto bye
if /i "%command%"=="ai" goto ai 
if /i "%command%"=="AI" goto ai
if /i "%command%"=="help" goto ai

echo I don't understand that command, Sir.
pause
goto jarvis

:hello
echo Hello sankit. How can I help you?
pause
goto jarvis

:bye
shutdown /s 10
pause
goto jarvis

:hi
echo Hisankit. How can I help you?
pause
goto jarvis


:time
echo Current time is %time%
pause
goto jarvis

:youtube
start chrome.exe https://www.youtube.com
goto jarvis

:ai
start chrome.exe https://chatgpt.com/
goto jarvis


:google
start chrome.exe https://www.google.com
goto jarvis

:song
start chrome.exe https://www.youtube.com/watch?v=42r8Stt-30w&list=RD42r8Stt-30w&start_radio=1
goto jarvis



:notepad
start notepad
goto jarvis

:exit
echo Goodbye Sir.
timeout /t 2 >nul
exit