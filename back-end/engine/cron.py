#https://django-cron.readthedocs.io/en/latest/installation.html

from django_cron import CronJobBase, Schedule

class Cron(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'engine.cron'    # a unique code

    def do(self):
    	#let batch_size
        #request.engine()