from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text', 'limit_date', 'visible', 'authors_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    

    # Sobrescreve método nativo da classe ModelAdmin
    # request.user = "pega um usuário logado"
    # obj = objeto que está sendo salvo (question)
    # Após a mudança do atributo do obj, o método nativo save model deve voltar ao modo de atuação anterior 
    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.authors_name = usuario
        super(QuestionAdmin, self).save_model(request, obj, form, change)

    #admin?
    def get_queryset(self, request):
        qs = super(QuestionAdmin, self).get_queryset(request)
        qs = qs.filter(authors_name = request.user)
        return qs


admin.site.register(Question, QuestionAdmin)
