# -*- coding: cp1252 -*-
# es necesario importar todos estos m�dulos para poder trabajar con
# TurtleArt
# Plugin Author: Joriks <jorikst@gmail.com>
import gst
import gtk
from fcntl import ioctl
import os
from gettext import gettext as _
from plugins.plugin import Plugin
from TurtleArt.tapalette import make_palette
from TurtleArt.talogo import media_blocks_dictionary, primitive_dictionary
from TurtleArt.tautils import get_path, debug_output
import logging
_logger = logging.getLogger('TurtleArt-activity Robot plugin')
class SugarRobot(Plugin):

    def __init__(self,parent):
        self._parent = parent
        self._status = False

    def setup(self):
        palette = make_palette('Robot',
                               colors=["#006060", "#A00000"],
                               help_string=_('Plugin de robot para TurtleArt'))
        
        #Definici�n de la primitiva de avance
        primitive_dictionary['RobotAvanza'] = self._boton_adelante
        #Creaci�n del bot�n Avanzar
        palette.add_block('RobotAvanza',
                          style='basic-style-larg',
                          prim_name='RobotAvanza',
                          help_string=_('Boton que hace avanzar al robot'))
        self._parent.lc.def_prim('RobotAvanza', 1, lambda self,
                                 valor: primitive_dictionary['RobotAvanza'](valor))

        #Definici�n de la primitiva de retroceso
        primitive_dictionary['RobotRetrocede'] = self._boton_retroceso
        #Creaci�n del bot�n Retroceder
        palette.add_block('RobotRetrocede',
                          style='basic-style-larg',
                          prim_name='RobotRetrocede',
                          help_string=_('Boton que hace retroceder al robot'))
        self._parent.lc.def_prim('RobotRetrocede', 1, lambda self,
                                 valor: primitive_dictionary['RobotRetrocede'](valor))

        #Definici�n de la primitiva de giro izquierda
        primitive_dictionary['RobotIzquierda'] = self._boton_izquierda
        #Creaci�n del bot�n giro izquierda
        palette.add_block('RobotIzquierda',
                          style='basic-style-larg',
                          prim_name='RobotIzquierda',
                          help_string=_('Boton que hace girar a la izquierda al robot'))
        self._parent.lc.def_prim('RobotIzquierda', 1, lambda self,
                                 valor: primitive_dictionary['RobotIzquierda'](valor))

        #Definici�n de la primitiva de giro derecha
        primitive_dictionary['RobotDerecha'] = self._boton_Derecha
        #Creaci�n del bot�n giro derecha
        palette.add_block('RobotDerecha',
                          style='basic-style-larg',
                          prim_name='RobotDerecha',
                          help_string=_('Boton que hace girar a la derecha al robot'))
        self._parent.lc.def_prim('RobotDerecha', 1, lambda self,
                                 valor: primitive_dictionary['RobotDerecha'](valor))


    def _boton_adelante(self,valor):
        print "Valor de avance", valor

    def _boton_retroceso(self,valor):
        print "Valor de retroceso", valor

    def _boton_izquierda(self,valor):
        print "Valor de avance a la izquierda", valor

    def _boton_derecha(self,valor):
        print "Valor de avance a la derecha", valor

