# CSIS516
## The CSIS Inventory and Maintenance System

### Project Description
The CIMS project/software will have asset inventory and maintenance record keeping functions. Assets and their corresponding information such as serial number, purchase date, EOL date, and more will be able to be tracked. Similarly, assets will have a maintenance history so parts of larger assets (such as servers) can have their replacement cycles tracked. 

### Project Purpose
The purpose of this project is to provide more efficient and effective record keeping for CSIS department assets. This project will streamline department recordkeeping operations and enable more efficient inventory and maintenance activities.

### Project Value 
The value derived from this project is saved time, saved money, and an improved student educational experience through cutting edge technologies. As the department's equipment is inventoried in this system the CSIS department will be able to better track how old equipment is, when it needs to be replaced, and the total costs of the department's equipment. From this, we can derive value to ensure the department's technology assets are maintained on a proper cadence to provide students a superior educational experience with cutting edge technology.

### Project Dependencies/Technologies Used

Technologies used for this project include:
* MySQL Server
* Python 3.13
* Django
* HTML/CSS

Python Packages Used:
* Django
* Django-bootstrap5
* Mysqlclient
* uWSGI

### Setup Instructions

1. Ensure Python 3.13 or higher is installed on your system.

2. Git clone the repository.

3. Create a Python virtual environment and activate it.

4. *Only if running on Linux* - Install the required packages to run the mysqlclient package with the following command:

    `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config`
    
    See the mysqlclient project [reference](https://pypi.org/project/mysqlclient/) for more information.

5. Run `python -m pip install -r requirements.txt`.

6. Install MySQL server on the localhost, either with the installer or in a Docker container. You may need to work with and load the MySQL timezone tables. More information can be found in the [Django docs](https://docs.djangoproject.com/en/5.2/ref/databases/#time-zone-definitions) and in the [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/mysql-tzinfo-to-sql.html).

7. Create a database user with the following commands using these credentials and privileges:
        ```
        USE cims1;
        CREATE USER cimsuser IDENTIFIED BY 'CimsUser123!';
        GRANT ALL 
        ON *.*
        TO cimsuser;
        ```

8. In the cims1 directory, run `python manage.py makemigrations` to generate the necessary SQL code.

9. In the same directory run `python manage.py migrate` to make the necessary migrations.

10. Run `uwsgi -http :8000 -module cims1proj.wsgi` to start the server and run the application.

11. The application should now be available at https://yourhostIP:8000

### Youtube

For a live walkthrough of the project, please see the following [video](https://youtu.be/jKo5FaNNaNw)

## A Quick Note on the Commit History
I had some challenges with my repos so I've had to rebuild them a of couple times. My commit history may look short but I do have history earlier than the earliest date shown.
