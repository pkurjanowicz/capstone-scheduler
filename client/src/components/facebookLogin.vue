<template>
    <div>
    <p>fbLogin line 3</p>

    <facebook-login class="button"
      
      appId="2344508732526791"
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
          console.log("fblogin line getUserData");
          this.personalID = userInformation.id;
          this.email = userInformation.email;
          this.name = userInformation.name;
        }
      )
    },
    sdkLoaded(payload) {
      // eslint-disable-next-line no-console
      console.log("fblogin line sdkLoaded");
      this.isConnected = payload.isConnected
      this.FB = payload.FB
      if (this.isConnected) this.getUserData()
    },

    onLogin() {

      if (location.protocol != 'https:') {
        location.href = 'https:' + window.location.href.substring(window.location.protocol.length);
        this.isConnected = true
        // eslint-disable-next-line no-console
        console.log("fblogin line onLogin");
        this.getUserData()
      }
    },
     onLogout() {
      this.isConnected = false;
    }
}
}
</script>

<style>

</style>