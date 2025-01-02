# Copyright (c) 2024-2024 Huawei Technologies Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from components.utils.log import logger
from components.utils.file_open_check import ms_open
from components.utils.constants import TEXT_FILE_MAX_SIZE
from msit_graph.graph_extract.graph_extract import GraphAnalyze


def save_dym_op(data, path):
    with ms_open(path, 'w', TEXT_FILE_MAX_SIZE) as f:
        f.write("\t".join(["Op_Name", "SubOp_Name", "Input", "Output"]) + "\n")
        for row in data:
            f.write("\t".join(map(str, row)) + "\n")
    logger.info(f"The list of dynamic shape operator saved in {path}.")


class DynamicShape:
    def __init__(self, graph):
        self.graph = graph
        self.dynamic_to_static_edges = []

    @staticmethod
    def is_dynamic_shape(node):
        def is_dynamic_shape_attr(attr):
            return (attr.name == "_is_unknown_shape" or attr.name == "_force_unknown_shape") and attr.i == 1
        for attr in node.attribute:
            if is_dynamic_shape_attr(attr):
                return True
        return False

    def add_dynamic_op(self, parent_name, sub_node_name, inputs, outputs):
        dynamic_op = (parent_name, sub_node_name, inputs, outputs)
        if dynamic_op not in self.dynamic_to_static_edges:
            self.dynamic_to_static_edges.append(dynamic_op)

    def process_node(self, node, parent_name=None):
        if self.is_dynamic_shape(node):
            self.add_dynamic_op(parent_name or "", node.name, node.input, node.output)
        for attr in node.attribute:
            if hasattr(attr, 'g') and attr.g:
                for sub_node in attr.g.node:
                    self.process_node(sub_node, node.name)

    def find_dynamic_shape_op(self):
        for node in self.graph.node:
            self.process_node(node)
        return self.dynamic_to_static_edges



def execute(args):
    if args.type == "dshape":
        pb_graph = GraphAnalyze.load_graph_def_from_pbtxt(args.graph_path)
        dym_ops = DynamicShape(pb_graph).find_dynamic_shape_op()
        if os.path.exists(args.output) and os.path.isdir(args.output):
            save_dym_op(dym_ops, os.path.join(args.output, "dynamic_shape_ops.txt"))
        else:
            raise Exception("Please check if the directory exists.")