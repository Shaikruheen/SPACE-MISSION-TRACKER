class Mission:
    def __init__(self, name, agency, year, status):
        self.name = name
        self.agency = agency
        self.year = year
        self.status = status

    def show_info(self):
        print(f"Mission Name: {self.name}, "
              f"Agency: {self.agency}, "
              f"Year: {self.year}, "
              f"Status: {self.status}")


class MissionTracker:
    def __init__(self):
        self.missions = []

    def add_mission(self, mission):
        self.missions.append(mission)
        print(f"✅ Mission '{mission.name}' has been added.")

    def view_all_mission(self):
        print("\n=== All Missions ===")
        if not self.missions:
            print("No missions available.")
        else:
            for mission in self.missions:
                mission.show_info()

    def filter_by_status(self, status):
        print(f"\n🔍 Missions with status '{status}':")
        found = False
        for mission in self.missions:
            if mission.status.lower() == status.lower():
                mission.show_info()
                found = True
        if not found:
            print(f"No missions found with status: {status}")

    # ------- Search --------
    def search_mission(self, keyword):
        """
        Search missions by a keyword that can match
        either the mission name or the agency name.
        """
        print(f"\n🔎 Searching for '{keyword}':")
        found = False
        for mission in self.missions:
            if keyword.lower() in mission.name.lower() or \
               keyword.lower() in mission.agency.lower():
                mission.show_info()
                found = True
        if not found:
            print("No matching mission found.")

    # -------- Update Status --------
    def update_status(self, mission_name, new_status):
        """
        Update the status of a mission whose name matches mission_name.
        """
        for mission in self.missions:
            if mission.name.lower() == mission_name.lower():
                old_status = mission.status
                mission.status = new_status
                print(f"Status of '{mission.name}' changed "
                      f"from '{old_status}' to '{new_status}'.")
                return
        print(f"No mission found with the name '{mission_name}'.")



if __name__ == "__main__":
    # Create some missions
    mission1 = Mission("Mars Rover", "NASA", 2020, "Completed")
    mission2 = Mission("Lunar Gateway", "ESA", 2021, "In Progress")
    mission3 = Mission("James Webb Telescope", "NASA", 2022, "Completed")

    # Create the tracker and add missions
    mission_tracker = MissionTracker()
    mission_tracker.add_mission(mission1)
    mission_tracker.add_mission(mission2)
    mission_tracker.add_mission(mission3)

    # Filter by status
    mission_tracker.filter_by_status("Completed")

    # View all missions
    mission_tracker.view_all_mission()

    # --- Using the new features ---
    # Search for missions by a keyword
    mission_tracker.search_mission("NASA")
    mission_tracker.search_mission("Gateway")

    # Update the status of a mission
    mission_tracker.update_status("Lunar Gateway", "Completed")

    # Check that the update worked
    mission_tracker.view_all_mission()
