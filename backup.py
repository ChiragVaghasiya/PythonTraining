from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta
import calendar
from odoo import models, fields, api, _
from odoo.http import request
import fiscalyear

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
        
    @api.model
    def get_user_employee_details_payslip(self):
        uid = request.session.uid
        employee = self.env['hr.employee'].sudo().search_read([('user_id', '=', uid)], limit=1)

        # ********************* YTD SUMMARY IT STATEMENT TABLE ********************* #
        ytd_summary_it_statement_data = {}
        fiscalyear.START_MONTH = 4
        currentfiscalstart = fiscalyear.FiscalYear(datetime.now().year).start.date() if datetime.now().month < 4 else fiscalyear.FiscalYear(datetime.now().year+1).start.date()
        currentfiscalend = fiscalyear.FiscalYear(datetime.now().year).end.date()  if datetime.now().month < 4 else fiscalyear.FiscalYear(datetime.now().year+1).end.date()
        fetch_details = self.env['hr.payslip'].search([('employee_id', '=', employee[0].get('id')),('date_from','>=',currentfiscalstart),('date_to', '<=', currentfiscalend)])
        # total_amount = 0
        for details in fetch_details:
            for line in details.line_ids:
                if "Newid" in str(line.id):
                    pass
                else:
                    if line.salary_rule_id.taxable or line.salary_rule_id.is_deduction:
                        if line.salary_rule_id.taxable :
                            a = "Income"
                        elif line.salary_rule_id.is_deduction:
                            a = "Deduction"
                        if ytd_summary_it_statement_data.get(a):
                            if ytd_summary_it_statement_data.get(a).get(line.salary_rule_id.code):
                                if ytd_summary_it_statement_data.get(a).get(line.salary_rule_id.code).get(details.date_from.month):
                                    pass
                                else:
                                    ytd_summary_it_statement_data.get(a).get(line.salary_rule_id.code)[details.date_from.month] = line.amount
                            else:
                                ytd_summary_it_statement_data.get(a)[line.salary_rule_id.code] = {details.date_from.month : line.amount}
                        else:
                            ytd_summary_it_statement_data[a] = {line.salary_rule_id.code : {details.date_from.month : line.amount}}
        print("=================================",ytd_summary_it_statement_data)
                        # total_amount += line.amount

        last_day = calendar.monthrange(date.today().year, date.today().month)[1]
        last_full_date = date(date.today().year, date.today().month, last_day)
        current_date = last_full_date 
        enddate = date(currentfiscalend.year,currentfiscalend.month,currentfiscalend.day)
        if enddate > current_date:
            remaining_months = relativedelta(enddate, current_date).months
        else:
            remaining_months = 0
        fetch_details_projected = self.env['hr.contract'].search([('employee_id', '=', employee[0].get('id')),('state','=','open')])
        counter_month = datetime.now().month
        counter_year = datetime.now().year
        if( datetime.strptime(f'{counter_year}-{counter_month}', "%Y-%m") > datetime.strptime(f'{fetch_details_projected.date_end.year}-{fetch_details_projected.date_end.month}', "%Y-%m")):
            if self.env['hr.contract'].search([('employee_id', '=', employee[0].get('id')),('state','=','draft')]):
                fetch_details_projected = self.env['hr.contract'].search([('employee_id', '=', employee[0].get('id')),('state','=','draft')])
        for i in range(0,remaining_months+1):
            for projected_details in fetch_details_projected:
                for line in projected_details.applicable_salary_rule_ids:
                    if line.rule_id.taxable :
                        a = "Income"
                    elif line.rule_id.is_deduction:
                        a = "Deduction"
                    if ytd_summary_it_statement_data.get(a):
                        if ytd_summary_it_statement_data.get(a).get(line.rule_id.code):
                            if ytd_summary_it_statement_data.get(a).get(line.rule_id.code).get(counter_month):
                                pass
                            else:
                                ytd_summary_it_statement_data.get(a).get(line.rule_id.code)[counter_month] = line.amount
                        else:
                            ytd_summary_it_statement_data.get(a)[line.rule_id.code] = {counter_month : line.amount}
                    else:
                        ytd_summary_it_statement_data[a] = {line.rule_id.code : {counter_month : line.amount}}
            if(datetime.now().month == 12 or counter_month == 12):
                counter_month = 1
                counter_year += 1
            else:
                counter_month += 1
        total_of_months = 0
        for i in ytd_summary_it_statement_data:
            for j in ytd_summary_it_statement_data[i]:
                items = list(ytd_summary_it_statement_data[i][j].items())
                for key,value in ytd_summary_it_statement_data[i][j].items():
                    total_of_months += value
                items.insert(0, ('Total', total_of_months))
                total_of_months = 0
                ytd_summary_it_statement_data[i][j] = dict(items)
                
        print("===========ytd_summary_it_statement_data================",ytd_summary_it_statement_data)

        a = {
            'Income' : 
                {
                    'BASIC' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    'HRA' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    'GROSS' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    },

            'Deduction' : 
                {
                    'GRATUITY' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    'ESIC_EE' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    'PF_EE' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    'PT' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    'Total_Deduction' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    },

            'Net_Amount' : 
                {
                    'Total_amount' :[
                        ['Total',0.00],
                        ['Apr',0.00],
                        ['May',0.00],
                        ['Jun',0.00],
                        ['Jul',0.00],
                        ['Aug',0.00],
                        ['Sep',0.00],
                        ['Oct',0.00],
                        ['Nov',0.00],
                        ['Dec',0.00],
                        ['Jan',0.00],
                        ['Feb',0.00],
                        ['Mar',0.00]],
                    }
        }
        if employee :
            data = {
                'ytd_summary_it_statement_data' : ytd_summary_it_statement_data,
            }
            employee[0].update(data)
            return employee
        else:
            return False
