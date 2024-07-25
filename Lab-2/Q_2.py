# To solve the quadratic equation.

import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the two solutions
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    # print(math.sqrt(discriminant))

    return root1, root2

def main():
    print("Equation format: ax^2 + bx + c = 0")
    
    # Get coefficients from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Check if 'a' is not zero to ensure it's a quadratic equation
    if a == 0:
        print("The coefficient 'a' must not be zero for a quadratic equation.")
        return
    
    # Solve the quadratic equation
    root1, root2 = solve_quadratic(a, b, c)
    
    # Display the results
    print(f"The roots of the equation {a}x^2 + {b}x + {c} = 0 are:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

if __name__ == "__main__":
    main()
