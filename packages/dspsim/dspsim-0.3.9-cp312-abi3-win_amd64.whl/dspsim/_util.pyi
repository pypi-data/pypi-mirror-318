import enum


AddrAlign16: ErrorCode = ErrorCode.AddrAlign16

AddrAlign32: ErrorCode = ErrorCode.AddrAlign32

AddrAlign64: ErrorCode = ErrorCode.AddrAlign64

AddrAlignN: ErrorCode = ErrorCode.AddrAlignN

class AvrilCommand(enum.Enum):
    Nop = 0

    Write = 1

    Read = 2

    NopAck = 3

    WriteAck = 4

    ReadAck = 5

class AvrilMode(enum.Enum):
    Vmmi = 0

    Bootload = 1

    VMeta = 2

Bootload: AvrilMode = AvrilMode.Bootload

class DType(enum.Enum):
    @property
    def size(self) -> int: ...

    @property
    def is_uint(self) -> int: ...

    @property
    def is_int(self) -> int: ...

    @property
    def is_anyint(self) -> int: ...

    @property
    def is_float(self) -> int: ...

    @property
    def is_complex(self) -> int: ...

    @property
    def is_str(self) -> int: ...

    x = 0

    int8 = 65537

    uint8 = 1

    int16 = 65538

    uint16 = 2

    int32 = 65540

    uint32 = 4

    int64 = 65544

    uint64 = 8

    int128 = 65552

    uint128 = 16

    float = 131076

    double = 131080

    complex8 = 196610

    complex16 = 196612

    complex32 = 196616

    complex64 = 196624

    complex128 = 196640

    str4 = 262148

    str8 = 262152

    str16 = 262160

    str32 = 262176

    str64 = 262208

class ErrorCode(enum.Enum):
    NoError = 0

    Overflow = 1

    InvalidMode = 2

    InvalidCommand = 3

    InvalidAddress = 4

    ReadOnly = 5

    WriteOnly = 6

    AddrAlign16 = 7

    AddrAlign32 = 8

    AddrAlign64 = 9

    AddrAlignN = 10

    SizeAlign16 = 11

    SizeAlign32 = 12

    SizeAlign64 = 13

    SizeAlignN = 14

    KeyNotFound = 15

InvalidAddress: ErrorCode = ErrorCode.InvalidAddress

InvalidCommand: ErrorCode = ErrorCode.InvalidCommand

InvalidMode: ErrorCode = ErrorCode.InvalidMode

KeyNotFound: ErrorCode = ErrorCode.KeyNotFound

NoError: ErrorCode = ErrorCode.NoError

Nop: AvrilCommand = AvrilCommand.Nop

NopAck: AvrilCommand = AvrilCommand.NopAck

Overflow: ErrorCode = ErrorCode.Overflow

Read: AvrilCommand = AvrilCommand.Read

ReadAck: AvrilCommand = AvrilCommand.ReadAck

ReadOnly: ErrorCode = ErrorCode.ReadOnly

SizeAlign16: ErrorCode = ErrorCode.SizeAlign16

SizeAlign32: ErrorCode = ErrorCode.SizeAlign32

SizeAlign64: ErrorCode = ErrorCode.SizeAlign64

SizeAlignN: ErrorCode = ErrorCode.SizeAlignN

VMeta: AvrilMode = AvrilMode.VMeta

Vmmi: AvrilMode = AvrilMode.Vmmi

Write: AvrilCommand = AvrilCommand.Write

WriteAck: AvrilCommand = AvrilCommand.WriteAck

WriteOnly: ErrorCode = ErrorCode.WriteOnly

complex128: DType = DType.complex128

complex16: DType = DType.complex16

complex32: DType = DType.complex32

complex64: DType = DType.complex64

complex8: DType = DType.complex8

double: DType = DType.double

float: DType = DType.float

int128: DType = DType.int128

int16: DType = DType.int16

int32: DType = DType.int32

int64: DType = DType.int64

int8: DType = DType.int8

str16: DType = DType.str16

str32: DType = DType.str32

str4: DType = DType.str4

str64: DType = DType.str64

str8: DType = DType.str8

uint128: DType = DType.uint128

uint16: DType = DType.uint16

uint32: DType = DType.uint32

uint64: DType = DType.uint64

uint8: DType = DType.uint8

x: DType = DType.x
