import intcode

with open("year_2019/input_05.txt", encoding="utf-8") as f:
    full_input = f.read().strip()

computer1 = intcode.Computer(program=list(map(int, full_input.split(","))))
computer2 = intcode.Computer(program=list(map(int, full_input.split(","))))

computer1.input_callback = intcode.input_list_wrapper([1])
computer1.run()

computer2.input_callback = intcode.input_list_wrapper([5])
computer2.run()
