
import time

def get_puzzle_input():

    return "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6".split("\t")


def get_puzzle_example_input():
    return [0, 2, 7, 0]
    #return [2, 4, 1, 2]


if __name__ == "__main__":

    q = get_puzzle_input()

    q = [int(item) for item in q]
    print(q)

    print(type(q))
    print("q=", q)


    state_memory = {}
    count = 0

    dist_count = 0

    while str(q) not in state_memory:
        state_memory[str(q)] = 1
        winning_index = q.index(max(q))
        no_blocks_to_redistribute = q[winning_index]
        q[winning_index] = 0

        distribute_index = winning_index + 1

        dist_count += 1

        while no_blocks_to_redistribute > 0:
            state_memory[str(q)] = 1

            #print("dist ind: %d" % distribute_index, "q= ", q)

            if distribute_index >= len(q):
                distribute_index = 0

            q[distribute_index] += 1
            no_blocks_to_redistribute -= 1

            distribute_index += 1

        #print("end of dist, q=", q)

        #print("----")
        #print(state_memory)
        #time.sleep(1)


    print("break while -- we found something we've seen before", q, dist_count)
