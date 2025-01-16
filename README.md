# Rows of Grapevines

This Python program calculates the number of grapevines that can fit in a row in a vineyard. The calculation is based on the row length, space used by end-post assemblies, and the distance between vines. The program uses a user-friendly interface to collect these inputs and compute the result.

---

## **Features**
1. **User Input**:
   - Accepts the following inputs:
     - **Row Length** (`R`): Length of the row in feet.
     - **End-Post Assembly Space** (`E`): Space used by end-post assemblies in feet.
     - **Distance Between Vines** (`S`): Distance between vines in feet.

2. **Calculation**:
   - Calculates the number of grapevines that can fit in the row using the formula:
     \[
     V = \frac{R - 2E}{S}
     \]

3. **Output**:
   - Displays the total number of vines that can fit in the row.

---

## **How to Run**

### **Requirements**
- Python 3.x
- No additional libraries are required.

### **Steps**
1. Save the program as `grapevine_row_calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the program.
4. Run the program:
   ```bash
   python3 grapevine_row_calculator.py
