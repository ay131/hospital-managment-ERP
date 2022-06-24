from odoo import models, fields, api,_
 
class PatientReportWizard(models.TransientModel):

    _name = 'patient.report.wizard'
    _description = 'create report wizard'

    patient_id=fields.Many2one('hospital.patient',string='patient')
    age=fields.Integer(string='age' )



    def patient_report_action(self):
        domain=[]
        if self.patient_id:
            domain+=[('patient_id','=',self.patient_id.id)]
            
        if self.age:
            domain+=[('age','=',self.age)]

            
        patients=self.env['hospital.appointment'].search_read(domain)
        data={
            'patients':patients,
            
        }
        return self.env.ref('om_hospital.patient_reports_action').report_action(self,data=data)
      