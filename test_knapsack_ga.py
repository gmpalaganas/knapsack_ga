import knapsack_ga_binary as knapsack_binary
import knapsack_ga_array  as knapsack_array

import time

def main():
    file_name = 'test_data/knapsack_24.txt'
    with open(file_name) as f:
        n_items = int(f.readline())
        w_max = int(f.readline())
        
        weights = []

        for i in range(0,n_items):
            weights.append(int(f.readline()))

        values = []

        for i in range(0,n_items):
            values.append(int(f.readline()))

    f.close()

    p_size = 100 # Population Size
    m_rate = 100  # Mutation Rate 1% 
    acceptance = 0.6 # Convergence acceptance
    g_max = 1000 # Max generations

    g_sum = 0
    t_sum = 0

    iterations = 1 

    for i in range(0,iterations):
        start_time = time.time()
        (generations,solution) = \
                knapsack_array.solve_knapsack(values,weights,w_max,p_size,m_rate,g_max,acceptance)
        t_sum += time.time() - start_time
        g_sum += generations

    print("Knapsack Array Version stats: ")
    print("Average runtime: ", t_sum / iterations)
    print("Average generations: ", float(g_sum) / float(iterations))

    g_sum = 0
    t_sum = 0

    for i in range(0,iterations):
        start_time = time.time()
        (generations,solution) = \
                knapsack_binary.solve_knapsack(values,weights,w_max,p_size,m_rate,g_max,acceptance)
        t_sum += time.time() - start_time
        g_sum += generations

    print("Knapsack Binary Version stats: ")
    print("Average runtime: ", t_sum / iterations)
    print("Average generations: ", float(g_sum) / float(iterations))

if __name__ == "__main__":
    main()
