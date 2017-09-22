#
# document_summarizer/__init__.py - demo agent service adapter...
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from typing import List

from sn_agent.job.job_descriptor import JobDescriptor
from sn_agent.service_adapter.base import ModuleServiceAdapterABC


class DocumentSummarizer(ModuleServiceAdapterABC):
    type_name = "DocumentSummarizer"

    def __init__(self, app, service_ontology_node, required_service_nodes, name: str):
        super().__init__(app, service_ontology_node, required_service_nodes, name)

    def perform(self, job: JobDescriptor):
        pass

