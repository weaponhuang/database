# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
from v_site.models import Academys, Subjects, Teachers, Courses, Students, Comment, Homework

xadmin.site.register(Academys)
xadmin.site.register(Subjects)
xadmin.site.register(Teachers)
xadmin.site.register(Courses)
xadmin.site.register(Students)
xadmin.site.register(Comment)
xadmin.site.register(Homework)