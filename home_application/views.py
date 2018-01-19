# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
from common.log import logger
from home_application.models import MultRecord


def index(request):
    return HttpResponse('Hello World')


def multiplication_computer(request):
    multiplier = int(request.POST.get('multiplier'))
    multiplicand = int(request.POST.get('multiplicand'))
    mult_result = multiplier * multiplicand
    logger.debug(multiplier)
    mult_record = MultRecord(multiplier=multiplier, multiplicand=multiplicand, mult_result=mult_result)
    mult_record.save()
    return render_json({"result": True, "mult_result": mult_result})

def home(request):
    """
    首页
    """
    all_record = MultRecord.objects.all()
    ctx = {
        'all_record': all_record
    }
    return render_mako_context(request, '/home_application/home.html', ctx)


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
