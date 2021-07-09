from clvm.casts import int_from_bytes
from clvm_tools import binutils

from melati.consensus.block_rewards import calculate_base_farmer_reward, calculate_pool_reward
from melati.types.blockchain_format.program import Program
from melati.types.condition_opcodes import ConditionOpcode
from melati.util.bech32m import decode_puzzle_hash, encode_puzzle_hash
from melati.util.condition_tools import parse_sexp_to_conditions
from melati.util.ints import uint32

address1 = "xmx1pwsp7xpyv4ckre4qek7rt6yls5gykecuhv98dqgm2jr4jcxm7t8s0kweej"  # Gene wallet (m/12381/8444/2/42):
address2 = "xmx1pwsp7xpyv4ckre4qek7rt6yls5gykecuhv98dqgm2jr4jcxm7t8s0kweej"  # Rifo address (m/12381/8444/2/0)

ph1 = decode_puzzle_hash(address1)
ph2 = decode_puzzle_hash(address2)

pool_amounts = int(calculate_pool_reward(uint32(0)) / 2)
farmer_amounts = int(calculate_base_farmer_reward(uint32(0)) / 2)

assert pool_amounts * 2 == calculate_pool_reward(uint32(0))
assert farmer_amounts * 2 == calculate_base_farmer_reward(uint32(0))


def make_puzzle(amount: int) -> int:
    puzzle = f"(q . ((51 0x{ph1.hex()} {amount}) (51 0x{ph2.hex()} {amount})))"
    # print(puzzle)

    puzzle_prog = Program.to(binutils.assemble(puzzle))
    print("Program: ", puzzle_prog)
    puzzle_hash = puzzle_prog.get_tree_hash()

    solution = "()"
    prefix = "xmx"
    print("PH", puzzle_hash)
    print(f"Address: {encode_puzzle_hash(puzzle_hash, prefix)}")

    result = puzzle_prog.run(solution)
    error, result_human = parse_sexp_to_conditions(result)

    total_melati = 0
    if error:
        print(f"Error: {error}")
    else:
        assert result_human is not None
        for cvp in result_human:
            assert len(cvp.vars) == 2
            total_melati += int_from_bytes(cvp.vars[1])
            print(
                f"{ConditionOpcode(cvp.opcode).name}: {encode_puzzle_hash(cvp.vars[0], prefix)},"
                f" amount: {int_from_bytes(cvp.vars[1])}"
            )
    return total_melati


total_melati = 0
print("Pool address: ")
total_melati += make_puzzle(pool_amounts)
print("\nFarmer address: ")
total_melati += make_puzzle(farmer_amounts)

assert total_melati == calculate_base_farmer_reward(uint32(0)) + calculate_pool_reward(uint32(0))
