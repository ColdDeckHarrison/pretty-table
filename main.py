from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Squirtle", "Pikachu", "charmander", "pidgy"])
table.add_column("Energy Type", ["water", "electric", "fire", "normal"])
print(table)
