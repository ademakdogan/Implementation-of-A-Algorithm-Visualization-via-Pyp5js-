#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: A.Akdogan
"""
from random import randint
import argparse


class Node:

    def __init__(self, x, y):

        self.x = x 
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self. obstacle = False

    def add_neighbors(self,grid, columns, rows):

        neighbor_x = self.x
        neighbor_y = self.y
    
        if neighbor_x < columns - 1:
            self.neighbors.append(grid[neighbor_x+1][neighbor_y])
        if neighbor_x > 0:
            self.neighbors.append(grid[neighbor_x-1][neighbor_y])
        if neighbor_y < rows -1:
            self.neighbors.append(grid[neighbor_x][neighbor_y +1])
        if neighbor_y > 0: 
            self.neighbors.append(grid[neighbor_x][neighbor_y-1])
        #diagonals
        """ if neighbor_x > 0 and neighbor_y > 0:
            self.neighbors.append(grid[neighbor_x-1][neighbor_y-1])
        if neighbor_x < columns -1 and neighbor_y > 0:
            self.neighbors.append(grid[neighbor_x+1][neighbor_y-1])
        if neighbor_x > 0 and neighbor_y <rows -1:
            self.neighbors.append(grid[neighbor_x-1][neighbor_y+1])
        if neighbor_x < columns -1 and neighbor_y < rows -1:
            self.neighbors.append(grid[neighbor_x+1][neighbor_y+1]) """


        
class AStar:

    def __init__(self, cols, rows, start, end, obstacle_ratio = False, obstacle_list = False):

        self.cols = cols
        self.rows = rows
        self.start = start
        self.end = end
        self.obstacle_ratio = obstacle_ratio
        self.obstacle_list = obstacle_list

    @staticmethod
    def clean_open_set(open_set, current_node):

        for i in range(len(open_set)):
            if open_set[i] == current_node:
                open_set.pop(i)
                break

        return open_set

    @staticmethod
    def h_score(current_node, end):

        distance =  abs(current_node.x - end.x) + abs(current_node.y - end.y)
        
        return distance

    @staticmethod
    def create_grid(cols, rows):

        grid = []
        for _ in range(cols):
            grid.append([])
            for _ in range(rows):
                grid[-1].append(0)
        
        return grid

    @staticmethod
    def fill_grids(grid, cols, rows, obstacle_ratio = False, obstacle_list = False):

        for i in range(cols):
            for j in range(rows):
                grid[i][j] = Node(i,j)
                if obstacle_ratio == False:
                    pass
                else:
                    n = randint(0,100)
                    if n < obstacle_ratio: grid[i][j].obstacle = True
        if obstacle_list == False:
            pass
        else:
            for i in range(len(obstacle_list)):
                grid[obstacle_list[i][0]][obstacle_list[i][1]].obstacle = True

        return grid

    @staticmethod
    def get_neighbors(grid, cols, rows):
        for i in range(cols):
            for j in range(rows):
                grid[i][j].add_neighbors(grid, cols, rows)
        return grid
    
    @staticmethod
    def start_path(open_set, closed_set, current_node, end):

        best_way = 0
        for i in range(len(open_set)):
            if open_set[i].f < open_set[best_way].f:
                best_way = i

        current_node = open_set[best_way]
        final_path = []
        if current_node == end:
            temp = current_node
            while temp.previous:
                final_path.append(temp.previous)
                temp = temp.previous
            
            print("Done !!")

        open_set = AStar.clean_open_set(open_set, current_node)
        closed_set.append(current_node)
        neighbors = current_node.neighbors
        for neighbor in neighbors:
            if (neighbor in closed_set) or (neighbor.obstacle == True):
                continue
            else:
                temp_g = current_node.g + 1
                control_flag = 0
                for k in range(len(open_set)):
                    if neighbor.x == open_set[k].x and neighbor.y == open_set[k].y:
                        if temp_g < open_set[k].g:
                            open_set[k].g = temp_g
                            open_set[k].h= AStar.h_score(open_set[k], end)
                            open_set[k].f = open_set[k].g + open_set[k].h
                            open_set[k].previous = current_node
                        else:
                            pass
                        control_flag = 1
  
                if control_flag == 1:
                    pass
                else:
                    neighbor.g = temp_g
                    neighbor.h = AStar.h_score(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current_node
                    open_set.append(neighbor)

        return open_set, closed_set, current_node, final_path

    def main(self):

        grid = AStar.create_grid(self.cols, self.rows)
        grid = AStar.fill_grids(grid, self.cols, self.rows, obstacle_ratio = self.obstacle_ratio, obstacle_list = self.obstacle_list)
        grid = AStar.get_neighbors(grid, self.cols, self.rows)
        open_set  = []
        closed_set  = []
        current_node = None
        final_path  = []
        open_set.append(grid[self.start[0]][self.start[1]])
        self.end = grid[self.end[0]][self.end[1]]
        while len(open_set) > 0:
            open_set, closed_set, current_node, final_path = AStar.start_path(open_set, closed_set, current_node, self.end)
            if len(final_path) > 0:
                break

        return final_path


if __name__ == "__main__":

    ap = argparse.ArgumentParser()  
    ap.add_argument("-c", "--cols", required=True)
    ap.add_argument("-r", "--rows", required=True)
    ap.add_argument("-s", "--start_x", required=True, help = "x coor of start point")
    ap.add_argument("-q", "--start_y", required=True, help = "y coor of start point")
    ap.add_argument("-e", "--end_x", required=True, help = "x coor of end point")
    ap.add_argument("-t", "--end_y", required=True, help = "y coor of end point")
    ap.add_argument("-o", "--obstacle_ratio", required=False, help = "ratio of obstacle (black list)", default = 20)
    ap.add_argument("-l", "--obstacle_list", required=False, help = "You can also create own obstacle. It should be list of list --> [[0,1],[3,2]] add in your obstacle.json file", default = False, type = str)
    
    args = vars(ap.parse_args())
    if args["obstacle_list"] == "True":
        #print(args["obstacle_list"])
        import json
        json_file_path = "your_obstacle.json"
        with open(json_file_path, 'r') as j:
            contents = json.loads(j.read())
        data = json.loads(contents["data"])
        a_star = AStar(int(args["cols"]),  int(args["rows"]), [int(args["start_x"]), int(args["start_y"])], [int(args["end_x"]), int(args["end_y"])], False,data)
    else:
        a_star = AStar(int(args["cols"]),  int(args["rows"]), [int(args["start_x"]), int(args["start_y"])], [int(args["end_x"]), int(args["end_y"])], int(args["obstacle_ratio"]), False)

    final_path = a_star.main()
    if len(final_path) > 0:
        print("The way found!!!")
        for i in range(len(final_path)):
            print(final_path[i].x, final_path[i].y)
    else:   
        print("There is no legal way...You can decrease obstacle ration (default 20)")
 


