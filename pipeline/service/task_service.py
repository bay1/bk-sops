# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa
import importlib

from pipeline.conf import settings

adapter_api = importlib.import_module(settings.PIPELINE_ENGINE_ADAPTER_API)


def run_pipeline(pipeline, instance_id=None):
    adapter_api.run_pipeline(pipeline, instance_id)


def pause_pipeline(pipeline_id):
    return adapter_api.pause_pipeline(pipeline_id)


def revoke_pipeline(pipeline_id):
    return adapter_api.revoke_pipeline(pipeline_id)


def resume_pipeline(pipeline_id):
    return adapter_api.resume_pipeline(pipeline_id)


def pause_activity(act_id):
    return adapter_api.pause_activity(act_id)


def resume_activity(act_id):
    return adapter_api.resume_activity(act_id)


def retry_activity(act_id, inputs=None):
    return adapter_api.retry_activity(act_id, inputs=inputs)


def skip_activity(act_id):
    return adapter_api.skip_activity(act_id)


def skip_exclusive_gateway(gateway_id, flow_id):
    return adapter_api.skip_exclusive_gateway(gateway_id, flow_id)


def forced_fail(act_id):
    return adapter_api.forced_fail(act_id)


def get_state(node_id):
    return adapter_api.get_state(node_id)


def get_topo_tree(pipeline_id):
    return adapter_api.get_topo_tree(pipeline_id)


def get_inputs(act_id):
    return adapter_api.get_inputs(act_id)


def get_outputs(act_id):
    return adapter_api.get_outputs(act_id)


def get_activity_histories(act_id):
    return adapter_api.get_activity_histories(act_id)


def callback(act_id, data=None):
    return adapter_api.callback(act_id, data)


def get_single_state(act_id):
    return adapter_api.get_single_state(act_id)
