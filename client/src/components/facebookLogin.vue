<template>
    <div>

    <facebook-login class="button"
      
      appId="430359124531296"
      @login="onLogin"
      @logout="onLogout"
      @sdk-loaded="sdkLoaded">
    </facebook-login>
    
    
  
    </div>

</template>
<script>

import facebookLogin from 'facebook-login-vuejs';

export default {
    name: "facebookLoginbutton",
    components: { facebookLogin },

    data() {
        return {
            idImage, loginImage, mailImage, faceImage,
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
          // eslint-disable-next-line no-console
          console.log("fblogin line 37");
          this.personalID = userInformation.id;
          this.email = userInformation.email;
          this.name = userInformation.name;
        }
      )
    },
    sdkLoaded(payload) {
      // eslint-disable-next-line no-console
      console.log("fblogin line 45");
      this.isConnected = payload.isConnected
      this.FB = payload.FB
      if (this.isConnected) this.getUserData()
    },

    onLogin() {
      this.isConnected = true
       // eslint-disable-next-line no-console
      console.log("fblogin line 55");
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