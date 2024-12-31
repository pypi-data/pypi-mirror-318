from xrlint.node import DataArrayNode
from xrlint.plugins.xcube.rules import plugin
from xrlint.rule import RuleOp, RuleContext


@plugin.define_rule(
    "spatial-dims-order",
    version="1.0.0",
    description="Spatial dimensions should have order [...,y,x].",
)
class SpatialDimsOrder(RuleOp):
    def data_array(self, ctx: RuleContext, node: DataArrayNode):
        if node.in_data_vars():
            dims = list(node.data_array.dims)
            try:
                yx_names = ["y", "x"]
                yx_indexes = tuple(map(dims.index, yx_names))
            except ValueError:
                try:
                    yx_names = ["lat", "lon"]
                    yx_indexes = tuple(map(dims.index, yx_names))
                except ValueError:
                    return
            n = len(dims)
            y_index, x_index = yx_indexes
            if y_index != n - 2 or x_index != n - 1:
                expected_dims = [d for d in dims if d not in yx_names] + yx_names
                # noinspection PyTypeChecker
                ctx.report(
                    f"order of dimensions should be"
                    f" {','.join(expected_dims)}, but was {','.join(dims)}"
                )
