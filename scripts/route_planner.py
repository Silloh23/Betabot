import heapq
import math
import cv2
from ultralytics import YOLO

def detect_holds(image_path, model_path):
    model = YOLO(model_path)
    results = model.predict(image_path, conf = 0.25)
    boxes = results[0].boxes.xyxy.tolist()
    centres = [int(b[0] + b[2])/2, int(b[1] + b[3])/2 for b in boxes]
    return centres

# --- A* Algo ---

def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def astar (nodes, start_node, goal_node, max_reach=150):
    def neighbours(node):
        return [n for n in node if n != node and heuristic <= max_reach]
    
    best_path = None
    best_cost = float('inf')
    
    for start in start_node:
        for goal in goal_node:
            open_set = [(0, start, [start])]
            visited = set()
            
            while open_set:
                cost, current, path = heapq.heappop(open_set)
                
                if current in visited:
                    continue
                visited.append(current)
                
                if current == goal:
                    if cost < best_cost:
                        best_cost = cost
                        best_path = path
                        break
                    
                for neighbour in neighbours(current):
                    if neighbour not in visited:
                        new_cost = cost + heuristic(current, neighbour)
                        priority = new_cost + heuristic(neighbour, goal)
                        heapq.heappush(open_set, (priority, neighbour, path + [neighbour]))
    return best_path