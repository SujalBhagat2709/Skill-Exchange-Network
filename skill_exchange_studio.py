"""
Skill Exchange Network Studio
-----------------------------
Main interface for Skill Exchange Network.
"""

from skill_exchange_network import SkillExchangeNetwork


class SkillExchangeStudio:

    def __init__(self):

        self.network = SkillExchangeNetwork()
        self.member = None

    # ----------------------------------
    # Add Member
    # ----------------------------------
    def add_member(self):

        print(
            "\n========== ADD MEMBER ==========\n"
        )

        member_id = input(
            "Member ID: "
        ).strip()

        name = input(
            "Name: "
        ).strip()

        skills_offered = [

            skill.strip()

            for skill in input(
                "Skills You Can Teach (comma separated): "
            ).split(",")

            if skill.strip()

        ]

        skills_wanted = [

            skill.strip()

            for skill in input(
                "Skills You Want To Learn (comma separated): "
            ).split(",")

            if skill.strip()

        ]

        availability = [

            time.strip()

            for time in input(
                "Availability (comma separated): "
            ).split(",")

            if time.strip()

        ]

        member = self.network.add_member(

            member_id,
            name,
            skills_offered,
            skills_wanted,
            availability

        )

        print(
            "\nMember added successfully."
        )

        self.network.display_member(
            member
        )

    # ----------------------------------
    # Select Member
    # ----------------------------------
    def select_member(self):

        if not self.network.members:

            print(
                "\nNo members available."
            )

            return None

        member_id = input(
            "\nEnter Member ID: "
        ).strip()

        for member in self.network.members:

            if member["ID"] == member_id:

                return member

        print(
            "\nMember not found."
        )

        return None

    # ----------------------------------
    # Find Matches
    # ----------------------------------
    def find_matches(self):

        member = self.select_member()

        if not member:

            return

        self.network.display_matches(
            member
        )

    # ----------------------------------
    # Best Match
    # ----------------------------------
    def best_match(self):

        member = self.select_member()

        if not member:

            return

        match = self.network.best_match(
            member
        )

        if not match:

            print(
                "\nNo suitable skill exchange found."
            )

            return

        print(
            "\n========== BEST SKILL EXCHANGE ==========\n"
        )

        print(
            f"Member       : "
            f"{match['Member']}"
        )

        print(
            f"Match Score  : "
            f"{match['Match Score']}%"
        )

        print(
            f"Match Level  : "
            f"{match['Match Level']}"
        )

        details = match["Details"]

        print(
            f"Can Learn    : "
            f"{details['Skills Member Can Learn']}"
        )

        print(
            f"Can Teach    : "
            f"{details['Skills Member Can Teach']}"
        )

        print(
            f"Availability : "
            f"{details['Common Availability']}"
        )

    # ----------------------------------
    # Mutual Exchanges
    # ----------------------------------
    def mutual_exchanges(self):

        self.network.display_mutual_exchanges()

    # ----------------------------------
    # View Network
    # ----------------------------------
    def view_network(self):

        self.network.display_network()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("             SKILL EXCHANGE NETWORK")
            print("=" * 60)

            print("1. Add Member")
            print("2. Find Skill Matches")
            print("3. Find Best Match")
            print("4. View Mutual Exchanges")
            print("5. View Network")
            print("6. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_member()

            elif choice == "2":

                self.find_matches()

            elif choice == "3":

                self.best_match()

            elif choice == "4":

                self.mutual_exchanges()

            elif choice == "5":

                self.view_network()

            elif choice == "6":

                print(
                    "\nThank you for using Skill Exchange Network."
                )

                break

            else:

                print(
                    "\nInvalid choice."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = SkillExchangeStudio()

    studio.menu()
