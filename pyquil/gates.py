##############################################################################
# Copyright 2016-2017 Rigetti Computing
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##############################################################################

from pyquil.quilatom import unpack_qubit, unpack_classical_reg
from pyquil.quilbase import (Measurement, Gate, Wait, Reset, Halt, Nop, ClassicalTrue,
                             ClassicalFalse, ClassicalNot, ClassicalAnd, ClassicalOr, ClassicalMove,
                             ClassicalExchange)


def I(qubit):
    """Produces the I instruction.

    I = [1, 0]
        [0, 1]

    This gate is a single qubit identity gate.
    Note that this gate is different that the NOP instruction as noise channels
    are typically still applied during the duration of identity gates. Identities will
    also block parallelization like any other gate.

    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="I", params=[], qubits=[unpack_qubit(qubit)])


def X(qubit):
    """Produces the X instruction.

    X = [[0, 1],
         [1, 0]]

    This gate is a single qubit X-gate.

    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="X", params=[], qubits=[unpack_qubit(qubit)])


def Y(qubit):
    """Produces the Y instruction.

    Y = [[0, 0 - 1j],
         [0 + 1j, 0]]

    This gate is a single qubit Y-gate.

    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="Y", params=[], qubits=[unpack_qubit(qubit)])


def Z(qubit):
    """Produces the Z instruction.

    Z = [[1, 0],
         [0, -1]]

    This gate is a single qubit Z-gate.

    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="Z", params=[], qubits=[unpack_qubit(qubit)])


def H(qubit):
    """
    H = (1 / sqrt(2)) * [[1, 1],
                         [1, -1]]

    Produces the H instruction. This gate is a single qubit Hadamard gate.

    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="H", params=[], qubits=[unpack_qubit(qubit)])


def S(qubit):
    """Produces the S instruction.

    S = [[1, 0],
         [0, 1j]]

    This gate is a single qubit S-gate.

    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="S", params=[], qubits=[unpack_qubit(qubit)])


def T(qubit):
    """Produces the T instruction.

    T = [[1, 0],
         [0, exp(1j * pi / 4)]]

    This gate is a single qubit T-gate. It is the same as RZ(pi/4).

    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="T", params=[], qubits=[unpack_qubit(qubit)])


def RX(angle, qubit):
    """Produces the RX instruction.

    RX(phi) = [[cos(phi / 2), -1j * sin(phi / 2)],
               [-1j * sin(phi / 2), cos(phi / 2)]]

    This gate is a single qubit X-rotation.

    :param angle: The angle to rotate around the x-axis on the bloch sphere.
    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="RX", params=[angle], qubits=[unpack_qubit(qubit)])


def RY(angle, qubit):
    """Produces the RY instruction.

    RY(phi) = [[cos(phi / 2), -sin(phi / 2)],
               [sin(phi / 2), cos(phi / 2)]]

    This gate is a single qubit Y-rotation.

    :param angle: The angle to rotate around the y-axis on the bloch sphere.
    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="RY", params=[angle], qubits=[unpack_qubit(qubit)])


def RZ(angle, qubit):
    """Produces the RZ instruction.

    RZ(phi) = [[cos(phi / 2) - 1j * sin(phi / 2), 0]
               [0, cos(phi / 2) + 1j * sin(phi / 2)]]

    This gate is a single qubit Z-rotation.

    :param angle: The angle to rotate around the z-axis on the bloch sphere.
    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="RZ", params=[angle], qubits=[unpack_qubit(qubit)])


def PHASE(angle, qubit):
    """Produces the PHASE instruction.

    PHASE(phi) = [[1, 0],
                  [0, exp(1j * phi)]]

    This is the same as the RZ gate.

    :param angle: The angle to rotate around the z-axis on the bloch sphere.
    :param qubit: The qubit apply the gate to.
    :returns: A Gate object.
    """
    return Gate(name="PHASE", params=[angle], qubits=[unpack_qubit(qubit)])


def CZ(control, target):
    """Produces a CZ instruction.

    CZ = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, -1]]


    This gate applies to two qubit arguments to produce the controlled-Z gate instruction.

    :param control: The control qubit.
    :param target: The target qubit. The target qubit has an Z-gate applied to it if the control
        qubit is in the excited state.
    :returns: A Gate object.
    """
    return Gate(name="CZ", params=[], qubits=[unpack_qubit(q) for q in (control, target)])


def CNOT(control, target):
    """Produces a CNOT instruction.

    CNOT = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]]

    This gate applies to two qubit arguments to produce the controlled-not gate instruction.

    :param control: The control qubit.
    :param target: The target qubit. The target qubit has an X-gate applied to it if the control
        qubit is in the excited state.
    :returns: A Gate object.
    """
    return Gate(name="CNOT", params=[], qubits=[unpack_qubit(q) for q in (control, target)])


def CCNOT(control1, control2, target):
    """Produces a CCNOT instruction.

    CCNOT = [[1, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 1, 0]]

    This gate applies to three qubit arguments to produce the controlled-controlled-not gate
    instruction.

    :param control1: The first control qubit.
    :param control2: The second control qubit.
    :param target: The target qubit. The target qubit has an X-gate applied to it if both control
        qubits are in the excited state.
    :returns: A Gate object.
    """
    qubits = [unpack_qubit(q) for q in (control1, control2, target)]
    return Gate(name="CCNOT", params=[], qubits=qubits)


def CPHASE00(angle, control, target):
    """Produces a CPHASE00 instruction.

    CPHASE00(phi) = diag([exp(1j * phi), 1, 1, 1])

    This gate applies to two qubit arguments to produce the variant of the controlled phase
    instruction that affects the state 00.

    :param angle: The input phase angle to apply when both qubits are in the ground state.
    :param control: Qubit 1.
    :param target: Qubit 2.
    :returns: A Gate object.
    """
    qubits = [unpack_qubit(q) for q in (control, target)]
    return Gate(name="CPHASE00", params=[angle], qubits=qubits)


def CPHASE01(angle, control, target):
    """Produces a CPHASE01 instruction.

    CPHASE01(phi) = diag([1.0, exp(1j * phi), 1.0, 1.0])

    This gate applies to two qubit arguments to produce the variant of the controlled phase
    instruction that affects the state 01.

    :param angle: The input phase angle to apply when q1 is in the excited state and q2 is in
        the ground state.
    :param control: Qubit 1.
    :param target: Qubit 2.
    :returns: A Gate object.
    """
    qubits = [unpack_qubit(q) for q in (control, target)]
    return Gate(name="CPHASE01", params=[angle], qubits=qubits)


def CPHASE10(angle, control, target):
    """Produces a CPHASE10 instruction.

    CPHASE10(phi) = diag([1, 1, exp(1j * phi), 1])

    This gate applies to two qubit arguments to produce the variant of the controlled phase
    instruction that affects the state 10.

    :param angle: The input phase angle to apply when q2 is in the excited state and q1 is in
        the ground state.
    :param control: Qubit 1.
    :param target: Qubit 2.
    :returns: A Gate object.
    """
    qubits = [unpack_qubit(q) for q in (control, target)]
    return Gate(name="CPHASE10", params=[angle], qubits=qubits)


def CPHASE(angle, control, target):
    """Produces a CPHASE instruction, which is a synonym for CPHASE11.

    CPHASE(phi) = diag([1, 1, 1, exp(1j * phi)])

    This gate applies to two qubit arguments to produce the variant of the controlled phase
    instruction that affects the state 11.

    :param angle: The input phase angle to apply when both qubits are in the excited state.
    :param control: Qubit 1.
    :param target: Qubit 2.
    :returns: A Gate object.
    """
    qubits = [unpack_qubit(q) for q in (control, target)]
    return Gate(name="CPHASE", params=[angle], qubits=qubits)


def SWAP(q1, q2):
    """Produces a SWAP instruction.

    SWAP = [[1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]]

     This gate swaps the state of two qubits.

    :param q1: Qubit 1.
    :param q2: Qubit 2.
    :returns: A Gate object.
    """
    return Gate(name="SWAP", params=[], qubits=[unpack_qubit(q) for q in (q1, q2)])


def CSWAP(control, target_1, target_2):
    """
    CSWAP = [[1, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1]]

    Produces a CSWAP instruction. This gate swaps the state of two qubits.

    :param control: The control qubit.
    :param target-1: The first target qubit.
    :param target-2: The second target qubit. The two target states are swapped if the control is
        in the excited state.
    """
    qubits = [unpack_qubit(q) for q in (control, target_1, target_2)]
    return Gate(name="CSWAP", params=[], qubits=qubits)


def ISWAP(q1, q2):
    """Produces an ISWAP instruction.

    ISWAP = [[1, 0,  0,  0],
             [0, 0,  1j, 0],
             [0, 1j, 0,  0],
             [0, 0,  0,  1]]

    This gate swaps the state of two qubits, applying a -i phase to q1 when it
    is in the excited state and a -i phase to q2 when it is in the ground state.

    :param q1: Qubit 1.
    :param q2: Qubit 2.
    :returns: A Gate object.
    """
    return Gate(name="ISWAP", params=[], qubits=[unpack_qubit(q) for q in (q1, q2)])


def PSWAP(angle, q1, q2):
    """Produces a PSWAP instruction.

    PSWAP(phi) = [[1, 0,             0,             0],
                  [0, 0,             exp(1j * phi), 0],
                  [0, exp(1j * phi), 0,             0],
                  [0, 0,             0,             1]]

    This is a parameterized swap gate.

    :param angle: The angle of the phase to apply to the swapped states. This phase is applied to
        q1 when it is in the excited state and to q2 when it is in the ground state.
    :param q1: Qubit 1.
    :param q2: Qubit 2.
    :returns: A Gate object.
    """
    return Gate(name="PSWAP", params=[angle], qubits=[unpack_qubit(q) for q in (q1, q2)])


WAIT = Wait()
"""
This instruction tells the quantum computation to halt. Typically these is used while classical memory is being
manipulated by a CPU in a hybrid classical/quantum algorithm.

:returns: A Wait object.
"""
RESET = Reset()
"""
This instruction resets all the qubits to the ground state.

:returns: A Reset object.
"""
NOP = Nop()
"""
This instruction applies no operation at that timestep. Typically these are ignored in error-models.

:returns: A Nop object.
"""
HALT = Halt()
"""
This instruction ends the program.

:returns: A Halt object.
"""


def MEASURE(qubit, classical_reg=None):
    """
    Produce a MEASURE instruction.

    :param qubit: The qubit to measure.
    :param classical_reg: The classical register to measure into, or None.
    :return: A Measurement instance.
    """
    qubit = unpack_qubit(qubit)
    address = None if classical_reg is None else unpack_classical_reg(classical_reg)
    return Measurement(qubit, address)


def TRUE(classical_reg):
    """
    Produce a TRUE instruction.

    :param classical_reg: A classical register to modify.
    :return: A ClassicalTrue instance.
    """
    return ClassicalTrue(unpack_classical_reg(classical_reg))


def FALSE(classical_reg):
    """
    Produce a FALSE instruction.

    :param classical_reg: A classical register to modify.
    :return: A ClassicalFalse instance.
    """
    return ClassicalFalse(unpack_classical_reg(classical_reg))


def NOT(classical_reg):
    """
    Produce a NOT instruction.

    :param classical_reg: A classical register to modify.
    :return: A ClassicalNot instance.
    """
    return ClassicalNot(unpack_classical_reg(classical_reg))


def AND(classical_reg1, classical_reg2):
    """
    Produce an AND instruction.

    :param classical_reg1: The first classical register.
    :param classical_reg2: The second classical register, which gets modified.
    :return: A ClassicalAnd instance.
    """
    left = unpack_classical_reg(classical_reg1)
    right = unpack_classical_reg(classical_reg2)
    return ClassicalAnd(left, right)


def OR(classical_reg1, classical_reg2):
    """
    Produce an OR instruction.

    :param classical_reg1: The first classical register.
    :param classical_reg2: The second classical register, which gets modified.
    :return: A ClassicalOr instance.
    """
    left = unpack_classical_reg(classical_reg1)
    right = unpack_classical_reg(classical_reg2)
    return ClassicalOr(left, right)


def MOVE(classical_reg1, classical_reg2):
    """
    Produce a MOVE instruction.

    :param classical_reg1: The first classical register.
    :param classical_reg2: The second classical register, which gets modified.
    :return: A ClassicalMove instance.
    """
    left = unpack_classical_reg(classical_reg1)
    right = unpack_classical_reg(classical_reg2)
    return ClassicalMove(left, right)


def EXCHANGE(classical_reg1, classical_reg2):
    """
    Produce an EXCHANGE instruction.

    :param classical_reg1: The first classical register, which gets modified.
    :param classical_reg2: The second classical register, which gets modified.
    :return: A ClassicalExchange instance.
    """
    left = unpack_classical_reg(classical_reg1)
    right = unpack_classical_reg(classical_reg2)
    return ClassicalExchange(left, right)


STANDARD_GATES = {'I': I,
                  'X': X,
                  'Y': Y,
                  'Z': Z,
                  'H': H,
                  'S': S,
                  'T': T,
                  'PHASE': PHASE,
                  'RX': RX,
                  'RY': RY,
                  'RZ': RZ,
                  'CZ': CZ,
                  'CNOT': CNOT,
                  'CCNOT': CCNOT,
                  'CPHASE00': CPHASE00,
                  'CPHASE01': CPHASE01,
                  'CPHASE10': CPHASE10,
                  'CPHASE': CPHASE,
                  'SWAP': SWAP,
                  'CSWAP': CSWAP,
                  'ISWAP': ISWAP,
                  'PSWAP': PSWAP
                  }
"""
Dictionary of standard gates. Keys are gate names, values are gate functions.
"""

__all__ = list(STANDARD_GATES.keys()) + ['WAIT', 'RESET', 'NOP', 'HALT', 'MEASURE', 'TRUE',
                                         'FALSE', 'NOT', 'AND', 'OR', 'MOVE', 'EXCHANGE',
                                         'Gate']
