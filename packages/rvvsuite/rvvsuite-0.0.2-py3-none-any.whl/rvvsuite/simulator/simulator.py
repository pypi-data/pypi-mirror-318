from ..common.icb import icb
from ..common.vector import vector
from ..common.supported_features import GROUP_OF_OPCODES


DEFAULT_CONFIGS = {
    'pc_width': 10,
    'addr_width': 12,
    'elen': 32,
    'vlen': 128,
}


class simulator:
    def __init__(self, imem: dict = {}, dmem: dict = {}, configs: dict = DEFAULT_CONFIGS) -> None:
        self.imem = imem
        self.dmem = dmem
        self.configs = configs
        self.x_reg_file = {key: 0 for key in range(32)}
        self.v_reg_file = {key: 0 for key in range(32)}
        self.pc = 0


    def __apply_changes(self, changes: dict) -> None:
        self.pc = changes['pc']
        
        if 'x_reg_file' in changes:
            for rd, value in changes['x_reg_file'].items():
                self.x_reg_file[rd] = value

        if 'v_reg_file' in changes:
            for vd, value in changes['v_reg_file'].items():
                self.v_reg_file[vd] = value

        if 'dmem' in changes:
            for addr, byte in changes['dmem'].items():
                self.dmem[addr] = byte
    
    
    def run(self):
        vlen = self.configs['vlen']
        elen = self.configs['elen']
        addr_width = self.configs['addr_width']
        dmem_size = 2 ** addr_width
        pc_width = self.configs['pc_width']
        imem_size = 2 ** pc_width

        changlog = [{ 'pc': 0}]

        while True:
            if  self.pc >= imem_size: # End of IMEM
                break
            
            if self.pc % 4 != 0: # Check if pc is aligned
                raise ValueError(f'Invalid PC: {self.pc}. Must be aligned to 4.')
            
            inst = self.imem.get(self.pc, 0) # 0 if pc is not in imem

            if inst == 0: # No more inst
                break

            opcode = icb.get_bits(inst, start=0, width=7)
            
            if opcode == 0b1010111: # v_arith
                opcode, vd, funct3, vs1_rs1_imm, vs2, vm, funct6 = simulator.__decode_inst_v_arith(inst)

                print(f'v_arith: {opcode=:7b} {vd=} {funct3=:3b} {vs1_rs1_imm=} {vs2=} {vm=:1b} {funct6=:6b}')
                
                vect2 = vector(self.v_reg_file[vs2], elen=elen, vlen=vlen)
                if funct3 == 0b000: # OPIVV
                    vect1 = vector(self.v_reg_file[vs1_rs1_imm], elen=elen, vlen=vlen)
                elif funct3 == 0b100: # OPIVX
                    vect1 = vector(vect=[icb(self.x_reg_file[vs1_rs1_imm], width=elen)] * (vlen // elen), elen=elen, vlen=vlen)
                elif funct3 == 0b011: # OPIVI
                    vect1 = vector(vect=[icb(vs1_rs1_imm, width=5)] * (vlen // elen), elen=elen, vlen=vlen)
                else:
                    raise ValueError(f'Unsupported funct3: 0b{funct3:3b}.')
                
                masks = self.__get_masks(vm)

                result = self.__vop(funct6, vect2, vect1, masks)

                changes = {
                    'pc': self.pc + 4,
                    'v_reg_file': {vd: result}
                }

            elif opcode == 0b0000111: # v_load
                opcode, vd, width_code, rs1, lumop_rs2_vs2, vm, mop, mew, nf = simulator.__decode_inst_v_load(inst)

                print(f'v_load {opcode=:7b} {vd=} {width_code=:3b} {rs1=} {lumop_rs2_vs2=} {vm=:1b} {mop=:2b}')

                masks = self.__get_masks(vm)
                
                if width_code == 0b000: # 8-bit
                    width = 8
                elif width_code == 0b101: # 16-bit
                    width = 16
                elif width_code == 0b110: # 32-bit
                    width = 32
                else:
                    raise ValueError(f'Unsupported width_code: 0b{width_code:3b}.')

                base_addr = self.x_reg_file[rs1]

                if mop == 0b00: # unit-stride
                    read_vect = self.__vload_unit_stride(vd, width, base_addr, masks)
                
                elif mop == 0b01: # indexed-unordered
                    index_vect = vector(self.v_reg_file[lumop_rs2_vs2], elen=elen, vlen=vlen)
                    read_vect = self.__vload_indexed_unordered(vd, width, base_addr, index_vect, masks)

                elif mop == 0b10: # strided
                    stride = self.x_reg_file[lumop_rs2_vs2]
                    read_vect = self.__vload_strided(vd, width, base_addr, stride, masks)

                else:
                    raise ValueError(f'Unsupported mop: 0b{mop:2b}.')
                
                changes = {
                    'pc': self.pc + 4,
                    'v_reg_file': {vd: read_vect}
                }

            elif opcode == 0b0100111: # v_store
                opcode, vs3, width_code, rs1, sumop_rs2_vs2, vm, mop, mew, nf = simulator.__decode_inst_v_store(inst)

                print(f'v_store {opcode=:7b} {vs3=} {width_code=:3b} {rs1=} {sumop_rs2_vs2=} {vm=:1b} {mop=:2b}')
                
                masks = self.__get_masks(vm)
                
                if width_code == 0b000: # 8-bit
                    width = 8
                elif width_code == 0b101: # 16-bit
                    width = 16
                elif width_code == 0b110: # 32-bit
                    width = 32
                else:
                    raise ValueError(f'Unsupported width_code: 0b{width_code:3b}.')

                base_addr = self.x_reg_file[rs1]
                write_vect = vector(self.v_reg_file[vs3], elen=elen, vlen=vlen)

                if mop == 0b00: # unit-stride
                    dmem_changes = self.__vstore_unit_stride(write_vect, width, base_addr, masks)
                
                elif mop == 0b01: # indexed-unordered
                    index_vect = vector(self.v_reg_file[sumop_rs2_vs2], elen=elen, vlen=vlen)
                    dmem_changes = self.__vstore_indexed_unordered(write_vect, width, base_addr, index_vect, masks)

                elif mop == 0b10: # strided
                    stride = self.x_reg_file[sumop_rs2_vs2]
                    dmem_changes = self.__vstore_strided(write_vect, width, base_addr, stride, masks)

                else:
                    raise ValueError(f'Unsupported mop: 0b{mop:2b}.')
                
                changes = {
                    'pc': self.pc + 4,
                    'dmem': dmem_changes
                }

            elif opcode in GROUP_OF_OPCODES:
                if GROUP_OF_OPCODES[opcode] == 'u_type':
                    rd = icb.get_bits(inst, start=7, width=5)
                    imm20 = icb.get_bits(inst, start=12, width=20)

                    print(f'u_type: {opcode=:7b} {rd=} {imm20=:b}')

                    if opcode == 0b0110111: #lui
                        changes = {
                            'pc': self.pc + 4,
                            'x_reg_file': {rd: imm20 << 12}
                        }

                    elif opcode == 0b0010111: # auipc
                        raise ValueError(f'Unsupported opcode: 0b{opcode:7b} (Not implemented yet).')

                elif GROUP_OF_OPCODES[opcode] == 'i_type':
                    rd = icb.get_bits(inst, start=7, width=5)
                    funct3 = icb.get_bits(inst, start=12, width=3)
                    rs1 = icb.get_bits(inst, start=15, width=5)
                    imm12 = icb.get_bits(inst, start=20, width=12)

                    print(f'i_type: {opcode=:7b} {funct3:3b} {rd=} {rs1=} {imm12=:b}')

                    if funct3 == 0b000: # addi
                        opnd2 = icb(self.x_reg_file[rs1], 32)
                        opnd1 = icb(imm12, 12)
                        changes = {
                            'pc': self.pc + 4,
                            'x_reg_file': {rd: (opnd2 + opnd1).repr}
                        }
                    else:
                        raise ValueError(f'Unsupported funct3: 0b{funct3:3b} (Not implemented yet).')

                else:
                    raise ValueError(f'Unsupported opcode: 0b{opcode:7b}.')

            else:
                raise ValueError(f'Unsupported opcode: 0b{opcode:7b}.')

            changlog.append(changes)

            self.__apply_changes(changes)

        return changlog
    

    def __vop(self, funct6: int, vect2: vector, vect1: vector, masks: list[int]):
        if funct6 == 0b000000: # vadd
            result_vect = vect2.__vadd__(vect1, masks)
        elif funct6 == 0b000010: # vsub
            result_vect = vect2.__vsub__(vect1, masks)
        elif funct6 == 0b000011: # vrsub
            result_vect = vect2.__vrsub__(vect1, masks)
        elif funct6 == 0b001001: # vand
            result_vect = vect2.__vand__(vect1, masks)
        elif funct6 == 0b001010: # vor
            result_vect = vect2.__vor__(vect1, masks)
        elif funct6 == 0b001011: # vxor
            result_vect = vect2.__vxor__(vect1, masks)
        elif funct6 == 0b100101: # vsll
            result_vect = vect2.__vsll__(vect1, masks)
        elif funct6 == 0b101000: # vsrl
            result_vect = vect2.__vsrl__(vect1, masks)
        elif funct6 == 0b101001: # vsra
            result_vect = vect2.__vsra__(vect1, masks)
        elif funct6 == 0b011000: # vmseq
            result_vect = vect2.__vmseq__(vect1, masks)
        elif funct6 == 0b011001: # vmsne
            result_vect = vect2.__vmsne__(vect1, masks)
        elif funct6 == 0b011010: # vmsltu
            result_vect = vect2.__vmsltu__(vect1, masks)
        elif funct6 == 0b011011: # vmslt
            result_vect = vect2.__vmslt__(vect1, masks)
        elif funct6 == 0b011100: # vmsleu
            result_vect = vect2.__vmsleu__(vect1, masks)
        elif funct6 == 0b011101: # vmsle
            result_vect = vect2.__vmsle__(vect1, masks)
        elif funct6 == 0b011110: # vmsgtu
            result_vect = vect2.__vmsgtu__(vect1, masks)
        elif funct6 == 0b011111: # vmsgt
            result_vect = vect2.__vmsgt__(vect1, masks)
        elif funct6 == 0b000100: # vminu
            result_vect = vect2.__vminu__(vect1, masks)
        elif funct6 == 0b000101: # vmin
            result_vect = vect2.__vmin__(vect1, masks)
        elif funct6 == 0b000110: # vmaxu
            result_vect = vect2.__vmaxu__(vect1, masks)
        elif funct6 == 0b000111: # vmax
            result_vect = vect2.__vmax__(vect1, masks)
        elif funct6 == 0b010111: # vmerge
            result_vect = vect2.__vmerge__(vect1, masks)
        elif funct6 == 0b010111: # vmv
            result_vect = vect1
        else:
            raise ValueError(f'Unsupported funct6: 0b{funct6:6b}.')
        
        return result_vect.to_register()

    
    def __vload_unit_stride(self, vd: int, width: int, base_addr: int, masks: list[int]) -> int:
        dmem_size = 1 << self.configs['addr_width']
        vlen = self.configs['vlen']
        elen = self.configs['elen']
        num_of_elms = vlen // elen

        read_vect = self.v_reg_file[vd]

        for i in range(num_of_elms):
            addr = base_addr + i * (width // 8)
            # if addr >= dmem_size: # TODO: Uncomment after constrain dmem access range
            #     raise ValueError(f"The address: {addr} is out of DMEM (DMEM size is {dmem_size})")

            elm_i = 0
            if masks[i] == 1:
                for j in range(width // 8):
                    elm_i |= self.dmem.get(addr + j, 0) << (j * 8)

            read_vect |= icb(elm_i, width).__sext__(elen).repr << (i * elen)

        return read_vect
    

    def __vload_indexed_unordered(self, vd: int, width: int, base_addr: int, index_vect: vector, masks: list[int]) -> int:
        dmem_size = 1 << self.configs['addr_width']
        vlen = self.configs['vlen']
        elen = self.configs['elen']
        num_of_elms = vlen // elen

        read_vect = self.v_reg_file[vd]

        for i in range(num_of_elms):
            addr = base_addr + index_vect.get_element(i).repr
            # if addr >= dmem_size: # TODO: Uncomment after constrain dmem access range
            #     raise ValueError(f"The address: {addr} is out of DMEM (DMEM size is {dmem_size})")

            elm_i = 0
            if masks[i] == 1:
                for j in range(width // 8):
                    elm_i |= self.dmem.get(addr + j, 0) << (j * 8)

            read_vect |= icb(elm_i, width).__sext__(elen).repr << (i * elen)

        return read_vect
    

    def __vload_strided(self, vd: int, width: int, base_addr: int, stride: int, masks: list[int]) -> int:
        dmem_size = 1 << self.configs['addr_width']
        vlen = self.configs['vlen']
        elen = self.configs['elen']
        num_of_elms = vlen // elen

        read_vect = self.v_reg_file[vd]

        for i in range(num_of_elms):
            addr = base_addr + i * stride
            # if addr >= dmem_size: # TODO: Uncomment after constrain dmem access range
            #     raise ValueError(f"The address: {addr} is out of DMEM (DMEM size is {dmem_size})")

            elm_i = 0
            if masks[i] == 1:
                for j in range(width // 8):
                    elm_i |= self.dmem.get(addr + j, 0) << (j * 8)

            read_vect |= icb(elm_i, width).__sext__(elen).repr << (i * elen)

        return read_vect
    

    def __vstore_unit_stride(self, write_vect: vector, width: int, base_addr: int, masks: list[int]) -> dict:
        dmem_size = 1 << self.configs['addr_width']
        vlen = self.configs['vlen']
        elen = self.configs['elen']
        num_of_elms = vlen // elen

        dmem_changes = {}
        for i in range(num_of_elms):
            addr = base_addr + i * (width // 8)
            # if addr >= dmem_size: # TODO: Uncomment after constrain dmem access range
            #     raise ValueError(f"The address: {addr} is out of DMEM (DMEM size is {dmem_size})")

            if masks[i] == 1:
                write_elm = write_vect.get_element(i).repr
                for j in range(width // 8):
                    byte = icb.get_bits(write_elm, start=(addr + j), width=8)
                    dmem_changes[addr] = byte

        return dmem_changes
    

    def __vstore_indexed_unordered(self, write_vect: vector, width: int, base_addr: int, index_vect: vector, masks: list[int]) -> dict:
        dmem_size = 1 << self.configs['addr_width']
        vlen = self.configs['vlen']
        elen = self.configs['elen']
        num_of_elms = vlen // elen

        dmem_changes = {}
        for i in range(num_of_elms):
            addr = base_addr + index_vect.get_element(i).repr
            # if addr >= dmem_size: # TODO: Uncomment after constrain dmem access range
            #     raise ValueError(f"The address: {addr} is out of DMEM (DMEM size is {dmem_size})")

            if masks[i] == 1:
                write_elm = write_vect.get_element(i).repr
                for j in range(width // 8):
                    byte = icb.get_bits(write_elm, start=(addr + j), width=8)
                    dmem_changes[addr] = byte

        return dmem_changes
    

    def __vstore_strided(self, write_vect: vector, width: int, base_addr: int, stride: int, masks: list[int]) -> dict:
        dmem_size = 1 << self.configs['addr_width']
        vlen = self.configs['vlen']
        elen = self.configs['elen']
        num_of_elms = vlen // elen

        dmem_changes = {}
        for i in range(num_of_elms):
            addr = base_addr + i * stride
            # if addr >= dmem_size: # TODO: Uncomment after constrain dmem access range
            #     raise ValueError(f"The address: {addr} is out of DMEM (DMEM size is {dmem_size})")

            if masks[i] == 1:
                write_elm = write_vect.get_element(i).repr
                for j in range(width // 8):
                    byte = icb.get_bits(write_elm, start=(addr + j), width=8)
                    dmem_changes[addr] = byte

        return dmem_changes


    def __get_masks(self, vm: int) -> list[int]:
        vlen = self.configs['vlen']
        elen = self.configs['elen']

        if vm:
            return [1] * (vlen // elen)
        
        return [
            icb.get_bits(self.v_reg_file[0], start=(i * elen), width=1)
            for i in range(vlen // elen)
        ]
    

    @staticmethod
    def __decode_inst_v_arith(inst: int) -> tuple:
        opcode = icb.get_bits(inst, start=0, width=7)
        vd = icb.get_bits(inst, start=7, width=5)
        funct3 = icb.get_bits(inst, start=12, width=3)
        vs1_rs1_imm = icb.get_bits(inst, start=15, width=5)
        vs2 = icb.get_bits(inst, start=20, width=5)
        vm = icb.get_bits(inst, start=25, width=1)
        funct6 = icb.get_bits(inst, start=26, width=6)

        return opcode, vd, funct3, vs1_rs1_imm, vs2, vm, funct6


    @staticmethod
    def __decode_inst_v_load(inst: int) -> tuple:
        opcode = icb.get_bits(inst, start=0,width=7)
        vd = icb.get_bits(inst, start=7,width=5)
        width_code = icb.get_bits(inst, start=12,width=3)
        rs1 = icb.get_bits(inst, start=15,width=5)
        lumop_rs2_vs2 = icb.get_bits(inst, start=20,width=5)
        vm = icb.get_bits(inst, start=25,width=1)
        mop = icb.get_bits(inst, start=26,width=2)
        mew = icb.get_bits(inst, start=28,width=1)
        nf = icb.get_bits(inst, start=29,width=3)

        return opcode, vd, width_code, rs1, lumop_rs2_vs2, vm, mop, mew, nf


    @staticmethod
    def __decode_inst_v_store(inst: int) -> tuple:
        opcode = icb.get_bits(inst, start=0, width=7)
        vs3 = icb.get_bits(inst, start=7, width=5)
        width_code = icb.get_bits(inst, start=12, width=3)
        rs1 = icb.get_bits(inst, start=15, width=5)
        sumop_rs2_vs2 = icb.get_bits(inst, start=20, width=5)
        vm = icb.get_bits(inst, start=25, width=1)
        mop = icb.get_bits(inst, start=26, width=2)
        mew = icb.get_bits(inst, start=28, width=1)
        nf = icb.get_bits(inst, start=29, width=3)

        return opcode, vs3, width_code, rs1, sumop_rs2_vs2, vm, mop, mew, nf
    
    