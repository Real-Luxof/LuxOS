from ..utilityfolder.blocks import *
import api

plr = api.entity(varname=plr,character="#000000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[104, 268],replace=Air,inventory=api.inventory(slotnum=20,slotdata={"slot1": None,"slot2": None,"slot3": None,"slot4": None,"slot5": None,"slot6": None,"slot7": None,"slot8": None,"slot9": None,"slot10": None,"slot11": None,"slot12": None,"slot13": None,"slot14": None,"slot15": None,"slot16": None,"slot17": None,"slot18": None,"slot19": None},selectedindex="slot1"),dead=False,deffactor=0.5,atkfactor=0.5,reach=1,handvalue=1)
worldtype = [500, Limit(upper_limit=25, lower_limit=495)]