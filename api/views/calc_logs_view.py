from django.views.generic import ListView
from api.models import CalculationLog
from utils.constants import CALCULATION_LOGS_TEMPLATE


class CalculationLogListView(ListView):
    model = CalculationLog
    template_name = CALCULATION_LOGS_TEMPLATE
    context_object_name = "logs"
