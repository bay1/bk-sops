# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component
from blueking.component.shortcuts import get_client_by_user

__group_name__ = _(u"个人服务(SELFAPI)")


class GetDfuasgeService(Service):
    __need_schedule__ = False  # 是否异步执行

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        client = get_client_by_user(executor)

        host_ip = data.get_one_of_inputs('self_server_ip')
        host_system = data.get_one_of_inputs('self_server_system')
        hsot_disk = data.get_one_of_inputs('self_server_disk')

        api_kwargs = {
            'ip': host_ip,
            'system': host_system,
            'disk': hsot_disk
        }
        api_result = client.self_server.get_dfusage_bay1(api_kwargs)

        if api_result['result']:
            data.set_outputs('data', api_result)
            return True
        else:
            data.set_outputs('ex_data', api_result['message'])
            return False

    def outputs_format(self):
        return [
            self.OutputItem(name=_(u'JOB任务ID'), key='job_inst_id', type='int'),
            self.OutputItem(name=_(u'JOB任务链接'), key='job_inst_url', type='str')
        ]


class GetDfuasgeComponent(Component):
    name = _(u'磁盘容量查询')
    code = 'self_server_get_dfusage'
    bound_service = GetDfuasgeService
    form = settings.STATIC_URL + 'custom_atoms/test/self_server_get_dfusage.js'
