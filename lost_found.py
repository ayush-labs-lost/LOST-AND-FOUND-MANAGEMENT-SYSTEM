import json
lost_items = {
    101: {
        "name": "Earbuds",
        "category": "Electronics",
        "location": "Library",
        "date": "22-09-2026",
        "person": "Rahul"
    },
    102: {
        "name": "phone charger",
        "category": "Electronic parts",
        "location": "Block A",
        "date": "21-09-2026",
        "person": "Aman"
    }
}
found_items = {
    201: {
        "name": "phone charger",
        "category": "Electronic parts",
        "location": "Block A",
        "date": "22-09-2026",
        "person": "Rohit"
    }
}
claimed_items = {}
def load_data():
        global lost_items
        global found_items
        global claimed_items
try:

        with open("data.json", "r") as file:
            data = json.load(file)
        lost_items = {
            int(key): value
            for key, value in data["lost_items"].items()
        }
        found_items = {
            int(key): value
            for key, value in data["found_items"].items()
        }
        claimed_items = {
            int(key): value
            for key, value in data["claimed_items"].items()
        }

except FileNotFoundError:
        print("\nNo saved data found. Starting with default data.")

def report_lost_item():
    print("\n" + "=" * 45)
    print("           REPORT LOST ITEM")
    print("=" * 45)
    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location where it was lost: ")
    date = input("Enter date(DDMMYY): ")
    person = input("Enter your name: ")
    if lost_items:
        item_id = max(lost_items.keys()) + 1
    else:
        item_id = 101
    lost_items[item_id] = {
        "name": item_name,
        "category": category,
        "location": location,
        "date": date,
        "person": person
    }
    print("\n✅ Lost item reported successfully!")
    print("Your Item ID is:", item_id)
def report_found_item():
    print("\n" + "=" * 45)
    print("           REPORT FOUND ITEM")
    print("=" * 45)
    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location where it was found: ")
    date = input("Enter date: ")
    person = input("Enter your name: ")
    if found_items:
        item_id = max(found_items.keys()) + 1
    else:
        item_id = 201
    found_items[item_id] = {
        "name": item_name,
        "category": category,
        "location": location,
        "date": date,
        "person": person
    }
    print("\nFound item reported successfully!")
    print("Your Item ID is:", item_id)
def search_item():
    print("\n" + "=" * 45)
    print("              SEARCH ITEM")
    print("=" * 45)
    keyword = input("Enter item name to search: ").lower()
    found = False
    # Search in lost items
    for item_id, item in lost_items.items():
        if keyword in item["name"].lower():
            print("\n--- LOST ITEM FOUND ---")
            print("Item ID   :", item_id)
            print("Item Name :", item["name"])
            print("Category  :", item["category"])
            print("Location  :", item["location"])
            print("Date      :", item["date"])
            print("Reported By:", item["person"])
            found = True
    for item_id, item in found_items.items():
        if keyword in item["name"].lower():
            print("\n--- FOUND ITEM ---")
            print("Item ID   :", item_id)
            print("Item Name :", item["name"])
            print("Category  :", item["category"])
            print("Location  :", item["location"])
            print("Date      :", item["date"])
            print("Found By  :", item["person"])
            found = True
    if not found:
        print("\nNo matching item found.")
def view_lost_items():
    print("\n" + "=" * 80)
    print("                         LOST ITEMS")
    print("=" * 80)
    if not lost_items:
        print("No lost items reported.")
        return
    print(f"{'ID':<8}{'ITEM':<25}{'CATEGORY':<18}{'LOCATION':<20}")
    print("-" * 80)
    for item_id, item in lost_items.items():
        print(
            f"{item_id:<8}"
            f"{item['name']:<25}"
            f"{item['category']:<18}"
            f"{item['location']:<20}"
        )
def view_found_items():
    print("\n" + "=" * 80)
    print("                         FOUND ITEMS")
    print("=" * 80)
    if not found_items:
        print("No found items reported.")
        return
    print(f"{'ID':<8}{'ITEM':<25}{'CATEGORY':<18}{'LOCATION':<20}")
    print("-" * 80)
    for item_id, item in found_items.items():
        print(
            f"{item_id:<8}"
            f"{item['name']:<25}"
            f"{item['category']:<18}"
            f"{item['location']:<20}"
        )
def claim_item():
    print("\n" + "=" * 45)
    print("           CLAIM / RECOVER ITEM")
    print("=" * 45)
    try:
        item_id = int(input("Enter Found Item ID: "))
    except ValueError:
        print("\nInvalid ID! Please enter a number.")
        return
    if item_id not in found_items:
        print("\nNo found item with this ID.")
        return
    item = found_items[item_id]
    print("\nItem Details")
    print("-" * 30)
    print("Item Name :", item["name"])
    print("Category  :", item["category"])
    print("Location  :", item["location"])
    print("Date      :", item["date"])
    print("Found By  :", item["person"])
    claimant = input("\nEnter claimant name: ")
    item["claimed_by"] = claimant
    claimed_items[item_id] = item
    del found_items[item_id]
    print("\nItem claimed successfully!")
    print("Claimed By:", claimant)
def remove_item():
    print("\n" + "=" * 45)
    print("              REMOVE ITEM")
    print("=" * 45)
    try:
        item_id = int(input("Enter Item ID to remove: "))
    except ValueError:
        print("\nInvalid ID! Please enter a number.")
        return
    if item_id in lost_items:
        del lost_items[item_id]
        print("\nLost item removed successfully!")
    elif item_id in found_items:
        del found_items[item_id]
        print("\nFound item removed successfully!")
    elif item_id in claimed_items:
        del claimed_items[item_id]
        print("\nClaimed item removed successfully!")
    else:
         print("\nNo item found with this ID.")
def show_statistics():
    print("\n" + "=" * 45)
    print("              STATISTICS")
    print("=" * 45)
    lost_count = len(lost_items)
    found_count = len(found_items)
    claimed_count = len(claimed_items)
    total_items = lost_count + found_count + claimed_count
    print("\nLost Items    :", lost_count)
    print("Found Items   :", found_count)
    print("Claimed Items :", claimed_count)
    print("-" * 45)
    print("Total Items   :", total_items)
def save_data():
    data = {
        "lost_items": lost_items,
        "found_items": found_items,
        "claimed_items": claimed_items
    }
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("\nData saved successfully!")
load_data()
while True:
    print("\n" + "=" * 55)
    print("        LOST & FOUND MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. Search Item")
    print("4. View Lost Items")
    print("5. View Found Items")
    print("6. Claim / Recover Item")
    print("7. Remove Item")
    print("8. Statistics")
    print("9. Exit")
    print("-" * 55)
    choice = input("Enter your choice: ")
    if choice == "1":
        report_lost_item()
    elif choice == "2":
        report_found_item()
    elif choice == "3":
        search_item()
    elif choice == "4":
        view_lost_items()
    elif choice == "5":
        view_found_items()
    elif choice == "6":
        claim_item()
    elif choice == "7":
        remove_item()
    elif choice == "8":
        show_statistics()
    elif choice == "9":
        save_data()
        print("\nThank you for using Lost & Found Management System!")
        break
    else:
        print("\nInvalid choice! Please enter a number from 1 to 9.")


