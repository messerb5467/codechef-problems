#!/usr/bin/env python3
import argparse
import itertools
import logging
import networkx as nx
import re
import sys
from dataclasses import dataclass
from queue import LifoQueue

@dataclass(frozen=True)
class CompressedString:
    number: int
    chars: str
    is_substring: bool

    def __str__(self):
        return ''.join(list(self.chars)*self.number)

class DecompressedString:
    def __init__(self, comp_string, msg_level=None):
        self.comp_string = comp_string + "!"
        self.comp_string_network = nx.DiGraph()
        self.string_index = 0
        self.number_stack = LifoQueue()
        self.char_stack = LifoQueue()
        self.node_stack = LifoQueue()
        self.edge_stack = LifoQueue()

        logging.basicConfig(stream=sys.stderr,
                            level=msg_level)

    def _get_compressed_substring(self, end_char):
        accumulator = ''
        while self.string_index != len(self.comp_string) and \
              self.comp_string[self.string_index] != end_char:
            char = self.comp_string[self.string_index]
            if char == "]" or \
               char == "!":
                break
            accumulator += char
            self.string_index += 1
        return accumulator

    def _get_string_until_char_and_stack(self, end_char, stack):
        substring = self._get_compressed_substring(end_char)
        if substring:
            logging.debug(f"The substring is {substring}")
            stack.put(substring)
            return True
        return False

    def _update_string_index(self):
        if self.string_index < len(self.comp_string):
            self.string_index += 1

    def _add_node_to_graph(self, is_substring=False):
        self._update_string_index()
        if self.string_index < len(self.comp_string):
            if re.search(r'[a-z]', self.comp_string[self.string_index]):
                self._get_string_until_char_and_stack(']', self.char_stack)
            elif re.search(r'[0-9]', self.comp_string[self.string_index]):
                edge_weight = self.number_stack.get()
                logging.debug(f"The edge weight is: {edge_weight}")
                self.edge_stack.put(edge_weight)
                return False
        self._update_string_index()
        self.comp_string_network.add_node(CompressedString(int(self.number_stack.get() if not self.number_stack.empty() else 1),
                                                           self.char_stack.get(),
                                                           is_substring))
        nodes = list(self.comp_string_network.nodes)
        logging.debug(f"The nodes are: {str(nodes)}")
        node_cnt = len(nodes)
        if node_cnt > 1:
            # node_cnt is 1-based while indexing is 0-based.
            self.comp_string_network.add_edge(nodes[node_cnt - 2], nodes[node_cnt - 1], weight=1)
            if not self.node_stack.empty():
                logging.debug("Adding the back edge in")
                self.comp_string_network.add_edge(nodes[node_cnt - 1], self.node_stack.get(), weight=self.edge_stack.get())
        elif node_cnt == 1 and is_substring:
            logging.debug("Putting an item on the node stack.")
            self.node_stack.put(nodes[node_cnt - 1])

        return True

    def parse_comp_string(self, is_substring=False):
        if self.string_index == len(self.comp_string):
            return
        else:
            search_res = re.search(r'\[', self.comp_string[self.string_index:])
            end_char = '[' if search_res else '!'
            stack = self.number_stack if search_res else self.char_stack
            stack_result = self._get_string_until_char_and_stack(end_char, stack)
            if stack_result:
                add_node_result = self._add_node_to_graph(is_substring=is_substring)
                if add_node_result:
                    self.parse_comp_string()
                else:
                    self.parse_comp_string(is_substring=True)

    def print_decomp_string(self):
        simple_cycles = list(nx.simple_cycles(self.comp_string_network))
        if simple_cycles:
            nodes = list(self.comp_string_network.nodes)
            network_str_form = ''
            reversed_cycles = list(reversed(nodes))
            for node in reversed_cycles:
                node_idx = reversed_cycles.index(node)
                weight = int(self.comp_string_network.get_edge_data(node, reversed_cycles[node_idx - 1])["weight"])
                if weight > 1:
                    j = 0
                    while j < weight:
                        network_str_form += ''.join(list(map(lambda x: str(x), nodes)))
                        j += 1
                    logging.info(network_str_form)
        else:
            nodes_str_list = list(map(lambda x: str(x), self.comp_string_network))
            string_rep = ''.join(nodes_str_list)
            logging.info(string_rep)

    def parse_and_print_comp_string(self):
        self.parse_comp_string()
        self.print_decomp_string()

def process_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('comp_string',
                        help='The compressed string to parse.')
    parser.add_argument('-m',
                        '--msg-level',
                        default=logging.INFO,
                        help="The logging level to set for this run")
    return parser.parse_args()

def main():
    args = process_parameters()
    decomp_string = DecompressedString(args.comp_string, msg_level=args.msg_level)
    decomp_string.parse_and_print_comp_string()

if __name__ == '__main__':
    main()
