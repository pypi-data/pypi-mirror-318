import dendropy
from iterpop import iterpop as ip
from nanto import isanan, nantonone
import pandas as pd
import string
import typing

from ._impl import keydefaultdict
from ._impl import parse_ancestor_list as _parse_ancestor_list


def alife_dataframe_to_dendropy_trees(
    df: pd.DataFrame,
    setattrs: typing.Optional[typing.Union[
        typing.Iterable[str],
        typing.Mapping[str, str],
    ]] = None,
    setup_edge_lengths: bool = False,
    *,
    progress_wrap: typing.Callable = lambda x, **_: x,
) -> typing.List[dendropy.Tree]:
    """Open a phylogeny dataframe formatted to the artificial life community
    data format standards as zero or more dendropy trees, depending on the
    number of clades with no common ancestor.

    The following columns will automatically be applied as attributes to
    generated Node objects:
        * edge_length,
        * id,
        * label,
        * origin_time, and
        * taxon_label.

    Parameters
    ----------
    df:
        Pandas DataFrame to convert.
    setattrs: optional
        Dataframe columns that should be attached as attributes to Node
        objects within the trees. If a map is provided, values at columns in
        keys will be attached with the corresponding value as the attr name.
    setup_edge_lengths: bool, optional
        Should we try to set up edge lengths using the origin_time column?
        Will not override if edge_length is provided as a column of df.
    """

    df = df.copy()

    df['parsed_ancestor_list'] \
        = df['ancestor_list'].apply(_parse_ancestor_list)

    # maps id to node
    def setup_node(id: int) -> dendropy.Node:
        res = dendropy.Node()
        res.id = id
        return res
    nodes = keydefaultdict(setup_node)

    # maps id to origin time
    root_nodes = []

    for __, row in progress_wrap(df.iterrows(), total=len(df)):
        node = nodes[row['id']]

        if setattrs is not None:
            for col_name in setattrs:
                attr_name: str
                try:
                    attr_name = setattrs[col_name]
                except TypeError:
                    attr_name = col_name
                assert attr_name not in (
                    'edge_length',
                    'origin_time',
                    'taxon',
                    'taxon_label',
                )
                assert not hasattr(node, attr_name)
                setattr(node, attr_name, row[col_name])

        node.origin_time = nantonone(row.get('origin_time', default=None))
        node.label = row.get('label', default=None)
        taxon_label = row.get('taxon_label', default=None)
        if taxon_label not in ('None', None):
            node.taxon = dendropy.Taxon(label=taxon_label)
        node.edge_length = nantonone(row.get('edge_length', None))

        if row['parsed_ancestor_list']:
            ancestor_id = ip.popsingleton(row['parsed_ancestor_list'])
            nodes[ancestor_id].add_child(node)
        else:
            root_nodes.append(node)

    # set up edge lengths
    if setup_edge_lengths:
        for id, parent_node in progress_wrap(nodes.items(), total=len(nodes)):
            for child_node in parent_node.child_node_iter():
                if child_node.edge_length is None and None not in (
                    getattr(child_node, 'origin_time', None),
                    getattr(parent_node, 'origin_time', None),
                ):
                    assert child_node.origin_time >= parent_node.origin_time
                    child_node.edge_length \
                        = child_node.origin_time - parent_node.origin_time

        for root_node in root_nodes:
            if (
                root_node.edge_length is None
                and getattr(root_node, 'origin_time', None) is not None
            ):
                assert not isanan(root_node.origin_time)
                root_node.edge_length = root_node.origin_time

    res = [
        dendropy.Tree(seed_node=root_node)
        for root_node in root_nodes
    ]
    for tree in res:
        tree.is_rooted = True
    return res
