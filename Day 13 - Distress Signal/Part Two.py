import functools
from inputs.input import get_input

inp = [i for i in get_input(13).read().split("\n") if i != ""]


def get_lists(value, first=True):
    if "[" in value:
        count = 0
        first_found = None
        replace_list = []
        new_string = ""
        for i, c in enumerate(value):
            new_string += c
            if c == "[":
                count += 1
                if first_found is None:
                    first_found = i
            elif c == "]":
                count -= 1
                if count == 0:
                    sub_list = value[first_found:i+1]
                    first_found = None
                    replace_list.append(get_lists(sub_list[1:-1], False))
                    new_string = new_string.replace(sub_list, "!")
        new_string = new_string.split(",")
        new_list = []
        for i in new_string:
            if i == "!":
                new_list.append(replace_list.pop(0))
            else:
                new_list.append(int(i))
        if first:
            return new_list[0]
        return new_list
    else:
        return [int(i) for i in value.split(",") if i != ""]


def compare_packets(left, right):
    for i in range(0, len(left)):
        if (len(right) == i and len(left) > i):
            return -1
        if (
            type(left[i]) == int
            and type(right[i]) == int
        ):
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
            continue
        elif (
            type(left[i]) == list
            and type(right[i]) == list
        ):
            r = compare_packets(left[i], right[i])
            if r is not None:
                return r
        else:
            new_left = left[i] if type(left[i]) == list else [left[i]]
            new_right = right[i] if type(right[i]) == list else [right[i]]
            r = compare_packets(new_left, new_right)
            if r is not None:
                return r
    if len(left) < len(right):
        return 1


divisor_packets = [[2]],[[6]]

packets = [*divisor_packets]
for packet in inp:
    packets.append(get_lists(packet))

packets.sort(key=functools.cmp_to_key(compare_packets), reverse=True)

print((packets.index(divisor_packets[0])+1)*(packets.index(divisor_packets[1])+1))
