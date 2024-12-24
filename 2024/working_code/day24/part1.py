import re

def get_inputs():
    INPUT_REGEX = "(.{3}): (.)"
    GATE_REGEX = "(.{3}) (XOR|OR|AND) (.{3}) -> (.{3})"
    ACTUAL_FILE = "input.txt"
    TEST_FILE = "input_test.txt"
    input_wires = {}
    gates = {}
    output_wires = set()
    with open(ACTUAL_FILE, "r") as input_file:
        parser_type = 'input'
        for line in input_file.readlines():
            if line == '\n':
                parser_type = 'gate'
            elif parser_type == 'input':
                wire, value = re.findall(INPUT_REGEX, line)[0]
                input_wires[wire] = int(value)
            elif parser_type == 'gate':
                input_wire_1, gate_type, input_wire_2, output_wire = re.findall(GATE_REGEX, line)[0]
                if output_wire[0] == 'z':
                    output_wires.add(output_wire)
                if input_wire_1 in gates:
                    if input_wire_2 in gates[input_wire_1]:
                        gates[input_wire_1][input_wire_2].append((gate_type, output_wire))
                    else:
                        gates[input_wire_1][input_wire_2] = [(gate_type, output_wire)]
                else:
                    gates[input_wire_1] = { input_wire_2: [(gate_type, output_wire)]}
                if input_wire_2 in gates:
                    if input_wire_1 in gates[input_wire_2]:
                        gates[input_wire_2][input_wire_1].append((gate_type, output_wire))
                    else:
                        gates[input_wire_2][input_wire_1] = [(gate_type, output_wire)]
                else:
                    gates[input_wire_2] = { input_wire_1: [(gate_type, output_wire)]}

    output_wires = sorted(output_wires)
    return input_wires, gates, output_wires

def print_input_wires(input_wires):
    for key, value in input_wires.items():
        print(f'{key}: {value}')
    print()

def print_gates(input_wires):
    for key, value in input_wires.items():
        print(f'{key}: {value}')
    print()

def calculate_gate(input1, input2, gate_type):
    if gate_type == 'XOR':
        return input1 ^ input2
    if gate_type == 'OR':
        return input1 | input2
    if gate_type == 'AND':
        return input1 & input2

def calculate(input_wires, gates):
    calculated = set()
    while gates:
        for input_wire_1 in input_wires.copy():
            if input_wire_1 not in gates:
                continue

            for input_wire_2 in gates[input_wire_1].copy():
                if input_wire_2 not in input_wires:
                    continue

                # Valid gates
                for gate in gates[input_wire_1][input_wire_2]:
                    gate_type, output_wire = gate
                    # print(f'Calculating {input_wire_1} {gate_type} {input_wire_1} -> {output_wire}')
                    input_value_1, input_value_2 = input_wires[input_wire_1], input_wires[input_wire_2]
                    input_wires[output_wire] = calculate_gate(input_value_1, input_value_2, gate_type)

                    try:
                        gates[input_wire_1].pop(input_wire_2)
                    except:
                        pass
                    try:
                        gates[input_wire_2].pop(input_wire_1)
                    except:
                        pass
                    try:
                        if gates[input_wire_1] == {}:
                            gates.pop(input_wire_1)
                    except:
                        pass
                    try:
                        if gates[input_wire_2] == {}:
                            gates.pop(input_wire_2)
                    except:
                        pass

                    # print_input_wires(input_wires)
                    # print_gates(gates)
                    # input()

    return input_wires

input_wires, gates, output_wires = get_inputs()
final_input_wires = calculate(input_wires, gates)
total = 0
for exponent, output_wire in enumerate(output_wires):
    total += final_input_wires[output_wire] * 2 ** exponent
print(total)
