<template>
    <div id="app">
        <h1>testfblogin page</h1>
        <facebookLogin class="button"
            appId="2344508732526791"
            @login="onLogin"
            @logout="onLogout"
            @get-initial-status="getUserData">
        </facebookLogin>

    </div>

</template>
<script>
import Vue from 'vue'
import facebookLogin from 'facebook-login-vuejs';

export default {
    name: "facebookLogin",

    data() {
        return {
            isConnected: false,
            name: '',
            email: '',
            personalID: '',
            FB: undefined
        }
    },


methods: {
    getUserData() {
      this.FB.api('/me', 'GET', { fields: 'id,name,email' },
        userInformation => {
          this.personalID = userInformation.id;
          this.email = userInformation.email;
          this.name = userInformation.name;
        }
      )
    },
    sdkLoaded(payload) {
      this.isConnected = payload.isConnected
      this.FB = payload.FB
      if (this.isConnected) this.getUserData()
    },

    onLogin() {
      this.isConnected = true
      this.getUserData()
    },
     onLogout() {
      this.isConnected = false;
    }
}
}
</script>

<style>

</style>