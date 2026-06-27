def calculate_box_inertia(mass, width, height, depth):
    Ixx = (1 / 12) * mass * (height**2 + depth**2)
    Iyy = (1 / 12) * mass * (width**2 + depth**2)
    Izz = (1 / 12) * mass * (width**2 + height**2)
    return {"ixx": Ixx, "iyy": Iyy, "izz": Izz, "ixy": 0.0, "ixz": 0.0, "iyz": 0.0}


def calculate_cylinder_inertia(mass, radius, length, axis='z'):
    I_long = (1 / 2) * mass * radius**2
    I_short = (1 / 12) * mass * (3 * radius**2 + length**2)

    if axis == 'z':
        return {"ixx": I_short, "iyy": I_short, "izz": I_long, "ixy": 0.0, "ixz": 0.0, "iyz": 0.0}
    elif axis == 'x':
        return {"ixx": I_long, "iyy": I_short, "izz": I_short, "ixy": 0.0, "ixz": 0.0, "iyz": 0.0}
    elif axis == 'y':
        return {"ixx": I_short, "iyy": I_long, "izz": I_short, "ixy": 0.0, "ixz": 0.0, "iyz": 0.0}
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'")


def calculate_sphere_inertia(mass, radius):
    I = (2 / 5) * mass * radius**2
    return {"ixx": I, "iyy": I, "izz": I, "ixy": 0.0, "ixz": 0.0, "iyz": 0.0}


def main():
    print("📦 Inertia Tensor Calculator")
    print("Choose a shape:")
    print("1. Box")
    print("2. Cylinder")
    print("3. Sphere")

    choice = input("Enter 1, 2, or 3: ").strip()

    try:
        if choice == "1":
            print("\n-- Box --")
            mass = float(input("Enter mass (kg): "))
            width = float(input("Enter width (m): "))
            height = float(input("Enter height (m): "))
            depth = float(input("Enter depth (m): "))
            inertia = calculate_box_inertia(mass, width, height, depth)

        elif choice == "2":
            print("\n-- Cylinder --")
            mass = float(input("Enter mass (kg): "))
            radius = float(input("Enter radius (m): "))
            length = float(input("Enter length (m): "))
            axis = input("Enter axis of cylinder (x, y, or z): ").strip().lower()
            inertia = calculate_cylinder_inertia(mass, radius, length, axis)

        elif choice == "3":
            print("\n-- Sphere --")
            mass = float(input("Enter mass (kg): "))
            radius = float(input("Enter radius (m): "))
            inertia = calculate_sphere_inertia(mass, radius)

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
            return

        print("\n🧮 Inertia Tensor (about center of mass):")
        for key, value in inertia.items():
            print(f"{key.upper()}: {value:.8e} kg·m²")  # scientific notation

    except ValueError:
        print("⚠️ Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
