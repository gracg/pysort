from dataclasses import dataclass


@dataclass
class RunResult:
    name: str
    size: int
    read_operations: int
    write_operations: int
    comparison_operations: int
