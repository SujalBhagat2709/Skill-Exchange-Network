"""
Skill Exchange Network
----------------------
File : skill_exchange_network.py

Purpose
-------
Connects people who want to learn a skill with people
who can teach that skill, while also considering what
each person can offer in return.

Example
-------
Person A:
Wants  -> Python
Offers -> Excel

Person B:
Wants  -> Excel
Offers -> Python

The system identifies them as a strong mutual match.

Features
--------
✔ Add Member
✔ Add Skills Wanted
✔ Add Skills Offered
✔ Find Learning Matches
✔ Find Mutual Exchanges
✔ Calculate Match Score
✔ Rank Matches
✔ Display Network
"""


class SkillExchangeNetwork:

    def __init__(self):

        self.members = []

    # ----------------------------------
    # Add Member
    # ----------------------------------
    def add_member(self,
                   member_id,
                   name,
                   skills_offered,
                   skills_wanted,
                   availability):

        member = {

            "ID":
                member_id,

            "Name":
                name,

            "Skills Offered":
                [
                    skill.strip().lower()
                    for skill in skills_offered
                ],

            "Skills Wanted":
                [
                    skill.strip().lower()
                    for skill in skills_wanted
                ],

            "Availability":
                [
                    time.strip().lower()
                    for time in availability
                ]

        }

        self.members.append(
            member
        )

        return member

    # ----------------------------------
    # Find Common Items
    # ----------------------------------
    def common_items(self,
                     first_list,
                     second_list):

        first_set = set(
            first_list
        )

        second_set = set(
            second_list
        )

        return sorted(
            first_set.intersection(
                second_set
            )
        )

    # ----------------------------------
    # Calculate Match
    # ----------------------------------
    def calculate_match(self,
                        member,
                        other_member):

        score = 0

        # What member wants and
        # what other member offers
        skills_received = self.common_items(

            member["Skills Wanted"],

            other_member["Skills Offered"]

        )

        if skills_received:

            score += min(
                len(skills_received) * 30,
                60
            )

        # What other member wants and
        # what member offers
        skills_given = self.common_items(

            other_member["Skills Wanted"],

            member["Skills Offered"]

        )

        if skills_given:

            score += min(
                len(skills_given) * 30,
                30
            )

        # Availability compatibility
        common_times = self.common_items(

            member["Availability"],

            other_member["Availability"]

        )

        if common_times:

            score += 10

        return min(
            score,
            100
        ), {

            "Skills Member Can Learn":
                skills_received,

            "Skills Member Can Teach":
                skills_given,

            "Common Availability":
                common_times

        }

    # ----------------------------------
    # Match Level
    # ----------------------------------
    def match_level(self,
                    score):

        if score >= 80:

            return "Excellent Exchange"

        elif score >= 60:

            return "Strong Exchange"

        elif score >= 40:

            return "Possible Exchange"

        return "Weak Exchange"

    # ----------------------------------
    # Find Matches
    # ----------------------------------
    def find_matches(self,
                     member):

        matches = []

        for other_member in self.members:

            if (
                other_member["ID"]
                ==
                member["ID"]
            ):

                continue

            score, details = self.calculate_match(

                member,

                other_member

            )

            if score > 0:

                matches.append({

                    "Member ID":
                        other_member["ID"],

                    "Member":
                        other_member["Name"],

                    "Match Score":
                        score,

                    "Match Level":
                        self.match_level(
                            score
                        ),

                    "Details":
                        details

                })

        return sorted(

            matches,

            key=lambda match:
            match["Match Score"],

            reverse=True

        )

    # ----------------------------------
    # Find Best Match
    # ----------------------------------
    def best_match(self,
                   member):

        matches = self.find_matches(
            member
        )

        if not matches:

            return None

        return matches[0]

    # ----------------------------------
    # Find Mutual Exchanges
    # ----------------------------------
    def mutual_exchanges(self):

        exchanges = []

        checked_pairs = set()

        for member in self.members:

            for other_member in self.members:

                if member["ID"] == other_member["ID"]:

                    continue

                pair = tuple(sorted([

                    member["ID"],
                    other_member["ID"]

                ]))

                if pair in checked_pairs:

                    continue

                checked_pairs.add(pair)

                first_to_second = self.common_items(

                    member["Skills Wanted"],

                    other_member["Skills Offered"]

                )

                second_to_first = self.common_items(

                    other_member["Skills Wanted"],

                    member["Skills Offered"]

                )

                if (
                    first_to_second
                    and
                    second_to_first
                ):

                    exchanges.append({

                        "Member 1":
                            member["Name"],

                        "Member 2":
                            other_member["Name"],

                        "Member 1 Learns":
                            first_to_second,

                        "Member 2 Learns":
                            second_to_first

                    })

        return exchanges

    # ----------------------------------
    # Display Member
    # ----------------------------------
    def display_member(self,
                       member):

        print(
            "\n========== MEMBER PROFILE ==========\n"
        )

        for key, value in member.items():

            print(
                f"{key:<22}: {value}"
            )

    # ----------------------------------
    # Display Matches
    # ----------------------------------
    def display_matches(self,
                        member):

        matches = self.find_matches(
            member
        )

        if not matches:

            print(
                "\nNo suitable skill matches found."
            )

            return

        print(
            "\n========== SKILL MATCHES ==========\n"
        )

        for index, match in enumerate(

                matches,

                start=1):

            print(
                f"{index}. "
                f"{match['Member']} | "
                f"Score: "
                f"{match['Match Score']}% | "
                f"{match['Match Level']}"
            )

            details = match["Details"]

            print(
                f"   Can Learn: "
                f"{details['Skills Member Can Learn']}"
            )

            print(
                f"   Can Teach: "
                f"{details['Skills Member Can Teach']}"
            )

            print(
                f"   Availability: "
                f"{details['Common Availability']}"
            )

            print()

    # ----------------------------------
    # Display Mutual Exchanges
    # ----------------------------------
    def display_mutual_exchanges(self):

        exchanges = self.mutual_exchanges()

        if not exchanges:

            print(
                "\nNo mutual skill exchanges found."
            )

            return

        print(
            "\n========== MUTUAL EXCHANGES ==========\n"
        )

        for exchange in exchanges:

            print(
                f"{exchange['Member 1']} "
                f"<-> "
                f"{exchange['Member 2']}"
            )

            print(
                f"  {exchange['Member 1']} learns: "
                f"{exchange['Member 1 Learns']}"
            )

            print(
                f"  {exchange['Member 2']} learns: "
                f"{exchange['Member 2 Learns']}"
            )

            print()

    # ----------------------------------
    # Display Network
    # ----------------------------------
    def display_network(self):

        if not self.members:

            print(
                "\nNo members in the network."
            )

            return

        print(
            "\n========== SKILL EXCHANGE NETWORK ==========\n"
        )

        for member in self.members:

            print(
                f"{member['ID']} | "
                f"{member['Name']}"
            )

            print(
                f"  Offers: "
                f"{member['Skills Offered']}"
            )

            print(
                f"  Wants:  "
                f"{member['Skills Wanted']}"
            )

            print()


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    network = SkillExchangeNetwork()

    member_a = network.add_member(

        "M001",

        "Rahul",

        [
            "python",
            "excel"
        ],

        [
            "web development",
            "javascript"
        ],

        [
            "evening",
            "weekend"
        ]

    )

    member_b = network.add_member(

        "M002",

        "Priya",

        [
            "javascript",
            "web development"
        ],

        [
            "python",
            "excel"
        ],

        [
            "evening",
            "weekend"
        ]

    )

    member_c = network.add_member(

        "M003",

        "Amit",

        [
            "graphic design"
        ],

        [
            "python"
        ],

        [
            "morning"
        ]

    )

    network.display_network()

    print(
        "\nMatches for Rahul:"
    )

    network.display_matches(
        member_a
    )

    network.display_mutual_exchanges()
