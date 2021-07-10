# Doctor-Appointment-Scheduler(Socket Programming)
An application that schedules appointments of patients with doctors based upon their availability.It is a client-server architecture-based communication which uses TCP and UDP sockets.

The program runs in 3 phases: user authentication, scheduling an appointment at an available time, getting estimated cost of visit from the scheduled doctor by sending insurance information. We have the healthcenter server for authenticating users and reserving time slots, 2 patients and 2 doctors. Communication between the health center server and patients in the first 2 phases is through TCP sockets. In the last phase, communication between the doctors and the patients is through dynamic UDP sockets.
Sequence in which to run programs:
Healthcenterserver.py -> doctor1.py -> doctor2.py -> patient1.py ->patient2.py


•	In the beginning, the Health Center server displays the doctors table and the patients table present in the database with all the values inserted in the respective tables. It also displays its own port number and IP address
 

•	At first, upon running both doctor1.py and doctor2.py, they both display just their port number and IP address and they will remain open to interact with patients in Phase 3
 

 
•	Phase 1: patient 1 connects to the server using TCP socket.
This only includes patient authentication
 
•	Phase 2 :After authentication and connection, the server sends a list of all possible time slots of both doctors along with a list of ONLY available time slots to the patient along with the port number and the patient has to choose one slot.
 
Here patient is asked to enter index of his/her preferred time slot.
If an invalid index in entered (integer outside the range of 1-6), then the server will keep asking you to re-enter (while loop) until you enter a valid index.
 





•	If the index is valid and available to the patient, then that slot is reserved for the patient, it is removed from the list of available slots and isn’t displayed further. The patient is also shown details of the doctor from the chosen time slot.
 

•	Phase 3 : After choosing a time slot, the doctor patient connection is scheduled by virtue of a udp connection where doctor from the given patient insurance database sends the estimated cost of the appointment to the patient.
 

 
The doctor1 port will still remain open in case of a possible connection with patient2

•	Repeat similar steps for patient2.

•	We saw that patient1 selected the time slot with index 1. So that time slot will not be available to patient2 and hence it will not be displayed. However, still if patient2 tries to enter index 1 as its preferred appointment index, then a message will be displayed to patient2 saying that the chosen index is not available and hence it is made to exit the program and the connection of patient2 with the health centre server is immediately closed.




