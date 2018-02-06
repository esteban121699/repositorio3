# -*- coding: utf-8 -*-

from odoo import models, fields, api

class docente(models.Model):
    _name="itd.docente"
    _description="Docente"
    _rec_name = "nombre"

    nombre=fields.Char("NOMBRE:")
    apellido= fields.Char("APELLIDO:")
    email= fields.Char("EMAIL:")
    phone= fields.Char("TELEFONO FIJO:")
    movil= fields.Char("MOVIL:")
    direccion= fields.Char("DIRECCION;")
    dni= fields.Char("DNI:")
    id_curso= fields.One2many("itd.curso","id_docente")

class alumno(models.Model):
    _name = "itd.alumno"
    _description = "Alumno"
    _rec_name = "nombre"

    nombre = fields.Char("NOMBRE:")
    apellido = fields.Char("APELLIDO:")
    email = fields.Char("EMAIL:")
    phone = fields.Char("TELEFONO FIJO:")
    movil = fields.Char("MOVIL:")
    direccion = fields.Char("DIRECCION:")
    dni = fields.Char("DNI:")
    nacimiento=fields.Date("FECHA DE NACIMIENTO:")
    estado=fields.Selection([('1','Registrado'),('2','Matriculado'),('3','Retirado')],'ESTADO')
    id_nota= fields.One2many("itd.nota","id_alumno")

class nota(models.Model):
    _name = "itd.nota"
    pra1=fields.Integer("PRACTICA 1:")
    pra2=fields.Integer("PRACTICA 2:")
    par=fields.Integer("EXAMEN PARCIAL:")
    fin=fields.Integer("EXAMEN FINAL:")
    pp=fields.Integer("PROMEDIO PONDERADO:")
    id_alumno=fields.Many2one("itd.alumno", string="Alumno")
    id_curso=fields.Many2one("itd.curso", string="Curso")

class curso(models.Model):
    _name = "itd.curso"
    nombre = fields.Char("CURSO:")
    descripcion = fields.Char("DESCRIPCION:")
    tiempo = fields.Char("TIEMPO(HR):")
    id_docente=fields.Many2one("itd.docente")
    id_nota= fields.One2many("itd.nota","id_curso")
