import csv

def read_data_from_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            data.append((row[8], float(row[9]), float(row[5])))  # Name, Price, Benchmark
    return data

def generate_combinations(cpu_data, gpu_data, ram_data, ssd_data, budget):
    combinations = []
    for cpu in cpu_data:
        for gpu in gpu_data:
            for ram in ram_data:
                for ssd in ssd_data:
                    total_price = cpu[1] + gpu[1] + ram[1] + ssd[1]
                    total_benchmark = cpu[2] + gpu[2] + ram[2] + ssd[2]
                    if total_price <= budget:
                        combinations.append((cpu, gpu, ram, ssd, total_price, total_benchmark))
    return combinations

def branch_and_bound(combinations, budget):
    best_combination = {
        'components': None,
        'total_price': 0,
        'total_benchmark': 0
    }
    best_score = 0
    for i, (cpu, gpu, ram, ssd, total_price, total_benchmark) in enumerate(combinations):
        if total_benchmark > best_score:
            best_score = total_benchmark
            best_combination['components'] = [cpu, gpu, ram, ssd]
            best_combination['total_price'] = total_price
            best_combination['total_benchmark'] = total_benchmark
        print(f"Progress: {i+1}/{len(combinations)}", end='\r')
    return best_combination

def formula(budget):
    cpu_data = read_data_from_csv("cpu_data.csv")
    gpu_data = read_data_from_csv("gpu_data.csv")
    ram_data = read_data_from_csv("ram_data.csv")
    ssd_data = read_data_from_csv("ssd_data.csv")

    combinations = generate_combinations(cpu_data, gpu_data, ram_data, ssd_data, budget)
    print("Searching for the best combination...")
    best_combination = branch_and_bound(combinations, budget)
    print_combination(best_combination)

    return best_combination

def print_combination(best_combination):
    if best_combination['components'] is None:
        print("No combination found within the budget.")
        return

    print("Best Combination:")
    for component in best_combination['components']:
        print(f"{component[0]} - Price: ${component[1]} - Benchmark: {component[2]}")
    print(f"Total Price: ${best_combination['total_price']} - Total Benchmark: {best_combination['total_benchmark']}")
