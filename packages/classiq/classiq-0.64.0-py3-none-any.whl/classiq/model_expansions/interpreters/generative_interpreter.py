from functools import singledispatchmethod

from classiq.interface.generator.functions.builtins.internal_operators import (
    CONTROL_OPERATOR_NAME,
    INVERT_OPERATOR_NAME,
    WITHIN_APPLY_NAME,
)
from classiq.interface.model.bind_operation import BindOperation
from classiq.interface.model.classical_if import ClassicalIf
from classiq.interface.model.control import Control
from classiq.interface.model.inplace_binary_operation import InplaceBinaryOperation
from classiq.interface.model.invert import Invert
from classiq.interface.model.phase_operation import PhaseOperation
from classiq.interface.model.power import Power
from classiq.interface.model.quantum_expressions.quantum_expression import (
    QuantumAssignmentOperation,
)
from classiq.interface.model.quantum_function_call import QuantumFunctionCall
from classiq.interface.model.quantum_statement import QuantumStatement
from classiq.interface.model.repeat import Repeat
from classiq.interface.model.variable_declaration_statement import (
    VariableDeclarationStatement,
)
from classiq.interface.model.within_apply_operation import WithinApply

from classiq.model_expansions.interpreters.base_interpreter import BaseInterpreter
from classiq.model_expansions.quantum_operations import (
    BindEmitter,
    ClassicalIfEmitter,
    QuantumFunctionCallEmitter,
    RepeatEmitter,
    VariableDeclarationStatementEmitter,
)
from classiq.model_expansions.quantum_operations.shallow_emitter import ShallowEmitter


class GenerativeInterpreter(BaseInterpreter):
    @property
    def is_shallow(self) -> bool:
        return True

    @singledispatchmethod
    def emit(self, statement: QuantumStatement) -> None:  # type:ignore[override]
        raise NotImplementedError(f"Cannot emit {statement!r}")

    @emit.register
    def emit_quantum_function_call(self, call: QuantumFunctionCall) -> None:
        QuantumFunctionCallEmitter(self).emit(call)

    @emit.register
    def emit_bind(self, bind: BindOperation) -> None:
        BindEmitter(self).emit(bind)

    @emit.register
    def emit_quantum_assignment_operation(self, op: QuantumAssignmentOperation) -> None:
        ShallowEmitter(
            self, "assignment_operation", components=["expression", "result_var"]
        ).emit(op)

    @emit.register
    def emit_inplace_binary_operation(self, op: InplaceBinaryOperation) -> None:
        ShallowEmitter(
            self, "inplace_binary_operation", components=["target", "value"]
        ).emit(op)

    @emit.register
    def emit_variable_declaration(
        self, variable_declaration: VariableDeclarationStatement
    ) -> None:
        VariableDeclarationStatementEmitter(self).emit(variable_declaration)

    @emit.register
    def emit_classical_if(self, classical_if: ClassicalIf) -> None:
        ClassicalIfEmitter(self).emit(classical_if)

    @emit.register
    def emit_within_apply(self, within_apply: WithinApply) -> None:
        ShallowEmitter(
            self,
            WITHIN_APPLY_NAME,
            components=["within", "apply", "compute", "action"],
        ).emit(within_apply)

    @emit.register
    def emit_invert(self, invert: Invert) -> None:
        ShallowEmitter(self, INVERT_OPERATOR_NAME, components=["body"]).emit(invert)

    @emit.register
    def emit_repeat(self, repeat: Repeat) -> None:
        RepeatEmitter(self).emit(repeat)

    @emit.register
    def emit_control(self, control: Control) -> None:
        ShallowEmitter(
            self,
            CONTROL_OPERATOR_NAME,
            components=["expression", "body", "else_block"],
        ).emit(control)

    @emit.register
    def emit_power(self, power: Power) -> None:
        ShallowEmitter(self, CONTROL_OPERATOR_NAME, components=["power", "body"]).emit(
            power
        )

    @emit.register
    def emit_phase(self, phase: PhaseOperation) -> None:
        ShallowEmitter(self, "phase", components=["expression", "theta"]).emit(phase)
