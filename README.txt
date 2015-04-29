                                            |                         DisRes                        |
                                            _________________________________________________________


DEPLOYMENT 
==========
* DisRes is highly configurable disaster response application which provides both mobile and web clients
  to the users to speed up the response process.
* To deploy DisRes for a particular a region, all that is required is to register all the 
  disaster rescue organisations from our website. After this step is done users can register and use 
  both web and android application at the time of disaster.
* At present it is deployed globally on 
  https://disrescrowdsoucing.pythonanywhere.com/crowdsourcing
  Organisations and users can register here.

FEATURES
========

1. User
   ----
   1.1. Report a SOS request (reported by disaster victim)
   1.2. Report an observation (reported by a responsible citizen - First Responder)
   1.3. View all the previous SOSs
   1.4. View responses for each SOS request
   1.5. Search
        1.5.1. Search by Organisation Name
        1.5.2. Search by Organisation Type
        1.5.3. Search by Address
        1.5.4. Search by coordinates
   1.6. Display organisations on map
   1.7. Keyword search
        1.7.1. Twitter
        1.7.2. Instagram

2. Organisation
   ------------
   2.1. Have a list of SOSs of all the confirmed disasters
   2.2. Organisation can open a SOS and view its details
   2.3. Organisation can respond to each SOS request seperately
   2.4. Search
        2.4.1. Search by Organisation Name
        2.4.2. Search by Organisation Type
        2.4.3. Search by Address
        2.4.4. Search by coordinates
   2.5. Display organisations on map
   2.6. Keyword search
        2.6.1. Twitter
        2.6.2. Instagram

3. Admin
   -----
   3.1. Can view a list of disasters reported
   3.2. Disasters are created by grouping SoSs and Observations reported
        around a specific location and in some finite interval of time
   3.3. Admin can confirm the disaster - 
        On doing this an email is sent to all the organisations corresponding to that disaster
        and they can respond to this disaster
   3.4. Admin can delete a disaster -
        Results in deleting all the SoSs and Observations of that disaster
   3.5. Admin can click on the disaster and view all the SoSs and Observations of that disaster
   3.6. Display organisations on map
   3.7. Keyword search
        3.7.1. Twitter
        3.7.2. Instagram
   3.8. Search
        3.8.1. Search by Organisation Name
        3.8.2. Search by Organisation Type
        3.8.3. Search by Address
        3.8.4. Search by coordinates
