@echo off

REM ���ñ���
title Running run_apis.py...
python run_apis.py
IF %ERRORLEVEL% NEQ 0 (
    echo ����run_apis.pyʧ��.
    ENDLOCAL
    EXIT /B 1
)