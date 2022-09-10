from dataclasses import dataclass


@dataclass
class RunResult:
    name: str
    size: int
    read_operations: int
    write_operations: int
    comparison_operations: int

    def to_tuple(self):
        return (self.name,self.size,self.read_operations,self.write_operations,self.comparison_operations)

    @staticmethod
    def labels():
        return ['name','size','read_operations','write_operations','comparison_operations']

    @staticmethod
    def short_labels():
        return ['name','size','reads','writes','comparisons']
