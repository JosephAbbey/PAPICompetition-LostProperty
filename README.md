# LostProperty *(Name not final)*

# Description:

## The Problem:
The price of living is rising all the time, and thus saving money where possible is becoming more important as time goes on. Equally, as we become more aware of the effects of mass production on the environment, we must make sure to limit unnecessary purchases. A source of issue for both of these problems is the inefficiency of our current lost property system. Its current design makes locating lost items hard even when they have been discovered, and unclaimed items are seemingly lost to time as there is no good record of how long they have been there; resulting in items being able to remain indefinitely.

## The Solution:
The solution is to create an accessible catalogue-like system which allows easy access to a record of items currently held in the lost property system. This system would categorize items by their characteristics and would flag items which have been unclaimed for longer than a user-specified time-frame. This would make it easier to identify if a lost item has made its way to lost property and would allow unclaimed items to be recycled or donated to charity.

# Details

## The Team

Name     | Github Username |
:-------:|:---------------:|
Joseph A | JosephAbbey     |
Ben J    | BenjaminJones07 |
Micah B  | 123mjb          |
Oxford W | notaguydaddy    |
Aditya C | JustTyping1     |
James U  |                 |
Alex P   |                 |

## Languages:
- Back-end : Python
- Communication : Flask API
- Front-end : HTML/JS (React possibly)

# List of Objectives

- ## Database:
    - Items
        - id       : INT
        - title    : Names[id]
        - category : Categories[id]
        - image    : BLOB
        - foundIn  : Locations[id]
        - storeIn  : INT (Boxes will be numbered)
        - desc     : TEXT

    - Locations
        - id           : INT
        - locationName : STRING

    - Categories
        - id    : INT
        - name  : STRING

    - Names
        - id       : INT
        - name     : TEXT

- ## Back-end:
    - Notify manager (Pseudone)
        - Send message to manager
    - Add item (Pseudone)
        - Verify input
        - Add entry to database
    - Get items (Pseudone)
        - Check for categories
        - Get corresponding database entries
    - Remove item (Pseudone)
        - Verify input
        - Remove entry from database
    - Item expiry (Pseudone)
        - Get items with entry timestamp before certain timestamp
        - Remove item
        - Notify manager with approprite message
    - Photo get (Pseudone)
        - Verify valid ID
        - Return DB BLOB as Photo

- ## Front-end:
    - Catalogue
    - Catagories
    - Details
    - Add item
    - Remove item
    - Claim item
