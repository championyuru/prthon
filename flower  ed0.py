# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:25 2020

@author: SCE
"""
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

while True:
    x,y,z =mc.player.getTilePos ()
    mc.setBlock(x,y,z,38)
    time.sleep(0.1)

