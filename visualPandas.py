#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo para la visualización de datos con módulo Pandas
"""
import pandas as pd

df = pd.read_csv('AirPassengers.csv')
print(df['time'][135])

names = ['Wade','James','Kobe','Curry']
total = [55, 50, 44, 36]
data_set = list(zip(names, total))
data_frame = pd.DataFrame(data = data_set, columns = ['Names', 'Total'])
data_frame.to_csv('points.csv', index=False, header=False)



