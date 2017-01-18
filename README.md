The basic structure is creating,
viewing, modifying and deleting of your MaxCDN zones and users.

In order to login into the API you need to provide your CDN Company Alias, Consumer Key and
Consumer Secret.

# Main menu:
  After you’ve entered your credentials you will be presented with the following options:

  **1. Change API Credentials** - You will be prompted to re enter your Company Alias, Consumer
  Key and Consumer Secret.
  
  **2. Zone management** – Allows operations with Pull, Push and VOD zones.
  
  **3. User management** – Allows creating, modifying, deleting and viewing of user accounts.

##Zone management:
###Pull Zones
  **Create** – Creates a pull zone with the Zone Name that you specified, and the link to your
  origin(must include http:// or https://)
  
  **Modify** – You will be prompted to enter the ID of the zone you want to modify, after that you
  can modify a Pull Zone with specific parameters by typing in the parameter following a value of
  that parameter.
  
  **Delete** – Deletes a Pull Zone with a specified ID
  
  **Purge Files** - Purges the files on your zone specified with the Pull Zone ID and the URI of the file you
  want to purge(example: /images, /myfiles)
  
  **Purge Zones** - Purges the entire Pull Zone specified with the Pull Zone ID
  
  **View Zones** – Displays the list of all Pull Zones on the account with the Pull Zone ID, date of creation
  and the Zone URL.
  
###Push Zone
  **Create** - Creates a Push zone with the Zone Name and Password that you specified.
  
  **Modify** - You will be prompted to enter the ID of the zone you want to modify, after that you can
  modify a Push Zone with specific parameters by typing in the parameter following a value of that
  parameter.
  
  **Delete** - Deletes a Push Zone with a specified ID
  
  **View Zones** - Displays the list of all Push Zones on the account with the Pull Zone ID, date of creation
  and the Zone URL.
  
###VOD Zone
  **Create** - Creates a VOD Zone with the Zone Name and Password that you specified.
  
  **Modify** - You will be prompted to enter the ID of the zone you want to modify, after that you can
  modify a VOD Zone with specific parameters by typing in the parameter following a value of that
  parameter.
  
  **Delete** - Deletes a VOD Zone with a specified ID
  
  **View Zones** - Displays the list of all Push Zones on the account with the Pull Zone ID, date of creation
  and the Zone URL.
  
## User management:
  **Create a new user** – Creates a new user with the users email, password, first name and last name
  specified.
  
  **Modify a current user** - You will be prompted to enter the ID of the user you want to modify, after that
  you can modify the user with specific parameters by typing in the parameter following a value of that
  parameter.
  
  **Delete a current user** - Deletes a user with a specified ID.
  
  **View Users** - Displays the list of all users on the account with the user ID, first name and last name.
