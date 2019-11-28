<template>
  <div class="boxes">
    

    
    <input v-model="enteredUserName" id="enteredUserName" /><label for="enteredUserName"> Enter your User Name</label>
    <br>
    <input v-model="enteredPassword"/><label for="enteredPassword"> Enter your password</label>
    <br>
    <button v-on:click="enterLoginInfo();">Login to the Purple Cape Scheduler</button>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "login",
  
  data () {
    return {
      userLoggedIn: true,
      enteredUserName: '',
      enteredPassword: '',
      
      }
},

methods: {
    enterLoginInfo() {
        axios.post('user_login', { username_item: this.enteredUserName, password_item: this.enteredPassword })
      
     
    },
      //userLoggedIn is the state to be handed off to CalendarView
      loginInfoEntered () {
        this.$emit('loginInfoEntered', this.userLoggedIn)
        
    },
  mounted() {
    
  }
  
  }
}
</script>
<style>
.boxes {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;
  text-align: right;
  margin: 10% 0;
  min-height: 200px;
  background-color: rgba(33, 33, 33, .3);
  align-items: center;
}
.boxes :first-child {
    align-self: center;
}
</style>

