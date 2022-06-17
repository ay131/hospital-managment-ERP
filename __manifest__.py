# -*- coding: utf-8 -*-
{
    'name': "hospital management ",

    'summary': "hospital management system for all hospitalllll lllll",

    'description': "hospital management system",
    'sequence':-100,
 

    'author': "abyo Company",
    'website': "http://www.com",

 
    # for the full list
    'category': 'hospital',
    'version': '0.1',
    'application' : 'Ture',
    # any module necessary for this one to work correctly
    'depends': ['sale','base','mail','product'],

    # always loaded
    'data': [
        # security
        'security/ir.model.access.csv',

        # data
        'data/data.xml',
        #wizard
        'wizard/appointment_report_view.xml',
        'wizard/create_appointment_view.xml',
        # views
        'views/doctor.xml',
        'views/appiontment.xml',
        'views/patient.xml',
        'views/menu.xml',
        # report
        'report/appointment_report_templet.xml',
        'report/doctor_report_templet.xml',
        'report/patient_report_templet.xml',
        'report/report.xml',
        
   
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}