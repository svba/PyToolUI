from dashboardui.dashboard import Dashboard
from dashboardui.dashboards.formdashboard import DashboardFormEditAction

class TableDashboard(Dashboard):
    def __init__(self, title, description, lst, editable=False):
        super(TableDashboard, self).__init__(title, description = description, template ="simple_table.html", rows=lst)
        self.editable = editable
        self._add_event("edit", DashboardFormEditAction)

    def get_additional_render_data(self):
        return {'editable' : self.editable}
