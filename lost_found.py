import json
lostitem = {
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
founditem = {
    201: {
        "name": "phone charger",
        "category": "Electronic parts",
        "location": "Block A",
        "date": "22-09-2026",
        "person": "Rohit"
    }
}
claimeditem = {}
def load_data():
        global lostitem
        global found_items
        global claimeditem
try:

        with open("data.json", "r") as file:
            data = json.load(file)
        lostitem = {
            int(key): value
            for key, value in data["lost_items"].items()
        }
        founditem = {
            int(key): value
            for key, value in data["found_items"].items()
        }
        claimeditem = {
            int(key): value
            for key, value in data["claimed_items"].items()
        }

except FileNotFoundError:
        print("\nNo saved data found. Starting with default data.")

def reportlostitem():
    print("\n" + "=" * 45)
    print("           REPORT LOST ITEM")
    print("=" * 45)
    itemname = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location where it was lost: ")
    date = input("Enter date(DDMMYY): ")
    person = input("Enter your name: ")
    if lostitem:
        itemid = max(lostitem.keys()) + 1
    else:
        itemid = 101
    lostitem[itemid] = {
        "name": itemname,
        "category": category,
        "location": location,
        "date": date,
        "person": person
    }
    print("\n✅ Lost item reported successfully!")
    print("Your Item ID is:", itemid)
def reportfounditem():
    print("\n" + "=" * 45)
    print("           REPORT FOUND ITEM")
    print("=" * 45)
    itemname = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location where it was found: ")
    date = input("Enter date: ")
    person = input("Enter your name: ")
    if founditem:
        itemid = max(founditem.keys()) + 1
    else:
        itemid = 201
    founditem[itemid] = {
        "name": itemname,
        "category": category,
        "location": location,
        "date": date,
        "person": person
    }
    print("\nFound item reported successfully!")
    print("Your Item ID is:", itemid)
def searchitem():
    print("\n" + "=" * 45)
    print("              SEARCH ITEM")
    print("=" * 45)
    keyword = input("Enter item name to search: ").lower()
    found = False
    # Search in lost items
    for item_id, item in lostitem.items():
        if keyword in item["name"].lower():
            print("\n--- LOST ITEM FOUND ---")
            print("Item ID   :", item_id)
            print("Item Name :", item["name"])
            print("Category  :", item["category"])
            print("Location  :", item["location"])
            print("Date      :", item["date"])
            print("Reported By:", item["person"])
            found = True
    for item_id, item in founditem.items():
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
def viewlostitems():
    print("\n" + "=" * 80)
    print("                         LOST ITEMS")
    print("=" * 80)
    if not lostitem:
        print("No lost items reported.")
        return
    print(f"{'ID':<8}{'ITEM':<25}{'CATEGORY':<18}{'LOCATION':<20}")
    print("-" * 80)
    for item_id, item in lostitem.items():
        print(
            f"{item_id:<8}"
            f"{item['name']:<25}"
            f"{item['category']:<18}"
            f"{item['location']:<20}"
        )
def viewfounditems():
    print("\n" + "=" * 80)
    print("                         FOUND ITEMS")
    print("=" * 80)
    if not founditem:
        print("No found items reported.")
        return
    print(f"{'ID':<8}{'ITEM':<25}{'CATEGORY':<18}{'LOCATION':<20}")
    print("-" * 80)
    for item_id, item in founditem.items():
        print(
            f"{item_id:<8}"
            f"{item['name']:<25}"
            f"{item['category']:<18}"
            f"{item['location']:<20}"
        )
def claimitem():
    print("\n" + "=" * 45)
    print("           CLAIM / RECOVER ITEM")
    print("=" * 45)
    try:
        item_id = int(input("Enter Found Item ID: "))
    except ValueError:
        print("\nInvalid ID! Please enter a number.")
        return
    if item_id not in founditem:
        print("\nNo found item with this ID.")
        return
    item = founditem[item_id]
    print("\nItem Details")
    print("-" * 30)
    print("Item Name :", item["name"])
    print("Category  :", item["category"])
    print("Location  :", item["location"])
    print("Date      :", item["date"])
    print("Found By  :", item["person"])
    claimant = input("\nEnter claimant name: ")
    item["claimed_by"] = claimant
    claimeditem[item_id] = item
    del founditem[item_id]
    print("\nItem claimed successfully!")
    print("Claimed By:", claimant)
def removeitems():
    print("\n" + "=" * 45)
    print("              REMOVE ITEM")
    print("=" * 45)
    try:
        item_id = int(input("Enter Item ID to remove: "))
    except ValueError:
        print("\nInvalid ID! Please enter a number.")
        return
    if item_id in lostitem:
        del lostitem[item_id]
        print("\nLost item removed successfully!")
    elif item_id in founditem:
        del founditem[item_id]
        print("\nFound item removed successfully!")
    elif item_id in claimeditem:
        del claimeditem[item_id]
        print("\nClaimed item removed successfully!")
    else:
         print("\nNo item found with this ID.")
def statistics():
    print("\n" + "=" * 45)
    print("              STATISTICS")
    print("=" * 45)
    lost_count = len(lostitem)
    found_count = len(founditem)
    claimed_count = len(claimeditem)
    total_items = lost_count + found_count + claimed_count
    print("\nLost Items    :", lost_count)
    print("Found Items   :", found_count)
    print("Claimed Items :", claimed_count)
    print("-" * 45)
    print("Total Items   :", total_items)
def savedata():
    data = {
        "lost_items": lostitem,
        "found_items": founditem,
        "claimed_items": claimeditem
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
        reportlostitem()
    elif choice == "2":
        reportfounditem()
    elif choice == "3":
        searchitem()
    elif choice == "4":
        viewlostitems()
    elif choice == "5":
        viewfounditems()
    elif choice == "6":
        claimitem()
    elif choice == "7":
        removeitems()
    elif choice == "8":
        statistics()
    elif choice == "9":
        savedata()
        print("\nThank you for using Lost & Found Management System!")
        break
    else:
        print("\nInvalid choice! Please enter a number from 1 to 9.")


