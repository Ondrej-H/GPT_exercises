def analyze_missions(missions: list[dict]) -> dict:
    mission_names = [mission["name"] for mission in missions]

    successful_missions = [mission["name"] for mission in missions if mission["success"]]

    failed_missions = [mission["name"] for mission in missions if not mission["success"]]

    agencies = {mission["agency"] for mission in missions}

    destinations = {mission["destination"] for mission in missions}

    missions_after_2000 = [mission["name"] for mission in missions if mission["year"] > 2000]

    longest_mission = max(missions, key=lambda mission: mission["duration_days"])["name"]

    shortest_mission = min(missions, key=lambda mission: mission["duration_days"])["name"]

    newest_mission = max(missions, key=lambda mission: mission["year"])["name"]

    oldest_mission = min(missions, key=lambda mission: mission["year"])["name"]

    missions_by_duration = [mission["name"] for mission in sorted(missions, key=lambda mission: mission["duration_days"], reverse=True)]

    success_rate = round((100 / len(missions)) * len(successful_missions))

    return {
        "mission_names": mission_names,
        "successful_missions": successful_missions,
        "failed_missions": failed_missions,
        "agencies": agencies,
        "destinations": destinations,
        "missions_after_2000": missions_after_2000,
        "longest_mission": longest_mission,
        "shortest_mission": shortest_mission,
        "newest_mission": newest_mission,
        "oldest_mission": oldest_mission,
        "missions_by_duration": missions_by_duration,
        "success_rate": success_rate
    }

missions = [
    {"name": "Apollo 11", "agency": "NASA", "year": 1969, "duration_days": 8, "success": True, "destination": "Moon"},
    {"name": "Voyager 1", "agency": "NASA", "year": 1977, "duration_days": 17000, "success": True, "destination": "Interstellar Space"},
    {"name": "Mars 3", "agency": "Soviet Space Program", "year": 1971, "duration_days": 188, "success": False, "destination": "Mars"},
    {"name": "Rosetta", "agency": "ESA", "year": 2004, "duration_days": 4594, "success": True, "destination": "Comet"},
    {"name": "Chandrayaan-2", "agency": "ISRO", "year": 2019, "duration_days": 48, "success": False, "destination": "Moon"},
    {"name": "Perseverance", "agency": "NASA", "year": 2020, "duration_days": 1000, "success": True, "destination": "Mars"},
]

print(analyze_missions(missions))