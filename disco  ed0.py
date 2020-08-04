# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:25 2020

@author: SCE
"""
import time
import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

while True:
    color=random.randrange(16)
    mc.setBlocks(x+11,y-1,z+11,x-11,y-1,z-11,95,color)
    time.sleep(0.5)
