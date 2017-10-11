import numpy as np

def normalize_data(data):
    areas = data[:,0]
    rooms = data[:,1]
    max_area = np.amax(areas)
    max_rooms = np.amax(rooms)
    areas = [area / max_area for area in areas]
    rooms = [room / max_rooms for room in rooms]
    normalized_data = [[areas[i], rooms[i]] for i in range(len(data))]
    return normalized_data, max_area, max_rooms
    