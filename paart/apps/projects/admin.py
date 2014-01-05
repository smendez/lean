from __future__ import absolute_import

from django.contrib import admin

from .models import (Goal, FiscalYear, Purpose, Classification, Stage, Benefit,
    Topic, Opportunity, Department, Priority, Methodology, Project, ProjectInfo, State, ProjectStateHistory)

from .forms import ProjectStateHistoryUserForm


class FiscalYearAdmin(admin.ModelAdmin):
    model = FiscalYear


class PurposeAdmin(admin.ModelAdmin):
    model = Purpose
    list_display = ('label', 'enabled')


class ClassificationAdmin(admin.ModelAdmin):
    model = Classification
    list_display = ('label', 'enabled')


class StageAdmin(admin.ModelAdmin):
    model = Stage
    list_display = ('label', 'enabled')


class BenefitAdmin(admin.ModelAdmin):
    model = Benefit
    list_display = ('label', 'enabled')


class TopicAdmin(admin.ModelAdmin):
    model = Topic
    list_display = ('label', 'enabled')


class GoalAdmin(admin.ModelAdmin):
    model = Goal
    list_display = ('label', 'enabled')


class OpportunityAdmin(admin.ModelAdmin):
    model = Opportunity
    list_display = ('label', 'enabled')


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('label', 'enabled')


class PriorityAdmin(admin.ModelAdmin):
    model = Priority
    list_display = ('label', 'enabled')


class MethodologyAdmin(admin.ModelAdmin):
    model = Methodology
    list_display = ('label', 'enabled')


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    #list_display = ('label', 'fiscal_year', 'purpose', 'classification', 'department')
    #filter_horizontal = ('opportunity', 'sharing_benefit')


class ProjectProjectInfoAdmin(admin.ModelAdmin):
    model = ProjectInfo
    #list_display = ('fiscal_year', 'purpose', 'classification', 'department')
    #filter_horizontal = ('opportunity', 'sharing_benefit')


class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = ('label', 'enabled', 'default')


class ProjectStateHistoryAdmin(admin.ModelAdmin):
    model = ProjectStateHistory
    form = ProjectStateHistoryUserForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(FiscalYear, FiscalYearAdmin)
admin.site.register(Purpose, PurposeAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Methodology, MethodologyAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectInfo, ProjectProjectInfoAdmin)
admin.site.register(ProjectStateHistory, ProjectStateHistoryAdmin)
