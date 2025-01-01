import random
from tqdm import trange, tqdm
import numpy as np

import string
from pathlib import Path
from dspsim.avril import Avril, AvrilIface, VReg


def main():
    """"""
    with Avril(0, timeout=0.02) as av:
        meta = av.read_all_meta()
        # print(meta)
        for name, iface in meta.items():
            print(f"{name}: {iface}")

        sram0 = av.get_interface("sram0")
        sram0.load_register_file(Path("reg_map.yaml"))

        sram0["x"] = 99
        assert sram0["x"] == 99

        sram1 = AvrilIface(av, "sram1")

        # assign random register names to all registers.
        sram1.load_registers(
            {
                "".join(random.choices(string.ascii_lowercase, k=32)): VReg(i)
                for i in sram1
            }
        )

        # Iterate through all addresses, incrementing by dtype.
        for addr in tqdm(sram0):
            x = random.randint(-(2**31), 2**31 - 1)
            sram0[addr] = x
            y = sram0[addr]
            assert y == x

        # Iterate through all registers.
        for r in tqdm(sram1.registers):
            x = random.random()
            sram1[r] = x
            y = sram1[r]
            assert np.isclose(y, x, atol=0.00001)


if __name__ == "__main__":
    main()
