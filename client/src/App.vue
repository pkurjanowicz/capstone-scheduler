<template>
  <div id="app">
    <input v-if="this.currentUser == '' " v-model="inputUserName"/>
    <button v-if="this.currentUser == '' " @click="submitNewUsername">Enter a username</button>
    <p v-if="this.currentUser != '' ">Welcome {{ currentUser }}!</p>

    <hr>

    <input type="checkbox" id="rangeCheckbox" v-model="checkbox">
    <label for="rangeCheckbox">Check this box to select a range.</label>
    <br>
    <date-picker v-if="!checkbox" v-model="datetime" lang="en" confirm type="datetime" format="YYYY-MM-DD HH:mm:ss a" width="500" placeholder="Select Date and Time"></date-picker>
    <date-picker v-if="checkbox" v-model="range" lang="en" range confirm type="datetime" format="YYYY-MM-DD HH:mm:ss a" width="500" placeholder="Select Date and Time"></date-picker>

    <p>Enter event name here.</p>
    <input v-model="eventName"/>
    <p>Enter event details here.</p>
    <input v-model="eventDetails"/>
    <!-- <button @click="submitNewEvent">Submit Event</button> -->
    <p>Enter any usernames you want to share with. (separate with spaces)</p>
    <input v-model="sharedUsers"/>

    <hr>

    <ul>
    </ul>
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
      datetime: '',
      range: ''
    }        
  },
  components: {
    DatePicker
  },
  methods: {
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
    }
  },
  submitNewEvent() {
    axios.post('/newevent', { new_event: this.inputUserName })
    .then
  }
}
</script>

<style>

</style>
