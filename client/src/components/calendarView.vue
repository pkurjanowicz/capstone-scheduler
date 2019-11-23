
// I am using this library in order to build this calendar: https://fullcalendar.io/docs/vue

<template>
  <div class='demo-app'>
    <div class='demo-app-top'>
      <button @click="toggleWeekends">toggle weekends</button>
      <button @click="gotoPast">go to a date in the past</button>
      (also, click a date/time to add an event)
    </div>
    <FullCalendar
      class='demo-app-calendar'
      ref="fullCalendar"
      defaultView="dayGridMonth"
      :header="{
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
      }"
      :plugins="calendarPlugins"
      :weekends="calendarWeekends"
      :events="calendarEvents"
      @dateClick="handleDateClick"
      />
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'

export default {
  name: 'calendarView',
  props: ['calendarEvents'],
  components: {
    FullCalendar // make the <FullCalendar> tag available ** PK
  },
  data: function() {
    return {
      calendarPlugins: [ // plugins must be defined in the JS ** PK
        dayGridPlugin,
        timeGridPlugin,
        interactionPlugin // needed for dateClick ** PK
      ],
      calendarWeekends: true,
    }
  },
  methods: {
    toggleWeekends() {
      this.calendarWeekends = !this.calendarWeekends // update a property **PK
    },
    gotoPast() {
      let calendarApi = this.$refs.fullCalendar.getApi() // from the ref="..." ** PK
      calendarApi.gotoDate('2000-01-01') // call a method on the Calendar object ** PK
    },
    handleDateClick(arg) {
          console.log('this is the date:'+ arg.date)
          /* TODO This is for you Kristin to put in the modal view show function, 
          I have provided you the arg.date here so you can auto populate that ** PK */
        }
  }
}

</script>

<style lang='scss'>

// you must include each plugins' css ** PK
// paths prefixed with ~ signify node_modules ** PK
@import '~@fullcalendar/core/main.css';
@import '~@fullcalendar/daygrid/main.css';
@import '~@fullcalendar/timegrid/main.css';

.demo-app {
  font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
  font-size: 14px;
}

.demo-app-top {
  margin: 0 0 3em;
}

.demo-app-calendar {
  margin: 0 auto;
  max-width: 900px;
}

</style>