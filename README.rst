STORE_TEST_VST
==============

Hello! Here is presented simple prototype of typical store, where you  can see list of items and every item description.
To see these functions you need to run some simple instructions below:

---
RUN API BACKEND
---

* Run: `python3 -m store_test_vst migrate`
* Run: `python3 -m store_test_vst web`

---
RUN FRONTEND
---

* Run: `cd client`
* Run: `npm run dev`

---
ACCESS FRONTEND
---

To see fronted part you should go `localhost:5000` in your browser. If everything work properly you will see welcome page with gorgeous background and button `View magic Stuff`. By presing this button you will see list of items for sell.

---
ACCESS BACKEND
---

To see admin panel you should go `localhost:8080` in your browser. You will see log in page, and can use next credentials:

* `user: admin`
* `password: admin`

By going to Item page on left part of the screen you will see the list of items and can add or view them if you want.

---
TESTING
---

You can run test pack, places in test.py files, by running next command:

* Run: `python3 -m store_test_vst test`

---
IN THE END
---

Hope you will enjoy it! :)