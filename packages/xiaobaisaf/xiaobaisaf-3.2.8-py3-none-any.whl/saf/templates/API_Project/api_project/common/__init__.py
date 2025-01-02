#! /usr/bin/env python
'''
Auther      : xiaobaiTser
Email       : 807447312@qq.com
createTime  : 2024/11/18 23:27
fileName    : __init__.py.py
'''

import os
import platform
import subprocess
import shutil
from .. import (
    DATA_DIR_PATH,
    REPORT_DIR_PATH,
    ALLURE_REPORT_DIR_PATH,
    LOG_DIR_PATH,
    PROJECT_CLEAN
)
from .ENV import ENV
from ..config.host_config import HOST
from..config.allure_config import Allure
from .LOG import Logger

logger = Logger()

def _clean(path:str = None):
    '''
    清空文件及或者删除指定的文件
    :param path: 文件夹或者文件
    :return:
    '''
    path = os.path.abspath(path)
    if os.path.isdir(path):
        try:
            shutil.rmtree(path)
            logger.info(f'[{path}]\t文件夹已经清空完毕~')
        except Exception as e:
            logger.error(str(e))
        if not os.path.exists(path):
            os.mkdir(path)
            logger.info(f'[{path}]\t文件夹已经创建完毕~')
    elif os.path.isfile(path):
        try:
            os.remove(path)
            logger.info(f'[{path}]\t文件已经删除完毕~')
        except Exception as e:
            logger.error(str(e))

def clean():
    ''' 清除上次执行的数据 '''

    if PROJECT_CLEAN.data_status:
        _clean(DATA_DIR_PATH)
    if PROJECT_CLEAN.report_status:
        _clean(REPORT_DIR_PATH)
    if PROJECT_CLEAN.allure_report_status:
        _clean(ALLURE_REPORT_DIR_PATH)

def kill_process(port:int = 0):
    if port == 0:
        return
    system = platform.system()
    if system == "Windows":
        try:
            # 使用netstat命令查找占用指定端口的进程PID，结合findstr进行文本筛选
            result = subprocess.run(
                ['netstat', '-ano', '|', 'findstr', f':{port}'],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                pids = set()
                for line in lines:
                    parts = line.split()
                    if len(parts) > 4:
                        pid = parts[4]
                        pids.add(pid)
                # 使用taskkill命令根据PID来终止进程
                for pid in pids:
                    subprocess.run(['taskkill', '/F', '/PID', pid], check=True)
                logger.info(f"已尝试在Windows系统中正常关闭占用端口 {port} 的进程")
            else:
                logger.error(f"在Windows系统中查找占用端口 {port} 的进程时出错:", result.stderr)
        except subprocess.CalledProcessError as e:
            logger.error(f"在Windows系统中终止占用端口 {port} 的进程时出错:", e)
    elif system == "Linux" or system == "Darwin":  # Darwin是macOS系统对应的标识
        try:
            # 使用lsof命令查找占用指定端口的进程PID
            result = subprocess.run(
                ['lsof', '-t', '-i:{}'.format(port)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                pids = result.stdout.strip().split('\n')
                for pid in pids:
                    # 先尝试发送SIGTERM信号（正常终止信号）给进程
                    subprocess.run(['kill', '-15', pid], check=True)
                    # 可以添加等待一段时间，检查进程是否已终止，如果没有再发送SIGKILL信号强制终止
                    # 这里为简化示例，暂未添加等待逻辑
                    # 例如可以使用ps命令结合grep等检查进程是否还存在，再决定是否发送SIGKILL信号
                logger.info(f"已尝试在 {system} 系统中正常关闭占用端口 {port} 的进程")
            else:
                logger.error(f"在 {system} 系统中查找占用端口 {port} 的进程时出错:", result.stderr)
        except subprocess.CalledProcessError as e:
            logger.error(f"在 {system} 系统中终止占用端口 {port} 的进程时出错:", e)
    else:
        logger.warning(f"不支持的操作系统: {system}")

def init():
    ''' 初始化 '''
    clean()
    ENV.load()
    ENV.set_env('HOST', HOST.CURRENT_HOST)
    kill_process(Allure.PORT)
    logger.info('初始化完毕~')
