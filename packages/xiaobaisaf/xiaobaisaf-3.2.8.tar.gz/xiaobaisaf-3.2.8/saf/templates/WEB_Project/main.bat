@echo off

REM ���ñ���
title Running main.py...
python main.py
IF %ERRORLEVEL% NEQ 0 (
    echo ����main.pyʧ��.
    ENDLOCAL
    EXIT /B 1
)