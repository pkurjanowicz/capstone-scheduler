<template>
  <div class="signup">
    <p>Enter your desired username and password</p>
    <input v-model="newUserName"/>
    <button @click="submitNewUsername">Sign up.</button>
    <p>{{ duplicate }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Signup',
  props: {
  },
  data() {
    return {
      newUserName: '',
      duplicate: ''
    }
  },
  methods: {
    // submitNewUsername() {
    //   let ts = this
    //   console.log("newUserName = ", ts.newUserName)
    //   axios.get('/user')
    //   .then(function (resp) {
    //     console.log(resp.data.usernames)
    //     ts.userResponse = resp.data.usernames
    //     console.log(typeof(ts.userResponse))
    //     for (let i = 0; i < ts.userResponse.length; i++) {
    //       console.log("i = ", i)
    //       let currentName = ts.userResponse[i]
    //       console.log("currentName = ", currentName.username)
    //       console.log("newUserName = ", ts.newUserName)
    //       console.log(currentName.username !== ts.newUserName)
    //       if (currentName.username !== ts.newUserName) {
    //         axios.post('/usersignup', { new_user: ts.newUserName })
    //         .then(() => {
    //           console.log("posted")
    //           this.newUserName = ""
    //         })
    //       }
    //       console.log("Duplicate!!!")
    //       return
    //     }
    //   })
    // }
      submitNewUsername() {
      axios.post('/usersignup', { new_user: this.newUserName })
      .then((response) => {
        console.log("posted")
        this.newUserName = ""
      }, (error) => {
        // console.log(split(error))
        console.log(error)
      })
      .catch(() => {
        this.duplicate = "Username already taken"
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
