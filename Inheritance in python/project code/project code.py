class IncidentPortal:
    def _init_(self):
        self.incidents = []

    def create_incident(self, date, person_id, incident_type):
        report_id = len(self.incidents) + 1  # Assign a unique report ID
        incident = {
            'report_id': report_id,
            'date': date,
            'person_id': person_id,
            'incident_type': incident_type
        }
        self.incidents.append(incident)
        print(f"Incident created with report ID: {report_id}")

    def read_incident_by_report_id(self, report_id):
        for incident in self.incidents:
            if incident['report_id'] == report_id:
                print("Incident details:")
                for key, value in incident.items():
                    print(f"{key}: {value}")
                return
        print("No incident found with the given report ID.")

    def update_incident(self, report_id, **kwargs):
        for incident in self.incidents:
            if incident['report_id'] == report_id:
                for key, value in kwargs.items():
                    if key in incident:
                        incident[key] = value
                print("Incident updated successfully.")
                return
        print("No incident found with the given report ID.")

    def delete_incident(self, report_id):
        for incident in self.incidents:
            if incident['report_id'] == report_id:
                self.incidents.remove(incident)
                print("Incident deleted successfully.")
                return
        print("No incident found with the given report ID.")

def main():
    portal = IncidentPortal()

    while True:
        print("\nIncident Reporting Portal")
        print("1. Create Incident")
        print("2. Read Incident by Report ID")
        print("3. Update Incident")
        print("4. Delete Incident")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date of the incident: ")
            person_id = input("Enter ID of the person: ")
            incident_type = input("Enter type of the incident: ")
            portal.create_incident(date, person_id, incident_type)

        elif choice == '2':
            report_id = int(input("Enter report ID to read incident: "))
            portal.read_incident_by_report_id(report_id)

        elif choice == '3':
            report_id = int(input("Enter report ID of the incident to update: "))
            updates = {}
            field = input("Enter field to update (date/person_id/incident_type): ")
            if field:
                value = input(f"Enter new value for {field}: ")
                updates[field] = value
            portal.update_incident(report_id, **updates)

        elif choice == '4':
            report_id = int(input("Enter report ID of the incident to delete: "))
            portal.delete_incident(report_id)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()
