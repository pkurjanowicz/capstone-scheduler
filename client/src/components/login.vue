<template>
  <div class="boxes">
    

    
    <input v-model="enteredUserName" id="enteredUserName" /><label for="enteredUserName"> Enter your User Name</label>
    <br>
    <input v-model="enteredPassword"/><label for="enteredPassword"> Enter your password</label>
    <br>
    <button v-on:click="enterLoginInfo();">Login to the Purple Cape Scheduler</button>
    <br>
    <p>Don't have a Purple Cape Scheduler?</p>
    <button v-on:click="register();">Register Here</button>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "login",
  
  data () {
    return {
      userLoggedIn: false,//be careful here, is it submitting true in both scenarios?
      loginInfoBool: false,
      enteredUserName: '',
      enteredPassword: '',
      
      }
},

methods: {
    enterLoginInfo() {
        axios.post('user_login', { username_item: this.enteredUserName, password_item: this.enteredPassword })
        axios.get('verify_login')
          .then((resp) => {
            this.loginInfoBool = resp.data.loginbool;
            console.log('logininfobool line 38:'+ this.loginInfoBool)
            if (this.loginInfoBool === true) {
              console.log('logininfobool line 40:   ' + this.loginInfoBool)
              this.$emit('loginInfoEntered', this.userLoggedIn)
              }
          }) 
          
     
    },
      //userLoggedIn is the state to be handed off to CalendarView, as of now it's not being called
      loginInfoEntered () {
        if (this.logInfoBool = True) {
          console.log('print only if true')
          this.$emit('loginInfoEntered', this.userLoggedIn)
        }
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

