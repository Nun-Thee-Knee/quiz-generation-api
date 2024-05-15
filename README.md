# CogniCraft

<h3>AI BACKEND</h3>

<h5>RUNNING ON WSGI WEB SERVER</h5>

[CogniCraft](https://cognicraft.onrender.com)
<br>
<br>
``
https://cognicraft.onrender.com
``

Requirements: POSTMAN/ThunderClient
<br>
<br>
Although the UI for uploading the PDF is provided which is accessible
through root directory "./"
<br>
If user wants to generate MCQ based on prompt then they can 
hit up the root directory "./data" and send the request via a json. 
<br>
The format is given below:-
```bazaar
{
    "topic": "Your topic goes here",
    "number": "The number of MCQ you want"
}
```
<h5>RUNNING ON LOCAL SERVER</h5>
Clone the repository using following link:-
<br>

``
https://github.com/Nun-Thee-Knee/CogniCraft.git
``

Requirements: Any IDE, python, Terminal
<br>
Open the Terminal and type cd over to AI:-
```shell
cd AI
```
Now run the following command to install all the packages associated
with the backend
<br>

```shell
pip install -r requirements.txt
```

After the installation is completed run the following command to start the service:
<br>
```shell
python main.py
```
