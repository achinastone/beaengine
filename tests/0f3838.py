#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):
        # 66 0F 38 38 /r
        # pminsb mm1, mm2/m64
        Buffer = '660f38389011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3838')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pminsb ')
        assert_equal(myDisasm.instr.repr, 'pminsb xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 38 /r
        # vpminsb xmm1, xmm2, xmm3/m128
        Buffer = 'c4020138443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.instr.repr, 'vpminsb xmm8, xmm15, xmmword ptr [r11+r14+22h]')

        # VEX.NDS.256.66.0F38.WIG 38 /r
        # vpminsb ymm1, ymm2, ymm3/m256
        Buffer = 'c4020538443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.instr.repr, 'vpminsb ymm8, ymm15, ymmword ptr [r11+r14+22h]')

        # EVEX.NDS.128.66.0F38.WIG 38 /r
        # vpminsb xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '6202050638443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x38')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.instr.repr, 'vpminsb xmm0, xmm15, xmmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.256.66.0F38.WIG 38 /r
        # vpminsb ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '6202052038443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x38')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.instr.repr, 'vpminsb ymm0, ymm15, ymmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.512.66.0F38.WIG 38 /r
        # vpminsb zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '6202054038443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x38')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.instr.repr, 'vpminsb zmm0, zmm15, zmmword ptr [rbx+rsi+22h]')
