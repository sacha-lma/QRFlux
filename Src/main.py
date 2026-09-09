import tkinter as tk




def main() -> None:

    ModuleSize, NbSlots, RequestedSentence = get_user_input()
    Win, canvas= initialize_Window(NbSlots, ModuleSize)

    #generated_matrix = generate_qr_matrix(converted_data = convert_to_binary(RequestedSentence))
    #draw_qr_code(generated_matrix, canvas, NbSlots, ModuleSize)

    Win.mainloop()

    print("QRFlux requested : ", RequestedSentence)

def get_user_input() -> tuple[int, int, str]:
    ModuleSize = int(input("Enter module size: (10 recommended) "))
    NbSlots = int(input("Enter number of slots: (41 recommended) "))

    while NbSlots < 27:
        print("Error: Number of slots must be at least 27.")
        NbSlots = int(input("Enter number of slots: (41 recommended) "))

    while ModuleSize < 5:
        print("Error: Module size must be at least 5.")
        ModuleSize = int(input("Enter module size: (10 recommended) "))

    RequestedSentence = input("request sentence: ")
    return ModuleSize, NbSlots, RequestedSentence

def initialize_Window(NbSlots: int, ModuleSize: int) -> tk.Tk:
    Win = tk.Tk()
    Win.title("QRFlux")
    Win.geometry("{}x{}".format(NbSlots * ModuleSize, NbSlots * ModuleSize))

    canvas = tk.Canvas(Win, width=NbSlots * ModuleSize, height=NbSlots * ModuleSize, bg="white")
    canvas.pack()

    return Win, canvas

def draw_qr_code(matrix: list[list[int]], canvas: tk.Canvas, NbSlots: int, ModuleSize: int) -> None:
    canvas.delete("all")
    for row in range(NbSlots):
        for col in range(NbSlots):
            if matrix[row][col] == 1:
                x0 = col * ModuleSize
                y0 = row * ModuleSize
                x1 = x0 + ModuleSize
                y1 = y0 + ModuleSize
                canvas.create_rectangle(x0, y0, x1, y1, fill="black", outline="black")

def convert_to_binary(data: str) -> list[int]:
    binary_data = []
    for char in data:
        binary_char = format(ord(char), '08b')  # Convert character to 8-bit binary
        binary_data.append(int(binary_char, 2))  # Convert binary string to integer
    return binary_data

def encrypt_data(data: list[int]) -> list[int]:
    # Placeholder for encryption logic
    # For demonstration, we'll just return the data as is
    return data

def generate_qr_matrix(data: list[int], NbSlots: int) -> list[list[int]]:
    matrix = initialize_matrix(NbSlots)
    matrix = place_orientation_patterns(matrix, NbSlots)
    matrix = size_patterns(matrix, NbSlots)
    return matrix

def initialize_matrix(NbSlots: int) -> list[list[int]]:
    return [[0 for _ in range(NbSlots)] for _ in range(NbSlots)]


def size_patterns(matrix: list[list[int]], NbSlots: int) -> list[list[int]]:
    for i in range(3, NbSlots - 3, 2):
        matrix[i][3] = 1
    return matrix

def place_orientation_patterns(matrix: list[list[int]], NbSlots: int) -> list[list[int]]:
    matrix[NbSlots - 4][NbSlots - 4] = 1
    matrix[NbSlots - 5][NbSlots - 4] = 1
    matrix[NbSlots - 5][NbSlots - 5] = 1
    matrix[NbSlots - 6][NbSlots - 4] = 1
    matrix[NbSlots - 8][NbSlots - 4] = 1
    matrix[NbSlots - 8][NbSlots - 5] = 1
    matrix[NbSlots - 8][NbSlots - 6] = 1
    matrix[NbSlots - 8][NbSlots - 7] = 1
    matrix[NbSlots - 7][NbSlots - 7] = 1
    matrix[NbSlots - 6][NbSlots - 7] = 1
    matrix[NbSlots - 5][NbSlots - 7] = 1
    matrix[NbSlots - 4][NbSlots - 7] = 1
    return matrix

if __name__ == "__main__":
    main()
