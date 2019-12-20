<template>
  <div id="app">
    <!-- Crude login -->
    <!-- <facebookLoginbutton v-if="this.currentUser == '' " /> -->
    <input class="signin-input" v-if="this.currentUser == '' " v-model="inputUserName" v-on:keyup.enter="submitNewUsername"/>
    <button class="button signinbutton" v-if="this.currentUser == '' " @click="submitNewUsername">Enter a username</button>
    <p v-if="this.currentUser != '' ">Welcome {{ currentUser }}!</p>
    <button class="button" v-if="this.currentUser != '' " @click="switchUser">Change user</button>
    <br>
    <!-- list all events for current user -->
    <!-- <h2>My events</h2>
    <button @click="getEvents">Update my events</button>
    <br> -->
  <div class="calendar_eventdetails"> 
    <div style="width:100%;">
      <calendarView
      :calendarEvents='zippedEvent'
      @eventClick='eventClick'
      @dateClick='dateClick'
      @select='select'
      @eventDrop='eventDrop'
      />
    </div>
    <div class="centeredModal">
      <eventDetailsModal
        v-if="isModalVisible" 
        @close="closeModal()"
        :title='eventClickTitle'
        :details='eventClickDescription'
        :start='eventClickStart'
        :end='eventClickEnd'
        :invites='eventInvites'
      />
    </div>
    <!-- Enter event information -->
    <div class="centeredModal">
      <!-- Modal window -->
      <addEventModal 
      v-if="showAddEventModal==true"
      @close="closeModal()"
      :date='newEventClickDate'
      :userID='currentUserID'
      :clearEvents='clearEventList'
      :eventsList='getEvents'
      :startDate='newEventStartDate'
      :endDate='newEventEndDate'
      :allDay="newEventAllDay"
      />
    </div>

  </div>
  </div>
</template>

<script>
import axios from 'axios'
import calendarView from './components/calendarView.vue'
import eventDetailsModal from './components/eventDetailsModal.vue'
import addEventModal from './components/addEventModal.vue'

let moment = require('moment')

export default {
  name: 'app',
  data() {
    return {
      isModalVisible: false,
      currentEventId: '',
      moment: moment,
      inputUserName: '',
      currentUser: '',
      currentUserID: '',
      eventResponseNames: [],
      eventResponseDetails: [],
      eventResponseStartTime: [],
      eventResponseEndTime: [],
      eventResponseID: [],
      zippedEvent: [],
      sharedUsers: [], 
      isModalVisible: false,
      newEventClickDate: '',
      showAddEventModal: false,
      eventInvites: '',
      dragEvent: false
    }        
  },
  components: {
    calendarView,
    eventDetailsModal,
    addEventModal,
  },
  methods: {
    eventClick(title, description, start, end, id) {
      this.eventClickTitle = title
      this.eventClickDescription = description
      this.eventClickStart = start
      this.eventClickEnd = end
      this.isModalVisible = true
      this.getInvites(id)
    },
    getInvites(id) {
      axios.post('/getinvites',{
        event_id: id
      }).then(resp => {
        this.eventInvites = resp.data.all_invites
      })
    },
    dateClick(date){
      this.newEventClickDate = date;
      this.showAddEventModal = true;
    },
    select(start, end, fullDay){
      this.showAddEventModal = false;
      this.newEventStartDate = start;
      this.newEventEndDate = end;
      this.showAddEventModal = true;
      this.newEventAllDay = fullDay;
    },
    eventDrop(dragID, dragStart, dragEnd){
      // Sets start time to UTC
      let dragEventStartDate = moment.utc(dragStart)
      dragStart = dragEventStartDate.toISOString()
      dragStart = dragEventStartDate.format("YYYY-MM-DD HH:mm:ss")

      // Sets end time to UTC.
      let dragEventEndDate = moment.utc(dragEnd)
      dragEnd = dragEventEndDate.toISOString()
      dragEnd = dragEventEndDate.format("YYYY-MM-DD HH:mm:ss")
      this.dragEvent = true;

      axios.patch('/updateevent', { id: dragID, start_time: dragStart, end_time: dragEnd, drag: this.dragEvent})
      .then(() => {
        this.getEvents()
      });
    },
    closeModal() {
      this.isModalVisible = false;
      this.showAddEventModal = false;
    },
    deleteEvent(id) {
      // There is currently an issue with the delete button failing to remove list items sometimes.
      // Refreshing the page restores proper functionality.
      // Update: perhaps it's related to a potential race condition, where the updated list isn't properly rendered in time.
      axios.delete('/deleteevent', {data: { event_id: id } })
      .then(() => {
        this.getEvents()
      })
    },
    clearEventList() {
      this.zippedEvent = []
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
      // I believe there is a race condition somewhere that sometimes prevents the list of events from updating on the webpage.
      // I included an "Update events" button to manually fix the problem.
      axios.post('/usersignup', { new_user: this.inputUserName })
      .then(() => {
        this.currentUser = this.inputUserName
        this.inputUserName = ""
        this.getCurrentUserID()
        this.getEvents()
      // Maybe this part was unnecissary. I was tinkering for a long time. If it aint broke...
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

            this.eventResponseNames.push(currentResponse[i])
            this.eventResponseDetails.push(currentResponse[i])
            this.eventResponseStartTime.push(currentResponse[i])
            this.eventResponseEndTime.push(currentResponse[i])
            this.eventResponseID.push(currentResponse[i])
          }
        }
        for (let i = 0; i < this.eventResponseNames.length; i++) {
          //if the event is all day keep the time in utc, otherwise it will change the start time to the previous day **KS
          let stringConvertStartTime = this.eventResponseStartTime[i].start_time
          let stringConvertEndTime = this.eventResponseEndTime[i].end_time
          if (!this.eventResponseStartTime[i].drag) {
            if (this.eventResponseStartTime[i].all_day == false){
              stringConvertStartTime = this.utcToLocalTime(stringConvertStartTime);
              stringConvertEndTime = this.utcToLocalTime(stringConvertEndTime);
            } 
          } else {
            stringConvertStartTime = this.utcToLocalTime(stringConvertStartTime);
            stringConvertEndTime = this.utcToLocalTime(stringConvertEndTime);
          }     
             
          //the zipped event must be in this format in order for calendarview to display it(as an object) **PK
          
          this.zippedEvent.push({
            title: this.eventResponseNames[i].event_name, 
            start: stringConvertStartTime,
            end: stringConvertEndTime,
            id: currentResponse[i].id,
            extendedProps: {
              title: this.eventResponseNames[i].event_name,
              description: this.eventResponseDetails[i].details,
              start: stringConvertStartTime,
              end: stringConvertEndTime, 
              id: currentResponse[i].id,
            },
            })
            //  ** PK
            //Maybe I will use these later? ** PK
        }
        this.eventResponseNames = []
        this.eventResponseDetails = []
        this.eventResponseStartTime = []
        this.eventResponseEndTime = []
      })
    },
    utcToLocalTime(date){
      var stillUtc = moment.utc(date).toDate();
      var local = moment(stillUtc).local().format('YYYY-MM-DD HH:mm:ss');
      return local;
    }
  }
}

</script>

<style>
  @import './assets/css/normalize.css';
  @import url(https://fonts.googleapis.com/css?family=Roboto:400,900&display=swap);
  @import './assets/css/styles.css';
  
</style>
