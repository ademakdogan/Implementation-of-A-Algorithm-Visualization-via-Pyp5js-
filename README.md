## Python Implementation of A* Algorithm   
A* is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases. 

   
--------------

### Pyp5js for Visualition   
This project has been created for A* algorithm implementation in Python 3. [Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm) is used as the Pseudocode source. The repository consists of two main parts. The first part is about visualization. Pyp5js is used to visualize the algorithm. You can find the repository [here](https://github.com/berinhard/pyp5js). In this section, obstacles are created randomly. The algorithm finds the best path according to the obstacles that occur differently at each step. Some examples can be seen below.   

   
![astar](images/astar.gif) 

--------------

### Define all parameters  
  
In the second one, the user can run the [AStar.py](AStar.py) file with the parameters that he/she has determined. The details of the parameters to be entered are shown below.


arguments:   

* -h, --help            show this help message and exit
* -c, --cols, Total number of columns to be entered
* -r, --rows, Total number of rows to be entered
* -s, --start_x, X coordinate of the start point        
* -q, --start_y, Y coordinate of the start point                  
* -e, --end_x, X coordinate of the end point
                        
* -t, --end_y, Y coordinate of the end point

* -o, --obstacle_ratio, ratio of obstacle (black list)
* -l , --obstacle_list,
                        You can also create own obstacle. It should be list of
                        list --> [[0,1],[3,2]] add in your [your_obstacle.json](your_obstacle.json) file


Example usage:  

```
  python AStar.py -c 25 -r 25 -s 1 -q 3 -e 23 -t 21 -l True
```   
Result:   
```
The way found!!!
23 20
23 19
23 18
23 17
23 16
23 15
23 14
23 13
23 12
23 11
23 10
23 9
23 8
23 7
23 6
23 5
23 4
23 3
22 3
21 3
20 3
19 3
18 3
17 3
16 3
15 3
14 3
13 3
12 3
11 3
10 3
9 3
8 3
7 3
6 3
5 3
4 3
3 3
2 3
1 3

``` 


--------------


  