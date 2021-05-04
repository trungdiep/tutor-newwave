from django.apps import AppConfig


class PlanCourseConfig(AppConfig):
    name = 'plan_course'
    verbose_name = "plane course"
    plugin_app = {
        'url_config':{
            'cms.djangoapp':{
                'namespace':'plan_course',
                'regex':'^plan-course/'
                'relative_path': 'urls',
            }
        }
    }