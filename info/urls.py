from django.urls import path
from .views import (
    about,
    apply,
    base,
    employers,
    home,
    impact,
    learners,
    training,
    terms,
    institutions,
    discourse,
    partners,
    resources,
    faq,
    aptitude,
)

app_name = 'info'

urlpatterns = [
    path('', home.Home.as_view(), name='Home'),
    path('about', about.About.as_view(), name='About'),
    path('what-people-say', discourse.Discourse.as_view(), name='Discourse'),
    path('learners', learners.Learners.as_view(), name='Learners'),
    path('programs', training.Training.as_view(), name='Training'),
    path('employers-network', employers.Employers.as_view(), name='Employers'),
    path('insitutions-network', institutions.Institutions.as_view(), name='Institutions'),
    path('impact', impact.Impact.as_view(), name='Impact'),
    path('apply', apply.Apply.as_view(), name='Apply'),
    path('privacy-policy', terms.PrivacyPolicy.as_view(), name='Privacy'),
    path('program-partners', partners.Partners.as_view(), name='Partners'),
    path('cyber-aptitude', aptitude.Aptitude.as_view(), name='Aptitude'),
    path('resources', resources.Resources.as_view(), name='Resources'),
    path('faq', faq.FAQ.as_view(), name='FAQ'),
    path('tos', terms.TOS.as_view(), name='TOS'),
]