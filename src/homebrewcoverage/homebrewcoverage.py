class HomebrewCoverage:
    num_branches: int = 0
    branches_taken: list = []
    func_name: str = ""

    def __init__(self, num_branches: int, func_name: str):
        self.num_branches = num_branches
        self.branches_taken = [False] * num_branches
        self.func_name = func_name

        # check if .txt file already exists, if so, read it to our branches_taken
        try:
            with open(f"{self.func_name}.txt", "r") as file:
                lines = file.readlines()
                for i in range(self.num_branches):
                    self.branches_taken[i] = True if "True" in lines[i] else False
        except FileNotFoundError:
            pass


    def taken(self, i: int):
        self.branches_taken[i] = True

        # write to file
        with open(f"{self.func_name}.txt", "w") as file:
            for i in range(self.num_branches):
                file.write(f"{self.branches_taken[i]}\n")

    def print_result(self):
        with open(f"{self.func_name}_result.txt", "w") as file:
            file.write(f"Branch coverage: {sum(self.branches_taken)} / {self.num_branches}\n")
            file.write(f"Branch coverage: {sum(self.branches_taken) / self.num_branches * 100} %\n")
            # file.write(f"Branches taken: {self.branches_taken}\n")

            for i in range(self.num_branches):
                file.write(f"Branch {i} taken: {self.branches_taken[i]} ")
            file.write("\n")
