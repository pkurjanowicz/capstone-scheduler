<template>
  <div class="boxes">
    
    <p>Register with The Purple Cape Scheduler</p>
    <br>

    <input v-model="newUserName" id="newUserName" /><label for="newUserName"> Enter a User Name</label>
    
    <br>
    <input v-model="newPassword"/><label for="newPassword"> Enter a password</label>
    <br>
    <input v-model="passwordConfirm"/><label for="passwordConfirm"> Confirm your password</label>
    <br>
    <button v-on:click="enterNewUserInfo();">Register for the Purple Cape Scheduler</button>
    <br>




    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "register",
  
  data () {
    return {
      newUserRegistered: true,
      regBool: '',
      newUserName: '',
      newPassword: '',
      passwordConfirm: '',
    
      
      }
},

methods: {
    
     enterNewUserInfo () {
        axios.post('usersignup', { new_user: this.newUserName, new_password: this.newPassword })

      /*
       axios.post('user_register', { new_user: this.newUserName, new_password: this.newPassword })
       axios.get('verify_registration')
          .then((resp) => {
            this.regBool = resp.data.registerBool;
            
            if (this.regBool === true) {
              axios.post('usersignup', { new_user: this.newUserName, new_password: this.newPassword })
              this.$emit('enterNewUserInfo', this.regBool)
              }
          }) 
       
      */
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
