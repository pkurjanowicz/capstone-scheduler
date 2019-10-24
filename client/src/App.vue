<template>
  <div id="app">
    <input v-if="this.currentUser == '' " v-model="inputUserName"/>
    <button v-if="this.currentUser == '' " @click="submitNewUsername">Enter a username</button>
    <p v-if="this.currentUser != '' ">Welcome {{ currentUser }}!</p>
    <button v-if="this.currentUser != '' " @click="switchUser">Change user</button>

    <hr>

    <input type="checkbox" id="rangeCheckbox" v-model="checkbox">
    <label for="rangeCheckbox">Check this box to select a range.</label>
    <br>
    <date-picker v-if="!checkbox" v-model="datetime" lang="en" confirm type="datetime"  format="YYYY-MM-DD HH:mm:ss a" width="500" placeholder="Select Date and Time"></date-picker>
    <date-picker v-if="checkbox" v-model="range" lang="en" range confirm type="datetime" format="YYYY-MM-DD HH:mm:ss a" width="500" placeholder="Select Date and Time"></date-picker>
    <p>Enter event name here.</p>
    <input v-model="eventName"/>
    <p>Enter event details here.</p>
    <input v-model="eventDetails"/>
    <br>
    <button @click="submitNewEvent">Submit</button>

    <hr>

    <button @click="convertTime">Convert time!</button>
    <p>User id #: {{ currentUserID }}</p>
    <p>event name: {{ eventName }}</p>
    <p>event details: {{ eventDetails }}</p>
    <p>datetime: {{ datetime }}</p>
    <p>converted datetime: {{ convertedDatetime }}</p>
    <!-- <p>range: {{ range }}</p> -->
    <p>timezone: {{ timezone }}</p>
    <p>timezoneStart: {{ timezoneStart }}</p>
    <p>timezoneEnd: {{ timezoneEnd }}</p>
  </div>
</template>

<script>
import DatePicker from 'vue2-datepicker'
import axios from 'axios'

export default {
  name: 'app',
  data() {
    return {
      inputUserName: '',
      currentUser: '',
      currentUserID: '',
      eventName: '',
      eventDetails: '',
      sharedUsers: [],
      checkbox: false,
      datetime: "",
      convertedDatetime: [],
      timezone: [],
      timezoneStart: 0,
      timezoneEnd: 0,
      startTime: '',
      endTime: '',
      range: '',
    }        
  },
  components: {
    DatePicker
  },
  methods: {
    convertTime() {
      let month = ""
      // convert month from letters to numbers. Ex: Mar -> 03
      month = this.datetime.getMonth() + 1
      if (month < 10) {
        month = "0" + month
      }
      this.datetime = this.datetime.toString().split(" ")
      this.convertedDatetime.push(this.datetime[3], month.toString(), this.datetime[2])
      this.convertedDatetime = this.convertedDatetime.join("-")
      this.convertedDatetime = this.convertedDatetime + " " + this.datetime[4]
      for (let i = 0; i < this.datetime.length; i++) {
        if (this.datetime[i].includes("(")) {
          this.timezoneStart = i
        }
        if (this.datetime[i].includes(")")) {
          this.timezoneEnd = i
        }
      }
      this.timezone = this.datetime.slice(this.timezoneStart, (this.timezoneEnd + 1))
      this.timezone = this.timezone.join("_")
      this.timezone = this.timezone.replace("(", "")
      this.timezone = this.timezone.replace(")", "")
      console.log(typeof(this.timezone))

      axios.post('newevent', { timezone: this.timezone, start_time: this.datetime })
      .then(() => {
        console.log("datetime sent")
      })
 
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
      axios.post('/usersignup', { new_user: this.inputUserName })
      .then((response) => {
        this.currentUser = this.inputUserName
        this.inputUserName = ""
        this.getCurrentUserID()
        console.log("then ", currentUserID)
      }, (error) => {
        this.currentUser = this.inputUserName
        this.inputUserName = ''
        this.getCurrentUserID()
        console.log("error ", currentUserID)
      })
      .catch(() => {
        console.log("catch")
      })
    },
    submitNewEvent() {
      axios.post('/newevent', { event_name: this.eventName, start_time: this.startTime, end_time: this.endTime, event_details: this.eventDetails})
      .then(() => {
        console.log("event created!")
        this.eventName = ''
        this.eventDetails = ''
        this.datetime = null
        this.range = ''
      })
    },
    switchUser() {
      this.currentUserID = ''
      this.currentUser = ''
    },
  }
}
</script>

<style>

</style>
