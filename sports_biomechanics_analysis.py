```python
import math


class SportsBiomechanics:
    def __init__(self):
        self.athletes = {}

    def add_athlete(self, athlete_id, name, sport):
        self.athletes[athlete_id] = {
            "name": name,
            "sport": sport,
            "sessions": []
        }
        print("Athlete added successfully!")

    def calculate_angle(self, a, b, c):
        """
        Calculate the angle formed by three 2D points.
        Point b is the vertex.
        """
        ba = (a[0] - b[0], a[1] - b[1])
        bc = (c[0] - b[0], c[1] - b[1])

        dot_product = ba[0] * bc[0] + ba[1] * bc[1]

        magnitude_ba = math.sqrt(
            ba[0] ** 2 + ba[1] ** 2
        )
        magnitude_bc = math.sqrt(
            bc[0] ** 2 + bc[1] ** 2
        )

        if magnitude_ba == 0 or magnitude_bc == 0:
            return None

        cosine = dot_product / (
            magnitude_ba * magnitude_bc
        )

        cosine = max(-1, min(1, cosine))

        angle = math.degrees(math.acos(cosine))

        return round(angle, 2)

    def add_session(
        self,
        athlete_id,
        activity,
        duration,
        heart_rate,
        jump_height
    ):
        if athlete_id not in self.athletes:
            print("Athlete not found!")
            return

        session = {
            "activity": activity,
            "duration": duration,
            "heart_rate": heart_rate,
            "jump_height": jump_height
        }

        self.athletes[athlete_id]["sessions"].append(session)

        print("Performance session recorded successfully!")

    def display_athletes(self):
        if not self.athletes:
            print("No athletes registered.")
            return

        print("\n--- REGISTERED ATHLETES ---")

        for athlete_id, athlete in self.athletes.items():
            print("Athlete ID:", athlete_id)
            print("Name:", athlete["name"])
            print("Sport:", athlete["sport"])
            print("Sessions:", len(athlete["sessions"]))
            print("-" * 30)

    def display_performance(self, athlete_id):
        if athlete_id not in self.athletes:
            print("Athlete not found!")
            return

        athlete = self.athletes[athlete_id]

        print("\n--- ATHLETE PERFORMANCE REPORT ---")
        print("Name:", athlete["name"])
        print("Sport:", athlete["sport"])

        if not athlete["sessions"]:
            print("No performance sessions recorded.")
            return

        for index, session in enumerate(
            athlete["sessions"], start=1
        ):
            print("\nSession:", index)
            print("Activity:", session["activity"])
            print("Duration:", session["duration"], "minutes")
            print("Heart Rate:", session["heart_rate"], "bpm")
            print("Jump Height:", session["jump_height"], "cm")

    def search_athlete(self, athlete_id):
        if athlete_id in self.athletes:
            athlete = self.athletes[athlete_id]
            print("\nAthlete Found!")
            print("ID:", athlete_id)
            print("Name:", athlete["name"])
            print("Sport:", athlete["sport"])
        else:
            print("Athlete not found!")


def main():
    system = SportsBiomechanics()

    while True:
        print("\n===== SPORTS BIOMECHANICS ANALYSIS =====")
        print("1. Register Athlete")
        print("2. Record Performance Session")
        print("3. Display All Athletes")
        print("4. View Athlete Performance")
        print("5. Search Athlete")
        print("6. Calculate Joint Angle")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            athlete_id = input("Enter Athlete ID: ")
            name = input("Enter Athlete Name: ")
            sport = input("Enter Sport: ")

            if athlete_id in system.athletes:
                print("Athlete ID already exists!")
            else:
                system.add_athlete(
                    athlete_id, name, sport
                )

        elif choice == "2":
            athlete_id = input("Enter Athlete ID: ")

            try:
                activity = input("Enter Activity: ")
                duration = float(
                    input("Enter Duration (minutes): ")
                )
                heart_rate = int(
                    input("Enter Heart Rate (bpm): ")
                )
                jump_height = float(
                    input("Enter Jump Height (cm): ")
                )

                if duration < 0 or heart_rate < 0 or jump_height < 0:
                    print("Values cannot be negative!")
                    continue

                system.add_session(
                    athlete_id,
                    activity,
                    duration,
                    heart_rate,
                    jump_height
                )

            except ValueError:
                print("Please enter valid numerical values.")

        elif choice == "3":
            system.display_athletes()

        elif choice == "4":
            athlete_id = input("Enter Athlete ID: ")
            system.display_performance(athlete_id)

        elif choice == "5":
            athlete_id = input("Enter Athlete ID: ")
            system.search_athlete(athlete_id)

        elif choice == "6":
            try:
                print("Enter coordinates for three points.")

                ax = float(input("Point A - x: "))
                ay = float(input("Point A - y: "))

                bx = float(input("Point B - x: "))
                by = float(input("Point B - y: "))

                cx = float(input("Point C - x: "))
                cy = float(input("Point C - y: "))

                angle = system.calculate_angle(
                    (ax, ay),
                    (bx, by),
                    (cx, cy)
                )

                if angle is None:
                    print("Cannot calculate angle for these points.")
                else:
                    print("Calculated Joint Angle:", angle, "degrees")

            except ValueError:
                print("Please enter valid numerical coordinates.")

        elif choice == "7":
            print("Thank you for using Sports Biomechanics Analysis!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
```
