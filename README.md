<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Branch and Bound for 0/1 Knapsack Problem</title>
</head>
<body>
    <div>
        <h1>Branch and Bound for 0/1 Knapsack Problem</h1>

        <h2>Introduction</h2>
        <p>This project implements the Branch and Bound algorithm to solve the 0/1 Knapsack Problem, a classic optimization problem in computer science.</p>

        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#introduction">Introduction</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#example">Example</a></li>
            <li><a href="#requirements">Requirements</a></li>
            <li><a href="#license">License</a></li>
        </ul>

        <h2>Introduction</h2>
        <p>This project implements the Branch and Bound algorithm to solve the 0/1 Knapsack Problem, a classic optimization problem in computer science.</p>

        <h2>Features</h2>
        <ul>
            <li>Branch and Bound algorithm implementation</li>
            <li>Calculation of bounds to prune branches</li>
            <li>Max-heap priority queue for efficient exploration</li>
            <li>Example usage and demonstration</li>
        </ul>

        <h2>Usage</h2>
        <ol>
            <li>Install Python if not already installed.</li>
            <li>Clone this repository to your local machine.</li>
            <li>Navigate to the project directory.</li>
            <li>Run the <code>knapsack_branch_and_bound.py</code> script, providing the weights, values, and capacity as input.</li>
        </ol>

        <h3>Example usage:</h3>
        <pre><code>python knapsack_branch_and_bound.py</code></pre>

        <h2>Example</h2>
        <pre><code>weights = [2, 5, 10, 4]
values = [40, 30, 50, 10]
capacity = 16

result = knapsack_branch_and_bound(weights, values, capacity)
print("Max Profit:", result[0])
print("Best Set of Items:", result[1])
</code></pre>

        <h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
        </ul>

        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>
</body>
</html>
