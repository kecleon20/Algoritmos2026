markdown
# 🐍 Data Structures & Algorithms in Python

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

Welcome to my repository of **Data Structures and Algorithms**, built entirely from scratch in Python. 

As an Advanced Systems Analysis student at UADER (Argentina), I believe that understanding how data is stored, processed, and optimized under the hood is essential for writing efficient code—especially when dealing with large datasets in Data Analytics and Software Development.

This repository contains my implementations of fundamental Abstract Data Types (ADTs) along with practical exercises solving real-world logical problems.

---

## 📂 Repository Structure

Here is a breakdown of what you will find in this repository:

| Directory | Data Structure / Concept | Key Implementations |
| :--- | :--- | :--- |
| 📁 **`/Recursividad`** | **Recursion** | Roman numeral conversion, recursive searching (e.g., "Star Wars backpack" problem). |
| 📁 **`/Pilas`** | **Stacks (LIFO)** | Stack implementation, pathfinding (robot returning home), array sorting using stacks. |
| 📁 **`/Colas`** | **Queues (FIFO)** | Queue implementation, notification filtering, priority queues using Heaps (Min/Max). |
| 📁 **`/Listas`** | **Lists & Nested Lists** | Sorted insertion, Binary Search, 1-to-N relationships (e.g., Trainers and their Pokémon). |
| 📁 **`/Arboles`** | **Trees & AVL Trees** | Self-balancing Binary Search Trees (AVL), complex data parsing (Jedi database, Mythological creatures). |
| 📁 **`/Grafos`** | **Graphs & Optimization** | BFS, DFS, **Dijkstra's Algorithm** (Shortest Path), **Kruskal's Algorithm** (Minimum Spanning Tree). |

---

## 🛠️ Key Concepts Mastered

*   **Object-Oriented Programming (OOP):** Custom classes for Nodes, Queues, Stacks, and Graphs.
*   **Algorithm Optimization:** Understanding Time Complexity (Big O). Using custom Min-Heaps to optimize Dijkstra's algorithm for pathfinding.
*   **Recursion:** Breaking down complex problems into base cases and recursive steps.
*   **File I/O & Parsing:** Reading external `.txt` files and mapping the data into complex node structures.
*   **Data Manipulation:** Working with dictionaries inside tree nodes to store multiple attributes (e.g., ranking, descriptions, relationships).

---

## 🚀 Highlighted Projects

### 1. Self-Balancing AVL Trees (Jedi & Creatures)
Implemented a Binary Tree that automatically balances itself using **simple and double rotations**. It reads data from external text files to build a database of Jedi (filtering by rank, lightsaber color) and Mythological creatures (tracking their defeaters and capturers).

### 2. Graph Optimization (Home Wiring & Network Topology)
Simulated a smart home wiring system and a computer network. Used **Kruskal's Algorithm** to find the most cost-effective way to wire the house, and **Dijkstra's Algorithm** (powered by a custom Min-Heap) to find the shortest network path from a PC to a printer or server.

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/kecleon20/Estructuras-de-Datos-Python.git
Navigate to any directory (e.g., /Arboles):

bash
cd Arboles
Run the Python files:

bash
python jedis.py

Created with 💻 by Thiago Chevallet
Connect with me on LinkedIn