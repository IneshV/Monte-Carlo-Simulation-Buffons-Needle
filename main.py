import numpy as np
import matplotlib.pyplot as plt

# Helper function to determine whether a stick intersects at least one vertical line
# vertical_lines is a list of x-coordinates of vertical lines
# Returns True if the stick's projection on the x-axis crosses any of those lines

def does_intersect(x1, x2, vertical_lines):
    # Sort endpoints so min_x <= max_x
    min_x, max_x = min(x1, x2), max(x1, x2)
    # Check if there is any vertical line x_line within [min_x, max_x]
    return any(min_x <= x_line <= max_x for x_line in vertical_lines)

# Main simulation function
if __name__ == "__main__":
    # 0. Set up the board
    # We have 5 vertical lines spaced 2 units apart: x = 0, 2, 4, 6, 8
    vertical_lines = [0, 2, 4, 6, 8]
    # We'll drop sticks of length = 1
    stick_length = 1.0
    # We'll define a region in which to drop the sticks
    # so that x in [0, 8], y in [0, 5] (for visualization)
    x_max = 8.0
    y_max = 5.0

    # 1. Initialize count of intersecting sticks to 0
    intersection_count = 0

    # Prompt user for the number of sticks to drop
    num_sticks = int(input("Enter the number of sticks to drop: "))

    # Lists to store stick endpoints for plotting
    sticks = []

    # 2. Drop each stick
    for i in range(num_sticks):
        # Random center (x_center, y_center)
        x_center = np.random.uniform(0, x_max)
        y_center = np.random.uniform(0, y_max)
        # Random angle in [0, 2*pi]
        theta = np.random.uniform(0, 2 * np.pi)

        # Compute endpoints of the stick
        x1 = x_center + (stick_length / 2.0) * np.cos(theta)
        y1 = y_center + (stick_length / 2.0) * np.sin(theta)
        x2 = x_center - (stick_length / 2.0) * np.cos(theta)
        y2 = y_center - (stick_length / 2.0) * np.sin(theta)

        # Check intersection
        if does_intersect(x1, x2, vertical_lines):
            intersection_count += 1

        # Store the stick endpoints
        sticks.append((x1, y1, x2, y2))

    # 3. Estimate Pi using Buffon's Needle formula:
    # Pi ~ (2 * stick_length * total_sticks) / (distance_between_lines * intersection_count)
    # Here distance_between_lines = 2.0, stick_length = 1.0
    # => Pi ~ (2 * 1.0 * num_sticks) / (2.0 * intersection_count) = num_sticks / intersection_count

    pi_estimate = 0.0
    if intersection_count > 0:
        pi_estimate = float(num_sticks) / float(intersection_count)

    print("\n--- Results ---")
    print(f"Total Sticks Dropped: {num_sticks}")
    print(f"Intersecting Sticks: {intersection_count}")
    print(f"Estimated Pi: {pi_estimate:.6f}")
    print(f"Actual Pi: {np.pi:.6f}")
    if intersection_count > 0:
        difference = abs(np.pi - pi_estimate)
        print(f"Difference from actual Pi: {difference:.6f}")

    # 4. Visualization
    fig, ax = plt.subplots(figsize=(8, 5))

    # Draw vertical lines
    for line_x in vertical_lines:
        ax.axvline(line_x, color='black', linewidth=1)

    # Plot the sticks
    for (x1, y1, x2, y2) in sticks:
        # Color red if it intersects, green otherwise
        color = 'red' if does_intersect(x1, x2, vertical_lines) else 'green'
        ax.plot([x1, x2], [y1, y2], color=color)

    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Buffon's Needle Simulation")

    plt.show()
