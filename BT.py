import csv

def read_data_from_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            data.append((row[8], float(row[9]), float(row[5])))  # Name, Price, Benchmark
    return data

def backtrack(cpu_data, gpu_data, ram_data, ssd_data, budget, index=0, current_combination=None, best_combination=None, progress_tracker=None):
    if current_combination is None:
        current_combination = {
            'components': [],
            'total_price': 0,
            'total_benchmark': 0
        }
    
    if best_combination is None:
        best_combination = {
            'components': None,
            'total_price': 0,
            'total_benchmark': 0
        }
    
    if progress_tracker is None:
        progress_tracker = {'count': 0, 'progress_interval': 1000}

    progress_tracker['count'] += 1
    if progress_tracker['count'] % progress_tracker['progress_interval'] == 0:
        print(f"Progress: {progress_tracker['count']} nodes explored.")

    if index == 4:
        if (current_combination['total_price'] <= budget and 
            current_combination['total_benchmark'] > best_combination['total_benchmark']):
            best_combination['components'] = list(current_combination['components'])
            best_combination['total_price'] = current_combination['total_price']
            best_combination['total_benchmark'] = current_combination['total_benchmark']
        return best_combination
    
    if index == 0:
        components_data = cpu_data
    elif index == 1:
        components_data = gpu_data
    elif index == 2:
        components_data = ram_data
    else:
        components_data = ssd_data

    for component in components_data:
        current_combination['components'].append(component)
        current_combination['total_price'] += component[1]
        current_combination['total_benchmark'] += component[2]

        best_combination = backtrack(cpu_data, gpu_data, ram_data, ssd_data, budget, index + 1, current_combination, best_combination, progress_tracker)
        
        current_combination['components'].pop()
        current_combination['total_price'] -= component[1]
        current_combination['total_benchmark'] -= component[2]

    return best_combination

def formula(budget):
    cpu_data = read_data_from_csv("cpu_data.csv")
    gpu_data = read_data_from_csv("gpu_data.csv")
    ram_data = read_data_from_csv("ram_data.csv")
    ssd_data = read_data_from_csv("ssd_data.csv")
    
    best_combination = backtrack(cpu_data, gpu_data, ram_data, ssd_data, budget)
    
    return best_combination

