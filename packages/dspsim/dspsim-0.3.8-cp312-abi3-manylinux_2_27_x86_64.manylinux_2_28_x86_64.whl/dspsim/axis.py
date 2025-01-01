from dspsim.framework import Signal8, SignalT, signal, port_info

from dspsim._framework import AxisTx8, AxisTx16, AxisTx32, AxisTx64

# from dspsim._framework import AxisTxU8, AxisTxU16, AxisTxU32, AxisTxU64
from dspsim._framework import AxisRx8, AxisRx16, AxisRx32, AxisRx64
# from dspsim._framework import AxisRxU8, AxisRxU16, AxisRxU32, AxisRxU64


from dspsim import util


TIDW = 8


class Axis:
    tdata: SignalT
    tvalid: Signal8
    tready: Signal8
    tid: Signal8 = None
    tlast: Signal8 = None

    _width: int
    _signed: bool

    def __init__(
        self,
        *,
        width: int,
        signed: bool = False,
        tid: bool = False,
        tlast: bool = False,
    ):
        self._width = width
        self._signed = signed

        self.tdata = signal(width=width, signed=signed)
        self.tvalid = signal()
        self.tready = signal()
        if tid:
            self.tid = signal(width=TIDW)
        if tlast:
            self.tlast = signal()

    def __str__(self) -> str:
        return f"Axis(width={self.width}, tid={self.tid}, tlast={self.tlast})"

    def __iter__(self):
        i = [self.tdata, self.tvalid, self.tready]
        if self.tid:
            i.append(self.tid)
        if self.tlast:
            i.append(self.tlast)
        return iter(i)

    @property
    def width(self):
        return self._width

    @property
    def signed(self) -> bool:
        return self._signed


def init_stream_model[ModelT](
    cls: type[ModelT],
    clk: Signal8,
    rst: Signal8,
    s_axis: Axis,
    m_axis: Axis,
    **extra,
) -> ModelT:
    """
    Init a model that contains a stream input and output using
    """

    args = dict(
        clk=clk,
        rst=rst,
        s_axis_tdata=s_axis.tdata,
        s_axis_tvalid=s_axis.tvalid,
        s_axis_tready=s_axis.tready,
        m_axis_tdata=m_axis.tdata,
        m_axis_tvalid=m_axis.tvalid,
        m_axis_tready=m_axis.tready,
    )

    portinfo = port_info(cls)

    # Connect an empty signal if the bus doesn't have it.
    # If the model doesn't have it, don't connect it.
    if "s_axis_tid" in portinfo:
        args["s_axis_tid"] = s_axis.tid if s_axis.tid else signal(width=TIDW)
    if "s_axis_tlast" in portinfo:
        args["s_axis_tlast"] = s_axis.tlast if s_axis.tlast else signal(width=1)

    if "m_axis_tid" in portinfo:
        args["m_axis_tid"] = m_axis.tid if m_axis.tid else signal(width=TIDW)
    if "m_axis_tlast" in portinfo:
        args["m_axis_tlast"] = m_axis.tlast if m_axis.tlast else signal(width=1)

    return cls(
        **args,
        **extra,
    )


AxisTxT = (
    AxisTx8 | AxisTx16 | AxisTx32 | AxisTx64
    # | AxisTxU8
    # | AxisTxU16
    # | AxisTxU32
    # | AxisTxU64
)
AxisRxT = (
    AxisRx8 | AxisRx16 | AxisRx32 | AxisRx64
    # | AxisRxU8
    # | AxisRxU16
    # | AxisRxU32
    # | AxisRxU64
)


def AxisTx(
    clk: Signal8,
    rst: Signal8,
    m_axis: Axis,
    tid_pattern: list[int] = [0],
    *,
    width: int = 32,
) -> AxisTxT:
    """"""
    uw = util.uint_width(width)
    _models = {8: AxisTx8, 16: AxisTx16, 32: AxisTx32, 64: AxisTx64}
    cls = _models[uw]
    # _umodels = {8: AxisTxU8, 16: AxisTxU16, 32: AxisTxU32, 64: AxisTxU64}
    # cls = _models[uw] if signed else _umodels[uw]

    return cls(
        clk=clk,
        rst=rst,
        m_axis_tdata=m_axis.tdata,
        m_axis_tvalid=m_axis.tvalid,
        m_axis_tready=m_axis.tready,
        m_axis_tid=m_axis.tid,
        m_axis_tlast=m_axis.tlast,
        tid_pattern=tid_pattern,
    )


def AxisRx(
    clk: Signal8,
    rst: Signal8,
    s_axis: Axis,
    *,
    width: int = 32,
) -> AxisRxT:
    """"""
    uw = util.uint_width(width)
    _models = {8: AxisRx8, 16: AxisRx16, 32: AxisRx32, 64: AxisRx64}
    cls: type[AxisRxT] = _models[uw]
    # _umodels = {8: AxisRxU8, 16: AxisRxU16, 32: AxisRxU32, 64: AxisRxU64}
    # cls = _models[uw] if signed else _umodels[uw]
    obj = cls(
        clk, rst, s_axis.tdata, s_axis.tvalid, s_axis.tready, s_axis.tid, s_axis.tlast
    )
    obj.width = width
    return obj
