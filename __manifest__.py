# -*- coding: utf-8 -*-
{
    'name': "hospital management ",

    'summary': "hospital management system for all hospitalllll lllll",

    'description': "hospital management system",
    'sequence':-100,
 

    'author': "abyo Company",
    'website': "http://www.abyo.com",

 
    # for the full list
    'category': 'hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','base','mail','product'],

    # always loaded
    'data': [
        # security
        'security/ir.model.access.csv',

        # data
        'data/data.xml',
    
        # views
        'views/doctor.xml',
        'views/appiontment.xml',
        'views/patient.xml',
        'views/menu.xml',
        
   
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}