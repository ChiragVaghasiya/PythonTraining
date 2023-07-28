import odoorpc
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

self = odoorpc.ODOO('localhost', port=8072)
self.login('HRMS', 'admin', 'admin')

counter_mounths = 4
counter_break = 0

for emp in self.env['hr.employee'].search([]):
    while(True):
        date_start = ( date.today() - relativedelta(months=counter_mounths,day=1) ).strftime("%Y-%m-%d 00:00:00")
        date_end = ( date.today() - relativedelta(months=counter_mounths,day=31) ).strftime("%Y-%m-%d 23:59:59")
        monthly_attendance = self.env['hr.attendance'].search([('employee_id', '=', emp), ('check_in', '>=', date_start), ('check_out', '<=', date_end)])
        if not monthly_attendance:
            counter_break += 1
            if counter_break == 2:
                counter_break = 0
                counter_mounths = 4
                break
            else:
                counter_mounths += 1
                continue
        counter_mounths += 1
        montyly_attendance_obj = self.env['hr.attendance'].browse(monthly_attendance)
        total_hours = sum(montyly_attendance_obj.mapped('worked_hours'))
        data = {
            'start_date': date_start,
            'end_date': date_end,
            'total_hours': round(total_hours, 2),
            'employee_id': emp
        }
        if self.env['attendance.history'].search([('employee_id', '=', emp), ('start_date', '=', date_start), ('end_date', '=', date_end)]):
            continue
        else:
            self.env['attendance.history'].create(data)
        montyly_attendance_obj.with_context(allow_modify_confirmed_sheet=True).unlink()