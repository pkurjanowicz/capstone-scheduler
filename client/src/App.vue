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
    <date-picker v-if="!checkbox" v-model="datetime" lang="en" confirm type="datetime"  format="YYYY-MM-DD HH:mm:ss" value-type="format" width="500" placeholder="Select Date and Time"></date-picker>
    <date-picker v-if="checkbox" v-model="range" lang="en" range confirm type="datetime" format="YYYY-MM-DD HH:mm:ss" value-type="format" width="500" placeholder="Select Date and Time"></date-picker>
    <p>Enter event name here.</p>
    <input v-model="eventName"/>
    <p>Enter event details here.</p>
    <textarea v-model="eventDetails"/>
    <br>
    <p id="failedEntry" v-if="failedEntry">You must be logged in, set a time, and enter an event name</p>
    <button @click="submitNewEvent">Submit</button>

    <hr>

    <p>User id #: {{ currentUserID }}</p>
    <p>event name: {{ eventName }}</p>
    <p>event details: {{ eventDetails }}</p>
    <p>current user: {{ currentUser }}</p>
    <p>converted datetime: {{ convertedDatetime }}</p>
    <!-- <p>range: {{ range }}</p> -->
    <p>timezone: {{ timezone }}</p>
    <p>timezoneStart: {{ timezoneStart }}</p>
    <p>timezoneEnd: {{ timezoneEnd }}</p>

    <hr>

    <h2>My events</h2>

    
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
      failedEntry: false
    }        
  },
  components: {
    DatePicker
  },
  methods: {
    submitNewEvent() {
      if(this.currentUserID == "" || this.eventName == "" || this.datetime =="") {
        this.failedEntry = true
        console.log("Failed entry")
        return
      }
      let year = 0
      let month = 0
      let day = 0
      let hour = 0
      let minute = 0
      let second = 0
    // look up 'regex' for details on the next line.
      this.convertedDatetime = this.datetime.split(/[-:\s]/)
      year = this.convertedDatetime[0]
      month = this.convertedDatetime[1]
      day = this.convertedDatetime[2]
      hour = this.convertedDatetime[3]
      minute = this.convertedDatetime[4]
      second = this.convertedDatetime[5]

    // this.datetime = this.datetime.toString().split(" ")
    //   this.convertedDatetime.push(this.datetime[3], month.toString(), this.datetime[2])
    //   this.convertedDatetime = this.convertedDatetime.join("-")
    //   this.convertedDatetime = this.convertedDatetime + " " + this.datetime[4]
    //   for (let i = 0; i < this.datetime.length; i++) {
    //     if (this.datetime[i].includes("(")) {
    //       this.timezoneStart = i
    //     }
    //     if (this.datetime[i].includes(")")) {
    //       this.timezoneEnd = i
    //     }
    //   }
    //   this.timezone = this.datetime.slice(this.timezoneStart, (this.timezoneEnd + 1))
    //   this.timezone = this.timezone.join("_")
    //   this.timezone = this.timezone.replace("(", "")
    //   this.timezone = this.timezone.replace(")", "")
    //   console.log(typeof(this.timezone))    let month = ""
    //   // convert month from letters to numbers. Ex: Mar -> 03
    //   month = this.datetime.getMonth() + 1
    //   if (month < 10) {
    //     month = "0" + month
    //   }
    //   this.datetime = this.datetime.toString().split(" ")
    //   this.convertedDatetime.push(this.datetime[3], month.toString(), this.datetime[2])
    //   this.convertedDatetime = this.convertedDatetime.join("-")
    //   this.convertedDatetime = this.convertedDatetime + " " + this.datetime[4]
    //   for (let i = 0; i < this.datetime.length; i++) {
    //     if (this.datetime[i].includes("(")) {
    //       this.timezoneStart = i
    //     }
    //     if (this.datetime[i].includes(")")) {
    //       this.timezoneEnd = i
    //     }
    //   }
    //   this.timezone = this.datetime.slice(this.timezoneStart, (this.timezoneEnd + 1))
    //   this.timezone = this.timezone.join("_")
    //   this.timezone = this.timezone.replace("(", "")
    //   this.timezone = this.timezone.replace(")", "")
    //   console.log(typeof(this.timezone))

      axios.post('/newevent', { owner_id: this.currentUserID, event_name: this.eventName, event_details: this.eventDetails, year: year, month: month, day: day, hour: hour, minute: minute, second: second })
      .then(() => {
        
      })
        console.log("event created!")
        this.eventName = ''
        this.eventDetails = ''
        this.datetime = null
        this.range = ''
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
      }, (error) => {
        this.currentUser = this.inputUserName
        this.inputUserName = ''
        this.getCurrentUserID()
        console.log("error ", currentUserID)
      })
      .catch(() => {
        console.log("catch")
        this.getCurrentUserID()
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
