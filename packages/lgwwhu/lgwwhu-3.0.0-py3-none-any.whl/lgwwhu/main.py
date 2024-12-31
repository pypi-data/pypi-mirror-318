#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:34:31 2024

@author: xiaoxiami
"""

import bilby
import sys
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from bilby.gw.conversion import redshift_to_luminosity_distance
from astropy import constants 
from pycbc.waveform import get_fd_waveform, get_td_waveform

import warnings
warnings.filterwarnings("ignore", "Wswiglal-redir-stdio")
import lal

# 定义常量类
class myconst:
    Mpc2M = 3.08568e22
    Msun = constants.M_sun.value
    as2rad = 0.0174532925 / 3600
    c = constants.c.value
    G = constants.G.value

# 计算距离
def lumDis(z):
    """
    in Mpc
    """
    return redshift_to_luminosity_distance(redshift=z)



def gravitational_lens_with_amplification(**kwords):
    # 提取字典中的参数
    ml = kwords.get('ml')  # 镜质量
    beta = kwords.get('beta')  # 入射角
    zs = kwords.get('zs')  # 背景源红移
    zl = kwords.get('zl')  # 镜红移
    lens_model = kwords.get('lens_model')  # 透镜模型
    sigmav = kwords.get('sigmav', 250)  # 速度弥散，默认250 km/s
    f_range = kwords.get('f_range', None)  # 频率范围，用于放大因子计算

    # 检查参数
    if lens_model not in ['point-mass', 'SIS']:
        raise ValueError("Unsupported lens model. Choose either 'point-mass' or 'SIS'.")
    if f_range is None or not isinstance(f_range, (list, tuple)) or len(f_range) != 3:
        raise ValueError("f_range must be a list or tuple with three elements: [f_min, f_max, delta_f].")

    # 解构频率范围
    f_min, f_max, delta_f = f_range
    frequencies = np.arange(f_min, f_max+delta_f, delta_f)  # 生成频率数组

    # 打印参数以测试
    print(f"ML: {ml}, beta: {beta}, zs: {zs}, zl: {zl}, lens_model: {lens_model}, sigmav: {sigmav}, f_range: {f_range}")
    
    # 计算距离
    DL = lumDis(zl) * myconst.Mpc2M / (1. + zl) / (1. + zl)
    DS = lumDis(zs) * myconst.Mpc2M / (1. + zs) / (1. + zs)
    DLS = DS - DL * (1 + zl) / (1 + zs)
    beta *= myconst.as2rad  # 转换为无量纲角度

    result = {}

    if lens_model == 'point-mass':
        ml = ml * myconst.Msun * myconst.G / myconst.c / myconst.c  # 修改这里，转换为米
        # 爱因斯坦半径
        thetaE = np.sqrt(4 * ml * DLS / DS / DL)  # 无量纲

        # 计算角度
        theta_plus = (beta + np.sqrt(beta * beta + 4 * thetaE * thetaE)) / 2.0
        theta_minus = (beta - np.sqrt(beta * beta + 4 * thetaE * thetaE)) / 2.0

        # 偏转角
        alpha1 = np.absolute(-4 * ml / theta_plus / DL) / myconst.as2rad
        alpha2 = np.absolute(-4 * ml / theta_minus / DL) / myconst.as2rad

        # 振幅放大因子
        smu1 = np.sqrt(theta_plus / np.sqrt(theta_plus**2 - theta_minus**2))
        smu2 = np.sqrt(-theta_minus / np.sqrt(theta_plus**2 - theta_minus**2))

        # 时间延迟
        timedelay = 4 * ml * (1 + zl) * (
            (theta_plus**2 - theta_minus**2) / (2 * thetaE**2) +
            np.log(-theta_plus / theta_minus)
        ) / myconst.c

        # 计算放大因子 F(f) 对于每个频率
        y = beta / thetaE
        w2 = 8 * np.pi *  ml * (1 + zl) / myconst.c

        F_values = []  # 存储每个频率的放大因子
        for f in frequencies:
            xm_val = (y + np.sqrt(y**2 + 4)) / 2
            phi_y = (xm_val - y)**2 / 2 - np.log(xm_val)
            F_value = complex(mp.exp(np.pi*w2*f/4+(1j*w2*f/2)*(np.log(w2*f/2)-2*phi_y))*mp.gamma(1-1j*w2*f/2)*complex(mp.hyp1f1(1j*w2*f/2, 1, 1j*w2*f*y**2/2)))
            F_values.append(F_value)

        result={
            "thetaE": thetaE,
            "theta_plus": theta_plus,
            "theta_minus": theta_minus,
            "alpha1": alpha1,
            "alpha2": alpha2,
            "smu1": smu1,
            "smu2": smu2,
            "timedelay": timedelay,
            "y": y,
            "w2": w2,
            "frequencies": frequencies,
            "F_values": F_values,
        }
        return result

    elif lens_model == 'SIS':
        thetaE = 4 * np.pi * sigmav * sigmav * DLS / DS
        
        if beta > thetaE:
            print(f"The misalignment angle should be less than Einstein angle, but it is larger.\nthetaE = {thetaE / myconst.as2rad} as\nExit...\n")
            sys.exit(0)
            
        theta_plus = beta + thetaE
        theta_minus = beta - thetaE
        smu1 = np.sqrt(abs(theta_plus / (theta_plus - thetaE)))
        smu2 = np.sqrt(abs(abs(theta_minus) / (abs(theta_minus) - thetaE)))
        timedelay = 2 * (1 + zl) * thetaE * beta * DL * DS / DLS
        alpha1 = 1
        alpha2 = -1

        
        # 打印所有结果
        print(f"thetaE: {thetaE} rad")
        print(f"theta_plus: {theta_plus} rad")
        print(f"theta_minus: {theta_minus} rad")
        print(f"alpha1: {alpha1} rad")
        print(f"alpha2: {alpha2} rad")
        print(f"smu1: {smu1}")
        print(f"smu2: {smu2}")
        print(f"timedelay: {timedelay} seconds")
        
        return thetaE, theta_plus, theta_minus, alpha1, alpha2, smu1, smu2, timedelay


def generate_waveform(**parameters):
    # 提取输入参数
    m1 = parameters['mass1']
    m2 = parameters['mass2']
    distance = parameters['distance']

    # 动态设置频率范围
    total_mass = m1 + m2
    if total_mass > 1000:  # 超大质量系统
        f_lower = 1e-4  # 最低频率 (1 mHz)
        f_max = 1  # 最大频率 (1 Hz)
        delta_f = 1 / 400  # 频率分辨率 (低频)
    else:  # 较小质量系统
        f_lower = 10  # 最低频率 (10 Hz)
        f_max = 1200  # 最大频率 (1200 Hz)
        delta_f = 1 / 4  # 频率分辨率 (高频)

    # 更新参数字典
    parameters['f_lower'] = f_lower
    parameters['delta_f'] = delta_f
    parameters['f_final'] = f_max

    # 生成波形
    hp, hc = get_fd_waveform(parameters)

    # 返回波形和频率范围
    return hp, hc, f_lower, f_max

def compute_lensed_waveform(waveform_params, lens_params):
    # 生成波形并获取频率范围
    hp, hc, f_lower, f_max = generate_waveform(**waveform_params)

    # Step 1: 筛选频率和波形数据
    valid_indices = (hp.sample_frequencies >= f_lower) & (hp.sample_frequencies <= f_max)
    filtered_frequencies = hp.sample_frequencies[valid_indices]
    filtered_hp = hp.data[valid_indices]
    filtered_hc = hc.data[valid_indices]

    # Step 2: 更新频率范围到 lens_params 并计算放大因子
    lens_params['f_range'] = [
        filtered_frequencies[0],
        filtered_frequencies[-1],
        filtered_frequencies[1] - filtered_frequencies[0]
    ]
    lens_results = gravitational_lens_with_amplification(**lens_params)
    F_values = np.array(lens_results['F_values'], dtype=complex)

    # Step 3: 计算放大后的波形
    lensed_hp = filtered_hp * F_values
    lensed_hc = filtered_hc * F_values

    # 返回计算结果
    return {
        "frequencies": filtered_frequencies,
        "amplification": F_values,
        "original_waveformhp": filtered_hp,
        "original_waveformhc": filtered_hc,
        "lensed_waveformhp": lensed_hp,
        "lensed_waveformhc": lensed_hc    
    }
