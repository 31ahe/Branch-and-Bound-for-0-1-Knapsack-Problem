import heapq

class Node:
    def __init__(self, level, profit, weight, bound, includes):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
        self.includes = includes  

    def __lt__(self, other):
        return self.bound > other.bound  
    
def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)

    def calculate_bound(node):
        if node.weight > capacity or node.level == n - 1:
            return 0  

        bound = node.profit
        j = node.level + 1
        total_weight = node.weight

        while j < n and total_weight + weights[j] <= capacity:
            total_weight += weights[j]
            bound += values[j]
            j += 1

        if j < n:
            if total_weight + weights[j] == capacity:
                bound += values[j]
            else:
                bound += (capacity - total_weight) * (values[j] / weights[j])

        return bound

    max_profit = 0
    best_set = []
    priority_queue = []

    root = Node(level=-1, profit=0, weight=0, bound=calculate_bound(Node(-1, 0, 0, 0, [])), includes=[])
    heapq.heappush(priority_queue, root)

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        print(f"Level {current_node.level}: Profit={current_node.profit}, Weight={current_node.weight}, Bound={current_node.bound}, Includes={current_node.includes}")

        if current_node.bound < max_profit:
            continue

        left_child = Node(
            level=current_node.level + 1,
            profit=current_node.profit + values[current_node.level + 1],
            weight=current_node.weight + weights[current_node.level + 1],
            bound=calculate_bound(Node(
                level=current_node.level + 1,
                profit=current_node.profit + values[current_node.level + 1],
                weight=current_node.weight + weights[current_node.level + 1],
                bound=0,
                includes=[]
            )),
            includes=current_node.includes + [current_node.level + 1],
        )

        if left_child.weight <= capacity and left_child.profit > max_profit:
            max_profit = left_child.profit
            best_set = left_child.includes

        heapq.heappush(priority_queue, left_child)

        if left_child.level < n - 1:
            right_child = Node(
                level=current_node.level + 1,
                profit=current_node.profit,
                weight=current_node.weight,
                bound=calculate_bound(Node(
                    level=current_node.level + 1,
                    profit=current_node.profit,
                    weight=current_node.weight,
                    bound=0,
                    includes=[]
                )),
                includes=current_node.includes.copy(),
            )

            heapq.heappush(priority_queue, right_child)

    return max_profit, best_set

weights = [2, 5, 10, 4]
values = [40, 30, 50, 10]
capacity = 16

result = knapsack_branch_and_bound(weights, values, capacity)
print("\nMax Profit:", result[0])
print("Best Set of Items:", result[1])
