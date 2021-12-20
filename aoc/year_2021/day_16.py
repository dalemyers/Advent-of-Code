"""Day 16"""

from typing import List, Optional
from aoc.shared.input import read_file_lines


def bits(data: bytes) -> List[int]:
    all_bits = []
    for byte in data:
        current_bits = [int(n) for n in bin(byte)[2:]]
        current_bits = [0] * 8 + current_bits
        current_bits = current_bits[-8:]
        all_bits.extend(current_bits)
    return all_bits


def bits_to_int(bits: List[int]) -> int:
    return int("".join(map(str, bits)), 2)


class BitStream:
    def __init__(self, data_bits: List[int]) -> None:
        self.stream = data_bits
        self.offset = 0

    @staticmethod
    def from_hex(hex_values: str) -> "BitStream":
        data_bytes = bytes.fromhex(hex_values)
        return BitStream(bits(data_bytes))

    def read(self, n: int) -> List[int]:
        read_bits = self.stream[self.offset : self.offset + n]
        self.offset += n
        return read_bits

    def read_version(self) -> int:
        values = self.read(3)
        return bits_to_int(values)

    def read_type_id(self) -> int:
        values = self.read(3)
        return bits_to_int(values)

    def read_literal(self) -> int:
        literal_bits = []
        while True:
            next_bits = self.read(5)
            literal_bits.extend(next_bits[1:])
            if next_bits[0] == 0:
                break
        return bits_to_int(literal_bits)

    def read_int(self, length: int) -> int:
        return bits_to_int(self.read(length))

    def substream(self, length: int) -> int:
        sub_bits = self.read(length)
        return BitStream(sub_bits)

    def has_data(self) -> bool:
        return self.offset < len(self.stream) - 1


class Packet:
    def __init__(self, version: int) -> None:
        self.version = version

    def version_sum(self) -> int:
        return self.version

    def value(self) -> int:
        return NotImplemented


class LiteralPacket(Packet):
    def __init__(self, version: int, value: int) -> None:
        super().__init__(version)
        self._value = value

    def value(self) -> int:
        return self._value

    def __str__(self) -> str:
        return f"<LiteralPacket {self._value}>"

    def __repr__(self) -> str:
        return self.__str__()


class OperatorPacket(Packet):

    packets: List[Packet]

    def __init__(self, version: int, type_id: int, packets: List[Packet]) -> None:
        super().__init__(version)
        self.type_id = type_id
        self.packets = packets

    def version_sum(self) -> int:
        total = self.version
        for p in self.packets:
            total += p.version_sum()
        return total


class SumPacket(OperatorPacket):
    def value(self) -> int:
        total = 0
        for p in self.packets:
            total += p.value()
        return total


class ProductPacket(OperatorPacket):
    def value(self) -> int:
        total = 1
        for p in self.packets:
            total *= p.value()
        return total


class MinimumPacket(OperatorPacket):
    def value(self) -> int:
        return min([p.value() for p in self.packets])


class MaximumPacket(OperatorPacket):
    def value(self) -> int:
        return max([p.value() for p in self.packets])


class GreaterThanPacket(OperatorPacket):
    def value(self) -> int:
        if self.packets[0].value() > self.packets[1].value():
            return 1

        return 0


class LessThanPacket(OperatorPacket):
    def value(self) -> int:
        if self.packets[0].value() < self.packets[1].value():
            return 1

        return 0


class EqualToPacket(OperatorPacket):
    def value(self) -> int:
        if self.packets[0].value() == self.packets[1].value():
            return 1

        return 0


PACKET_MAP = {
    0: SumPacket,
    1: ProductPacket,
    2: MinimumPacket,
    3: MaximumPacket,
    5: GreaterThanPacket,
    6: LessThanPacket,
    7: EqualToPacket,
}


def parse_packets(
    stream: BitStream, *, max_packets: Optional[int] = None
) -> List[Packet]:

    packets = []

    while True:

        if max_packets and len(packets) == max_packets:
            break

        if not stream.has_data():
            break

        version = stream.read_version()
        type_id = stream.read_type_id()

        if type_id == 4:
            literal = stream.read_literal()
            packets.append(LiteralPacket(version, literal))
            continue

        length_type_id = stream.read(1)[0]
        if length_type_id == 0:
            length = stream.read_int(15)
            subpackets = parse_packets(stream.substream(length))
        else:
            packet_count = stream.read_int(11)
            subpackets = parse_packets(stream, max_packets=packet_count)

        constructor = PACKET_MAP[type_id]

        packets.append(constructor(version, type_id, subpackets))

    return packets


def part1() -> int:
    """Part 1."""

    values = read_file_lines("year_2021/input_16.txt")[0]
    stream = BitStream.from_hex(values)

    packet = parse_packets(stream, max_packets=1)[0]

    return packet.version_sum()


def part2() -> int:
    """Part 2."""

    values = read_file_lines("year_2021/input_16.txt")[0]

    stream = BitStream.from_hex(values)

    packet = parse_packets(stream, max_packets=1)[0]

    return packet.value()


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
