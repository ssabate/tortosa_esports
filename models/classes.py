# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Persona(models.Model):
    _name = 'esports.persona'
    name = fields.Char('Nom', required=True)
    cognoms = fields.Char('Cognoms', required=True)
    dni = fields.Char('DNI', size=9, required=True)
    tlf1 = fields.Char('Telèfon fix', size=9)
    tlf2 = fields.Char('Telèfon mòbil', size=9)
    email = fields.Char('email')
    adressa = fields.Char('Adreça')
    codiPostal = fields.Char('Codi postal', size=5)
    poblacio = fields.Char('Població')

class Jugador():
    _name = 'esports.jugador'
    _inherit = 'esports.persona';
    sexe = fields.Selection([('Masculi', 'Masculí'), ('Femeni', 'Femení'), ('Indeterminat', 'Indeterminat')], 'Sexe', default='Indeterminat')
    dataNaix = fields.Date('Data naixement', required=True)
    categoria_id = fields.Many2one('esports.categoria', 'Categoria on juga')
    posicions_id = fields.Many2many('esports.posicio',string='Llista de posicions')

class Entrenador():
    _name = 'esports.entrenador'
    _inherit = 'esports.persona';
    categories_id = fields.One2many(
        'esports.categoria',
        # related model
        'entrenador_id',
        # field for "this" on related model
        'Categories que entrena')

#class JugadorEntrenador(Jugador,Entrenador):
#    _name = 'esports.jugador.entrenador'

class Categoria(models.Model):
    _name = 'esports.categoria'
    name = fields.Selection([('Junior', 'Junior'), ('Senior', 'Senior'), ('Infantil', 'Infantil')], 'Descripció')
    entrenador_id = fields.Many2one('esports.entrenador', 'Entrenador')
    jugadors_id = fields.One2many(
        'esports.jugador',
        # related model
        'categoria_id',
        # field for "this" on related model
        'Jugadors de la categoria')

class Posicio(models.Model):
    _name = 'esports.posicio'
    name = fields.Selection([('Porter', 'Porter'), ('LateralEsq', 'Lateral esquerre'), ('LateralDret', 'Lateral dret')], 'Posició')
    jugadors_id = fields.Many2many('esports.jugador',string='Llista de jugadors')

