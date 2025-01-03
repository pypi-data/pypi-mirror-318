#!/usr/bin/env python

'''
`anytree_tree_to_alife_dataframe` tests for
`alifedata-phyloinformatics-convert` package.
'''

import anytree
from iterpop import iterpop as ip
from os.path import dirname, realpath
import pandas as pd

import alifedata_phyloinformatics_convert as apc


def test_singleton():
    original_tree = anytree.Node("beep")
    assert original_tree.name == "beep"
    converted_df = apc.anytree_tree_to_alife_dataframe(original_tree)

    expected_df = pd.DataFrame({
        "id" : [0],
        "ancestor_list" : ["[None]"],
        "name" : ["beep"],
    })

    assert converted_df.equals(expected_df)


def test_simple_tree():
    udo = anytree.Node("Udo", id=0)
    marc = anytree.Node("Marc", parent=udo, id=1111)
    lian = anytree.Node("Lian", parent=marc, id=2222)
    dan = anytree.Node("Dan", parent=udo, id=333)
    jet = anytree.Node("Jet", parent=dan, id=444)
    jan = anytree.Node("Jan", parent=dan, id=555)
    joe = anytree.Node("Joe", parent=dan, id=666)

    converted_df = apc.anytree_tree_to_alife_dataframe(udo)
    expected_df = pd.DataFrame({
        "id" : [0, 1111, 333, 2222, 444, 555, 666],
        "ancestor_list" : [
            "[None]", "[0]", "[0]", "[1111]", "[333]", "[333]", "[333]"
        ],
        "name" : ["Udo", "Marc", "Dan", "Lian", "Jet", "Jan", "Joe"],
    })

    assert converted_df.equals(expected_df)


def test_simple_tree_origin_times():
    udo = anytree.Node("Udo", id=0, edge_length=1)
    marc = anytree.Node("Marc", parent=udo, id=1111, edge_length=1)
    lian = anytree.Node("Lian", parent=marc, id=2222, edge_length=1)
    dan = anytree.Node("Dan", parent=udo, id=333, edge_length=2)
    jet = anytree.Node("Jet", parent=dan, id=444, edge_length=4)
    jan = anytree.Node("Jan", parent=dan, id=555, edge_length=5)
    joe = anytree.Node("Joe", parent=dan, id=666, edge_length=6)

    converted_df = apc.anytree_tree_to_alife_dataframe(udo)
    expected_df = pd.DataFrame({
        "id" : [0, 1111, 333, 2222, 444, 555, 666],
        "ancestor_list" : [
            "[None]", "[0]", "[0]", "[1111]", "[333]", "[333]", "[333]"
        ],
        "edge_length" : [1, 1, 2, 1, 4, 5, 6],
        "name" : ["Udo", "Marc", "Dan", "Lian", "Jet", "Jan", "Joe"],
        "origin_time" : [1, 2, 3, 3, 7, 8, 9],
    })

    assert converted_df.equals(expected_df)
