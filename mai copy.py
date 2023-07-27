import odoorpc
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

self = odoorpc.ODOO('localhost', port=8072)
self.login('HRMS', 'admin', 'admin')

counter_mounths = 4
counter_break = 0

for emp in self.env['hr.employee'].search([('id', '=', 70)]):
    while(True):
        date_start = ( date.today() - relativedelta(months=counter_mounths,day=1) ).strftime("%Y-%m-%d %H:%M:%S")
        date_end = ( date.today() - relativedelta(months=counter_mounths,day=31) ).strftime("%Y-%m-%d %H:%M:%S")
        monthly_attendance = self.env['hr.attendance'].search([('employee_id', '=', emp), ('check_in', '>=', date_start), ('check_out', '<=', date_end)])
        print("===================",len(monthly_attendance),date_start)
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
        for i in montyly_attendance_obj:
            if((i.check_in >=  datetime.now() - relativedelta(months=5,day=1))and (i.check_out <= datetime.now() - relativedelta(months=5,day=31))):
                print("=================check_in===============",i.check_in)
                print("=================check_out===============",i.check_out)
        total_hours = sum(montyly_attendance_obj.mapped('worked_hours'))
        data = {
            'start_date': date_start,
            'end_date': date_end,
            'total_hours': round(total_hours, 2),
            'employee_id': emp
        }
        if self.env['attendance.history'].sudo().search([('employee_id', '=', emp), ('start_date', '=', date_start), ('end_date', '=', date_end)]):
            continue
        else:
            self.env['attendance.history'].create(data)
        # montyly_attendance_obj.with_context(allow_modify_confirmed_sheet=True).unlink()







        #        counter_mounths = 4
        # counter_break = 0

        # for emp in self.env['hr.employee'].search([]):
        #     while(True):
        #         date_start = date.today() - relativedelta(months=counter_mounths,day=1)
        #         date_end = date.today() - relativedelta(months=counter_mounths,day=31)
        #         monthly_attendance = self.env['hr.attendance'].search([('employee_id', '=', emp.id), ('check_in', '>=', date_start), ('check_out', '<=', date_end)])
        #         if not monthly_attendance:
        #             counter_break += 1
        #             if counter_break == 2:
        #                 counter_break = 0
        #                 counter_mounths = 4
        #                 break
        #             else:
        #                 counter_mounths += 1
        #                 continue
        #         counter_mounths += 1
        #         total_hours = sum(monthly_attendance.mapped('worked_hours'))
        #         data = {
        #             'start_date': date_start,
        #             'end_date': date_end,
        #             'total_hours': round(total_hours, 2),
        #             'employee_id': emp.id
        #         }
        #         if self.env['attendance.history'].search([('employee_id', '=', emp.id), ('start_date', '=', date_start), ('end_date', '=', date_end)]):
        #             continue
        #         else:
        #             self.env['attendance.history'].create(data)
            # self.env['hr.attendance'].sudo().search([('employee_id', '=', emp.id), ('check_out', '<=', date.today() - relativedelta(months=3,day=31))]).unlink()