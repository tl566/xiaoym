# -*- coding: utf-8 -*-
# config
"""
new Env('xiaoym参数设置');
"""
"""钢镚设置"""
cmzg_config = {
    'printf': 1,  # 实时日志开关,1为开，0为关

    'debug': 1,  # debug模式开关,1为开,0为关

    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers
}
"""小阅阅设置"""
xyy_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关

    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
}
