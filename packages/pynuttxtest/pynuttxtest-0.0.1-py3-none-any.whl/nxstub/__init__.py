############################################################################
# tools/pynuttx/nxstub/__init__.py
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.  The
# ASF licenses this file to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#
############################################################################

__version__ = "0.0.1"

import argparse
import logging
import traceback
import re

from typing import List

from . import utils
from .gdbstub import GDBStub, Target
from .target import RawMemory
from .registers import Registers, g_reg_table


def parse_log(elf, arch, logfile):

    memories: List[RawMemory] = []
    registers = Registers(elf, arch)
    if not logfile:
        return registers, memories

    def parse_register(regs, line):
        if len(line := line.split("up_dump_register: ")) != 2:
            return False

        if not (find_res := re.findall(r"([\w_]+): *([0-9xa-fXA-F]+)", line[1])):
            return False

        for name, value in find_res:
            name = name.lower()
            value = int(value, 16)
            try:
                regs.set(value, name=name)
            except KeyError:
                logging.warning(f"Ignore register {name}:{value}")

        return True

    def parse_stack(line):
        result = re.match(
            r".*stack_dump: (?P<ADDR>[0-9a-fxA-FX]+): (?P<VALS>( ?\w+)+)", line
        )
        if result is None:
            return None

        results = result.groupdict()

        addr = int(results["ADDR"], 16)
        data = b""
        for val in results["VALS"].split():
            # For little endian, the hex bytes should be reversed
            data += bytes.fromhex(val)[::-1]
        return RawMemory(addr, data)

    with open(logfile, "r") as f:
        for line in f:
            if parse_register(registers, line):
                continue

            if memory := parse_stack(line):
                memories.append(memory)

    return registers, memories


def gdbstub_start(args):
    memories = []
    registers = None

    for rawfile in args.rawfile or []:
        filename, address = rawfile.split(":")
        address = int(address, 16)
        with open(filename, "rb") as f:
            memories.append(RawMemory(address, f.read()))
            print(f"Add memory dump: {memories[-1]}")

    elf = utils.parse_elf(args.elf)
    registers, mem = parse_log(elf, args.arch, args.log)
    memories.extend(mem)

    core = utils.parse_elf(args.core) if args.core else None
    target = Target(elf, args.arch, registers, memories, core)

    stub = GDBStub(target=target, port=args.port)

    print(f"Start GDB server on port {args.port}...")
    stub.run()
    print("GDB server exited.")


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        prog="nxstub",
        description=f"nxstub v{__version__} - NuttX GDB server based on crash log, core dump or memory dump."
    )
    parser.add_argument(
        "-a",
        "--arch",
        type=str,
        required=True,
        choices=g_reg_table.keys(),
        help="The architecture of the target.",
    )
    parser.add_argument(
        "-e",
        "--elf",
        type=str,
        required=True,
        help="The elf file.",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=1234,
        help="The GDB server port.",
    )
    parser.add_argument(
        "-r",
        "--rawfile",
        type=str,
        nargs="*",
        help="The memory dump file, in format of 'memdump1.bin:address1 memdump2.bin:address2'.",
    )
    parser.add_argument(
        "-c",
        "--core",
        type=str,
        help="The core dump file.",
    )
    parser.add_argument(
        "-l",
        "--log",
        type=str,
        help="The crash dump log file.",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Show debug messages.",
    )

    return parser.parse_args(args)


def main():
    args = parse_args()

    if args.debug:
        logging.basicConfig()
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

    try:
        gdbstub_start(args)
    except Exception as e:
        print(f"GDBStub thread error: {e}:\n {traceback.format_exc()}")
        exit(1)
