from django.contrib import admin

from .models import Evaluation, Question

# Register your models here.



class QuestionInline(admin.TabularInline):
	model = Question
	extra = 0


class EvaluationAdmin(admin.ModelAdmin):
	inlines = [
		QuestionInline
	]

	class Meta:
		model = Evaluation


admin.site.register(Evaluation, EvaluationAdmin)


from .models import MpesaPayment


admin.site.register(MpesaPayment)