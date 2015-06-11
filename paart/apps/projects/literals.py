from django.utils.translation import ugettext_lazy as _

INFRASTRUCTURE_NEW = 'N'
INFRASTRUCTURE_OLD = 'O'

INFRASTRUCTURE_CHOICES = (
    (INFRASTRUCTURE_NEW, _(u'New')),
    (INFRASTRUCTURE_OLD, _(u'Existing')),
)

NEW_TASK = 'N'
IN_PROCESS_TASK = 'P'
COMPLETED_TASK = 'C'

TASK_STATUS = (
    (NEW_TASK, _(u'New task')),
    (IN_PROCESS_TASK, _(u'In process')),
    (COMPLETED_TASK, _(u'Completed task'))
)