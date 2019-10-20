<template>
  <div class="signin">
    <p>Please enter your username</p>
    <input v-model="userName"/>
    <button @click="submitUsername">Login</button>
  </div>
</template>

<script>
export default {
  name: 'Signin',
  props: {
  },
  data() {
    return {
      userName: ''
    }
  },
  methods: {
    submitUsername() {
      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
