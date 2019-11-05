<template>
  <div id="app">
    <input v-if="this.currentUser == '' " v-model="inputUserName"/>
    <button v-if="this.currentUser == '' " @click="submitNewUsername">Enter a username</button>
    <p v-if="this.currentUser != '' ">Welcome {{ currentUser }}!</p>
    <button v-if="this.currentUser != '' " @click="switchUser">Change user</button>

    <hr>

    <input type="checkbox" id="rangeCheckbox" v-model="checkbox">
    <label for="rangeCheckbox">Check this box to select a start and end time.</label>
    <br>
    <p v-if="!checkbox">Select start time.</p>
    <p v-if="checkbox">Select start and end time.</p>
    <date-picker v-if="!checkbox" v-model="datetime" lang="en" confirm type="datetime"  format="YYYY-MM-DD HH:mm:ss" width="500" placeholder="Select Date and Time"></date-picker>
    <date-picker v-if="checkbox" v-model="range" lang="en" range confirm type="datetime" format="YYYY-MM-DD HH:mm:ss" width="500" placeholder="Select Date and Time"></date-picker>
    <p>Enter event name here.</p>
    <input v-model="eventName"/>
    <p>Enter event details here.</p>
    <textarea v-model="eventDetails"/>
    <br>
    <p id="failedEntry" v-if="failedEntry">You must be logged in, set a time, enter an event name, and enter a description.</p>
    <button @click="submitNewEvent">Submit</button>

    <hr>

    <h2>My events</h2>
    <button @click="getEvents">Update my events</button>
    
    <br>

    <div id=eventList>
      <ul v-for="(event, index) in zippedEvent" :key="index">
        <li> {{ event[0] }} </li>
        <li> {{ event[1] }} </li>
        <li> {{ event[2] }} </li>
        <li> {{ event[3] }} </li>
        <button @click="deleteEvent(event[4])">Delete event</button>
        <p>---------------------------------</p>
      </ul>
    </div>
    
  </div>
</template>

<script>
import DatePicker from 'vue2-datepicker'
import axios from 'axios'

let moment = require('moment')

export default {
  name: 'app',
  data() {
    return {
      moment: moment,
      inputUserName: '',
      currentUser: '',
      currentUserID: '',
      eventName: '',
      eventDetails: '',
      eventID: '',
      eventResponseNames: [],
      eventResponseDetails: [],
      eventResponseStartTime: [],
      eventResponseEndTime: [],
      eventResponseID: [],
      zippedEvent: [],
      sharedUsers: [],
      checkbox: false,
      datetime: '',
      timezone: [],
      timezoneStart: 0,
      timezoneEnd: 0,
      startTime: '',
      endTime: '',
      range: [],
      failedEntry: false
    }        
  },
  components: {
    DatePicker
  },
  methods: {
    submitNewEvent() {
      this.clearEventList()
      this.setStartTime()

      // Sets start time to UTC
      let mStartTime = moment.utc(this.startTime)
      this.startTime = mStartTime.toISOString()
      this.startTime = mStartTime.format("YYYY-MM-DD HH:mm:ss")

      // Sets end time to UTC.
      let mEndTime = moment.utc(this.range[1])
      this.endTime = mEndTime.toISOString()
      this.endTime = mEndTime.format("YYYY-MM-DD HH:mm:ss")

      if (this.currentUserID == "" || this.eventName == "" || this.startTime == "") {
        this.failedEntry = true
        return
      }

      axios.post('/newevent', { owner_id: this.currentUserID, event_name: this.eventName, event_details: this.eventDetails, event_start_time: this.startTime, event_end_time: this.endTime})
      .then(() => {
        
      })
        this.eventName = ''
        this.eventDetails = ''
        this.startTime = ''
        this.range = ''
        this.endTime = ''
        this.getEvents()
    },
    deleteEvent(id) {
      axios.delete('/deleteevent', {data: { event_id: id } })
      .then(() => {
        this.getEvents()
      })
    },
    setStartTime() {
      if (this.range != []) {
        this.startTime = this.range[0]
        return
      }
      this.startTime = this.datetime
    },
    clearEventList() {
      this.zippedEvent = []
      const listID = document.getElementById("eventList")
      if (listID.firstChild) {
        while (listID.firstChild) listID.removeChild(listID.firstChild)
      }
    },
    getCurrentUserID() {
      axios.get('/user')
      .then((response) => {
        let currentResponse = response.data.usernames
        for (let i = 0; i < currentResponse.length; i++) {
          if (this.currentUser === currentResponse[i].username) {
            this.currentUserID = currentResponse[i].id
          }
        }
      })
    },
    submitNewUsername() {
      // I believe there is a race condition in here that sometimes prevents the list of events from updating on the webpage.
      axios.post('/usersignup', { new_user: this.inputUserName })
      .then(() => {
        this.currentUser = this.inputUserName
        this.inputUserName = ""
        this.getCurrentUserID()
        this.getEvents()
      }, () => {
        this.currentUser = this.inputUserName
        this.inputUserName = ''
        this.getCurrentUserID()
        this.getEvents()
      })
      .catch(() => {
        this.getCurrentUserID()
        this.getEvents()
      })
    },
    switchUser() {
      this.currentUserID = ''
      this.currentUser = ''
      this.clearEventList()
    },
    getEvents() {
      this.clearEventList()
      axios.get('/getevents')
      .then((response) => {
        let currentResponse = response.data.all_events
        for (let i = 0; i < currentResponse.length; i++) {
          if (this.currentUserID === currentResponse[i].owner_id) {

            this.eventResponseNames.push(currentResponse[i].event_name)
            this.eventResponseDetails.push(currentResponse[i].details)
            this.eventResponseStartTime.push(currentResponse[i].start_time)
            this.eventResponseEndTime.push(currentResponse[i].end_time)
            this.eventResponseID.push(currentResponse[i].id)
          }
        }
        for (let i = 0; i < this.eventResponseNames.length; i++) {
          let stringConvertStartTime = this.eventResponseStartTime[i].toString()
          let stringConvertEndTime = this.eventResponseEndTime[i].toString()
          this.zippedEvent.push([stringConvertStartTime, stringConvertEndTime, this.eventResponseNames[i], this.eventResponseDetails[i], this.eventResponseID[i]])
        }
        this.eventResponseNames = []
        this.eventResponseDetails = []
        this.eventResponseStartTime = []
        this.eventResponseEndTime = []
      })
    }
  }
}
</script>

<style>

</style>
