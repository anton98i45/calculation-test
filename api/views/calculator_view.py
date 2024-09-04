from django.views.generic.edit import FormView
from api.forms import CalculationForm
from api.serivces import CalculationService
from utils.constants import CALCULATOR_TEMPLATE


class CalculateView(FormView):
    template_name = CALCULATOR_TEMPLATE
    form_class = CalculationForm
    success_url = "/"

    def form_valid(self, form):
        expression = form.cleaned_data["expression"]
        result, error = CalculationService().safe_eval_expression(expression)
        context = self.get_context_data(form=form, result=result, error=error)
        return self.render_to_response(context)
