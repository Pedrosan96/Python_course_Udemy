#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo para usarlo en Debbuging
"""
import pdb


print('Statement 1')
for i in range(5):
    print('Statement'+ str(i+2))
pdb.set_trace()      ##El debugger se abre con esta linea
print('Statement 7')
