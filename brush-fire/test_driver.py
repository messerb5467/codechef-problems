def save_bushes(test_file):
  with open(test_file) as f:
    num_tests = int(f.readline())
    for i in range(0, num_tests):
      bush_graph = nx.DiGraph()
      num_bushes, starting_burn, num_bushes_to_save = get_ints_from_string(f.readline())
      process_bush_relations(f, bush_graph, num_bushes, starting_burn)
      sentimental_bushes = get_ints_from_string(f.readline())